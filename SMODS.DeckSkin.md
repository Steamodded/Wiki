
# API Documentation: `SMODS.DeckSkin`
This API extends the game's Friends of Jimbo collabs screen to create new deck skins for all suits, including modded ones.

Note: Atlases in this class are not automatically prefixed.

- **Required parameters:**
    - `key`
    - `suit`: The suit this skin applies to.
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
    - `palettes`: A list of tables with the following values:
        - `key` (Use `'hc'` or `'lc'` to consider this palette a default high-/low-contrast palette)
        - `ranks`: A list of ranks the skin provides sprites for.
        - `display_ranks`: A list of ranks to show in the preview.
        - `atlas`: Atlas for the cards.
        - `pos_style = 'deck'`: Determines how to access sprite positions.
            - As a string:
                - `'deck'`: Use the `pos` table of the playing card.
                - `'suit'`: `y` position is always zero, `x` position is taken from the card's `pos`.
                - `'collab'`: Use the base game's `G.COLLABS.pos`.
                - `'ranks'`: Use the palette's rank list for the `x` position.
            - As a table:
                - `fallback_style`: Any of the above strings. Is used when a rank that isn't specified is loaded.
                - `[rank]`: Using a rank as a key, it takes a table with an atlas and pos.
        - `colour`: Replaces the suit's colour in the `G.C` table with this one when skin is applied.
        - `suit_icon`: A table defining the icon for the suit
            - `atlas`: An atlas with the icons
            - `pos = 0`: The position for the icon. If set to a number, it will use y = pos, x = suit's vanilla icon pos. If it's a table [see reference](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards).
	    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - `hc_default` (optional): If this is true, use high-contrast textures for unchanged sprites.

## API Methods
- `has_ds_card_ui(card, deckskin, palette)`
		- Enable UI on cards in preview
		- Called for every currently displayed card in preview
- `generate_ds_card_ui(card, deckskin, palette, info_queue, desc_nodes, specific_vars, full_UI_table)`
		- Freely define the UI of card descriptions in preview
		- Called for every card that has a UI in preview, enabled by `has_ds_card_ui`

