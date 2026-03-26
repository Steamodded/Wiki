# API Documentation: `SMODS.CanvasSprite`
This class extends Balatro's `Sprite` object, and creates a Sprite that renders the contents of a Love2D Canvas. Note that unlike vanilla Sprites, creating a CanvasSprite uses a single table as the argument.

Once a CanvasSprite is created (e.g. `local sprite = SMODS.CanvasSprite { ... }`), the object will contain a `canvas` object, which is the Love2D canvas itself (e.g. `sprite.canvas`). This is where everything should be rendered.

- **Optional parameters** *(defaults)*:
    - `X, Y, W, H = 0, 0, G.CARD_W, G.CARD_H`: the vanilla Sprite position and dimension parameters.
	- `canvasW, canvasH = 71, 95`: the width and height of the Love2D canvas in pixels.
	- `canvasScale = 10`: a multiplier applied to the canvas dimensions; higher numbers help make the image sharper.
	- `text, text_offset, text_colour, text_width, text_height, ref_table, ref_value, text_font, text_transform`: all these parameters are related to `card.canvas_text` usage (see below).

## Using `card.canvas_text`
If a card object has either a CanvasSprite or a table of CanvasSprites stored at `card.canvas_text`, SMODS will automatically render that CanvasSprite in a standard drawstep. This drawstep goes above the center, front, edition, seal, and sticker sprites, but below any floating sprites or the debuff shader. The following parameters control the text drawn, with their defaults specified:
- `text = ""`: this must be a string. The string will be rendered exactly as it is typed.
- `text_offset = { x = 0, y = 0 }`: this table controls the position of the center of the whole string of text. The origin is the top-left of the canvas.
- `text_colour = G.C.UI.TEXT_LIGHT`: this controls the color of the text itself.
- `text_width = canvasW`: This scales the text by specifying its width in pixels.
- `text_height = canvasH`: This scales the text by specifying its height in pixels.
- `ref_table, ref_value`: If both of these are set and the table and value actually exist, the CanvasSprite will use `ref_table[ref_value]` as its text string *instead of* the string in the `text` parameter.
- `text_font = 1`: This can be set to the key of a font in `SMODS.Fonts`, or the index of a font in `G.FONTS`. The default value of 1 selects the standard pixel font used throughout the rest of Balatro.
- `text_transform`: This can be a table containing all the transformation parameters for the `love.graphics.draw` call that draws the text, if you want more control over it. It must contain elements in the same order as [love.graphics.draw](https://love2d.org/wiki/love.graphics.draw) uses for its parameters, starting at `x`. (canvas_text does not support the shearing factor parameters)

To attach a CanvasSprite with canvas_text functionality to the card, you should do this (or make it an array of CanvasSprites) in the card's `set_sprites` function:
```lua
set_sprites = function(self, card, front)
  G.E_MANAGER:add_event(Event({
	  blockable = false,
		func = function()
		  card.canvas_text = SMODS.CanvasSprite {
			  text = "foobar",
			  ...
			}
			return true
	}))
end
```
The event is only necessary if you plan on referencing the card's ability table in the function (e.g. as the CanvasSprite's `ref_table`); if that is not needed, then you can just define the canvas_text variable/table directly in the function.

## Rendering CanvasSprites yourself
This will only be a basic setup tutorial, and will not go into detail about how to use Love2D's graphics features. Love2D has [its own documentation](https://love2d.org/wiki/love.graphics) about that subject.

An [SMODS.DrawStep](https://github.com/Steamodded/smods/wiki/SMODS.DrawStep) will be needed. In the DrawStep's `func`, you should first check for the card that actually has the CanvasSprite (e.g. SMODS's DrawStep for rendering canvas_texts checks `if card.canvas_text` before doing anything). Then the function should consist of the following (assuming the CanvasSprite was created at `card.canvassprite`):
```lua
love.graphics.push()
love.graphics.origin()
card.canvassprite.canvas:renderTo(love.graphics.clear, 0, 0, 0, 0)
-- rendering code
love.graphics.pop()
```
The `love.graphics` functions safely reset the origin to the top left of the canvas without affecting anything else, and the `renderTo` function both demonstrates how to access the sprite's canvas object itself and clears the canvas to full transparency (since it's being drawn to every frame).
