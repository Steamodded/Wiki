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


# Other joker calculations
## End of round
 1. Iterate through `G.jokers.cards` calling `calculate_joker` with context:
```lua
end_of_round = true
game_over = game_over -- true or false
```

   *This evaluation checks for `saved` effects*<br>
   **rental** and **perishable** calculations also happen here<br>
   Use `if context.end_of_round and not context.repetition and not context.individual then` to trigger this.

 2. If the game is not over, iterate through `G.hand.cards`<br>
   i) establish the repetition loop `reps`<br>
   ii) calculate `get_end_of_round_effect` on the current card with no context<br>
   *This evaluation looks for `h_dollars`*<br>
   iii) call `eval_card` with context:
```lua
end_of_round = true
cardarea = G.hand
repetition = true
repetition_only = true
```
   *This evaluation looks for `repetitions` effects from **seals***<br>
   iv) call `eval_card` with context:
```lua
cardarea = G.hand
other_card = G.hand.cards[i]
repetition = true
end_of_round = true
card_effects = effects
```
   *This evaluation looks for `repetitions` effects from **jokers***<br>
   v) iterate through `effects` and look for:
```lua
h_dollars
extra
```

## Discard cards from highlighted
1) iterate through `G.hand.cards` calling `eval_card` with context:```
pre_discard = true
full_hand = G.hand.highlighted
hook = hook``` *This evaluation looks for **cards** that do something to a discarded hand before it is discarded*
2) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
pre_discard = true
full_hand = G.hand.highlighted
hook = hook``` *This evaluation looks for **jokers** that do something to a discarded hand before it is discarded*
3)  iterate through `G.hand.cards` calling `eval_card` with context:```
discard = true
full_hand = G.hand.highlighted``` *This evaluation looks for `remove` effects from **cards** when it is discarded*
4) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
discard = true
other_card = G.hand.highlighted[i]
full_hand = G.hand.highlighted``` *This evaluation looks for `remove` effects from **jokers** when a card is discarded*
5) if there are any **destroyed** cards in the discarded cards, call `calculate_joker` with context:```
cardarea = G.jokers
remove_playing_cards = true
removed = destroyed_cards``` *This evaluation checks to see if a **joker** has an effect on a removed card*
## New round
1) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
setting_blind = true
blind = G.GAME.round_resets.blind``` *This evaluation checks to see if a **joker** has an effect when a blind is selected
## Use consumeable
1) When a consumeable removes a card, iterate through `G.jokers.cards` calling `calculate_joker` with contet:```
remove_playing_cards = true
removed = destroyed_cards```
## Open a booster
1) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
open_booster = true
card = self```
## Redeem voucher
1) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
buying_card = true
card = self```
## Calculate joker
1) if joker is *Blueprint* or *Brainstorm* call `calculate_joker` with the same context
## Update draw to hand
1) on the first hand of a round, iterate through `G.jokers.cards` calling `calculate_joker` with context `first_hand_drawn = true`
## Use card
1) If card is consumeable, iterate through `G.jokers.cards` calling `calculate_joker` with context:```
using_consumeable = true
consumeable = card```
## Sell joker
1) When a joker is sold, call `calculate_joker` with context `selling_self = true`
## Sell card
1) If selling card, iterate through `G.jokers.cards` calling `calculate_joker` with context:```
selling_card = true
card = card```
## Buy from shop
1) When buying a joker, call `calculate_joker` with context:```
buying_card = true
card = c1```
2) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
buying_card = true
card = c1```
## Toggle shop
1) If leaving the shop, iterate through `G.jokers.cards` calling `calculate_joker` with context `ending_shop = true`
## Reroll shop
1) If rerolling the shop, iterate through `G.jokers.cards` calling `calculate_joker` with context `reroll_shop = true`
## Skip booster
1) If skipping a booster pack, iterate through `G.jokers.cards` calling `calculate_joker` with context `skipping_booster = true`
## Skip blind
1) If skipping a blind, iterate through `G.jokers.cards` calling `calculate_joker` with context `skip_blind = true`
## Playing card added
1) When adding a playing card, iterate through `G.jokers.cards` calling `calculate_joker` with context:```
playing_card_added = true
cards = cards```

***
*Guide written by Eremel_ and Divvy_*
