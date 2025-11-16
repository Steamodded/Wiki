# API Documentation: `SMODS.Stake`
**Class prefix:** `stake`
- **Required parameters:**
	- `key`
    - `applied_stakes`: An array of keys of stakes that should also be applied when this stake is active. This is evaluated recursively to include all stakes applied by applied stakes, so you usually don't need to specify multiple stakes here.
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - `loc_txt` should contain a `sticker` table that also consists of a `name` and `text`. It is used for the tooltip of the stake's win sticker.
        - When using localization files, the stake description should be placed in `descriptions.Stake[key]`, while the sticker description should be placed in `descriptions.Other[key:sub(7)..'_sticker']`, i.e., the `stake_` prefix is removed.
> [!IMPORTANT]
> An extra line that lists applied stakes is appended at the end of the description only when `loc_txt` is used. If you are using localization files, you should add this yourself.
- **Optional parameters** *(defaults)*:
    - `atlas = 'chips', pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
    - `sticker_atlas, sticker_pos`: The atlas and position to use for this stake's win sticker.
    - `unlocked = false, prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
        - If `unlocked` is set to `false`, the stake is unlocked by first winning a run on each of the `applied_stakes`.
    - `colour = [white]`: The colour used for this stake in the stake selection column.
    - `above_stake`: The stake's key that this stake should appear directly above in the list. By default, your stake will be placed at the top of the list.
> [!NOTE] 
> Key prefixing is applied to `applied_stakes` and `above_stake` by default. If you want your stake above a stake from the base game or other mods, this can be adjusted by using `prefix_config`. [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)

## API methods
- `loc_vars` [(reference)](https://github.com/Steamodded/smods/wiki/Localization#Localization-functions)
    - Due to how the stake description box works, the functionality of `loc_vars` on stakes is limited. `info_queue` and `card` will not be used. Out of all possible return values, only `vars`, `key` and `set` are supported.
- `modifiers()`
    - Used for applying changes to the game state when your stake is applied at the start of a run.
