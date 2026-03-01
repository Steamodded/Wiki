# ​Calculate Functions

Objects can have a ​calculate​ function defined on them to allow them to react to different events happening in the game. The main time for this to happen is during scoring, but there are many other contexts that the game uses to calculate effects. There is a full list of contexts available at the end of this guide.

## Creating A Calculate Function

To create a calculate function on your object, add this code to your object definition.

```lua
calculate = function(self, card, context)
    -- calculation code goes in here
end,
```

In this function, `self` refers to the center object that is used to create cards of this type, `card` refers to the actual card you are calculating on, and `context` refers to the table of values sent to the calculate. You will need to use `card` and `context` to calculate any effects within your object.

>[!NOTE]
>Some objects do not have the card parameter in their function definition. Their function would look like `calculate = function(self, context)`

Any values that you want to use during your calculate function should be stored in the `config` of the joker. To initialise and save these values correctly, they should be contained in the `extra` table, as shown here.

```lua
config = {extra = {chips = 10, change = 5}},
```

There are three steps to writing the calculation code within your function.

1. Checking for the correct context
2. Any logic/effects you want to do
3. Returning any effects that need to be handled

### Step 1: Context Checks

All code within your calculate function should be inside a **context check**. This statement will ensure that your effect will open happen in the timing that you want it to happen. There is a full list of contexts at the end of this guide, but here are some common ones you might want to use.

- `if context.joker_main then` The main scoring timing of jokers
- `if context.cardarea == G.play and context.main_scoring` The main scoring of played cards *(used for modifiers to cards)*
- `if context.before then` For effects that happen in the scoring loop but before anything is scored
- `if context.final_scoring_step then` For effects that modify the score after all cards have been scored
- `if context.cardarea == G.play and context.repetition then` For adding repetitions to played cards

### Step 2: Logic/Effects

In this step, you need to add your actual logic for calculation. Values that are defined in your object's config can be access by using `card.ability.`, for example, here is some code that increases the chips an object will give out by 5 every time the effect is evaluated.

```lua
card.ability.extra.chips = card.ability.extra.chips + card.ability.extra.change
```

> [!NOTE]
> This is a simple scaling value - we now use a different function to scale values to allow for interactions with other effects. See `SMODS.scale_card` in **Advanced Usage** for more information.

### Step 3: Returning Effects

Any effects that you want to be evaluated will need to be returned in a table. To score the chips from Step 2, you should use this return table.

```lua
return {
    chips = card.ability.extra.chips
}
```

There are a range of different keys that you can return in this table. These keys can be combined to have multiple effects from the same calculation step.

- `chips`,`mult`,`xmult`, `xchips`, `dollars` - scores these values *(automatically adds a message to the card that is being scored)*
- `swap` - swaps current chips and mult values with each other
- `balance` - balances the current chips and mult values *(plasma deck effect)*
- `level_up` - levels up the played hand by the number returned *(You can specify a different hand to be levelled up by using `level_up_hand`)*
- `saved` - used during `context.end_of_round` to prevent game over
- `message` - used to return a custom message
  - will automatically be put on the scored card unless `message_card` is also returned
  - colour of message background will be `G.C.FILTER` unless `colour` is returned
  - a custom sound can be added to a custom message by using `sound`
	  - you can use `pitch` and `volume` to modify the pitch and volume of your sound
- `func` - return a function to be called at the correct timing *(advanced)*
- `extra` - an extra table set out the same as this one *(advanced)*
- `effect` - set as true to mark your joker as having triggered

If you do not want the default messages to be shown when adding `chips` etc. there are 2 ways to do this

1. Use `remove_default_message = true` in your return table to ignore the message completely. This allows you to use a completely custom message instead
2. Use `chip_message = {message = 'string', colour = COLOUR, }`} to change the text of the default message *(this maintains default timings)*. This table is formatted similarly to a normal calculation return.

___

Putting all this together, we get the following function that will increment chips each time the object is scored, and then score the new amount of chips.

```lua
calculate = function(self, card, context)
    if context.joker_main then
        card.ability.extra.chips = card.ability.extra.chips + card.ability.extra.change
        return {
            chips = card.ability.extra.chips
        }
    end
end
```

Here is another example for a Joker that increases the amount of mult it gives when you play any type of Flush *(Flush, Straight Flush, Flush Five, Flush House)*.

```lua
calculate = function(self, card, context)
    -- Check if we have played a Flush before we do any scoring and increment the mult
    if context.before and next(context.poker_hands['Flush']) then
        card.ability.extra.mult = card.ability.extra.mult + card.ability.extra.change
        return {
            message = 'Upgraded!',
            colour = G.C.RED
        }    
    end
    -- Add the mult in main scoring context
    if context.joker_main then
        return {
            mult = card.ability.extra.mult
        }
    end
end
```

> [!NOTE]
> If you want to evaluate effects outside of the return table, use `SMODS.calculate_effect({effects}, card)`. See below for more details.

# Advanced Usage

## Helper Functions
There are some helper functions that you may wish to use during your calculation events.

- `SMODS.calculate_effect(effect, scored_card, from_edition)`
	- Handles triggering a table of effects. Used to alter the timings of when effects are triggered, or used outside of a calculate function.
	- `effect` - Table of effects akin to the return table in `calculate` functions
	- `scored_card` - Card or object to juice up and attach messages to during evaluation of effects
	- `from_edition` - *(not required)* set to `true` to use automatic edition messaging

