# API Documentation: SMODS.Achievement
- **Required parameters:**
	- `key`,
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - Rather than a `text` table, `loc_txt` should contain a `description` table. When using localization files, the name should be placed in `misc.achievement_names[key]`, the description should be placed in `misc.achievement_descriptions[key]`.
- **Optional parameters** *(defaults)*:
    - `atlas = 'Joker', pos = { x = 1, y = 0 }, hidden_pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
        - `pos` is used when the achievement has been earned, `hidden_pos` if it has not been earned.
    - `earned`: Achievement is considered "earned". Achievement will stay earned on loaded profiles unless `reset_on_startup` is true
    - `reset_on_startup`: Unearns the achievement if already earned when the profile is loaded
    - `bypass_all_unlocked = false`: Sets if the achievement can be earned on profiles that pressed the "Unlock All" button
    - `hidden_name = true`: Hides the name of the achievement if not earned
    - `hidden_text`: Hides the description of the achievement if not earned

## API methods
- `unlock_condition(self, args) -> bool`
    - Runs every time `check_for_unlock` is called. Returns true if the achievement should be earned. 