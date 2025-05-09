
# Calculating Objects
Objects can have a `calculate` function defined on them to allow them to react to different events happening in the game. The main time for this to happen is during **scoring**, but there are other contexts that the game calculates effects. There is a full list of contexts available at the end of this guide.

## Creating a Calculate Function
To create a calculate function on your object, add this code to your object definition.
```lua
calculate = function(self, card, context)
	-- calculation code goes in here
end,
```
In this function, `self` refers to the center object that is used to create cards of this type, `card` refers to the actual card you are calculating on, and `context` refers to the table of values sent to the calculate. You will need to use `card` and `context` to calculate any effects within your object.
There are three steps to writing the calculation code within your function.
1. Checking for the correct context
2. Any logic/effects you want to do
3. Returning any effects that need to be handled

### Step 1: Context Checks
All code within your calculate function should be inside a **context check**. This statement will ensure that your effect will open happen in the timing that you want it to happen. There is a full list of contexts at the end of this guide, but here are some common ones you might want to use.
- `if context.joker_main then` The main scoring timing of jokers
- `if context.cardarea == G.play and context.main_scoring` The main scoring of played cards *(used for modifiers to cards)*
- `if context.before then` For effects that happen in the scoring loop but before anything is scored
- `if context.final_scoring_step then`For effects that modify the score after all cards have been scored
- `if context.cardarea == G.play and context.repetition then` For adding repetitions to played cards

### Step 2: Logic/Effects
In this step, you need to add your actual logic for calculation. Values that are defined in your object's config can be access by using `card.ability.`, for example, here is some code that increases the chips an object will give out by 10 every time the effect is evaluated.
```lua
card.ability.extra.chips = card.ability.extra.chips + card.ability.extra.chip_gain
```

### Step 3: Returning Effects
Any effects that you want to be evaluated will need to be returned in a table. To score the chips from Step 2, you should use this return table.
```lua
return {
	chips = card.ability.extra.chips
}
```
There are a range of different keys that you can return in this table.
- `chips`,`mult`,`xmult`, `dollars` - scores these values *(automatically adds a message to the card that is being scored)*
- `swap` - swaps current chips and mult values with each other
- `level_up` - levels up the played hand by the number returned
- `saved` - used during `context.end_of_round` to prevent game over
- `message` - used to return a custom message
	- will automatically be put on the scored card unless `message_card` is also returned
	- colour of message background will be `G.C.FILTER` unless `colour` is returned
	- sound will be `generic1` unless `sound` is returned
- `func` - return a function to be called at the correct timing *(advanced)*
- `extra` - an extra table set out the same as this one *(advanced)*

If you do not want the default messages to be shown when adding `chips` etc. there are 2 ways around this
1. Use `remove_default_message = true` in your return table to ignore the message completely
2. Use `chip_message = 'text'` to change the text *(this maintains default timings)*
___
Putting all this together, we get the following function that will increment chips each time the object is scored, and then score the new amount of chips.
```lua
calculate = function(self, card, context)
	if context.joker_main then
		card.ability.extra.chips = card.ability.extra.chips + card.ability.extra.chip_gain
		return {
			chips = card.ability.extra.chips
		}
	end
end
```
Here is another example for a Joker that increases the amount of mult it gives when you play a Flush.
```lua
calculate = function(self, card, context)
	-- Check if we have played a Flush before we do any scoring and increment the chips
	if context.before and next(context.poker_hands['Flush']) then
		card.ability.extra.mult = card.ability.extra.mult + card.ability.extra.mult_gain
		return {
			message = 'Upgraded!',
			colour = G.C.RED
		}
	end
	-- Add the chips in main scoring context
	if context.joker_main then
		return {
			mult = card.ability.extra.mult
		}
	end
```

> [!NOTE]
> If you want to evaluate effects outside of the return table, use `SMODS.calculate_effect({effects}, card)`,
> where `{effects}` is a table like the return table of a calculate function, and `card` is the card that is being evaluated.

> [!WARNING]
> If you use `context.xxx` inside `SMODS.calculate_effect` or an Event,
> you might need to save `context.xxx` in a local variable.
>
> (`context` is NOT constant. It could change later and cause you
> to reference an unrelated value.)

