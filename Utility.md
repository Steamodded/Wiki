# Utility functions
Steamodded provides utility functions that extend or replace vanilla functionality or provide other useful tools you may need when making your mod. This page contains information on these functions. Check out `src/utils.lua` if you'd like to learn more about a function's implementation.

## Debugging 
- `inspect(table) -> string`
    - Given an input table, outputs a shallow mapping of keys to values as a string. Gives no further information on subtables.
- `inspectDepth(table) -> string`
    - Given an input table, recursively creates a string representation up to a depth of 5.
- `inspectFunction(func) -> string`
    - Given an input function, outputs details on its name, source, line of definition and number of upvalues.
- `serialize(t, indent) -> string`
    - Given an input table, creates a string containing Lua code that evaluates to the serializable part of `t`. Information may be lost, and circular references are not resolved.
- `serialize_string(s) -> string`
    - Serializes the provided string.
- `tprint(t, indent) -> string`
    - Recursively stringifies an input table into pseudo-valid Lua code, leaving non-serializable values and tables above a depth of 5 into their default string representations.
- `SMODS.deepfind(tbl, val, mode, immediate) -> table`
    - Searches for provided `val` anywhere deep within the provided `tbl`. Returns a table of finds. 
    - `mode` - `"index"`/`"i"` will have `val` compared to the indexes in the tables. `"value"`/`"v"` will have `val` compared to the values in the tables. 
    - `immediate` - Will return immediately after finding the value the first time.
- `SMODS.debug_calculation()`
    - Enables debugging of Joker calculations. 
    - Every time that `Card:calculate_joker()` is called, `G.contexts` is updated for every value within `context`.

## Number formatting
- `round_number(num, precision) -> number`
    - Rounds the input number to a given amount of decimal places.
- `format_ui_value(value) -> string`
    - Stringifies the input if it is not a number. Otherwise return the number as it should be displayed in the UI (e.g. scientific notation).

## Randomness
- `SMODS.poll_rarity(_pool_key, _rand_key) -> string|number` 
    - Generates a random rarity for the given pool (the only vanilla pool that supports rarities is `'Joker'`). If `_rand_key` is present, use it as a seed.
- `SMODS.poll_seal(args) -> string?`
    - Checks if a seal should be generated, and generates one according to the specified arguments if so. The following arguments are supported:
    - `key` - Randomness seed for the check whether to generate a seal, defaults to `'stdseal'`.
    - `mod` - Multiplier to the base rate at which seals appear.
    - `guaranteed` - If this is `true`, always generate a seal.
    - `options` - A table of possible seals to generate. Defaults to all available seals.
    - `type_key` - Randomness seed for the roll which seal to generate.
- `SMODS.poll_enhancement(args) -> string?`
    - Checks if an enhancement should be generated, and generates one according to the specified arguments if so. The following arguments are supported: 
    - `key` - Randomness seed for the check whether to generate an enhancement, defaults to `'std_enhance'`.
    - `mod` - Multiplier to the base rate at which enhancements appear.
    - `guaranteed` - If this is `true`, always generate an enhancement.
    - `options` - A table of possible enhancements to generate. Defaults to all available enhancements.
    - `type_key` - Randomness seed for the roll which enhancement to generate.

## Mod-facing utilities
These functions facilitate specific tasks that many mods may use but may be harder to achieve when implemented individually. Some replace base game functions to create a more usable interface.
- `SMODS.find_mod(id) -> table`
    - Returns a list of mods that either match the given mod ID or provide it, and are enabled and loaded. 
    - The result of `next(SMODS.find_mod(id))` can be used to determine if a mod is present, akin to finding cards with `SMODS.find_card`.