> [!WARNING]
> If you use `context.xxx` inside `SMODS.calculate_effect` or an **Event**, you should save
>  `context.xxx` in a local variable first - *`context` is not constant, it changes between calculation steps and may cause you to reference an unrelated, or missing, value*
	
- `SMODS.blueprint_effect(copier, copied_card, context)`
	- Helper function to copy the ability of another object, similar to Blueprint/Brainstorm
	- `copier` is the card/object that will be copying the effect of `copied_card`, using the provided `context` table.
	- The returned table is the calculated effect of `copier_card`, with the display card set to `copier` with a `G.C.BLUE` colour tag. This table should either be returned from the `calculate` function, or fed into `SMODS.calculate_effect`.
	- Example:
		```lua 
			calculate = function(self, card, context)
				-- Reimplementation of Brainstorm
				local other_joker = G.jokers.cards[1]
				local other_joker_ret = SMODS.blueprint_effect(card, other_joker, context)
				if other_joker_ret then
					return other_joker_ret
				end
			end  
		```

## Optional Features
There are some optional scoring areas and contexts that can be enabled by using the following function.

```lua
SMODS.current_mod.optional_features = function()
    return {
        post_trigger = true,
        retrigger_joker = true,
        quantum_enhancements = true,
		cardareas = {
            discard = true,
            deck = true
        }
    }
end
```

These features **will** have an impact on performance, so only turn them on if you need their functionality.

### Retriggers
This feature allows you to retrigger other **Jokers**, much like how you can retrigger playing cards by default.
Retriggers are calculated in the following context.

```lua
if context.retrigger_joker_check then
```

```lua
context.retrigger_joker_check -- flag to identify this context, always TRUE
context.other_card -- a reference to the card being retriggered
context.other_context -- the context table that the joker triggered in
context.other_ret -- the return table from the joker trigger
}
```

Using this, you can narrow down specific situations in which to retrigger jokers. Return `repetitions = 1` to retrigger the joker.

The calculation will then be repeated with `retrigger_joker = retrigger_card` added to the original context table. If you want to block retriggers on a joker, you can either:
	- add `no_retrigger = true` to your return table
	- add `and not context.retrigger_joker` to your context check

### Post Triggers
This feature allows you to trigger effects **after** other Jokers trigger.
Post triggers are calculated in the following context.

```lua
if context.post_trigger then
```

```lua
context.post_trigger -- flag to identify this context, always TRUE
context.other_card -- a reference to the card being retriggered
context.other_context -- the context table that the joker triggered in
context.other_ret -- the return table from the joker trigger
context.blueprint_card -- only if present in the initial context
```

Similarly to retriggers, you can use these values to narrow down to specific situations if required. Post trigger returns are calculated the same as normal returns.

### Quantum Enhancements
Quantum enhancements allow playing cards to function as if they have an enhancement that they don't have.

 > [!WARNING]
 > This feature may cause crashes if `SMODS.has_enhancement` is called outside of a strict context check.
  
Quantum enhancements are calculated in the follow context.
```lua
if context.check_enhancement then
```

```lua
context.check_enhancement -- flag to identify this context, always TRUE
context.other_card -- a reference to the card being retriggered
context.no_blueprint -- this is an internal flag to stop blueprint from copying these effects
```

To add the quantum enhancements to specific cards, you should return the enhancement key and true, like so.
```lua
return {
	m_wild = true -- make cards function as wild cards
}
```

### Card Areas
Turning these card areas on allows every calculation call to iterate over the cards currently in the deck, and the cards currently in the discard pile. They can be specifically accessed by checking for either `context.card_area == G.deck` or `context.cardarea == G.discard`.

## Scaling Values
Scaling values within cards can be a simple line of code as shown in the above examples, but the by opting in to using `SMODS.scale_card` you can now allow other effects to detect, respond to, or manipulate, your scaling. This function will handle scaling your value and display an automatic message. The function is **entirely** customisable so you can tune it to your exact requirements.
### Using `SMODS.scale_card`
#### Basic Structure
This example code will scale the `chips` value of the card by the `change` value. It will display a `"Upgrade!"` message with a `G.C.FILTER` background. The amount the value changes by *could* be adjusted by other effects.

```lua
SMODS.scale_card(card, {
	ref_table = card.ability.extra, -- the table that has the value you are changing in
    ref_value = "chips", -- the key to the value in the ref_table
	scalar_value = "change", -- the key to the value to scale by, in the ref_table by default
})
```

The config of this joker would be defined as `config = {extra = {chips = 5, change = 2}}` for example. It is possible to take your `scalar_value` from a different table, by adding `scalar_table = card.ability.other_table` for example.

#### Blocking Scaling Manipulation
As this function allows for scaling detection effects to work, I would recommend it's use over doing it manually, but I understand the scaling manipulation can be an undesirable effect for some people. Therefore, you can block this from happening by adding `block_overrides` to your function call.

```lua
block_overrides = {
	value = true, -- blocks modifications to the ref_value
	scalar = true, -- blocks modifications to the scalar_value
	message = true -- blocks modifications to the scaling_message
}
```

This would block all modifications from other cards. You can also use a subset of these if you wish.

