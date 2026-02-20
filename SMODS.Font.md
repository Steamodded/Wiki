# API Documentation: `SMODS.Font`
This class allows you to use custom Fonts. Your mod must be located in its own subdirectory of the `Mods` folder. To make sure your font works, you have to put it in a `fonts` subdirectory inside `assets` The file structure should look something like this:
```bash
Mods
└──FontMod
	├── main.lua
	└── assets
		└── fonts
              └── HelveticaNeue.ttf

```

- **Required parameters:**
	- `key`: The key used to indentify your font (e.g. `'HelveticaNeue` *(`modname_HelveticaNeue`)*)
	- `path`: The font's name, including the extension (e.g. `'HelveticaNeue.ttf'`).
	
- **Optional parameters** *(defaults)*:
  - `render_scale`: Sets the font size. This is generally better as a higher value so it can be scaled down. The default value is `200`.
  - `FONTSCALE` : Multiplier to scale down the font to the intended display size. Multiplies `render_scale` so that it renders at a proper size. The default value is `0.1`.
  - `DESCSCALE` : Determines how big the description text should be in relation to normal text. Keep in mind that mobile UI makes this 1.5x bigger. The default font's value is `1`.
  - `squish` : Determines horizontal width of each character. The default value is `1`.
  - `TEXT_HEIGHT_SCALE` : Determines line spacing. The default value is `0.83`.
  - `TEXT_OFFSET`(table) : Determines the offset that the font is rendered. You might need to adjust this if the font renders in unexpected places. The default value is `{x=0, y=0}`.
  
- **Example Code**
```lua
SMODS.Font{
    key = "HelveticaNeue",
    path = "HelveticaNeue.ttf",
    render_scale = 200,
    TEXT_HEIGHT_SCALE = 0.83,
    TEXT_OFFSET = {x=0,y=0},
    FONTSCALE = 0.1,
    squish = 1,
    DESCSCALE = 1
}
```

## Applying fonts to text
For your font to show up in game, you can assign it to formatted text using the *style modifier code* `f:` Example:
```lua
j_modname_example = {
  name = "{f:modname_HelveticaNeue}Example",
  text = {
    {
    "{C:chips,f:modname_HelveticaNeue}+#1#{} Chips",
    },
  },
},
```
