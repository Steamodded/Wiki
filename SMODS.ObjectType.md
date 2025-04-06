# API Documentation: `SMODS.ObjectType`
- **Required parameters:**
	- `key`
- **Optional parameters** *(defaults)*:
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
	- `primary_colour`
	- `secondary_colour`
- **Optional parameters** *(defaults)*:
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
	```
	- `collection_rows = { 6, 6 }`: Customize the collection for this card type. Each value indicates a row with the specified amount of cards.
	- `shop_rate`: Setting a numerical value for `shop_rate` enables cards of this type to appear in the shop at the specified rate.
		- This sets a default rate, which can be modified by accessing `G.GAME[key:lower() .. '_rate']` during a run.

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
