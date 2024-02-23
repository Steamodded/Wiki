# MOD CORE API SPRITE Documentation

## WARNING: SPRITE API IS IN ALPHA

## Overview
The MOD CORE API SPRITE is a Lua script designed to manage sprite objects within Balatro. This interface facilitates the creation, registration, and integration of custom sprites into the existing game structure.

## File Structure for you mod
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

## Missing Implementation
Even if adding custom assets (so assets not replacing standard ones, but totally new ones), there is for now no possibility to use them with the API.
This option will be added in a small amount of time. 


Remember to never overwrite a function without calling it's reference from your new function. If you do not, you will overcome every other Mods code, making your mod incompatible with the others.

For more information and examples, you can look at the examples mods provided in this repository. 
