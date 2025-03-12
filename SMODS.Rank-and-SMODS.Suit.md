# API Documentation: `SMODS.Rank`
- **Required parameters:**
	- `key`
    - `card_key`: Used to create keys for playing cards, formatted like `S_R`, where `S` is the suit's and `R` is the rank's card key. Your mod prefix gets prepended by default.
    - `pos`: This is a partial `pos` table that only needs an `x` coordinate. As such, your atlas should organize ranks in columns.
    - `nominal`: The amount of chips this rank should score.
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - `loc_txt` should contain only a `name` string. For localization files, place this string in `misc.ranks[key]`.
- **Optional parameters** *(defaults)*:
    - `lc_atlas = 'cards_1', hc_atlas = 'cards_2'`: Atlas to use for low-contrast and high-contrast settings respectively. Use the same atlas key if you don't have separate high contrast textures. [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
    - `shorthand = key`: Short descriptor used in deck preview.
    - `face_nominal`: Numeric value (normally between 0 and 1) that determines the displayed order of ranks with the same nominal value.
    - `face = false`: whether this rank counts as a face card.
    - `next = {}`: The keys contained in the `next` table are considered to come after this card, e.g. for the purpose of evaluating straights.
    - `strength_effect = { fixed = 1 }`: Determines how cards of this rank behave when Strength is used.
        - If `strength_effect.fixed` is a numeric value and `next` indexed at that value is a valid rank's key, always convert into that rank.
        - If `strength_effect.random` is `true`, choose a random rank from `next`.
        - If `strength_effect.ignore` is `true` or none of the above apply, do nothing.
    - `straight_edge = false`: If this is `true`, this card behaves like an Ace in straights, i.e., it can only be used as the lowest- or highest-order card in the hand.
    - `suit_map = { Hearts = 0, Clubs = 1, Diamonds = 2, Spades = 3 }`
        - For any suit keys present as keys in `suit_map`, prefer using this rank's atlas over the suit's atlas. The value at the suit's key will be used as each sprite's `x` position instead of the one specified by the suit.
        - This indicates that you provide sprites for certain suits with your rank. Combinations of suits and ranks where neither side supports the other, blank sprites are used instead.

# API Documentation: `SMODS.Suit`
- **Required parameters:**
	- `key`
    - `card_key`: Used to create keys for playing cards, formatted like `S_R`, where `S` is the suit's and `R` is the rank's card key. Your mod prefix gets prepended by default.
    - `pos`: This is a partial `pos` table that only needs a `y` coordinate. As such, your atlas should organize suits in rows.
    - `ui_pos`: Sprite position of the miniature suit symbol used in deck view.
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - `loc_txt` should contain a `singular` and `plural` string only. When using localization files, assign to `misc.suits_singular[key]` and `misc.suits_plural[key]` respectively.
- **Optional parameters** *(defaults)*:
    - `lc_atlas = 'cards_1'`: Atlas to use when high-contrast cards are disabled.
    - `hc_atlas = 'cards_2'`: Atlas to use when high-contrast cards are enabled.
    - `lc_ui_atlas = 'ui_1'`: Atlas for miniature suit symbols when high-contrast cards are disabled.
    - `hc_ui_atlas = 'ui_2'`: Atlas for miniature suit symbols when high-contrast cards are enabled.
    - `lc_colour = [white]`: Text colour when high-contrast cards are disabled.
    - `hc_colour = [white]`: Text colour when high-contrast cards are enabled.

## API methods
These methods are available for both suits and ranks.
- `loc_vars` [(reference)](https://github.com/Steamodded/smods/wiki/Localization#Localization-functions)
    - This method provides very limited functionality compared to its counterpart on other classes. It has no support for any return values, but it does allow you to add tooltips to `info_queue`.
- `draw(self, card, layer)`
	- Draws additional sprites or shaders on cards.

## Utility: pools and randomness
- Suits and Ranks have special support for `in_pool` with an extended argument signature: `in_pool(self, args)`. `args.initial_deck` indicates when a starting deck is being generated. This can be used to set rules for when your cards should be added to starting decks independently of whether they can show up in other places. 
- Even though `SMODS.Suits` and `SMODS.Ranks` are unordered tables, it is possible to feed them directly into `pseudorandom_element` to get a random suit or rank while respecting `in_pool`. Example: `local rank = pseudorandom_element(SMODS.Ranks, pseudoseed('myrank'))`.