#### Customising The Scaling
The basic structure example above is for an **additive** effect with a `"Upgrade!"` message, but you might want to display something else.
##### Messages
It is easy to change the message to use any message in `G.localization.misc.v_dictionary_parsed`. Add `message_key = 'a_chips'` to change the message to one of these. You can also add `message_colour = G.C.RED` to change the colour displayed. These messages automatically pass the `scalar_value` as the variable, apart from when using `a_xmult` which passes the new total amount, to match vanilla cases. If you don't want **any** message at all, add `no_message = true`.
You can also provide your own custom message, much like returning a message from a calculate function.

```lua
scaling_message = {
	message = "Example message!",
	colour = G.C.BLUE
}
```
##### Scaling
By default, this function will automatically handle scaling that uses addition, subtraction, and multiplication. You can switch between these by adding an `operation` to the function call. Valid options are `operation = '-'` and `operation = 'X'` to switch to subtraction or multiplication respectively. If you need an entirely custom scaling function, you can set `operation` to be a function instead. Here is an example of Canio, where `face_cards` is a number defined before the `SMODS.scale_card` function.

```lua
operation = function(ref_table, ref_value, initial, change)
	ref_table[ref_value] = initial + face_cards*change
end,
```

### Responding to Scaling
#### Detecting Scaling
On the other side of this feature, is the ability to detect and manipulate value scaling. This is done by adding a `calc_scaling` function to your Joker-type card definitions. Within this function you can do any effects you need to do, and return a table of different effects. There is the ability to control timings somewhat with this return which will be explained below.

```lua
calc_scaling = function(self, card, other_card, initial_value, scalar_value, args)
	if scalar_value > 0 then
		return {
			message = 'Pre Scale',
			post = {
				message = 'Post Scale'
			}
		}
	end
end
```

This example will play a message **before** the scaling event, and **after** the scaling event. These tables accept any standard calculation return key. The `initial_value` and `scalar_value` values are dynamic, and respect any prior manipulation from other Joker-type cards. The `args` value is the initial table that was passed to `SMODS.scale_card`.

#### Manipulating Scaling
Manipulating scaling uses the same function as detection, but requires specific tables to be returned in the table.
```lua
return {
	override_value = { -- this will override the initial_value
		value = X, -- set the initial_value to X
		-- other calculation return keys accepted here, timing is before the scaling event
	},
	override_scalar_value = { -- this will override the scalar_value
		value = X, -- set the scalar_value to X
		-- other calculation return keys accepted here, timing is before the scaling event
	},
	override_message = { -- this will override the scaling_message
		message = 'override message'
		-- other calculation return keys here will be evaluated WITH the message timing
	}
}
``` 

## Using Probability
There are times where you may wish to code an effect that only has a **chance** to trigger, similar to Bloodstone from the vanilla game. Whilst you can use a random number and check it is within your bounds manually, there are some helper functions provided to ensure that other probability modifying effects are respected. These functions can be used to provide the values you display in your description, and also to be used in a conditional check for whether to trigger your effect or not. It is important to use the `SMODS.pseudorandom_probability` function such that effects that are based on probability rolls succeeding or failing can be triggered correctly.

- `SMODS.get_probability_vars(trigger_obj, base_numerator, base_denominator, identifier, from_roll, no_mod)`
	- Used to retrieve the updated **numerator** and **denominator** respecting any other effects that modify the probability. If you want a non-modifiable probability, don't use this function
	- `trigger_obj` - the object that the probability is coming from
	- `base_numerator`/`base_denominator` - the base values of your probability without any modification
	- `identifier` - optional string used to identify this specific probability *(suggested format: modprefix_objectkey)*
	- `from_roll` - internal value set to control animations **\*NOT FOR GENERAL USE**
	- `no_mod` - internal value set to block modifications *(generally used in SMODS.pseudorandom_probability)*
- `SMODS.pseudorandom_probability(trigger_obj, seed, base_numerator, base_denominator, identifier, no_mod)`
	- Used to determine whether the probability succeeds, with respect to the game seed. Returns either `true` or `false`
	- `trigger_obj` - the object that the probability is coming from
	- `seed` - a string used to generate the random result
	- `base_numerator`/`base_denominator` - the base values of your probability without any modification
	- `identifier` - optional string used to identify this specific probability, defaults to the `seed` if not provided
	- `no_mod` - set to `true` if you don't want your probability to be modified

Here is an example of using these functions to create a 1 in 4 chance to give 100 chips.

```lua
config = {extra = {numerator = 1, denominator = 4, chips = 100}},
loc_vars = function(self, info_queue, card)
	local num, denom = SMODS.get_probability_vars(card, card.ability.extra.numerator, card.ability.extra.denominator)
	return {vars = {num, denom, card.ability.extra.chips}}
end,
calculate = function(self, card, context)
	if context.joker_main and SMODS.pseudorandom_probability(card, 'example_prob', card.ability.extra.numerator, card.ability.extra.denominator) then
		return {
			chips = card.ability.extra.chips
		}
	end
end
```

Modifying and responding to probability checks is explained in the relevant contexts below.