- `SMODS.load_file(path, id) -> function`
    - Given a path to a file in the context of the mod currently being loaded, loads the file contents and returns them as a function. If this function is called after the mod loading stage, a mod's `id` must be specified in order to find the correct file.
    - Return type is the same as [love.filesystem.load](https://love2d.org/wiki/love.filesystem.load) and [loadfile](https://www.lua.org/manual/5.1/manual.html#pdf-loadfile).
    - Example usage: `assert(SMODS.load_file('jokers.lua'))()`
- `SMODS.juice_up_blind()`
    - Plays a 'juice up' animation on the Blind chip.
- `SMODS.change_base(card, suit, rank) -> Card?, string?`
    - Given a `Card` representing a playing card, changes the card's suit, rank, or both. Either argument may be omitted to retain the original suit or rank.
    - This function returns `nil` if it fails, with the second argument being a string with an error message. It is recommended to always wrap calls to it in `assert` so errors don't go unnoticed.
    - Examples: `assert(SMODS.change_base(card, 'Hearts'))` converts a card into Hearts. `assert(SMODS.change_base(card, nil, 'Ace'))` converts a card into an Ace. `assert(SMODS.change_base(card, 'Hearts', 'Ace'))` converts a card into an Ace of Hearts.
- `SMODS.modify_rank(card, amount) -> Card?, string?`
    - Given a `Card` representing a playing card, increases or decreases the card's rank by the specified `amount`. The rank is increased if `amount` is positive and decreased if it is negative.
    - This function returns `nil` if it fails, with the second argument being a string with an error message. It is recommended to always wrap calls to it in `assert` so errors don't go unnoticed.
    - Examples: `assert(SMODS.modify_rank(card, 1))` increases a card's rank by one, like the Strength Tarot. `assert(SMODS.modify_rank(card, -2))` decreases a card's rank by two.
- `SMODS.find_card(key, count_debuffed) -> table`
    - This function replaces `find_joker`. It operates using keys instead of names, which avoids overlap between mods.
    - Returns an array of all jokers or consumables in the player's possession with the given key. Debuffed cards count only if `count_debuffed` is true.
- `SMODS.add_card(t) -> Card`
    - This function replaces `add_joker`. It takes the same input parameters as `SMODS.create_card` (below) and additionally emplaces the generated card into its area and evaluates `add_to_deck` effects.
- `SMODS.create_card(t) -> Card`
    - This function replaces `create_card`. It provides a cleaner interface to the same functionality. The argument to this function should always be a table. The following fields are supported:
    - `set` - The card type to be generated, e.g. `'Joker'`, `'Tarot'`, `'Spectral'`
    - `area` - The card area this will be emplaced into, e.g. `G.jokers`, `G.consumeables`. Default values are determined based on `set`.
    - `legendary` - Set this to `true` to generate a card of Legendary rarity.
    - `rarity` - If this is specified, skip rarity polling and use this instead of a chance roll between 0 and 1.
        - Under vanilla conditions, values up to 0.7 indicate "Common" rarity, values above 0.7 and up to 0.95 indicate "Uncommon" rarity, and values above 0.95 indicate "Rare" rarity.
    - `skip_materialize` - If this is `true`, a `start_materialize` animation will not be shown.
    - `soulable` - If this is `true`, hidden Soul-type cards are allowed to replace the generated card. Usually, this is the case for cards generated for booster packs.
    - `key` - If this is specified, generate a card with the given key instead of the random one.
    - `key_append` - An additional RNG seeding string. This should be used to put different sources of card generation on different queues.
    - `no_edition` - If this is `true`, the generated card is guaranteed to have no randomly generated edition.
    - `edition`, `enhancement`, `seal` - Applies the specified modifier to the card.
    - `stickers` - This should be an array of sticker keys. Applies all specified stickers to the card.
- `SMODS.debuff_card(card, debuff, source)`
    - Allows manually setting and removing debuffs from cards.
    - `source` should be a unique identifier string. You must use the same source to remove a previously set debuff.
    - If `debuff` is the string `'reset'`, remove debuffs from all sources handled by this function.
    - If `debuff` is the string `'prevent_debuff'`, blocks all possible debuffs on the card until removed.
    - If `debuff` is another truthy value, set a debuff on the card.
    - If `debuff` is a falsy values, remove this debuff.
- `SMODS.recalc_debuff(card)`
    - Recalculates the debuff state of a card.
- `SMODS.merge_lists(...) -> table`
    - Takes any number of 2D arrays. Flattens the input into a 1D array that contains all elements once in the order they first appear and removes any duplicates.
    - This can be used to merge results from poker hand evaluation to create a combined hand.
- `SMODS.get_blind_amount(ante) -> number`
    - Provides score requirements for higher stages of ante scaling. If you want to implement your own scaling rules, you should modify this function.
- `SMODS.stake_from_index(index) -> string`
    - Given an index from the Stake pool, return the corresponding key, or `'error'` if it doesn't exist.
- `SMODS.smart_level_up_hand(card, hand, instant, amount)`
    - Akin to vanilla's `level_up_hand()`, but avoids uneccessary calling of `update_hand_text()`
    - `card` - If included, juices up this card during the animation
    - `hand` - Key to the hand being leveled up.
    - `instant` - Skips the level up animations.
    - `amount` - How much the poker hand is leveled. Defaults to 1.
- `SMODS.blueprint_effect(copier, copied_card, context) -> table?`
    - Helper function to copy the ability of another joker, akin to Blueprint/Brainstorm. 
    - `copier` is the card the will be copying the effect of `copied_card`, using the provided `context` table. 
    - The returned table is the calculated effect of `copied_card`, with the display card set to `copier`. 
    - Example: 
        ```lua
		calculate = function(self, card, context)
			-- This is an implementation of Brainstorm
			local other_joker = G.jokers.cards[1]
			local other_joker_ret = SMODS.blueprint_effect(other_joker, card, context)

			if other_joker_ret then
				return other_joker_ret
			end
		end
        ```
- `SMODS.has_enhancement(card, key) -> bool`
    - Returns true if the provided `card` has a specific enhancement.
- `SMODS.change_voucher_limit(mod)`
    - Modifies the Voucher shop limit by `mod`.
- `SMODS.change_booster_limit(mod)`
    - Modifies the Booster Pack shop limit by `mod`.
- `SMODS.change_free_rerolls(mod)`
    - Modifies the current amount of free shop rerolls by `mod`.
- `SMODS.shallow_copy(t) -> table`
    - Returns a shallow copy of the provided table.
- `time(func, ...) -> number`
    - Calls an input function with any given additional arguments: `func(...)` and returns the time the function took to execute in milliseconds. The return value from `func` is lost.

## Internal utilities
These functions are used internally by Steamodded which may be of use for mods.

### Injection
These are functions used during the injection process of mods or GameObjects.
- `SMODS.save_d_u(o)`
    - Saves the default discovery and unlock states of an object into a separate field for later use before they are overwritten with profile data.
- `SMODS.SAVE_UNLOCKS()`
    - Modified from base game code. Sets discovery and unlock data according to profile state after injection.
- `SMODS.process_loc_text(ref_table, ref_value, loc_txt, key)`
    - Saves a localization entry (usually consisting of a name and a description) into the game's dictionary, with the ability to handle a multi-language format. The `loc_txt` table should either have locale indexing at the top layer or none at all. If the table holds multiple entries, `key` can be used to choose a key one layer down.
    - Example: `SMODS.process_loc_text(G.localization.descriptions.Joker, 'my_joker_key', loc_txt)`
- `SMODS.handle_loc_file(path)`
    - Given a mod's path, reads any present localization files and adds entries to the dictionary.
- `SMODS.insert_pool(pool, center, replace)`
    - If `replace` is true or `center` has been taken ownership of, look for an entry in `pool` with the same key and replace it. Otherwise, append `center` to the end of `pool`.
- `SMODS.remove_pool(pool, key)`
    - Find an entry in pool with this `key` and remove it if found.
- `SMODS.create_loc_dump()`
    - Dumps localization entries created during injection into a single file, for purposes of converting to a file-based localization system.
- `SMODS.create_mod_badges(obj, badges)`
    - UI code for adding mod badges to an object.
- `SMODS.merge_defaults(t, defaults) -> t`
    - Starting with `t`, insert any key-value pairs from `defaults` that don't already exist in `t` into `t`. Modifies `t` and returns it as the result of the merge.
    - `nil` entries are interpreted as an empty table; `false` inputs count as a table where every possible key maps to `false`. Therefore, `t == nil` is weak and falls back to defaults, while `t == false` explicitly ignores `defaults` in its entirety. Due to this, this function may not always return a table.
    - This is used for controlling when keys should receive prefixes.
- `convert_save_data()`
    - Adjusts values in save data to make the save compatible with Steamodded's way of storing deck wins by stake key instead of index.
- `SMODS.restart_game()`
    - Restarts the game.
- `SMODS.get_optional_features()`
    - Inserts all enabled optional features by injected mods into the `SMODS.optional_features` table.
- `SMODS.localize_box(lines, args)`
    - Handles localizing description boxes within a localization entry. 

### Calculation
These functions are used for handling calculation events.
- `SMODS.calculate_context(context, return_table) -> table?`
	- Main function used to calculate effects on cards for the provided `context` over a majority of CardAreas.
	- If `return_table` is provided, the function will not return a table and instead put all the calculation returns into
	- Mods can hook this function to add extra CardAreas.
- `SMODS.calculate_card_areas(_type, context, return_table, args) -> table`
	- Calculates effects on cards for a specific group of CardAreas based on `_type`.
- `SMODS.score_card(card, context)`
	- Scores the provided `card`.
- `SMODS.calculate_main_scoring(context, scoring_hand)`
	- Handles the main scoring hand calculation event.
	- `scoring_hand` - Uses this table of cards if provided, else it looks through `context.cardarea.cards` for if any of them are inside of `context.scoring_hand`. 
- `SMODS.calculate_end_of_round_effects(context)`
	- Handles the end of round calculation event.
- `SMODS.calculate_destroying_cards(context, cards_destroyed, scoring_hand)`
	- Handles the card destroy calculation event.
	- `scoring_hand` - Uses this table of cards if provided, else it looks through `context.cardarea.cards` for if any of them are inside of `context.scoring_hand`. 
- `SMODS.calculate_individual_effect(effect, scored_card, key, amount, from_edition)`
	- Used to trigger a calculation effect based on provided `key`.
- `SMODS.calculate_effect_table_key(effect_table, key, card, ret)`
	- Triggers one key of an effect table returned from `eval_card`.
- `SMODS.trigger_effects(effects, card)`
	- Used to calculate a table of effects generated in `G.FUNCS.evaluate_play`.
- `SMODS.get_card_areas(_type, _context) -> table`
    - Returns a table of CardAreas based on the provided `_type` and `_context`. Can be hooked or injected into to add your own CardAreas.
    - Possible values of `_type`:
        - `"playing_cards"` - Playing card evaluation.
			- Default CardAreas are `G.hand`, `G.play` (if `_context` is not `"end_of_round"`), `G.deck` (if the "Deck Calculation" feature is enabled), and `G.discard` (if the "Discard Calculation" feature is enabled).
        - `"jokers"` - Joker evaluation.
			- Default CardAreas are `G.jokers`, `G.consumeables`, and `G.vouchers`. 
        - `"individual"` - Individual object evaluation.
			- Unlike above, this does not return CardAreas and instead returns tables with an `object` and `scored_card` field. `object` if the object that will have the `calculate` function called on, and `scored_card` is the card/object used for animation.
			- Default objects are the selected Back and the selected Blind.
    - `_context` - Optional string to indicate extra information about the context.
- `SMODS.calculate_retriggers(card, context, _ret) -> table`
    - Calculates the retriggers on a Joker. Requires the "Joker Retrigger" feature to be enabled.
- `SMODS.calculate_repetitions(card, context, reps)`
    - Calculates the repetitions on a playing card.
- `SMODS.get_enhancements(card, extra_only) -> table<key, true>`
    - Returns a table of key-bool pairs, the keys being the enhancements this card counts as having.
    - If the "Quantum Enhancement" feature is not enabled, this function will only return the card's current enhancement.
    - `extra_only` - The returned table will exclude the card's current enhancement.
- `SMODS.calculate_quantum_enhancements(card, effects, context)`
    - Calculates quantum enhancements. Requires the "Quantum Enhancements" feature to be enabled.
- `SMODS.shatters(card) -> bool`
    - Returns true if the card should be shattered.
- `SMODS.in_scoring(card, scoring_hand) -> bool`
    - Returns true if the card is within the scoring hand.

### Misc.
These are functions used by SMODS for miscellaneous features.
- `SMODS.size_of_pool(pool) -> number`
    - Returns the size of provided `pool`, excluding "UNAVAILABLE".
- `SMODS.get_next_vouchers(vouchers) -> table`
    - Returns the next Vouchers to spawn.
- `SMODS.add_voucher_to_shop(key) -> Card`
    - Adds a Voucher based on provided `key` to the shop.
- `SMODS.add_booster_to_shop(key) -> Card`
    - Adds a Booster Pack based on provided `key` to the shop.
- `SMODS.signed(val) -> string`
    - Returned a signed string of `val`, prefixed with "+" if positive.
- `SMODS.signed_dollars(val) -> string`
    - Returned a signed string of `val` as dollars, prefixed with "$" if positive and "-$" if negative.
- `SMODS.multiplicative_stacking(base, perma) -> number`
    - Returns the result of multiplying `base` and `perma + 1`.