# API Documentation: `SMODS.Challenge`
- **Required parameters:**
    - `key`
- **Optional parameters** *(defaults)*:
    - `loc_txt`, Skeleton:
    ```lua
    {
        name = '',
    }
    ```
    - `rules`: Custom rules and modifiers for the challenge.
        - `rules.custom`: Expects a list of tables with an `id` and optionally a `value` field (defaults to `true`). Sets `G.GAME.modifiers[id] = value`. Text for each rule should be stored in `G.localization.misc.v_text['ch_c_'..id]`, `value` is passed as a variable. The following custom rule keys are defined by the base game:
            - `all_eternal`, `chips_dollar_cap`, `daily`, `debuff_played_cards`, `discard_cost`, `flipped_cards`, `inflation`, `minus_hand_size_per_X_dollar`, `no_extra_hand_money`, `no_interest`, `no_reward`, `no_reward_specific`, `no_shop_jokers`, `none`, `set_eternal_ante`, `set_joker_slots_ante`, `set_seed`.
        - `rules.modifiers`: Expects a list of tables with an `id` and a `value` field. Sets each corresponding base modifier to the given value. The following modifiers are supported:
            - `dollars`, `discards`, `hands`, `reroll_cost`, `joker_slots`, `consumable_slots`, `hand_size`.
    - `jokers`: Expects a list of tables that represent jokers added at the start of the run. Each table can have the following fields:
        - `id` (required): The key of the joker to create.
        - `edition`: The edition of the joker, if any, given without the `e_` prefix.
        - `eternal`: If the joker is eternal.
        - `pinned`: If the joker is pinned.
    - `consumeables`: Behaves like `jokers`, but for consumables.
        - Supports all fields of `jokers` except `pinned`.
    - `vouchers`: Behaves like `jokers`, but for vouchers redeemed at the start of the run.
        - Supports the same fields as `consumeables`, but `edition` and `eternal` have no functional effect beyond displaying in the preview UI.
    - `restrictions`: Contains information about objects that are banned in this challenge.
        - `restrictions.banned_cards`: Expects a list of tables with keys to ban in their `id` fields.
            - This can be used to ban jokers, consumables, vouchers and booster packs. 
            - If a table has an `ids` field containing a list of center keys, only `id` is shown as banned in the challenge UI, but all of the `ids` are banned.
        - `restrictions.banned_tags`: Expects a list of tables with valid tag keys in their `id` fields.
        - `restrictions.banned_other`: Expects a list of tables with valid keys in their `id` field and a `type` string with the value `'blind'`.
            - Despite the name, the UI for this only supports using this to ban blinds.
            - Functionally, all three options achieve the same task of adding specified keys to `G.GAME.banned_keys`.
    - `deck`: Defines the challenge's deck.
        - `deck.type = 'Challenge Deck'`: The deck type for this challenge. It is not recommended to change this value.
        - `deck.cards`: Defines the cards present in the deck using a list of *control tables*. Control tables have the following structure:
            - `s`: Suit of the card, given by its `card_key`.
            - `r`: Rank of the card, given by its `card_key`.
            - `e`: Enhancement of the card, given by its key.
            - `d`: Edition of the card, given by its key without the `e_` prefix.
            - `g`: Seal of the card, given by its key. *(The key for this option is based on Gold Seals being the only available seals in the demo version.)* 
        - `deck.yes_ranks`, `deck.yes_suits`: Can be used only if no `cards` table is specified. Expects a key-indexed table of ranks/suits by their `card_key` and acts as a whitelist, i.e., it includes only cards of those ranks/suits in the starting deck.
        - `deck.no_ranks`, `deck.no_suits`: Same as `yes_ranks` and `yes_suits`, but acts as a blacklist, i.e., the specified ranks/suits are excluded.
        - `deck.enhancement`: Can be used only if no `cards` table is specified. Given an enhancement by its key, apply it to all cards in the starting deck.
        - `deck.edition`: Can be used only if no `cards` table is specified. Given an edition by its key without the `e_` prefix, apply it to all cards in the starting deck.
        - `deck.seal`: Can be used only if no `cards` table is specified. Given a seal by its key, apply it to all cards in the starting deck.

## API methods
- `unlocked(self) -> bool`
    - Defines when the challenge should be unlocked (or not).