## Adding Calculation Zones
By default, calculations operate over each of these areas: the cards that have been played *(G.play)*, the cards held in hand *(G.hand)*, the jokers and consumables *(G.jokers)*, the vouchers you have redeemed *(G.vouchers)*, the selected deck *(G.GAME.selected_back)*, and the current blind *(G.GAME.blind)*, as well as the optional areas mentioned above.

It is possible to add your own custom areas to the calculate process by hooking, or injecting into, `SMODS.get_card_areas`. This function can be found in `src/utils.lua` in the **smods** folder.

If you prefer to inject your code using a lovely patch, there are target lines provided for each type of area. An example patch to do this is below.
```toml
[[patches]]
[patches.pattern]
target = "=[SMODS _ "src/utils.lua"]"
pattern = '''-- TARGET: add your own CardAreas for joker evaluation'''
position = "after"
payload = '''t[#t+1] = G.custom_card_area'''
match_indent = true
```

## Adding New Calculations
There are situations where you would like to add your own calculation steps. This is easily done by using `SMODS.calculate_context(context, return_table)`.
This function **must** be given a `context` table, and it will pass your context through each calculation zone. If there is no `return_table` given to the function, it will trigger the effects automatically. If you wish to search for specific effects, or modify the returns of the calculation, adding a `return_table` will disable the automatic triggering.
*You can see implementations of `SMODS.calculate_context` by searching your lovely dumps and the SMODS files for the function.*

# Contexts

A **context** is a table of data that the game sends to your calculate function at different points of the game. It is a way of triggering your effects within these timings, and also a way of retrieving some useful data at that moment. 

Below is a list of every context currently in the game. There is a short explanation of when the context is called, followed by a standard logic check for the context - this can be customised to provide a tighter check. There is also a list of the flags that each context has, as well as a description for what they are.

> [!IMPORTANT]
> All calculation of jokers that evaluates no secondary card is called with `main_eval = true` in the context table. This should be used for the main evaluation of the joker within that context. See `context.end_of_round` for more information.

## Main Scoring Contexts

Each scoring context shares some similar properties, explained here.

```lua
context.cardarea -- This is used to check what area the card being evaluated is in.
-- Possible options are by default G.play, "unscored", G.hand and G.jokers
context.scoring_hand -- In contexts evaluated during the scoring loop, this contains
-- a table of the cards that score
context.full_hand -- In contexts evaluated during the scoring loop, this contains a
-- table of all the cards that are played
context.scoring_name -- In context evaluated during the scoring loop, this contains
-- a string of the played poker hand name
context.poker_hands -- In contexts evaluated during the scoring loop, this contains
-- a table of all poker hands contained within the scoring cards
```

These values can be added to the conditional checks to narrow down when your effects happen. For example, checking for `context.cardarea == G.play` would allow your effects to only happen on playing cards that are part of the played poker hand.

Detailed here is an ordered list of all contexts that are used during the main scoring loop. These are the only contexts where returning chip and mult manipulations works.

---
#### context.before
This context is used for effects that happen before scoring begins.
**Any chip and mult returns here will not be added to the score.**

```lua
if context.before then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.before -- boolean value to flag this context, always TRUE
```

---
#### context.initial_scoring_step
This context is used for modifying the initial chip and mult values **before** any cards are scored.

```lua
if context.initial_scoring_step then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.initial_scoring_step -- boolean value to flag this context, always TRUE
```
---
#### context.main_scoring
This context is used for the effects from playing cards when they are scored. This is used for enhancements, editions and seals (or any other card modifiers)

```lua
if context.main_scoring and context.cardarea == G.play then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.main_scoring -- boolean value to flag this context, always TRUE
```

---
#### context.individual
This context is used for triggering joker effects on playing cards. It iterates over the cards in each area one by one. Change the `cardarea` you are checking to apply effects to cards in different areas.

```lua
if context.individual and context.cardarea == G.play then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.individual -- boolean value to flag this context, always TRUE
context.other_card -- the playing card to apply the effect to
```

---
#### context.repetition
This context is used for adding repetitions to playing cards. The `card_effects` table can be used to apply repetitions to cards that do specific things. You must return `repetitions = X`, where `X` is a number, when using this context. If your return table does not contain it, it will be ignored.

```lua
if context.repetition and context.cardarea == G.play then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.repetition -- boolean value to flag this context, always TRUE
context.repetition_only -- boolean value set to true within calculate functions on playing card modifiers
context.card_effects -- this is a table of effects that has been calculated during context.main_scoring
```

---
#### context.pre_joker
This context is used for triggering effects of **editions** on jokers before the joker does it's main scoring. *(used for chips/mult)*

```lua
if context.pre_joker then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.edition -- boolean value to flag this context, always TRUE
context.pre_joker -- boolean value to flag this context, always TRUE
```

---
#### context.joker_main
This context is used for triggering normal scoring effects on **jokers**.

```lua
if context.joker_main then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.joker_main -- boolean value to flag this context, always TRUE
```

---
#### context.other_joker
This context is used for triggering joker effects from other jokers. It will pass each other 'Joker' style object to your calculate function

```lua
if context.other_joker then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.other_joker -- this is a reference to the other object being considered. It is present for Joker objects, but other areas have their own identifier.
-- By default these are context.other_consumeable and context.other_voucher.
context.other_main -- this is a reference to the other object being considered where the identifier does not change.
```

