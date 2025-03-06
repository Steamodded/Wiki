# API Documentation: `SMODS.Rarity`
- **Required parameters:**
    - `key`
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - The only supported field is `name`. In localization files, it must be set as both `misc.labels['k_'..key:lower()]` and `misc.dictionary['k_'..key:lower()]`.
- **Optional parameters** *(defaults)*:
    - `pools`: Table with a list of ObjectType keys to add this rarity to. Skeleton:
    ```lua
    {
        ["Joker"] = true, --uses self.default_rate when polled
        ["Joker"] = { rate = 0.7 },
    }
    ```
    - `badge_colour`: Colour of the rarity's badge.
    - `default_weight`: Setting a numerical value for `default_weight` enables cards with this rarity to appear in the shop at the specified weight.
        - This sets a default weight, which can be modified by accessing `G.GAME[key:lower() .. '_mod']` during a run.

## API methods
- `get_weight(self, weight, object_type) -> number`
    - Returns weight. Use for finer control over the rarity's weight. 
- `gradient(self, dt)`
    - Used to control the badge colour gradient.
    - **Defining a `gradient` function on your rarity is deprecated.**

## Util methods
- `SMODS.poll_rarity(_pool_key, _rand_key) -> key`
    - Polls all rarities tied to `_pool_key` and returns rarity key. 