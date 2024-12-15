# API Documentation: `SMODS.Edition`
- **Required parameters:**
	- `key`
	- `shader`, the shader key for your shader. `shader = false` is allowed. This will create edition with no shader.
- **Optional parameters** *(defaults)*:
	- `atlas = 'Joker'`, The atlas that is used to draw the edition in the collection
	- `pos = {x = 0, y = 0}`, The position used to draw the edition in the collection
	- `discovered = false`,
	- `unlocked = true`,
	- `loc_txt`, Skeleton:
	```lua
		{
			name = '',
			label = '',
			text = { '' },
		}
	```
		- `name` is displayed at the top of info boxes
		- `label` is displayed in the badge
	- `config`, Skeleton:
	```lua
		{
			chips = 10,
			mult = 10,
			x_mult = 2,
			p_dollars = 3,
			card_limit = 2,
		}
	```
	- `in_shop = false`, whether the edition can spawn naturally in the shop/booster packs
	- `weight = 0`, the weighting of the edition, see below for more details
	- `extra_cost`, the extra cost applied to cards in the shop with the edition
	- `apply_to_float = false`, whether the shader should be applied to floating sprites or not
	- `badge_colour = G.C.DARK_EDITION`, used to set a custom badge colour
	- `sound = { sound = "foil1", per = 1.2, vol = 0.4 }`, used to set a custom sound when the edition is applied
	- `disable_shadow`, disables shadow drawn under the card.
	- `disable_base_shader = false`, whether the base shader should be applied (`booster` for Booster packs and Spectral cards, `voucher` for Vouchers and Invisible Joker, `dissolve` otherwise). Enable this if your shader modifies card transparency or shape in any way. Example:<br/>![image](https://github.com/user-attachments/assets/c7b32385-e486-40c2-9a83-c8a09a67185c)

## API methods
- `loc_vars(self, info_queue) -> { vars ?= table }`
	- Used for passing variables to edition descriptions.
- `get_weight(self) ->  number `
	- Used to modify the weight of edition on certain conditions.
- `on_apply(card) -> void`
	- Used to modify Card when edition is applied
- `on_remove(card) -> void`
	- Used to modify Card when edition is removed
- `on_load(card) -> void`
	- Used to modify Card with edition when it is loaded from save file.

## Other information
### SMODS.Shader
A shader is required for a custom edition.
- **Required parameters:**
	- `key`
	- `path`, the file name of your shader. Shaders must be stored in `assets/shaders/` and be a `.fs` file. The name of your file **must** be the name of your shader.

### API methods
- `send_vars(sprite, @nullable card) -> table`
	- Used to send extra vars to the shader. Card may be `nil` if shader is not applied to a Card. Returned table entries are sent to the shader via `Shader:send(key, value)`. Usage example may be found in `example_mods/Mods/EditionExamples` - [here](https://github.com/Steamopollys/Steamodded/blob/4cfad55f612447db9cd85afed54044a70f7b9337/example_mods/Mods/EditionExamples/EditionExamples.lua#L126) and [here](https://github.com/Steamopollys/Steamodded/blob/4cfad55f612447db9cd85afed54044a70f7b9337/example_mods/Mods/EditionExamples/assets/shaders/gold.fs#L24)


#### Working with Shaders
[ionized.fs](https://github.com/Steamopollys/Steamodded/blob/main/example_mods/Mods/EditionExamples/assets/shaders/ionized.fs) has shader code explanation with comments.
For a general guide, look at [LOVE2D introduction to shaders](https://blogs.love2d.org/content/beginners-guide-shaders).

If you want to see vanilla Balatro shaders, unzip the Balatro.exe and go to `resources/shaders` folder.

To see values for default externs, check out `engine/sprite.lua` -> `Sprite:draw_shader`.


#### Useful shaders resources
- [The book of shaders](https://thebookofshaders.com) - beginner friendly introduction to shaders.
- [GLSL Editor](https://patriciogonzalezvivo.github.io/glslEditor/) - preview your fragment shaders live.
- [GLSL Image Processing System](https://github.com/kajott/GIPS/releases) - preview your fragment shaders live. The program additionally provides some built-in shaders as examples.
- [Inigo Quilez articles](https://iquilezles.org/articles/) - in-depth articles on algorithms and techniques you could use in shaders. A lot of those are for 3D, but there's some 2D stuff as well.
- [Shadertoy](https://www.shadertoy.com) - tons of shaders from other people to learn from. A lot of them are pretty complex and 3D, but you can find simple 2D ones.

Note: in all resources the language is slightly different from LOVE2D shaders language, but the logic works the same way.


### Weight System
The default game editions have the following weights
```
negative = 3
polychrome = 3 (takes negative's weight in some circumstances)
holographic = 14
foil = 20
```
The base chance for an edition to appear in the shop is 4%, thus there is a 2% chance for a foil joker to appear. Adding custom editions to the shop maintains this 4% chance. Therefore, if you add an edition with a weight of 40, it will have a 2% chance to spawn, and foil will be reduced to 1% chance.

When the Hone and Glow Up vouchers are purchased, the weights of the base editions are adjusted. Custom editions do not have this bonus applied by default. This means that the vouchers do not increase the edition chances to 8%/16%, but rather increase the chances of the default editions by 2X and 4X respectively. To add your edition to the Hone and Glow Up functionality, add this to your edition definition.
```lua
get_weight = function(self)
	return G.GAME.edition_rate * self.weight
end
```

### Edition methods
- `Card:set_edition(edition, immediate, silent)`
	- `edition`, `nil` removes edition, `key` of edition as a string
	- `immediate`, *boolean*
	- `silent`, *boolean*
Use this function to set the edition of a card

- `poll_edition(_key, _mod, _no_neg, _guaranteed, _options)` *(defaults)*
	- `_key = edition_generic`, *string* - key value for a random seed
	- `_mod = 1`, *number* - scale of chance against base card
	- `_no_neg = false`, *boolean* - disables negative edition chance *(chance is added to polychrome)*
	- `_guaranteed = false`, *boolean* - disables base card
	- `_options = all editions marked in_shop`, *table* - List of editions to poll. Two variations.
	Option 1 - list of keys for included editions. This method respects defined weights,
	```lua
	{"e_foil", "e_holo","e_negative"}
	```
	Option 2 - table of keys and weights. Used to override default weights,
	```lua
	{
		e_foil = 1,
		e_holo = 1,
		e_negative = 1
	}
	```