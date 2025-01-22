# API Documentation: `SMODS.Sticker`
- **Required parameters:**
	- `key`
	- `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
- **Optional parameters** *(defaults)*:
	- `atlas = 'stickers', pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
	- `badge_colour`: Colour of this sticker's badge.
    - `hide_badge`: If set to `true`, no badge is shown for this sticker.
	- `default_compat`: Default compatibility with cards. If `true`, all cards can have this sticker unless otherwise specified.
	- `compat_exceptions`: Array of keys of centers that have non-default compatibility with this sticker.
		- `default_compat = true`: sticker cannot be applied to centers in `compat_exceptions`
		- `default_compat = false`: sticker can only be applied to centers in `compat_exceptions`
	- `sets`, list of pools that this sticker is allowed to be applied on, format: 
	```lua
		{
			Joker = true
		}
	```
	- `rate = 0.3`: Chance of the sticker applying on an eligible card
	- `needs_enable_flag`: If set to `true`, this sticker requires `G.GAME.modifiers['enable_'..self.key]` to be `true` before it can be applied.

## API methods
- `calculate(self, card, context)` [(reference)](https://github.com/Steamodded/smods/wiki/Calculate-Functions)
- `loc_vars` [(reference)](https://github.com/Steamodded/wiki/Localization#Localization-functions)
	- Due to some constraints, the functionality of `loc_vars` on stickers is limited. Out of all possible return values, only `vars`, `key` and `set` are supported.
- `should_apply(self, card, center, area, bypass_roll) -> bool`
	- Returns true if the sticker can be applied to the card. 
	- `bypass_roll` skips the RNG check and only looks for compatibility
- `apply(self, card, val)`
	- Handles applying and removing the sticker
	- Sets `card.ability[self.key]` to `val` by default. 
- `draw(self, card, layer)`
	- Draws the sprite and shader of the sticker.