# API Documentation: `SMODS.ConsumableType`
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
	- `rarities` allows cards to show up at different rates.
		-  Expects a list of tables like this:
		```lua
			{
				key = '', -- using string values is recommended, but numeric values are also possible
				rate = 0.5,
			}
		```
		- The sum of all rates is normalized internally, so you don't need to concern yourself with making these values add up to `1`.

## API methods
- `inject_card(self, center)`
	- Used for modifying any registered cards of this type, or adding them to additional pools.
- `delete_card(self, center)`
	- Used for removing cards from additional pools when deleted.

# API Documentation: `SMODS.UndiscoveredSprite`
For consumable types, a sprite for undiscovered objects must be registered. The keys of both objects should match exactly. Remember to use `raw_atlas_key` if you want to reference an atlas from the base game.
- **Required parameters:**
	- `key`
	- `atlas`
	- `pos`