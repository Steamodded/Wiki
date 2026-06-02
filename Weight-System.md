# Object Weights
*(Added in 1531zeebee)*

With the **`object_weights`** optional feature enabled, every object in the game is now polled based on a weight value that is assigned to it. By default, this value is **10**. These polls do not mirror seeded values when the feature is not enabled. To assign a non-default weight to any of your objects, add `weight = X` to your object definitions. The internal system will then respect this value when deciding which objects to choose in all areas of the game.

You can also add `get_weight = function(self, weight)` to any of your objects if they have internal ways of modifying their own weight. This function should returned the modified weight value.

Due to these changes, there is now a new polling function that you **should** use whenever you need to select an object. This will ensure that you are respecting object weights, and any modifications to them that people have made.

## `SMODS.poll_object(args) -> string|nil`
This function returns a key of an object that is appropriate for the `args` that you provide. If there are no matches *(for example if a chance roll fails)*, it will not return a value. The following arguments are supported:
- `type`: specify a single type (or attribute) to poll
- `types`: Table[string] specify a table of types to poll
- `rarities`: Table[string] specify a table of rarities to include *(only for standard object types*) <br><br>
- `pool` = Table[string] specify a table of object keys to use as the pool instead of having the function generate one <br><br>
- `filter`: function(pool) -> Table[{key = string, type = string}] specify a function to filter the pool once it has been generated, must return the modified pool
- `chance`: % of success as a decimal value 0-1, editions, enhancements and seals have a default chance internally
- `mod`: multiplier to the base chance
- `seed`: specify a seed to use for the poll chance (defaults are available)
- `type_key`: a second poll seed if repolling is used
- `append`: appended onto the poll seed
- `guaranteed`: set to `true` to override default chance
- `no_negative`: swaps negative edition to polychrome for vanilla functionality when `true`
- `blind_type`: can be set to `"boss"`, `"big"`, or `"small"` to select an appropriate boss *(NOTE: currently there is no use of big and small blinds)* <br><br>
- `print`: set to `true` to display debug messages *(useful for understanding your pool)*
*Arguments to poll attributes (default behaviour is to find an object that matches all attributes)*
- `attributes`: Table[string] specify a table of attributes to poll *(preferred for attribute polling)*
- `union`: set to `true` to switch to join each set rather than find the intersection
- `rarity`: attribute polling respects rarity by default. Set this to a rarity key to select a specific rarity, or set to `false` to ignore rarity completely
- `closest_match`: set to `true` to stop the pool becoming completely empty due to a lack of matching attributes *(NOTE: attributes are found in the order they are given)*
- `allow_duplicates`: set to `true` to allow duplicates to be given
- `allow_legendaries`: set to `true` to allow legendaries to be included *(NOTE: if the pool consists of **only** legendary objects, they are always allowed)*

## Utility

### Modifying weights through calculation
A context has been added to adjust any weighted pool when it is being created.

#### context.modify_weights
This context is used to modify weights in `SMODS.poll_object` when the **`object_weights`** optional feature is enabled.

```lua
if context.modify_weights then
```

```lua
context.modify_weights -- flag to identify this context, always TRUE
context.pool -- the booster pack center that has ended
context.pool_types
```

The pool is structured as a table of tables, where each table is structured as below. Modifying the weight value in this table will affect the final weighted table to be used.

```lua
{key = 'object_key', weight = number_of_weight}
```


### Adding alternate objects
New object types should work fine with this system, but may need some extra set up in certain scenarios. 
- If your object should only have a chance of being successful, you can set a base chance that will always be used by adding `SMODS.base_rate_percentage[type_key] = X` where `X` is a number 0-1 that represents the percent chance of generating your object. *(for example, editions have 0.04)*
- If your object that relies on chance should use the chance roll as it's poll amount *(like Editions)*, add `SMODS.no_repoll[type_key] = true`.
- If your object needs to modify the type polling key in a specific way other than default, add `SMODS.poll_keys[type_key] = {str = 'new_key', block_infill = true or false, ante = true or false}`. You can see how these affect the key by looking at `SMODS.get_poll_key` in `src/utils/weights.lua`.
- If your object isn't stored in `G.P_CENTERS`, you can add `SMODS.game_table_from_type[type_key] = table`.
