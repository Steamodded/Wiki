# API Documentation: `SMODS.DeckSkin`
This API extends the game's Friends of Jimbo collabs screen to create new deck skins for all suits, including modded ones.
- - **Required parameters:**
    - `key`
    - `suit`: The suit this skin applies to.
    - `ranks`: A list of ranks the skin provides sprites for.
    - `lc_atlas`: Atlas for the low-contrast version.
- **Optional parameters** *(defaults)*:
    - `loc_txt`, string base value
    - `posStyle = 'deck'`: Determines how to access sprite positions.
        - `'deck'`: Use the `pos` table of the playing card.
        - `'suit'`: `y` position is always zero, `x` position is taken from the card's `pos`.
        - `'collab'`: Use the base game's `G.COLLABS.pos`
    - `hc_atlas`: Atlas for the high-contrast version. Defaults to `lc_atlas`.