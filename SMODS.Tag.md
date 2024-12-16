# API Documentation: `SMODS.Tag`
- **Required parameters:**
    - `key`
- **Optional parameters** *(defaults)*:
    - `loc_txt`: Uses the standard skeleton.
    - `config = {}`
    - `atlas = 'tags'`
    - `pos = { x = 0, y = 0 }`
    - `min_ante`: Minimum ante needed for this tag to appear. Use in_pool for more advanced spawn restrictions instead.
    - `discovered = false` 

## API methods
- `apply(self, tag, context)`
    - This function defines the tag's behavior when triggering. Unlike vanilla tags, this function is not restricted by `self.config.type` matching `context.type`, meaning you have to check context manually.
        - To trigger the tag, you should call `tag:yep(message, colour, func)` and set `tag.triggered = true`.
        - `message` is the string to display upon trigger,
        - `colour` is the colour of the message box,
        - `func` is a function that gets executed as an event before the used tag gets removed. This function should always return `true`.
- `set_ability(self, tag)`
    - This function allows you to store any additional information your tag may need when it is created. Values should be stored within `tag.ability`.

The following functions provide the same interface and functionality as their `SMODS.Center` counterparts.
- `in_pool(self, args) -> bool, { allow_duplicates = bool }`
	- Define custom logic for when a card is allowed to spawn. A card can spawn if `in_pool` returns true and all other checks are met.
	- `allow_duplicates` allows this card to spawn when one already exists, even without Showman.
	- When called from `generate_card_ui`, the `_append` key is passed as `args.source`.
- `loc_vars(self, info_queue, tag) -> { vars ?= table, main_start ?= table, main_end ?= table, key ?= string, replace_debuff ?= bool }`
	- Pass variables (`vars`) to tag descriptions.
	- Add tooltips by appending to `info_queue`.
	- You can force the use of a different description entirely (`key`).
	- Add additional text to the start or end of a tag description with `main_start` or `main_end`.
- `generate_ui(self, info_queue, tag, desc_nodes, specific_vars, full_UI_table)`
	- The default implementation of this function acts as a wrapper of `loc_vars`. For advanced UI implementations, define this function directly. 
