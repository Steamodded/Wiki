# API Documentation: `SMODS.Back`
**Class prefix:** `b`
- **Required parameters:**
	- `key`,
	- `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
- **Optional parameters** *(defaults)*:
    - `atlas = 'centers', pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
    - `config = {}, unlocked = true, discovered = false, no_collection, prefix_config, dependencies, display_size, pixel_size` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
		- `config` values will be saved under `G.GAME.selected_back.effect.config`
    - `initial_deck`: *(Added in 1501a)* Allows for easier customisation of your starting deck.
        - `ranks`, `suits`: A list of ranks and suits to include/exclude.
        - `exclude = false`: If `true`, `ranks`/`suits` will be trated as blacklists instead of whitelists.


## API methods
- `calculate(self, back, context)` [(reference)](https://github.com/Steamodded/smods/wiki/Calculate-Functions)
    - This method is called from `Back:trigger_effect()` and incorporated into the standard calculation pipeline. This does not apply to vanilla `trigger_effect` functionality, which can be used as normal from this function by checking for `context.context == 'eval'` or `context.context == 'final_scoring_step` respectively.
    - **Defining a `trigger_effect` function on your deck is deprecated.**
- `loc_vars, locked_loc_vars, generate_ui` [(reference)](https://github.com/Steamodded/smods/wiki/Localization#Localization-functions)
- `apply(self, back)`
    - Apply modifiers at the start of a run. If you want to modify the starting deck, you must use events to do so.
- `calc_dollar_bonus(self, back) -> number, table`
	- For awarding money at the end of the round (e.g. Delayed Gratification, Cloud Nine)
	- *(Added in 1531zeebee)* Optionally, you can return a table as the second value to modify the text in the round evaluation screen with any of the following arguments:
		- `text`: Replaces the default name text.
		- `key`, `set`: Allows changing the key and/or set of the name in the localization (ignored if `text` is set)
		- `text_colour`, `scale`: Allows changing the colour and scale of the text respectively
- `check_for_unlock(self, args) -> bool`
	- Configure unlock conditions. Refer to the function `check_for_unlock` in Balatro's code for more information.
