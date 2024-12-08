_This guide is missing any contexts added by RetriggerAPI_

# Score Evaluation

The process of score evaluation in Balatro is quite linear.
There are well-defined stages that go one after another, but the actual implementation is somewhat convoluted.
Perhaps one of the better ways to understand most of this process is by reading the code of [Divvy's Simulation](https://github.com/DivvyCr/Balatro-Simulation/blob/main/src/Engine.lua).
It's a perfect replication of the game's score evaluation but rewritten in a clearer manner.
Nevertheless, the rest of this guide explains the high-level details of this process.

## Set-Up

Once you play a hand, the game must first determine what cards are actually scoring.
For instance, if you play `A228`, only the pair of `2s` will be scored (unless you have the Splash joker!)

For this, the game uses `G.FUNCS.get_poker_hand_info(..)`, which takes an array of Card objects and returns a tuple of five values in this order:

 - The name of the play (eg. 'High Card', 'Pair', or 'Straight')
 - The localized name of the play
 - A table mapping play names (eg. 'High Card') to arrays of Card objects; it contains *all possible plays* out of the played hand, so a 'Two Pair' play will also have at least two 'Pair' values.<br>
   Eg. `poker_hands["Pair"] == { {2, 2}, {Q, Q} }`, but instead of numbers and letters, there will be Card objects.
 - An array of *scoring* Card objects (eg. only the pair of `2s` out of `A228`)
 - The special name of the play (eg. 'Royal Flush') or its standard name if no special name exists

```lua
-- Example usage:
local hand_name, localized_hand_name, poker_hands, scoring_hand, customised_hand_name = G.FUNCS.get_poker_hand_info(..)
```

Now, as I alluded, the scoring cards may be different in special circumstances, such as when 'Splash' is present.
Therefore, if it *is* present, the game adds all cards to scoring cards.
(It also adds any Stone cards during this process, even if no 'Splash' is present)

## Check for Blind Debuffs

The game will now check whether the played hand is actually debuffed by the blind.
For instance, if you play fewer than five cards under the Psychic.

If the hand *is debuffed*, then the game will calculate the effects of all jokers with the special `context` argument containing `debuffed_hand = true`.
In the vanilla game, only 'Matador' actually does anything with this.

If the hand is *not debuffed*, then the game will carry out its full score evaluation, explained further below.

## The Context

First, however, it is important to understand the `context` argument that is used throughout the whole process.
The `context` is just a special argument that is passed to all objects that influence score evaluation.

### Bare-Minimum Context

All context arguments will always contain the following:

 - `cardarea`: which CardArea is being evaluated (either `G.jokers`, `G.hand`, or `G.play`)
 - `full_hand`: an array of all played Card objects (incl. non-scoring)
 - `scoring_hand`: an array of all scored Card objects
 - `scoring_name`: the name of the play (eg. 'High Card', or 'Straight')
 - `poker_hands`: the table mapping play names to Card objects (explained earlier)

```lua
-- Example minimal context:
local minimal_context = {
   cardarea = G.jokers,
   full_hand = G.play.cards,
   scoring_hand = scoring_hand, -- from G.FUNCS.get_poker_hand_info(..)
   scoring_name = hand_name,    -- from G.FUNCS.get_poker_hand_info(..)
   poker_hands = poker_hands    -- from G.FUNCS.get_poker_hand_info(..)
}
```

### More Context

Lastly, the context is further extended with particular flags and/or data, which signify  and help during the different stages of score evaluation.
One of these flags was mentioned earlier &ndash; `debuffed_hand = true` &ndash; so the full context would look like this:

```lua
-- Example context:
local context = {
   cardarea = G.jokers,
   full_hand = G.play.cards,
   scoring_hand = scoring_hand, -- from G.FUNCS.get_poker_hand_info(..)
   scoring_name = hand_name,    -- from G.FUNCS.get_poker_hand_info(..)
   poker_hands = poker_hands,   -- from G.FUNCS.get_poker_hand_info(..)
   debuffed_hand = true
}
```

### The Purpose of Context

Context enables the strict order of evaluation that Balatro relies upon.
Consider that upgrade jokers like 'Hiker' and 'Green Joker' are evaluated before anything else &ndash; it would be confusing otherwise.
Similarly, the 'DNA' joker must copy a card up-front.
Then, there are also jokers that do something for each scored card like 'Hiker' and 'Odd Todd', as opposed to jokers that do something after all cards were evaluated like 'Green Joker' and 'Hologram'.

Notice how some jokers appear multiple times?
Each time, there is a different *context*.
This is why `context` is vital.

On top of that, consider jokers like 'Blueprint' and 'Brainstorm'.
They must somehow know what joker they are replicating, so the `context` will also contain data (in this case, it would be `min_context + {other_joker = JOKER_OBJ}`)

## Stages of Evaluation

Hence, there are multiple stages within score evaluation:

 1. **Before** Stage<br>
   For any jokers that need to do something *before* score evaluation.<br>
   Sets `context.cardarea = G.jokers` and `context.before = true`
 2. **Score** Initialisation Stage<br>
   Sets chips and mult to those associated with the current hand level.
 3. **Blind** Effects Stage<br>
   For any blind effects like 'Flint' halving initial chips and mult.<br>
   This is handled by `Blind:modify_hand(..)` in game.
 4. **Scoring-Cards** Evaluation Stage<br>
   Evaluates each Card in `context.scoring_hand`, with `context.cardarea = G.play`.<br>
   See 'Card Evaluation' section below.
 5. **Held-Cards** Evaluation Stage<br>
   Evaluates each Card in `G.hand.cards`, with `context.cardarea = G.hand`.<br>
   See 'Card Evaluation' section below.
 6. **Global** Joker Effects Stage<br>
   For any jokers that do something *after* all cards have been evaluated.<br>
   Sets `context.cardarea = G.jokers` and `context.joker_main = true`
 7. **Consumable** Effects Stage<br>
   For any consumable effects (due to 'Observatory' for example).<br>
   This is a very short and custom stage.
 8. **Deck** Effects Stage<br>
   For any deck effects like 'Plasma' merging chips and mult.<br>
   This is handled by `Back:trigger_effect(..)` in game, with `context.final_scoring_step = true`
 9. Card **Destruction** Stage<br>
   Self-explanatory.
 10. **After** Stage<br>
    For any jokers that need to do something *after* a hand is played like 'Loyalty Card.<br>
    Sets `context.cardarea = G.jokers` and `context.after = true`
   
## Card Evaluation

Stages **4** and **5** go through each scored/held card and do the following:

 0. If the card is debuffed, do nothing.
 1. Collect repetitions from seals
   Sets `context.other_card = [CARD]` and `context.repetition = true` and `context.repetition_only = true`
 2. Collect repetitions from jokers
   Sets `context.other_card = [CARD]` and `context.repetition = true`
 3. For each collected repetition:
   - Evaluate the Card object via `eval_card([CARD], context)`
   - For each joker, evaluate joker effects via `[JOKER]:calculate_joker(context)`
    Sets `context.other_card = [CARD]` and `context.individual = true`
   - The return values of the above evaluations comprise a table that contains some fields described below.

```lua
-- Table with possible fields, returned from each card evaluation above:
{
  chips = 0,  -- Chips to add
  mult = 0,   -- Mult to add
  x_mult = 1, -- Mult multiplier
  h_mult = 1, -- TODO

  message = nil, -- TODO

  -- TODO: Difference between 'dollars' vs 'p_dollars'?
  dollars = 0,   -- Dollars to add
  p_dollars = 0, -- Dollars to add

  extra.chip_mod = 0, -- Chips to add
  extra.mult_mod = 0, -- Mult to add
  extra.swap = nil,   -- Should swap chips and mult?
  extra.func = nil,   -- TODO

  -- Effects due to Card's edition:
  edition.chip_mod = 0,   -- Chips to add
  edition.mult_mod = 0,   -- Mult to add
  edition.x_mult_mod = 0  -- Mult multiplier
}
```

## Joker Evaluation

Stage **6** goes through each joker and applies its global effect, if any.
For each joker:

 1. Evaluate its edition via `eval_card([JOKER], context)`<br>
   Sets `context.edition = true`
 2. Evaluate its effect via `eval_card([JOKER], context)`<br>
   Sets `context.joker_main = true`
 3. Evaluate any replications of this joker (by jokers like 'Blueprint'); see below.<br>
   Sets `context.other_joker = [JOKER]`
   
```lua
-- Joker-on-Joker simplified code
-- Assume we are currently evaluating the effects of 'current_joker'

context.other_joker = current_joker

for _, another_joker in ipairs(G.jokers.cards) do
   -- Yes, we pass 'current_joker' as context to all other jokers.
   another_joker:calculate_joker(context)
end
```

## Destruction

Lastly, the game will check if any scored cards or jokers need to be destroyed.
For each scored card, the game will first check if any joker destroys it via:

```lua
[JOKER]:calculate_joker({destroying_card = [CARD], full_hand = G.play.cards})
```

Then, the game will check if any Glass cards break.
Any destroyed cards are saved in the array `cards_destroyed`.

Then, the game will go through all jokers again, checking if any jokers were triggered due to a card being destroyed:

```lua
eval_card([CARD], {cardarea = G.jokers, remove_playing_cards = true, removed = cards_destroyed})
```


# Other Evaluation

Jokers are also evaluated after other player actions, not just when a hand is played.
The two main actions are discarding cards and winning the round, which have dedicated sections below.
All other actions are listed in the 'Everything Else' section at the bottom, for quick reference.

## Discard

Once you discard a hand, the game also does multiple stages of evaluation:

 1. **Before** Stage (Held Cards)<br>
   Sets `context.pre_discard = true` and `context.full_hand = G.hand.highlighted` (ie. which cards will be discarded)<br>
   *Also*, it sets `context.hook = true` if 'The Hook' blind is active.
    1. Evaluates **each held card** with that context.
    2. Evaluates **each joker** with that context.
 2. **Discard** Stage<br>
   Sets `context.discard = true` and `context.full_hand = G.hand.highlighted` (ie. which cards are discarded)
    1. Evaluates **each held card** with that context.
    2. Evaluates **each joker** with that context and also `context.other_card = discarded_card` (ie. it's evaluated *for each discarded card*)<br>
      This checks if any joker returns `remove = true`, like 'Trading Card' in vanilla.
 3. Card **Destruction** Stage<br>
   Evaluates **each joker** with `context.cardarea = G.jokers`<br>
   Sets `context.remove_playing_cards = true` and `context.removed = cards_destroyed`

## End of Round

Once you win (or lose) a round, the game also does multiple stages of evaluation:

 1. **Game Over** Effects<br>
   Sets `context.end_of_round = true` and `game_over = true` if the player just lost the the game<br>
   This checks if any joker returns `saved = true`, like 'Mr. Bones' in vanilla.
 2. **Held-Cards** Evaluation Stage<br>
   Sets `context.cardarea = G.hand` and `context.end_of_round = true`<br>
   This follows the same steps described in the 'Card Evaluation' section above.
 
> [!NOTE]
> For **End of Round** effects that trigger once, your joker should use:<br>
> `if context.end_of_round and not context.repetition and not context.individual then ...`

## Everything Else

Whenever any of the events below take place, *each joker* will be evaluated via `[JOKER]:calculate_joker(context)`.
All changes to context are mentioned alongside the event:

 - Round-related events
   - **New Round**: sets `context.setting_blind = true` and `context.blind = G.GAME.round_resets.blind` (ie. the type of blind)<br>
    Used by 'Madness', 'Burglar', and others in vanilla
   - **Drawing First Hand**: sets `context.first_hand_drawn = true`<br>
    Used by 'DNA', 'Trading Card', and others in vanilla
   - **Skipping a Blind**: sets `context.skip_blind = true`<br>
    Used only by 'Throwback' in vanilla
 - Set-up modifications
   - **Adding a Playing Card**: sets `context.playing_card_added = true` and `context.cards = cards` (ie. which cards added)<br>
    Used only by 'Hologram' in vanilla
   - **Using a Consumable**: sets `context.using_consumeable = true` and `context.consumeable = card` (ie. which consumable)<br>
    Used by 'Fortune Teller', 'Glass Joker', and others in vanilla
   - **Selling a Joker/Consumable**: sets `context.selling_card = true` and `context.card = card` (ie. which card)<br>
    *Also*, if selling a joker, that joker is evaluated with `context.selling_self = true`<br>
    Used only by 'Campfire' and 'Luchador' in vanilla
 - Shop-related events
   - **Buying Anything**: sets `context.buying_card = true` and `context.card = card` (ie. a joker/consumable/card/voucher object)<br>
    *Also*, if buying a joker, that joker is evaluated with the same context as above.
   - **Opening a Booster Pack**: sets `context.open_booster = true` and `context.card = booster` (ie. which booster)<br>
    Used only by 'Hallucination' in vanilla
   - **Skipping a Booster**: sets `context.skipping_booster = true`<br>
    Used only by 'Red Card' in vanilla
   - **Rerolling Shop**: sets `context.reroll_shop = true`<br>
    Used only by 'Flash Card' in vanilla
   - **Leaving Shop**: sets `context.ending_shop = true`<br>
    Used only by 'Perkeo' in vanilla

***
*Guide written by Divvy*