---
#### context.post_joker
This context is used for triggering effects of **editions** on jokers after the joker does it's main scoring. *(used for xmult and xchips)*

```lua
if context.post_joker then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.edition -- boolean value to flag this context, always TRUE
context.post_joker -- boolean value to flag this context, always TRUE
```

---
#### context.final_scoring_step
This context is used for any effects after cards have been calculated but before the score is totalled.

```lua
if context.final_scoring_step then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.final_scoring_step -- boolean value to flag this context, always TRUE
```

---
#### context.destroy_card
This context is used for marking cards to be destroyed after a hand has been played. To destroy the card you must add `remove = true` to your return table.

```lua
if context.destroy_card and context.cardarea == G.play then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.destroy_card -- this is a reference to the playing card being checked
context.destroying_card -- this is a reference to the playing card being checked ONLY if it's a scored card
```

---
#### context.remove_playing_cards
This context is used for triggering effects that are conditional to cards being removed.

```lua
if context.remove_playing_cards then
```

```lua
context.cardarea, context.scoring_hand, -- note scoring hand does not always exist here
context.remove_playing_cards -- boolean value to flag this context, always TRUE
context.removed -- a table of cards that have been destroyed
```

> [!WARNING]
> This is also called after other destruction events without the `scoring_hand` part of the context. **Do not** rely on it in your calculation.

---
#### context.after
This context is used for effects after scoring. **Any chip and mult returns here will not be added to the score.**

```lua
if context.after then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.after -- boolean value to flag this context, always TRUE
```

## Other Contexts
There are other calculations that the game does at different points of playing the game. 
These contexts do not always share the properties of the above ones, but you can use this snippet to see what each context contains.

```lua
local output = ""
for k, v in pairs(context) do output = output .. k .. ': ' .. type(v) .. ' / ' end
print(output)
-- Prints a string such as this:
-- main_eval: boolean / buying_card: boolean / cardarea: table / card: table /
```

---
#### context.debuffed_hand
This context is used for trigger effects when playing a hand that is **debuffed** by the current blind.

```lua
if context.debuffed_hand then
```

```lua
context.cardarea, context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.debuffed_hand -- boolean value to flag this context, always TRUE
```

---
#### context.end_of_round
This context is used for end of round effects. The end of round context will be called multiple times to allow playing cards to have effects too. Take note of the recommended condition checks here.

*For a basic effect at the end of round that triggers __once__. This can also be used within playing card modifiers.*
```lua
if context.end_of_round and context.main_eval then
```

```lua
context.cardarea -- Note that G.play/unscored are not valid here
context.end_of_round -- boolean value to flag this context, always TRUE
context.main_eval -- boolean value to flag this context within a joker-type object, always TRUE
context.game_over -- boolean value to flag whether the game is over or not
context.beat_boss -- boolean value to flag whether a Boss Blind is active
```

> [!NOTE]
> You can return `saved = true` or `saved = 'loc_key'` to prevent a game loss. The loc_key will allow for a custom message to be displayed, otherwise it will default to `Saved by Mr. Bones`

*For an effect on playing cards from a joker-type object.*
```lua
if context.end_of_round and context.individual and context.cardarea == G.hand then
```

```lua
context.cardarea -- Note that G.play/unscored are not valid here
context.end_of_round -- boolean value to flag this context, always TRUE
context.individual -- boolean value to flag this context, always TRUE
context.other_card -- the playing card to apply the effect to
context.beat_boss -- boolean value to flag whether a Boss Blind is active
```

*For a repetition on playing cards from a joker-type object.*
```lua
if context.end_of_round and context.repetition and context.cardarea == G.hand then
```

```lua
context.cardarea -- Note that G.play/unscored are not valid here
context.end_of_round -- boolean value to flag this context, always TRUE
context.repetition -- boolean value to flag this context, always TRUE
context.other_card -- the palying card to apply the effect to
context.beat_boss -- boolean value to flag whether a Boss Blind is active
context.card_effects -- this is a table of effects that has been calculated during the end of round step
```

*For an effect from playing card modifiers.*
```lua
if context.playing_card_end_of_round and context.cardarea == G.hand then
```

```lua
context.cardarea -- Note that G.play/unscored are not valid here
context.end_of_round -- boolean value to flag this context, always TRUE
context.playing_card_end_of_round -- boolean value to flag this context, always TRUE
context.beat_boss -- boolean value to flag whether a Boss Blind is active
```

*For a repetition from playing card modifiers.*
```lua
if context.playing_card_end_of_round and context.repetition and context.cardarea == G.hand then
```

```lua
context.cardarea -- Note that G.play/unscored are not valid here
context.end_of_round -- boolean value to flag this context, always TRUE
context.playing_card_end_of_round -- boolean value to flag this context, always TRUE
context.repetition -- boolean value to flag this context, always TRUE
context.beat_boss -- boolean value to flag whether a Boss Blind is active
context.card_effects -- this is a table of effects that has been calculated during the end of round step
```

---
#### context.setting_blind
This context is used for effects when the blind is started.

```lua
if context.setting_blind then
```

```lua
context.setting_blind -- boolean value to flag this context, always TRUE
context.blind -- a reference to the selected blind
```

---
#### context.drawing_cards
This context is used when cards are about to be drawn to the hand, **before** the cards are actually drawn. Returning `modify = number` or `cards_to_draw = number` will change the amount of cards that will be drawn.

