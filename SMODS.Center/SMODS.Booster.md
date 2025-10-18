# API Documentation: `SMODS.Booster`
**Class prefix:** `p`
- **Required parameters:**
	- `key`,
	- `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - `loc_txt` can contain an additional `group_name` string. This is the bottom text while on the pack opening screen.
        - With localization files, this text should be stored in `misc.dictionary[group_key or 'k_booster_group_'..key]`
- **Optional parameters** *(defaults)*:
    - `atlas = 'Booster', pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
    - `config, discovered = false, no_collection, prefix_config, dependencies, display_size, pixel_size` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
        - The default `config` table is `{ extra = 3, choose = 1 }`; `extra` is the amount of cards in the pack, `choose` is the amount of choices.
        - Note: `unlocked` on boosters is currently unsupported.
	- `pools`: List of keys to ObjectTypes this center should be injected into
		-  Expects a list of keys like this:
		```lua
			{
				["Foo"] = true,
				["Bar"] = true,
			}
		```
    - `group_key`: Key to the group name (see above) of this booster. Useful when multiple booster packs share the same group name.
	- `cost = 4`,
    - `weight = 1`: Determines how freqently the pack appears in the shop.
    - `draw_hand = false`: If this is `true`, draw playing cards to hand when this pack is opened.
    - `kind`: Used for grouping packs together. For example, this can be used in `get_pack()` to generate a booster pack of a given type.
    - `select_card`:
		- Set to string of destination card area, ex. `'consumeables'`, to save cards from the pack instead of using them.
		- Set to table of form `{Set = 'area'}` to change behaviour according to a card's `Set` (e.g. `{Tarot = 'consumeables'}` to only save `Tarot` cards, relevant if you have multiple types of consumables in a booster).
		- Set to a function `select_card(card, pack) -> string?` to control if and where `card` should be saved for any `card, pack` combination.

## API methods
- `loc_vars, generate_ui` [(reference)](https://github.com/Steamodded/smods/wiki/Localization#Localization-functions)
	- SMODS.Booster implements a default `loc_vars` function that returns `card.ability.choose` and `card.ability.extra`. If your booster pack defines both of these values in its `config` you can omit defining `loc_vars`.
- `create_card(self, card, i) -> table|Card`
	- Creates the cards inside of the booster pack. `card` is the booster pack card, `i` is the position of the card to be generated. If the returned table is not a `Card`, it is passed into [`SMODS.create_card`](https://github.com/Steamodded/smods/wiki/Utility#mod-facing-utilities).
 	- Example 1, manual card creation:
	```lua
	-- to create a booster pack of standard cards
	create_card = function(self, card)
	    local newCard = SMODS.create_card({set = "Playing Card", area = G.pack_cards, skip_materialize = true})
	    return newCard
	end,
	```
   	- Example 2, return passed into `SMODS.create_card`:
	```lua
	-- to create a booster pack of foil jokers
	create_card = function(self, card)
	    return {set = "Joker", area = G.pack_cards, skip_materialize = true, soulable = true, key_append = "unique_string_for_rng", edition = "e_foil"}
	end,
	```
- `update_pack(self, dt)`
	- Handles the booster back's UI elements when this booster is opened. 
- `ease_background_colour(self)`
	- Changes the background color whilst this booster is opened. 
- `particles(self)`
	- Handles adding particle effects. 
- `create_UIBox(self) -> table`
	- Returns the booster's UIBox. 
- `set_ability(self, card, initial, delay_sprites)`
	- Set up initial ability values or manipulate sprites in an advanced way.
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

## Utility function
- `SMODS.Booster:take_ownership_by_kind(kind, obj, silent)`
    - Finds all booster packs with matching `kind` and calls `SMODS.Booster:take_ownership()` for each one with arguments `obj, silent` passed through.
