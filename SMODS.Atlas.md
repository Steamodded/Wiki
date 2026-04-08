# API Documentation: `SMODS.Atlas`
This class allows you to use custom spritesheets ("Atlases") or replace existing ones. Your mod must be located in its own subdirectory of the `Mods` folder. Due to Balatro's pixel smoothing setting, it is required to provide both a single and double resolution image file. The file structure should look something like this:
```bash
Mods
└──NegateTexturePack
	├── NegateTexturePack.lua
	└── assets
		├── 1x
		│   ├── BlindChips-negate.png
		│   ├── Jokers-negate.png
		│   └── boosters-negate.png
		└── 2x
			├── BlindChips-negate.png
			├── Jokers-negate.png
			└── boosters-negate.png
```

- **Required parameters:**
	- `key`
	- `px`: the width of each individual sprite at single resolution, in pixels.
	- `py`: the height of each individual sprite at single resolution, in pixels.
	- `path`: the image file's name, including the extension (e.g. `'Jokers-negate.png'`).
		- If you want to use different sprites depending on the selected language, you can also provide a table:
		```lua
		path = {
			['default'] = 'Jokers.png', -- use this for any languages not specified
			['zh_CN'] = 'Jokers-zh-CN.png',
			['ja'] = 'Jokers-ja.png',
		}
		```
- **Optional parameters** *(defaults)*:
	- `prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
	- `atlas_table = 'ASSET_ATLAS'`
		- Use `ASSET_ATLAS` for non-animated sprites
		- Use `ANIMATION_ATLAS` for animated sprites
		- Use `ASSET_IMAGES` for other images
	- `frames`: for animated sprites, you must provide the number of frames of the animation. Each row should contain one animation, with each column showing one frame.
	- `raw_key`: Set this to `true` to prevent the loader from adding your mod prefix to the `key`. Useful for replacing sprites from the base game or other mods.
	- `language`: Restrict your atlas to a specific locale. Useful for introducing localized sprites while leaving other languages intact.
	- `disable_mipmap`: Disable mipmap being applied to this texture. Might remove artifacts on smaller textures.

## Applying textures to cards
For objects of any class that have a visual representation in-game, you can assign a sprite from your atlas by setting `atlas` to the key of your atlas and `pos` to the position of the sprite on this atlas (`{ x = 0, y = 0 }` refers to the top-left corner). `hc_atlas` and/or `lc_atlas` can also be set instead to assign different sprites between the High Contrast and Low Contrast settings. For floating sprites, similar to Legendary Jokers or The Soul, you can define a `soul_pos` for that sprite, which can contain a custom `draw` function for that sprite.

Example:
```lua
SMODS.Joker {
	key = 'my_joker',
	atlas = 'my_atlas',
	pos = { x = 1, y = 1 }, -- second row, second colum
	soul_pos = { 
		x = 0 , y = 0 -- first row, first colum
		draw = function(card, scale_mod, rotate_mod) -- omit this function if you want the default behaviour
			-- custom draw code
		end
	}
}
```
