# MOD CORE API DECK Documentation

## Overview
The MOD CORE API DECK is a Lua script designed to manage deck objects within Balatro. This script facilitates the creation, registration, and integration of custom decks into the existing game structure.

## Code Structure

### Deck Object Definition
- `SMODS.Deck`: This object serves as a blueprint for creating deck objects. Each deck has several attributes:
  - `name`: The name of the deck.
  - `slug`: A unique identifier for the deck, prefixed with `b_`.
  - `config`: A table for additional configuration settings, including the effect.
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
local newDeck = SMODS.Deck:new("MyDeck", "my_deck_slug", {my_deck_effect = value})
newDeck:register()
```

## Missing Implementation
The Deck "Selection UI" and the "Deck function effects" are not implemented the API for now and need to be manually added. This is how to implement these 2 features properly and without causing incompatibility between your Mod and others: 
```lua
-- Using the "AbsoluteDeck" mod as an example


-- Save function ref so we can append some logic to it
local Backapply_to_runRef = Back.apply_to_run
-- Function used to apply new Deck effects
function Back.apply_to_run(arg_56_0)
        -- Call the function before adding our additional logic
	Backapply_to_runRef(arg_56_0)

        -- Example using the "polyglass" effect
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

```lua
-- Using the "AbsoluteDeck" mod as an example


-- Save function ref so we can append some logic to it
local Backgenerate_UIRef = Back.generate_UI
-- Function used to generate a selection UI for our deck
function Back.generate_UI(arg_53_0, arg_53_1, arg_53_2, arg_53_3)
        -- If this is not our Deck, run the parent function
	local deck = Backgenerate_UIRef(arg_53_0, arg_53_1, arg_53_2, arg_53_3)
	local name = arg_53_1 or arg_53_0.name

        -- If this is our deck we generate the UI
	if name == "Absolute Deck" then
		arg_53_3 = arg_53_3 or 0.7
		arg_53_2 = arg_53_2 or 0.9
                
                -- We return the UI table of our Deck
		return {
			n = G.UIT.ROOT,
			config = {
				align = "cm",
				minw = arg_53_3 * 3,
				minh = arg_53_3 * 2.5,
				id = arg_53_0.name,
				colour = G.C.CLEAR
			},
			nodes = {
				{
					n = G.UIT.R,
					config = {
						align = "cm"
					},
					nodes = {
						{
							n = G.UIT.T,
							config = {
								text = "Start with a Deck",
								scale = arg_53_2 * 0.5,
								colour = G.C.UI.TEXT_DARK
							}
						}
					}
				},
				{
					n = G.UIT.R,
					config = {
						align = "cm"
					},
					nodes = {
						{
							n = G.UIT.T,
							config = {
								text = "full of",
								scale = arg_53_2 * 0.5,
								colour = G.C.UI.TEXT_DARK
							}
						}
					}
				},
				{
					n = G.UIT.R,
					config = {
						align = "cm"
					},
					nodes = {
						{
							n = G.UIT.T,
							config = {
								text = "Polyglass ",
								scale = arg_53_2 * 0.5,
								colour = G.C.SECONDARY_SET.Planet
							}
						},
						{
							n = G.UIT.T,
							config = {
								text = "cards",
								scale = arg_53_2 * 0.5,
								colour = G.C.UI.TEXT_DARK
							}
						}
					}
				}
			}
		}
	end

        -- Return the UI table of the Deck of the parent function if this is not our Deck
	return deck
end
```

Remember to never overwrite a function without calling it's reference from your new function. If you do not, you will overcome every other Mods code, making your mod incompatible with the others.

For more information and examples, you can look at the examples mods provided in this repository. 
