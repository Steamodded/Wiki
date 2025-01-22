# API Documentation: `SMODS.Consumable`
**Class prefix:** `c`
- **Required parameters:**
	- `key`,
    - `set` (`'Tarot'`, `'Planet'`, `'Spectral'` or the key of a modded consumable type)
	- `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
- **Optional parameters** *(defaults)*:
    - `atlas = 'Tarot', pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
    - `config = {}, unlocked = true, discovered = false, no_collection, prefix_config, dependencies, display_size, pixel_size` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
	- `cost = 3`,
    - `hidden` for legendary consumables like The Soul. For further customization:
		- `soul_set = 'Spectral'`, legendaries may appear when a card of either their own set or this one are being generated.
		- `soul_rate = 0.003`, determines how likely this legendary is to replace each card in a pack
		- `can_repeat_soul`, allows repeats of this card as if Showman were present

## API methods
- `calculate(self, card, context)` [(reference)](https://github.com/Steamodded/smods/wiki/Calculate-Functions)
- `loc_vars, locked_loc_vars, generate_ui` [(reference)](https://github.com/Steamodded/wiki/Localization#Localization-functions)
- `use(self, card, area, copier)`
	- Defines the behavior of a consumable when used. *(The `copier` argument is a remnant from an effect no longer present in the game and can be ignored.)*
- `can_use(self, card) -> bool`
	- Determines whether a consumable is currently able to be used.
- `keep_on_use(self, card) -> bool`
	- Allows a used card to stay where it is or be moved to the consumables area from a booster pack instead of getting destroyed.
- `set_ability(self, card, initial, delay_sprites)`
	- Set up initial ability values or manipulate sprites in an advanced way.
- `add_to_deck(self, card, from_debuff)`
	- Modify the game state when this card is obtained.
	- Cards are considered added when they become undebuffed (in this case, `from_debuff` will be true).
- `remove_from_deck(self, card, from_debuff)`
	- Modify the game state when this card is sold, destroyed, or otherwise removed.
	- Cards are considered removed when debuffed (in this case, `from_debuff` will be true).
- `in_pool(self, args) -> bool, { allow_duplicates = bool }`
	- Define custom logic for when a card is allowed to spawn. A card can spawn if `in_pool` returns true and all other checks are met.
	- `allow_duplicates` allows this card to spawn when one already exists, even without Showman.
	- When called from `generate_card_ui`, the `_append` key is passed as `args.source`.
- `update(self, card, dt)`
	- For actions that happen every frame.
- `set_sprites(self, card, front)`
	- For advanced sprite manipulation that happens when a card is created or loaded.
- `load(self, card, card_table, other_card)`
	- For modifications to sprites or the card itself when a run is reloaded.
- `check_for_unlock(self, args) -> bool`
	- Configure unlock conditions. Refer to the function `check_for_unlock` in Balatro's code for more information.
- `set_badges(self, card, badges)`
	- Add additional badges, leaving existing badges intact. This function doesn't return; add badges by appending to `badges`.
	- Avoid overwriting existing elements. It will cause text to appear on the top left corner of your screen instead.
	- Function for creating badges: `create_badge(_string, _badge_col, _text_col, scaling)`
		- `_string`: Text displayed on the badge.
		- `_badge_col = G.C.GREEN`: Background colour.
		- `_text_col = G.C.WHITE`: Text colour.
		- `_scaling = 1`: Relative size of the badge.
	- Example:
	```lua
	{
		set_badges = function(self, card, badges)
			badges[#badges+1] = create_badge(localize('k_your_string'), G.C.RED, G.C.BLACK, 1.2 )
		end,
	}
	```
- `set_card_type_badge(self, card, badges)`
	- Same as `set_badges`, but bypasses creation of the card type / rarity badge, allowing you to replace it with a custom one.
- `draw(self, card, layer)`
	- Draws the sprite and shader of the card.