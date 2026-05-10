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
	- `default_compat`: Default compatibility with cards. If `true`, all cards can have this modifier unless otherwise specified. Note: modifier compatibility, sets, rate, and needs_enable_flag are all focused on *natural* application of modifiers e.g. in the shop. for manual applicaiton only Card:add_modifier(modifier, true) is needed
	- `compat_exceptions`: Array of keys of centers that have non-default compatibility with this modifier.
		- `default_compat = true`: modifier cannot be applied to centers in `compat_exceptions`
		- `default_compat = false`: modifier can only be applied to centers in `compat_exceptions`
	- `sets`, list of pools that this modifier is allowed to be applied on, format: 
	```lua
		{
			Joker = true
		}
	```
	- `rate = 0.3`: Chance of the modifier applying on an eligible card
	- `needs_enable_flag`: If set to `true`, this modifier requires `G.GAME.modifiers['enable_'..self.key]` to be `true` before it can be applied.
	- `always_scores`: If `true`, editioned card always counts in scoring.
  - `never_scores`: If `true`, editioned card never counts in scoring (supersedes `always_scores`).
  - `draw_shader` If `draw_shader` is a `boolean` it will draw this modifier with the `voucher` shader otherwise if it is a `string` it will draw it with the specified shader.

## API methods
- `calculate(self, card, context)` [(reference)](https://github.com/Steamodded/smods/wiki/Calculate-Functions)
- `loc_vars` [(reference)](https://github.com/Steamodded/smods/wiki/Localization#Localization-functions)
	- Due to some constraints, the functionality of `loc_vars` on modifiers is limited. Out of all possible return values, only `vars`, `key` and `set` are supported.
- `should_apply(self, card, center, area, bypass_roll) -> bool`
	- Returns true if the modifier can be applied to the card. 
	- `bypass_roll` skips the RNG check and only looks for compatibility
	- If this function is redefined it will ignore all optional parameter flags listed above. You can call and store the return of `SMODS.CardModifier.should_apply(self, card, center, area, bypass_roll)` in this function to retain the default functionality.
- `apply(self, card, val)`
	- Handles applying and removing the modifier
	- By default, sets `card.ability[self.key]` to `config` if it exists and `val` is truthy or to `val` otherwise. 
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
