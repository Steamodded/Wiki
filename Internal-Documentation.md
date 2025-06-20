# Internal Documentation
SMODS has internal functions that are used for loading mods, creating and handling GameObjects, and general backend operations. Mods may be interested in using or modifying these functions. 

- [Injection](#injection)
- [Calculation](#calculation)
- [Misc.](#misc)

***

## Injection
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
- `SMODS.merge_defaults(t, defaults) -> t?`
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

## Calculation
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

## Misc.
These are functions used by SMODS for miscellaneous features.
- `SMODS.signed(val) -> string`
    - Returned a signed string of `val`, prefixed with "+" if positive.
- `SMODS.signed_dollars(val) -> string`
    - Returned a signed string of `val` as dollars, prefixed with "$" if positive and "-$" if negative.
- `SMODS.multiplicative_stacking(base, perma) -> number`
    - Returns the result of multiplying `base` and `perma + 1`.