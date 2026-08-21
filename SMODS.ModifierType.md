## API Documentation: `SMODS.ModiofierType`
- **Required parameters:**
	- `key`
		- ModifierTypes don't add your mod's prefix automatically to the key. You can still add your prefix manually to avoid conflicts.
- **Optional parameters** *(defaults)*:
  - `prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
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
	- `text_colour`: Set a custom text color used on the card type's badge. This can take any HEX color, and saves it as `G.C.UI[key]`.
  - `modifier_limit` = 1: Determined how many of this ModifierType can appear on a card at once. 

## API methods
- `ModifierType.create_UIBox_your_collection(self) -> table`
	- Returns the UIBox of the ConsumableType's collections menu. 
