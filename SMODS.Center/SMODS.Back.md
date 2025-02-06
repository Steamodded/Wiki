# API Documentation: `SMODS.Back`
**Class prefix:** `b`
- **Required parameters:**
	- `key`,
	- `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
- **Optional parameters** *(defaults)*:
    - `atlas = 'centers', pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
    - `config = {}, unlocked = true, discovered = false, no_collection, prefix_config, dependencies, display_size, pixel_size` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)


## API methods
- `calculate(self, back, context)` [(reference)](https://github.com/Steamodded/smods/wiki/Calculate-Functions)
    - This method is called from `Back:trigger_effect()` and incorporated into the standard calculation pipeline. This does not apply to vanilla `trigger_effect` functionality, which can be used as normal from this function by checking for `context.context == 'eval'` or `context.context == 'final_scoring_step` respectively.
    - **Defining a `trigger_effect` function on your deck is deprecated.**
- `loc_vars, locked_loc_vars, generate_ui` [(reference)](https://github.com/Steamodded/smods/wiki/Localization#Localization-functions)
- `apply(self, back)`
    - Apply modifiers at the start of a run. If you want to modify the starting deck, you must use events to do so.
- `in_pool(self, args) -> bool, { allow_duplicates = bool }`
	- Define custom logic for when a card is allowed to spawn. A card can spawn if `in_pool` returns true and all other checks are met.
	- `allow_duplicates` allows this card to spawn when one already exists, even without Showman.
	- When called from `generate_card_ui`, the `_append` key is passed as `args.source`.
- `check_for_unlock(self, args) -> bool`
	- Configure unlock conditions. Refer to the function `check_for_unlock` in Balatro's code for more information.