# MOD CORE API SPRITE Documentation

## WARNING: SPRITE API IS IN ALPHA

## Overview
The MOD CORE API SPRITE is a Lua script designed to manage sprite objects within Balatro. This interface facilitates the creation, registration, and integration of custom sprites into the existing game structure.

## File Structure for your mod
Assets need to be located under the directory `assets` and then between the `1x` and the `2x` version. It means that your assets will be located in:
`assets/1x/your_asset.png` and `assets/2x/your_asset.png`. The 2 version are necessary if you want to match every resolution. Example of how it would look:
```bash
# Using NegateTexturePack as an example

NegateTexturePack
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
You can tweak as you want, but the absolute rule `assets/1x` or `assets/2x` is mandatory.

## Code Structure

### Deck Object Definition
- `SMODS.Sprite`: This object serves as a blueprint for creating Sprite objects. Each Sprite has several attributes:
  - `name`: The name of the deck.
  - `top_lpath`: The top path of your assets.
  - `path`: The path for the asset.
  - `px`: Pixel X identifier for the asset.
  - `py`: Pixel Y identifier for the asset.
  - `type`: The asset type, either `animation_atli`, `asset_atli` or `asset_images`.
  - `frames`: Only used by `animation_atli` assets, represent the number of frame in an animation.

### Sprite Object Creation (`new` Method)
- This method initializes a new sprite object with specified attributes.
- `frames` is not required for non `animation_atli` assets type.
- Behind the scene, your `path` and `top_lpath` will be merged and transformed to match the specific needed format.

### Sprite Registration (`register` Method)
- This method registers a new deck in the `SMODS.Sprites` table, ensuring each sprite is unique within the mods.

### Sprite Injection (`injectSprites` Function)
- `injectSprites` integrates all registered sprite into the game's backend. It will overwrite and or add necessary assets. The function inject into the `assets` game structure, manages Sprite resolution based on the game parameters, ensures that sprites are properly recognized within the game's system and load them into the renderer. **DO NOT CALL IT UNLESS YOU KNOW WHAT YOU ARE DOING**, the Core will do it himself. 

### Sprite Render Reload Hook(`Game:set_render_settings()` overload Function)
- Ensure that the custom assets are correctly reloaded when the resolution is modified.

## Usage Example
To use this API, create one or more sprite instance and then register them. The Sprite API will inject them automaticaly:
```lua
-- Using the "NegateTexturePack" mod as an example

function SMODS.INIT.NegateTexturePack()
    sendDebugMessage("Launching Negate Texture Pack!")

    local negate_mod = SMODS.findModByID("NegateTexturePack")
    local sprite_jkr = SMODS.Sprite:new("Joker", negate_mod.path, "Jokers-negate.png", 71, 95, "asset_atli")
    local sprite_boost = SMODS.Sprite:new("Booster", negate_mod.path, "boosters-negate.png", 71, 95, "asset_atli")
    local sprite_blind = SMODS.Sprite:new("blind_chips", negate_mod.path, "BlindChips-negate.png", 34, 34, "animation_atli", 21)

    sprite_jkr:register()
    sprite_boost:register()
    sprite_blind:register()
end
```

## Base References
That's the list of textures loaded by the game, you can use it if you want to replace some of them:
```lua
-- G.animation_atli = {
--     {name = "blind_chips", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/BlindChips.png",px=34,py=34, frames = 21},
--     {name = "shop_sign", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/ShopSignAnimation.png",px=113,py=57, frames = 4}
-- }
-- G.asset_atli = {
--     {name = "cards_1", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/8BitDeck.png",px=71,py=95},
--     {name = "cards_2", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/8BitDeck_opt2.png",px=71,py=95},
--     {name = "centers", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/Enhancers.png",px=71,py=95},
--     {name = "Joker", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/Jokers.png",px=71,py=95},
--     {name = "Tarot", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/Tarots.png",px=71,py=95},
--     {name = "Voucher", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/Vouchers.png",px=71,py=95},
--     {name = "Booster", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/boosters.png",px=71,py=95},
--     {name = "ui_1", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/ui_assets.png",px=18,py=18},
--     {name = "ui_2", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/ui_assets_opt2.png",px=18,py=18},
--     {name = "balatro", path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/balatro.png",px=333,py=216},        
--     {name = 'gamepad_ui', path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/gamepad_ui.png",px=32,py=32},
--     {name = 'icons', path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/icons.png",px=66,py=66},
--     {name = 'tags', path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/tags.png",px=34,py=34},
--     {name = 'stickers', path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/stickers.png",px=71,py=95},
--     {name = 'chips', path = "resources/textures/"..self.SETTINGS.GRAPHICS.texture_scaling.."x/chips.png",px=29,py=29}
-- }
-- G.asset_images = {
--     {name = "playstack_logo", path = "resources/textures/1x/playstack-logo.png", px=1417,py=1417},
--     {name = "localthunk_logo", path = "resources/textures/1x/localthunk-logo.png", px=1390,py=560}
-- }

```

Remember to never overwrite a function without calling it's reference from your new function. If you do not, you will overcome every other Mods code, making your mod incompatible with the others.

For more information and examples, you can look at the examples mods provided in this repository. 