```lua
if context.drawing_cards then
```

```lua
context.drawing_cards -- flag to identify this context, always TRUE
context.amount -- the number of cards being drawn
```

---
#### context.hand_drawn/context.other_drawn
This context is used **after** cards are drawn to the hand. There is a differentiation between cards being drawn during a Blind, and outside of a Blind *(such as when opening a Booster Pack)*.

```lua
if context.hand_drawn then -- during a blind
```

```lua
if context.other_drawn then -- outside a blind
```

```lua
context.hand_drawn -- the list of cards that were drawn during a blind
context.other_drawn -- the list of cards that were drawn outside a blind
context.first_hand_drawn -- TRUE for the first hand drawn for the round
```

---
#### context.pre_discard
This context is used **before** cards are discarded.

```lua
if context.pre_discard then
```

```lua
context.pre_discard -- flag to identify this context, always TRUE
context.full_hand -- the list of all cards that are being discarded
context.hook -- true if the cards are being discarded by The Hook (may be used by other mods)
```

---
#### context.discard
This context is used on individual cards as they are discarded.

```lua
if context.discard then
```

```lua
context.discard -- flag to identify this context, always TRUE
context.other_card -- the card that is being discarded
context.full_hand -- the list of all cards that are being discarded
```
---
#### context.press_play
This context is used when the Play Hand button is pressed.

```lua
if context.press_play then
```

---
#### context.evaluate_poker_hand
This context is used to alter the poker hand that the played hand counts as. It can also provide cosmetic alterations too. For example, `replace_scoring_name = "Full House"` would make the hand score as a Full House, whilst `replace_display_name = "Fullest House"` would only change the text shown in the UI.

>[!CAUTION]
> As an advanced use, you can return `replace_poker_hands = {}` to provide a new updated poker hands table. It is only recommend you do this if you fully understand how this table should be structured.

```lua
if context.evaluate_poker_hand then
```

```lua
context.evaluate_poker_hand -- flag to identify this context, always TRUE
context.full_hand -- the list of all cards that are being selected
context.scoring_name -- the current poker hand
context.display_name -- the display name for the current poker hand
context.scoring_hand -- the list of cards in the selected hand that would be scored for the current poker hand
context.poker_hands -- the list of poker hands contained within the selected cards
```

---
#### context.modify_scoring_hand
This context is used when determining which cards in the selected hand should be scored, either while selecting the cards **or** when the hand is played. Each card passes through the context, and returning `add_to_hand = true` or `remove_from_hand = true` will do the according action *(removing has a higher priority than adding)*.

```lua
if context.modify_scoring_hand then
```

```lua
context.modify_scoring_hand -- flag to identify this context, always TRUE
context.other_card -- the individual card being evaluated for the hand
context.full_hand -- the list of all cards that are being played
context.scoring_hand -- the list of cards that are currently considered to be scoring (not immediately affected by results returned by this context)
context.in_scoring -- false while the hand is being selected, and true when the hand is played
```

---
#### context.debuff_hand
This context is used to check if the hand should score, for effects like The Eye or The Mouth. Returning `debuff = true` or `prevent_debuff = true` will do the according action *(preventing debuff has a higher priority)*. You can also specify a `debuff_text` string to be displayed on screen when the hand is selected and a `debuff_source` object which will wiggle to indicate where the debuff comes from.

```lua
if context.debuff_hand then
```

```lua
context.full_hand, context.scoring_hand, context.scoring_name, context.poker_hands
context.debuff_hand -- flag to identify this context, always TRUE
context.check -- true while the hand is being selected, and false when the hand is played
```

  ---
#### context.modify_hand
This context is used to modify the initial values of a hand, at the same time as `Blind:modify_hand`. You can change the chips and mult by modifying `_G.mult` and `_G.hand_chips` directly.

```lua
if context.modify_hand then
```

```lua
context.modify_hand -- flag to identify this context, always TRUE
context.full_hand -- the list of all cards that are being selected
context.scoring_name -- the current poker hand
context.scoring_hand -- the list of cards in the selected hand that would be scored for the current poker hand
context.poker_hands -- the list of poker hands contained within the selected cards
```

---
#### context.debuff_card
This context is used to check if each card in the deck should be debuffed when selecting a blind. Returning `debuff = true` or `prevent_debuff = true` will do the according action *(preventing debuff has a higher priority)*.

```lua
if context.debuff_card then
```

```lua
context.debuff_card -- the card being evaluated for debuffing
```

---
#### context.stay_flipped
This context is used to check whether a card should be flipped or not when it moves from one area to another. Returning `stay_flipped = true` or `prevent_stay_flipped = true` will do the according action *(preventing flipped has a higher priority)*.

```lua
if context.stay_flipped then
```

```lua
context.stay_flipped -- flag to identify this context, always TRUE
context.other_card -- the card being evaluated for flipping
context.from_area -- the card area the card was in previously
context.to_area -- the card area the card is moving into
```
  
---
#### context.blind_disabled
This context is used when a Boss Blind is disabled.

```lua
if context.blind_disabled then
```
  ---
#### context.blind_defeated
This context is used when a Blind is defeated.

```lua
if context.blind_defeated then
```
  ---
#### context.round_eval
This context is called **after** the end of the round, just before end-of-round cash is determined.

