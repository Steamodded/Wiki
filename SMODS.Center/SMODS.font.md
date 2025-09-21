
# API Documentation: `SMODS.Font` 

This repository provides a comprehensive guide and examples for using `SMODS.Font` in Balatro mods 

## Introduction
Balatro's text system supports basic styling, but `SMODS.Font` (introduced in Steamodded v1.x) allows modders to define and apply custom fonts. Fonts can be referenced by a unique key (e.g., `{f:my_custom_font}`) or by index (e.g., `{f:5}` for Balatro's default Noto JP font) in text strings using the `{f:}` modifier. This integrates with Balatro's text parsing system, making it versatile for modding.

## set up
. **Add Font Files**: Place TrueType font files (.ttf) in your mod's directory (e.g., `fonts/` subfolder).

## Usage
### Defining a Custom Font
Define a font in your mod's Lua file (e.g., `main.lua`) using `SMODS.Font`. 

```lua
SMODS.Font({
    key = 'custom_font',
    path = 'fonts/custom.ttf',
    render_scale = 200,         -- Base size in pixels (default: 200)
    TEXT_HEIGHT_SCALE = 0.83,   -- Line spacing (default: 0.83)
    TEXT_OFFSET = {x = 0, y = 0}, -- Alignment tweak (default: {0,0})
    FONTSCALE = 0.1,            -- Scale multiplier (default: 0.1)
    squish = 1,                 -- Horizontal stretch (default: 1)
    DESCSCALE = 1               -- Description scale (default: 1)
})
```

### Applying the Font
Use the `{f:key_or_index}` modifier in any text string that supports Balatro's formatting (e.g., Joker descriptions, tooltips, names). The closing tag `{/f}` is optional but recommended for resetting.

```lua
loc_txt = {
    name = "{f:custom_font}Styled Name",
    text = {
        "Gains {C:money}$#1#{} per round,",
        "{f:5}Default Font Mix{}"  -- Uses Balatro's default font index 5 (Noto JP)
    }
}
```

Reset to the default font using `{}` or `{f:0}` (base font index).

### Parameters
- **key** (string, required): Unique identifier for the font (e.g., 'my_custom_font'). Use in `{f:}` tags.
- **path** (string, required): Relative path to the .ttf file (e.g., 'fonts/myfont.ttf').
- **render_scale** (number, optional, default: 200): Base font size in pixels. Higher values improve quality when scaled.
- **TEXT_HEIGHT_SCALE** (number, optional, default: 0.83): Adjusts line spacing.
- **TEXT_OFFSET** (table {x: number, y: number}, optional, default: {x=0, y=0}): Shifts text for alignment.
- **FONTSCALE** (number, optional, default: 0.1): Scales font size (effective size = render_scale * FONTSCALE).
- **squish** (number, optional, default: 1): Adjusts horizontal character width.
- **DESCSCALE** (number, optional, default: 1): Scales description text (mobile multiplies by 1.5x).

**Notes**:
- Parameters often require trial and error due to LÖVE's font rendering variability.
- Only TrueType (.ttf) fonts are supported.
- Fonts are stored in `SMODS.Fonts` and accessible globally after definition.

## Applying Fonts in Different Contexts
1. **UI Elements**: Use `{f:}` in parsed text (e.g., tooltips, achievements, `SMODS.UI` elements).
2. **Localizations**: Link a font to a language in `SMODS.Language`:
   ```lua
   SMODS.Font({
       key = 'jp_custom_font',
       path = 'fonts/jpfont.ttf',
       render_scale = 200
   })

   SMODS.Language({
       key = 'jp_custom',
       label = 'Japanese (Custom Font)',
       font = 'jp_custom_font',
       -- Other language params...
   })
   ```
3. **Custom Rendering**: For manual rendering (e.g., with `love.graphics.print`), access the font via `SMODS.Fonts['key']` and set it with `love.graphics.setFont()`.
4. **Non-Parsed Text**: Hook into rendering functions using `SMODS.inject` for unsupported text areas.

## Examples
### Custom Joker with Font
Create a Joker with a custom font for its name and description.

```lua
-- Define the font
SMODS.Font({
    key = 'my_custom_font',
    path = 'fonts/myfont.ttf',
    render_scale = 250,
    TEXT_HEIGHT_SCALE = 0.85,
    TEXT_OFFSET = {x = 0, y = -2},
    FONTSCALE = 0.12,
    squish = 0.95,
    DESCSCALE = 1.1
})

-- Define the Joker
SMODS.Joker({
    key = 'custom_joker',
    loc_txt = {
        name = "{f:my_custom_font}Cool Joker Name",
        text = {
            "Gains {C:money}$#1#{} per round,",
            "{f:5}日本語 Bonus Text{}"  -- Uses default font index 5 (Noto JP)
        }
    }
})
```


