# API Documentation: `SMODS.Tag`
**Class prefix:** `tag`
- **Required parameters:**
    - `key`
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
- **Optional parameters** *(defaults)*:
    - `atlas = 'tags', pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
    - `config = {}, discovered = false, no_collection, prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters) 
    - `min_ante`: Minimum ante needed for this tag to appear. Use in_pool for more advanced spawn restrictions instead.

## API methods
- `loc_vars, generate_ui` [(reference)](https://github.com/Steamodded/wiki/Localization#Localization-functions)
- `in_pool(self, args) -> bool, { allow_duplicates = bool }`
	- Define custom logic for when a tag is allowed to spawn. A tag can spawn if `in_pool` returns true and all other checks are met.
	- When called from `generate_card_ui`, the `_append` key is passed as `args.source`.
- `apply(self, tag, context)`
    - This function defines the tag's behavior when triggering. Unlike vanilla tags, this function is not restricted by `self.config.type` matching `context.type`, meaning you have to check context manually.
        - To trigger the tag, you should call `tag:yep(message, colour, func)` and set `tag.triggered = true`.
        - `message` is the string to display upon trigger,
        - `colour` is the colour of the message box,
        - `func` is a function that gets executed as an event before the used tag gets removed. This function should always return `true`.
- `set_ability(self, tag)`
    - This function allows you to store any additional information your tag may need when it is created. Values should be stored within `tag.ability`.

