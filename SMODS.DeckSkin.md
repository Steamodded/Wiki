
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
- `has_ds_card_ui(card, self, palette)`
		- Enable UI on cards in preview
		- Called for every currently displayed card in preview
- `generate_ds_card_ui(card, self, palette, info_queue, desc_nodes, specific_vars, full_UI_table)`
		- Freely define the UI of card descriptions in preview
		- Called for every card that has a UI in preview, enabled by `has_ds_card_ui`


## DeckSkin Crediting
Steammodded now provides built-in methods to force enable card UI in the Customize Deck menu, which allows you to credit the artists for your DeckSkins. Using similar methods to the `generate_ui` function for Centers, modders can use two functions (`has_ds_card_ui` & `generate_ds_card_ui`) to enable UI to show when hovering over specific cards in your DeckSkin preview.

## Enabling the UI (has_ds_card_ui)
For every palette you define in your DeckSkin, there is the `display_ranks` list that defines which ranks will show in the preview, and in what order. When the preview is shown on screen, `has_ds_card_ui` is called for each card. If the return of the function is `true`, then the UI will be enabled for that card.

Utilizing the `card`, `deckskin`, and `palette` args, you can filter out the enabled ui by checking the rank of the cards, checking the key of the current palette, and more.
```lua
has_ds_card_ui = function(card, deckskin, palette)
    if card.base.value == "King" then 
        return true
    end
end
```

## Defining the UI (generate_ds_card_ui)
For every card that has its UI enabled by `has_ds_card_ui`, you can define the contents of it with `generate_ds_card_ui`, much like you would define the ui with [`generate_ui`](https://github.com/Steamodded/smods/wiki/Localization#generate_ui-advanced) in Centers. 

The following is a simple method for crediting artists with this function, which is used in the code for Steammodded when crediting the original artists for the vanilla Friends of Jimbo DeckSkins. The first localize function creates the header which says "Artist", and the second is for showing the artist, whose name goes in the vars:
```lua
generate_ds_card_ui = function(card, deckskin, palette, info_queue, desc_nodes, specific_vars, full_UI_table)
    if card.base.value == "King" then
        localize{type = 'other', key = 'artist', nodes = desc_nodes, vars = {}} 
        localize{type = 'other', key = 'artist_credit', nodes = desc_nodes, vars = { "ARTIST NAME HERE" }}
    end
end
```
![Visual example of the default crediting format used in the above code, seen in Balatro: Cardsauce](https://images-ext-1.discordapp.net/external/GKGG7ScABo6P6EzBX4Ih1VePDVXKMkhXhSPbGbIExss/https/i.imgur.com/pZ1XIP2.jpg?format=webp&width=1592&height=1291)