```lua
if context.round_eval then
```

  >[!NOTE]
  >You can call `add_round_eval_row` in this context to add to the cash out display.

---
#### context.modify_ante
This context is used when the ante is about to change. Returning `modify = number` will change the amount that the ante will change by.

```lua
if context.modify_ante then
```

```lua
context.modify_ante -- the amount the ante will change by
context.ante_end -- TRUE if the ante is being changed by defeating a Boss Blind
```
>[!TIP]
>Setting `modify = 0` will stop the ante from changing

---
#### context.ante_change
This context is used when the ante changes.

```lua
if context.ante_change then
```

```lua
context.ante_change -- the amount the ante has changed by
context.ante_end -- true if the ante is being changed by defeating a Boss Blind
```
  
---
#### context.starting_shop
This context is used when starting the shop.

```lua
if context.starting_shop then
```
  ---
#### context.ending_shop
This context is used when leaving the shop.

```lua
if context.ending_shop then
```

--- 
#### context.open_booster
This context is used after a Booster Pack is opened.

```lua
if context.open_booster then
```

```lua
context.open_booster -- flag to identify this context, always TRUE
context.card -- the booster pack object that was opened
context.booster -- the booster pack center that was opened
```

>[!TIP]
>You can access the cards in the booster pack by checking in `G.pack_cards.cards`
  
---
#### context.skipping_booster
This context is used when a Booster Pack is skipped.

```lua
if context.skipping_booster then
```

```lua
context.skipping_booster -- flag to identify this context, always TRUE
context.booster -- the booster pack center that was skipped

```
 --- 
#### context.ending_booster
This context is used when leaving a Booster Pack, either from skipping or from exhausting the choices.

```lua
if context.ending_booster then
```

```lua
context.ending_booster -- flag to identify this context, always TRUE
context.booster -- the booster pack center that has ended
```
  ---
#### context.buying_card
This context is used when buying a card from the shop, including Vouchers and Booster Packs.

```lua
if context.buying_card then
```

```lua
context.buying_card -- flag to identify this context, always TRUE
context.card -- the card that was bought
context.buying_self -- true when the evaluated card is the card that is being bought. recommended to use instead of context.buying_card when applicable
```

  >[!NOTE]
  >The card being bought will evaluate twice if you only check for `context.buying_card`. It is important to check for the existence of `context.buying_self` to prevent unintended side effects.

---
#### context.selling_card
This context is used when any card is sold.

```lua
if context.selling_card then
```

```lua
context.selling_card -- flag to identify this context, always TRUE
context.card -- the card being sold
```
  
---
#### context.selling_self
This context is used to evaluate a card as it is sold. *(Unlike `context.buying_card`, `context.selling_card` is **not** true during this context, and is evaluated separately.)*

```lua
if context.selling_self then
```
  ---
#### context.using_consumeable
This context is used when a consumable is used.

```lua
if context.using_consumeable then
```

```lua
context.using_consumeable -- flag to identify this context, always TRUE
context.consumeable -- the consumeable being used
context.area -- the card area that the consumeable is being used from
```
  ---
#### context.reroll_shop
This context is used when rerolling in the shop.

```lua
if context.reroll_shop then
```

```lua
context.reroll_shop -- flag to identify this context, always TRUE
context.cost -- how much it cost to reroll the shop
```
 
---
#### context.create_shop_card
This context is used when a card is created for the main shop area. You can return a table as `shop_create_flags` that will be passed into `SMODS.create_card` to change which card will be created.

```lua
if context.create_shop_card then
```

```lua
context.create_shop_card -- flag to identify this context, always TRUE
context.set -- The selected set of the card that is to be created
```

---
#### context.modify_shop_card
This context is used when a card is added to the main shop area. You can call other functions on this card, such as `Card:set_cost`, to alter the card within the shop. This context could also be used to respond to certain things appearing in the shop.

```lua
if context.modify_shop_card then
```

```lua
context.modify_shop_card -- flag to identify this context, always TRUE
context.card -- The card that has been added to the shop
```

---
#### context.money_altered
This context is used whenever money is gained or lost.

```lua
if context.money_altered then
```

```lua
context.money_altered -- flag to identify this context, always TRUE
context.amount -- the amount that money has changed by
context.from_shop -- true if the money changed while in the shop
context.from_tarot -- true if the money changed from using a consumeable
context.from_scoring -- true if the money changed while scoring
```

  >[!NOTE]
  >The tagging within this context *may* be inaccurate. Please report any inaccuracies to the SMODS team.

---
#### context.skip_blind
This context is used when a Blind is skipped.

```lua
if context.skip_blind then
```

---
#### context.tag_added
This context is used for effects that happen when a tag is added to your tag area.

```lua
if context.tag_added then
```

```lua
context.tag_added -- the tag that was created
```
  ---
#### context.prevent_tag_trigger
This context is used to prevent tags from triggering. You can return `prevent_trigger = true` to stop the tag from triggering.
*This context could also be used to modify a tag before it is triggered.*

```lua
if context.prevent_tag_trigger then
```

```lua
context.prevent_tag_trigger -- the tag that is about to trigger
context.other_context -- the context being checked for the tag
```

---
#### context.tag_triggered
This context is used after a tag successfully triggers.