## Contexts
Detailed here is a list of all contexts that are sent to calculate functions, as well as a unique identifier to use to reference them. As each context is sent to different areas, use the following logic statement to make sure you are calculating in the intended area.
```lua
if context.cardarea == G.play then -- replace G.play with G.jokers/G.hand as appropriate
```
---
### Main Scoring Loop
This context is used for effects that happen before scoring begins. 
```lua
if context.before and context.cardarea == G.play then
{
	cardarea = G.jokers, -- G.play, G.hand, (G.deck and G.discard optionally enabled)
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	before = true
}
```
---
This context is used for the effects from playing cards when they are scored. This is used for enhancements, editions and seals (or any other card modifiers)
```lua
if context.main_scoring and context.cardarea == G.play then
{
	cardarea = G.play, -- G.hand, (G.deck and G.discard optionally enabled)
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	main_scoring = true
}
```
---
This context is used for triggering joker effects on playing cards. 
```lua
if context.individual and context.cardarea == G.play then
{
	cardarea = G.play, -- G.hand, (G.deck and G.discard optionally enabled)
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	individual = true,
	other_card = card
}
```
---
This context is used for adding repetitions to playing cards. 
```lua
if context.repetition and context.cardarea == G.play then
{
	cardarea = G.play, -- G.hand, G.deck and G.discard optionally enabled
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	repetition = true,
	card_effects = effects -- this is the table of effects that has been calculated
}
```
---
This context is used for triggering editions on jokers before they score. *(used for chips/mult)*
```lua
if context.pre_joker then
{
	cardarea = G.jokers,
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	edition = true,
	pre_joker = true
}
```
---
This context is used for triggering normal scoring effects on **jokers**. 
```lua
if context.joker_main then
{
	cardarea = G.jokers,
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	joker_main = true,
}
```
---
This context is used for triggering joker effects from other jokers. 
```lua
if context.other_joker then
{
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	other_joker = card, --changes to other_consumeable as it iterates over consumeables
}
```
---
This context is used for triggering editions on jokers after they score. *(used for xmult)*
```lua
if context.post_joker then
{
	cardarea = G.jokers,
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	edition = true,
	post_joker = true
}
```
---
This context is used for any effects after cards have been calculated but before the score is totalled. 
```lua
if context.final_scoring_step and context.cardarea == G.play then
{
	cardarea = G.jokers, -- G.play, G.hand, (G.deck and G.discard optionally enabled)
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	final_scoring_step = true,
}
```
---
This context is used for marking cards to be destroyed.
```lua
if context.destroy_card then
{
	cardarea = G.play -- 'unscored', G.hand, (G.deck and G.discard optionally enabled)
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	destroy_card = card,
	destroying_card = card -- only when calculating in G.play.
	-- This is from vanilla, you can use context.destroy_card instead.
}
```
> [!TIP]
> Your return table to destroy a card without a message should look like
> `return { remove = true }`

