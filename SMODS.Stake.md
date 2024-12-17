# API Documentation: `SMODS.Stake`
- **Required parameters:**
	- `key`
    - `applied_stakes`: An array of keys of stakes that should also be applied when this stake is active. This is evaluated recursively to include all stakes applied by applied stakes, so you usually don't need to specify multiple stakes here.
        - Note: Key prefixing is applied to this option by default. If you're applying stakes from the base game or other mods, this can be adjusted by using `prefix_config.applied_stakes`. For example, `prefix_config = { applied_stakes = { mod = false } }` will remove all mod prefixes. You can also specify this per index, e.g. `prefix_config = { applied_stakes = { {}, { mod = false } } }` to add a mod prefix to the first, but not the second entry.
- **Optional parameters** *(defaults)*:
    - `atlas = 'chips'`
    - `pos = { x = 0, y = 0 }`
    - `sticker_atlas`: The atlas to use for this stake's win sticker.
    - `sticker_pos`: The sprite position for the win sticker.
    - `above_stake`: The stake's key that this stake should appear directly above in the list. By default, your stake will be placed at the top of the list.
        - Note: Key prefixing is applied to this option by default. If you want your stake above a stake from the base game or other mods, this can be adjusted by using `prefix_config.above_stake`. For example, `prefix_config = { above_stake = { mod = false } }` will remove the mod prefix.
    - `colour = [white]`: The colour used for this stake in the stake selection column.
    - `unlocked = false`: Whether this stake should be unlocked by default. If this is `false`, the stake is unlocked by first winning a run on each of the `applied_stakes`.

## API methods
- `modifiers()`
    - Used for applying changes to the game state when your stake is applied at the start of a run.