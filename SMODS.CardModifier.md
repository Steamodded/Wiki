# API Documentation: `SMODS.CardModifier`
- **Required parameters:**
	- `key`
	- `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
		- `loc_txt` should contain a `label` string used for the card's badge text
- **Optional parameters** *(defaults)*:
	- `atlas = 'stickers', pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
	- `config = {}, prefix_config, dependencies, badge_colour, text_colour` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
		- `config` values will be saved to `card.ability[modifier_key]`
	- `badge_colour`: Colour of this modifier's badge.
    - `hide_badge`: If set to `true`, no badge is shown for this modifier.
	- `always_scores`: If `true`, editioned card always counts in scoring.
  - `never_scores`: If `true`, editioned card never counts in scoring (supersedes `always_scores`).
  - `draw_shader` If `draw_shader` is a `boolean` it will draw this modifier with the `voucher` shader otherwise if it is a `string` it will draw it with the specified shader.

## API methods
- `calculate(self, card, context)` [(reference)](https://github.com/Steamodded/smods/wiki/Calculate-Functions)
- `loc_vars` [(reference)](https://github.com/Steamodded/smods/wiki/Localization#Localization-functions)
	- Due to some constraints, the functionality of `loc_vars` on modifiers is limited. Out of all possible return values, only `vars`, `key` and `set` are supported.
- `apply(self, card, val)`
	- Handles applying and removing the modifier
	- By default, sets `card.ability[ModifierType][self.key]` to `config` if it exists and `val` is truthy or to `val` otherwise. 
	- It is recommended to not redefine this function. If you still need to, you can call `SMODS.CardModifier.apply(self, card, val)` in this function to retain the default functionality.
- `draw(self, card, layer)`
	- Draws the sprite and shader of the modifier.

### Modifier methods
- `Card:calculate_moldifier(context, key)`
    Calculates a specific modifier on a card if present
    - `context` [(reference)](https://github.com/Steamodded/smods/wiki/Calculate-Functions)
    - `key` `key` of modifier as a string to check for

- `Card:add_modifier(modifier, bypass_check)`
	Use this function to add a modifier to a card
	- `modifier`, `key` of modifier as a string
	- `bypass_check`, *boolean* determines whether natural application checks e.g. such as in the shop should be used

- `Card:remove_modifier(modifier)`
	Use this function to remove a modifier from a card
	- `modifier`, `key` of modifier as a string
