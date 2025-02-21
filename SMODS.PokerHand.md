# API Documentation: `SMODS.PokerHand`
- **Required parameters:**
	- `key`
	- `mult`, `chips`: Base Mult and Chips
    - `l_mult`, `l_chips`: Amount of Mult/Chips scaling per hand level
    - `example`: Hand example to show in the Run Info tab, format:
    ```lua
        {
            { 'S_K', false }, -- King of Spades, does not score
            { 'S_9', true }, -- 9 of Spades, scores
            { 'D_9', true }, -- 9 of Diamonds, scores
            { 'H_6', false }, -- 6 of Hearts, does not score
            { 'D_3', false } -- 3 of Diamonds, does not score
        }
    ```
    - `evaluate`
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - Rather than a `text` table, `loc_txt` should contain a `description` table. The description is displayed when viewing the hand in the Run Info menu. When using localization files, the name should be placed in `misc.poker_hands[key]`, the description should be placed in `misc.poker_hand_descriptions[key]`.
- **Optional parameters** *(defaults)*:
    - `prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
	- `visible = true`: Is this hand visible in the poker hands menu from the start, or is it hidden until played for the first time?
    - `above_hand`: Sets the position in the hands menu above the specified hands. By default, hands are ordered by the product of their chips and mult.
    - `order_offset`: If this numeric parameter is specified, add its value to the product of chips and mult for the purpose of ordering.

## API methods
- `evaluate(parts, hand) -> table`
    - This function is used to determine if the played cards contain this hand, and which cards it's made up of.
    - See the next section for an explanation of parts.
    - The returned table should be an array that contains a table of all scoring cards, e.g.,
        - `{ hand }` if all cards score,
        - `{ SMODS.merge_lists(parts._flush, parts._straight) }` for all scoring cards that are part of a straight or flush, or
        - `{}` if the cards don't contain this hand.
- `modify_display_text(self, cards, scoring_hnd) -> string?`
    - Changes the displayed name of the poker hand. 
    - Returns the key to the new display name that gets localized (placed inside of `misc.poker_hands[key]`). 

## Utility functions
- `SMODS.merge_lists(...) -> table`
    - Takes any amount of parts and flattens them into an array containing all scoring cards present in any of the parts. This is particularly useful for composite hands.

# API Documentation: `SMODS.PokerHandPart`
This utility class allows easily re-using the same poker hand constructs to build composite hands without much boilerplate code. Before all hand types get evaluated, each part gets executed and added to `parts` for access in the `evaluate` functions.
- **Required parameters:**
    - `key`: *Keep in mind that your mod prefix is prepended to this!*
    - `func(hand) -> table`: This expects the same return value format as `evaluate` on poker hands.
- **Pre-existing parts:**
    - `parts._2, parts._3, parts._4, parts._5` **contain all groups of at least 2/3/4/5 cards that share the same rank.**
        - `parts._all_pairs` **provides a list of all cards that are part of at least one pair in the hand.** (This is equivalent to `SMODS.merge_lists(parts._2)`.)
        - `parts._flush` **corresponds to a Flush being present in the hand.**
        - `parts._straight` **corresponds to a Straight being present in the hand.**
        - `parts._highest` **holds the card with the highest nominal value**.