# API Documentation: `SMODS.DrawStep`
This class offers a standardized way of drawing sprites and shaders on cards instead of having to rely on patching `Card:draw()`.
- **Required parameters:**
	- `key`
    - `order`: Sets an order for this step. All draw steps are executed in order from lowest to highest. Refer to `src/card_draw.lua` in Steamodded's source code for the order values of base draw steps.
    - `func(card, layer)`: Handles the drawing logic of this `DrawStep`.
        - `card` is the card being drawn.
        - `layer` is one of `'card'`, `'shadow'`, `'both'`.
- **Optional parameters** *(defaults)*:
    - `layers = { both = true, card = true }`: Determines which values of the `layer` argument this `DrawStep` should be executed for. Unless you are defining custom types of layers and calling `Card:draw()` with them, you should only ever need to change this to `{ both = true, shadow = true }` when you are drawing a shadow.
    - `prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
