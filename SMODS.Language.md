# API Documentation: `SMODS.Language`
- **Required parameters:**
	- `key` (does not get prefixed by default)
    - `label`: The label displayed on the language selection screen
- **Optional parameters** *(defaults)*:
	- `font = 1`: When a number is specified, use the corresponding font provided by the game.
        - 1: m6x11plus (Latin alphabet)
        - 2: NotoSansSC-Bold (Simplified Chinese)
        - 3: NotoSansTC-Bold (Traditional Chinese)
        - 4: NotoSansKR-Bold (Korean)
        - 5: NotoSansJP-Bold (Japanese)
        - 6: NotoSans-Bold (Used in-game for Russian)
        - 7: Also m6x11plus (for some reason)
        - 8: GoNotoCurrent-Bold (unused asset)
        - 9: GoNotoCJKCore (unused asset)
        - You can also specify a table to use your own font. It should look something the following. The file is expected to be found in the `assets/fonts` subdirectory within your mod.
        ```lua
        {
            file = "myfont.ttf",
            render_scale = self.TILESIZE*10,
            TEXT_HEIGHT_SCALE = 0.83,
            TEXT_OFFSET = {x=10,y=-20},
            FONTSCALE = 0.1,
            squish = 1,
            DESCSCALE = 1
        },
        ```
    - `loc_key`: Treats the language with the given key as a base for this one, keeping any unchanged localization strings intact and adding changes from your localization and fonts, where applicable.

You should place a localization file for your language's translation in a file at `localization/[key].lua` within your mod files, where `[key]` is the language's key. Steamodded will also load files named this way from other mods if the language is active. Non-existent entries default to English text.