> [!TIP]
> If you want a card to destroy itself, you need `...and context.destroy_card == card` to avoid destroying other cards.
---
This context is used for effects on removing cards. 
```lua
if context.remove_playing_cards then
{
	cardarea = G.jokers, -- G.play, G.hand, (G.deck and G.discard optionally enabled)
	scoring_hand = scoring_hand,
	remove_playing_cards = true,
	removed = cards_destroyed
}
```
> [!WARNING]
> This is also called after discarding a hand without the `scoring_hand` part of the context.
---
This context is used for effects after scoring. 
```lua
if context.after and context.cardarea == G.play then
{
	cardarea = G.jokers, -- G.play, G.hand, (G.deck and G.discard optionally enabled)
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	after = true,
}
```
---
### Other Contexts
This context is used for trigger effects on playing a hand debuffed by the blind. 
```lua
if context.debuffed_hand and context.cardarea == G.play then
{
	cardarea = G.jokers, -- G.play, G.hand, (G.deck and G.discard optionally enabled)
	full_hand = G.play.cards,
	scoring_hand = scoring_hand,
	scoring_name = text,
	poker_hands = poker_hands,
	debuffed_hand = true,
}
```
---
This context is used for end of round effects. 
```lua
if context.end_of_round and context.cardarea == G.jokers then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	end_of_round = true,
	game_over = game_over -- true or false
}
```
---
This context is used for effects on cards from jokers at the end of the round. 
```lua
if context.end_of_round and context.individual then
{
	cardarea = G.hand, -- (G.deck and G.discard optionally enabled)
	end_of_round = true,
	individual = true,
	other_card = card
}
```
---
This context is used for repetitions on cards at the end of the round. 
```lua
if context.end_of_round and context.repetition then
{
	cardarea = G.hand, -- (G.deck and G.discard optionally enabled)
	end_of_round = true,
	repetition = true,
	other_card = card,
	card_effects = effects -- table of effects for the card
}
```
---
This context is used for effects when the blind is started. 
```lua
if context.setting_blind then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	setting_blind = true,
	blind = G.GAME.round_resets.blind
}
```
---
This context is used for effects before discarding. 
```lua
if context.pre_discard and context.cardarea == G.play then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	full_hand = G.hand.highlighted,
	pre_discard = true,
	hook = hook -- true when 'The Hook' discards cards
}
```
---
This context is used for effects on discarded cards. 
```lua
if context.discard then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	full_hand = G.hand.highlighted,
	discard = true
	other_card = G.hand.highlighted[i]
}
```
> [!TIP]
> Return `{ remove = true }` to destroy cards in this context.
---
This context is used for effects after opening a booster. 
```lua
if context.open_booster then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	open_booster = true,
	card = self -- the booster pack being opened
}
```
---
This context is used for effects after skipping a booster. 
```lua
if context.skipping_booster then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	skipping_booster = true,
}
```
---
This context is used for effects after buying a card.
```lua
if context.buying_card then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	buying_card = true,
	card = self -- the card being bought
}
```
The card being bought also calculates itself with context `{ buying_card = true, card = c1 }`.

---
This context is used for effects after selling a card. 
```lua
if context.selling_card then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	selling_card = true,
	card = card -- the card being sold
}
```
The card being sold also calculates itself with context `{ selling_self = true }`.

---
This context is used for effects after rerolling the shop. 
```lua
if context.reroll_shop then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	reroll_shop = true,
}
```
---
This context is used for effects after leaving the shop. 
```lua
if context.ending_shop then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	ending_shop = true,
}
```
---
This context is used for effects after drawing the first hand of a blind. 
```lua
if context.first_hand_drawn then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	first_hand_drawn = true,
}
```
---
This context is used for effects after drawing a hand. 
```lua
if context.hand_drawn then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	hand_drawn = true,
}
```
---
This context is used for effects after using a consumable 
```lua
if context.using_consumeable then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	using_consumeable = true,
	consumeable = card, -- the consumable being used
	area = G.consumeables, -- the area the card was used from (could be G.shop_jokers, G.pack_cards)
}
```
---
This context is used for effects after skipping a blind. 
```lua
if context.skip_blind then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	skip_blind = true,
}
```
---
This context is used for effects after adding a playing card to your deck.
(See also `context.card_added` for non-playing cards.)
```lua
if context.playing_card_added then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	playing_card_added = true,
	cards = cards -- the cards being added
}
```
---
This context is used for applying quantum enhancements. 
```lua
if context.check_enhancement then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	check_enhancement = true,
	other_card = card,
	no_blueprint = true
}
```
---
This context is used for effects after a Joker has triggered. 
```lua
if context.post_trigger then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	post_trigger = true,
	blueprint_card = context.blueprint_card, -- if applicable
	other_card = card, -- the card that triggered
	other_context = context, -- the context the trigger happened on
	other_ret = ret -- the return table from the trigger
}
```
---
This context is used for effects when a (non-playing) card is added to the deck (`Card:add_to_deck`).
(See also `context.playing_card_added` for playing cards.)
```lua
if context.card_added then
{
	cardarea = G.jokers, -- G.hand, (G.deck and G.discard optionally enabled)
	card_added = true,
	card = card
}
```
New playing card types may need to be excluded manually.
A patch target is provided.


> [!NOTE]
> All calculation of jokers that evaluates no secondary card is called with `main_eval = true` in the context table.
> All joker triggers are called with again when the joker is **retriggered** with
> `retrigger_joker = retrigger_card` added to the context table.
