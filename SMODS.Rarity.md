# API Documentation: `SMODS.Rarity`
- **Required parameters:**
    - `key`
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - The only supported field is `name`. In localization files, it must be set as both `misc.labels['k_'..key:lower()]` and `misc.dictionary['k_'..key:lower()]`.
- **Optional parameters** *(defaults)*:
    - `pools`: Table with a list of ObjectType keys to add this rarity to. Skeleton:
    ```lua
    {
        ["Joker"] = true, --uses self.default_weight when polled
        ["Joker"] = { weight = 0.7 }, -- alternatively specify a weight directly for each ObjectType
    }
    ```
    - `badge_colour`: Colour of the rarity's badge.
    - `default_weight`: Setting a numerical value for `default_weight` enables cards with this rarity to appear in the shop at the specified weight.
        - This sets a default weight, which can be modified by accessing `G.GAME[key:lower() .. '_mod']` during a run.
> [!NOTE]
> The game's default rarity weights for Jokers are `0.7` (Common), `0.25` (Uncommon) and `0.05` (Rare). Registering additional rarities will make other rarities less likely to appear, and weights don't correspond directly to chances. For example, if you add a joker rarity with a default weight of `0.5`, the chance of a shop joker having your rarity isn't 1 in 2, but instead `0.5/1.5` or 1 in 3, and only about 47% of shop jokers will be Common instead of the previous 70%.

## API methods
- `get_weight(self, weight, object_type) -> number`
    - Returns weight. Use for finer control over the rarity's weight. 
- `gradient(self, dt)`
    - Used to control the badge colour gradient.
    - **Defining a `gradient` function on your rarity is deprecated.**

## Util methods
- `SMODS.poll_rarity(_pool_key, _rand_key) -> key`
    - Polls all rarities tied to `_pool_key` and returns rarity key. 