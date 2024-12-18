# API Documentation: `SMODS.Rarity`
- **Required parameters:**
    - `key`
- **Optional parameters** *(defaults)*:
    - `loc_txt`, Skeleton:
    ```lua
    {
        name = '', -- used on rarity badge
    }
    ```
    - `pools`: Table with a list of ObjectType keys to add this rarity to. Skeleton:
    ```lua
    {
        ["Joker"] = true, --uses self.default_rate when polled
        ["Joker"] = { rate = 0.7 },
    }
    ```
    - `badge_colour`: Colour of the rarity's badge.
    - `default_rate`: Setting a numerical value for `default_rate` enables cards with this rarity to appear in the shop at the specified rate.
        - This sets a default rate, which can be modified by accessing `G.GAME[key:lower() .. '_mod']` during a run.

## API methods
- `get_rate(self, rate, object_type) -> number`
    - Returns rate. Use for finer control over the rarity's rate. 
- `gradient(self, dt)`
    - Used to control the badge colour gradient.

## Util methods
- `SMODS.poll_rarity(_pool_key, _rand_key) -> key`
-    Polls all rarities tied to `_pool_key` and returns rarity key. 