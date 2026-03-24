# API Documentation: `SMODS.ObjectType`
- **Required parameters:**
	- `key`
		- Unlike other game objects, ObjectTypes don't add your mod's prefix automatically to the key to allow multiple mods to share pools. You can still add your prefix manually to avoid conflicts.
- **Optional parameters** *(defaults)*:
	- `prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
	- `default`: Fallback card when object pool is empty
	- `cards`: List of keys to centers to auto-inject into this ObjectType
		-  Expects a list of keys like this:
		```lua
			{
				["j_foo_joker"] = true,
				["c_bar_tarot"] = true,
			}
		```
	- `rarities` allows cards to show up at different rates.
		-  Expects a list of tables like this:
		```lua
			{
				key = '',
				rate = 0.5,
			}
		```
		- The sum of all rates is normalized internally, so you don't need to concern yourself with making these values add up to `1`. Not defining a rate will use the default rate assigned by the rarity. 

## API Documentation: `SMODS.ConsumableType`
This is a subclass of `SMODS.ObjectType`. All values and functions tied to `SMODS.ObjectType` work for this class. 
- **Required parameters:**
	- `key`
		- Like with ObjectTypes, ConsumableTypes don't add your mod's prefix automatically to the key. You can still add your prefix manually to avoid conflicts.
	- `primary_colour`
	- `secondary_colour`
- **Optional parameters** *(defaults)*:
	- `no_collection` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
	- `loc_txt`, Skeleton:
	```lua
		{
			name = '', -- used on card type badges
			collection = '', -- label for the button to access the collection
			undiscovered = { -- description for undiscovered cards in the collection
				name = '',
				text = { '' },
			},
		}
		-- In localization files:
		-- name should be under should be under `G.localization.misc.dictionary['k_'.. key:lower()]`
		-- the badge label under `G.localization.misc.labels[key:lower()]`
		-- collection under `G.localization.misc.dictionary['b_'.. key:lower().. '_cards']`
		-- undiscovered under `G.localization.descriptions.Other['undiscovered_'.. key:lower()]`
	```
	- `collection_rows = { 6, 6 }`: Customize the collection for this card type. Each value indicates a row with the specified amount of cards.
	- `shop_rate`: Setting a numerical value for `shop_rate` enables cards of this type to appear in the shop at the specified rate.
		- This sets a default rate, which can be modified by accessing `G.GAME[key:lower() .. '_rate']` during a run.
	- `text_colour`: Set a custom text color used on the card type's badge. This can take any HEX color, and saves it as `G.C.UI[key]`.
    - `select_card`:
    	- Set to string of destination card area, ex. `'consumeables'`, to save cards of this type from Booster packs instead of using it.
		- Set to a function `select_card(card, pack) -> string?` to control if and where `card` should be saved for any `card, pack` combination.
		- Takes priority over `select_card` on the Booster pack

## API methods
- `ObjectType.inject_card(self, center)`
	- Used for modifying any registered cards of this type, or adding them to additional pools.
- `ObjectType.delete_card(self, center)`
	- Used for removing cards from additional pools when deleted.
- `ConsumableType.create_UIBox_your_collection(self) -> table`
	- Returns the UIBox of the ConsumableType's collections menu. 

# API Documentation: `SMODS.UndiscoveredSprite`
For consumable types, a sprite for undiscovered objects can be registered. Otherwise, the default undiscovered Joker sprite is used. The keys of both objects should match exactly. Remember to use `prefix_config.atlas = false` if you want to reference an atlas from the base game.
- **Required parameters:**
	- `key`
	- `atlas`
	- `pos`
   - **Optional parameters:**
  	- `no_overlay`: disables the floating ? sprite from undiscovered objects
  	- `overlay_pos`: customize the floating ? sprite using your atlas. Expects `{x = 0, y = 0}`