```lua
if context.tag_triggered then
```

```lua
context.tag_triggered -- the tag that was triggered
```
 
---
#### context.playing_card_added
This context is used when playing cards are added to the deck. *(This will only be called once even if several cards are added.)*

```lua
if context.playing_card_added then
```

```lua
context.playing_card_added -- flag to identify this context, always TRUE
context.cards -- the list of cards being added
```

>[!TIP]
>If you are ever adding playing cards, to trigger this context run `playing_card_joker_effects(cards)`

---  
#### context.card_added
This context is used when a **non-playing** card is added (called automatically within `Card:add_to_deck`).

```lua
if context.card_added then
```

```lua
context.card_added -- flag to identify this context, always TRUE
context.card -- the card that was added
```

---
#### context.joker_type_destroyed
This context is used whenever a **non-playing** card is destroyed. Return `no_destroy = true` to prevent the destruction.

```lua
if context.joker_type_destroyed then
```

```lua
context.joker_type_destroyed -- flag to identify this context, always TRUE
context.card -- the card that is being destroyed
context.shatters -- true if the card is being destroyed from "shattering" (meaning Card:shatter() was used on it)
```

---
#### context.change_suit/context.change_rank
This context is used for effects that happen whenever a playing card changes either suit or rank. These are *technically* the same context that adapts depending on which properties change.

```lua
if context.change_suit then
```

```lua 
if context.change_rank then
```

```lua
context.cardarea,
context.other_card -- the card that has changed
context.change_rank -- boolean value to flag that the rank has changed
context.new_rank -- the id of the rank the card has changed to, only present with change_rank
context.old_rank -- the id of the rank the card has changed from, only present with change_rank
context.rank_increase -- boolean value to flag whether the rank increased, only present with change_rank
context.change_suit -- boolean value to flag that the suit has changed
context.new_suit -- the key of the suit the card has changed to, only present with change_suit
context.old_suit -- the key of the suit the card has changed from, only present with change_suit
```

---
#### context.setting_ability

This context is used when a card sets its ability table. Common use-case is checking when a playing card changes enhancement. *(Does not include initial card creation.)*

```lua
if context.setting_ability then
```

```lua
context.setting_ability -- flag to identify this context, always TRUE
context.other_card -- the card that is setting the ability
context.new -- the key for the newly set ability
context.old -- the key for the card's previous ability
context.unchanged -- true if the new key is the same as the old key
```

---
#### context.mod_probability
This context should be used for any additive or multiplicative modifications to the probability. Return `numerator = amount` or `denominator = amount` to change them respectively.

```lua
if context.mod_probability then
```

```lua
context.numerator -- current numerator
context.denominator -- current denominator
context.mod_probability -- boolean value to flag this context, always TRUE
context.trigger_obj -- the object that the roll comes from (note: The Wheel blind switches between the blind object and the blind prototype object)
context.identifier -- a string value to identify the source of the roll
context.from_roll -- internal value used to only trigger certain return values when the roll is made rather than a tooltip update
```

---
#### context.fix_probability
This context should be used for setting either the numerator or the denominator. This takes priority over any modifications from `context.mod_probability`. Return `numerator = amount` or `denominator = amount` to change them respectively.

```lua
if context.fix_probability then
```

```lua
context.numerator -- current numerator
context.denominator -- current denominator
context.fix_probability -- boolean value to flag this context, always TRUE
context.trigger_obj -- the object that the roll comes from (note: The Wheel blind switches between the blind object and the blind prototype object)
context.identifier -- a string value to identify the source of the roll
context.from_roll -- internal value used to only trigger certain return values when the roll is made rather than a tooltip update
```

---
#### context.pseudorandom_result
This context should be used for setting either the numerator or the denominator.

```lua
if context.pseudorandom_result then
```

```lua
context.pseudorandom_result -- boolean value to flag this context, always TRUE
context.result -- the result of the chance roll
context.numerator -- the numerator used for the chance
context.denominator -- the denominator used for the chance
context.trigger_obj -- the object that the roll comes from (note: The Wheel blind switches between the blind object and the blind prototype object)
context.identifier -- a string value to identify the source of the roll
```

---
#### context.check_eternal
This context is used to determine whether a card should be considered to be Eternal (unable to be sold or destroyed).  You can return `no_destroy = true` within this context to add the Eternal effect to a card. Returning `no_destroy = {override_compat = true}` will apply the effect to cards that are marked as `eternal_compat = false`.

```lua
if context.check_eternal then
```

```lua
context.check_eternal -- flag to identify this context, always TRUE
context.other_card -- the card being evaluated
context.trigger -- the card checking for destruction, OR a table value containing the following:
	context.trigger.from_sell -- true when the card is checking if it can be sold
	context.trigger.destroy_cards -- true when the destruction effect is coming from SMODS.destroy_cards()
```

---
#### context.blueprint
This context is used when a calculation is being copied from a different object. It contains all properties of the original context, alongside these extra properties.

```lua
context.blueprint -- flag to identify copy effect
context.blueprint_card -- the original object the copy effect came from
context.blueprint_copier -- the current object copying the effect (differs when copy effects are chained)
context.blueprint_copiers_stack -- ordered table of objects copying the effect (used when copy effects are chained)
```

---

*Thanks to vitellary for their help documenting the various contexts.*
