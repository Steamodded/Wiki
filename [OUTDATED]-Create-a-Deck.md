# MOD CORE API DECK Documentation
## NOTE: THIS PAGE WAS MADE FOR STEAMODDED 0.9.8, AND SHOULD NOT BE REFERRED TO FOR NEWER VERSIONS.
## Overview
The MOD CORE API DECK is a Lua script designed to manage deck objects within Balatro. This script facilitates the creation, registration, and integration of custom decks into the existing game structure.

## Code Structure

### Deck Object Definition
- `SMODS.Deck`: This object serves as a blueprint for creating deck objects. Each deck has several attributes:
  - `name`: The name of the deck.
  - `slug`: A unique identifier for the deck, prefixed with `b_`.
  - `config`: A table for additional configuration settings, including the effect.
  - `loc_txt`: A special object used for the UI elements (for now).
  - `spritePos`: Coordinates for the deck's sprite, with default `{x = 0, y = 0}`.
  - `unlocked`: A boolean indicating if the deck is unlocked, defaulting to `true`.
  - `discovered`: A boolean to show if the deck is discovered, defaulting to `true`.

### Deck Object Creation (`new` Method)
- This method initializes a new deck object with specified attributes. Do not prefix the `slug` with `b_`, it will be done automatically. If `config` or `spritePos` are not provided, they default to an empty table and `{x = 0, y = 0}`, respectively. Both `unlocked` and `discovered` default to `true`.

### Deck Registration (`register` Method)
- This method registers a new deck in the `SMODS.Decks` table, ensuring each deck is unique within the game.

### Deck Injection (`injectDecks` Function)
- `injectDecks` integrates all registered decks into the game's backend. It adjusts various game settings (like `G.BACKS`, `G.P_CENTERS`) to include the new decks. The function assigns IDs, manages deck names and positions, and ensures that decks are properly recognized within the game's system. **DO NOT CALL IT UNLESS YOU KNOW WHAT YOU ARE DOING**, the Core will do it himself. 

## Usage Example
To use this API, create a new deck instance, register it, and then inject it into the game:
```lua
local loc_def = {
	["name"]="MyDeck",
	["text"]={
		[1]="My Deck !",
	},
}

local newDeck = SMODS.Deck:new("MyDeck", "my_deck_slug", {my_deck_effect = value}, loc_def)
newDeck:register()
```

## Missing Implementation
The "Deck function effects" is not implemented the API for now and need to be manually added. This is how to implement this feature properly and without causing incompatibility between your Mod and others: 
```lua
-- Using the "AbsoluteDeck" mod as an example


-- Save function ref so we can append some logic to it
local Backapply_to_runRef = Back.apply_to_run
-- Function used to apply new Deck effects
function Back.apply_to_run(arg_56_0)
	Backapply_to_runRef(arg_56_0)

	if arg_56_0.effect.config.polyglass then
		G.E_MANAGER:add_event(Event({
			func = function()
				for iter_57_0 = #G.playing_cards, 1, -1 do
					sendDebugMessage(G.playing_cards[iter_57_0].base.id)

					G.playing_cards[iter_57_0]:set_ability(G.P_CENTERS.m_glass)
					G.playing_cards[iter_57_0]:set_edition({
						polychrome = true
					}, true, true)
				end

				return true
			end
		}))
	end
end
```


Remember to never overwrite a function without calling it's reference from your new function. If you do not, you will overcome every other Mods code, making your mod incompatible with the others.

For more information and examples, you can look at the examples mods provided in this repository. 
