# API Documentation: `SMODS.Seal`
- **Required parameters:**
	- `key`,
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - For use with localization file, the description should be set as `descriptions.Other[key:lower()..'_seal']`.
		- `loc_txt` should contain an additional `label` string. It is used on badges, while `name` is displayed at the top of info boxes. For use with localization files, this label should be set as `misc.labels[key:lower()..'_seal']`.
- **Optional parameters** *(defaults)*:
    - `atlas = 'Joker', pos = { x = 0, y = 0 }` [(reference)](https://github.com/Steamodded/smods/wiki/SMODS.Atlas#applying-textures-to-cards)
    - `config = {}, discovered = false, no_collection, prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
        - Values in `config` are copied to `card.ability.seal` when the seal is applied to `card`.
    - `badge_colour = HEX('FFFFFF')`
    - `sound = { sound = 'gold_seal', per = 1.2, vol = 0.4 }`: The sound that should play when the seal is applied to a card.
        - `sound`: The key of the sound to play.
        - `per`: The pitch at which the sound should be played.
        - `vol`: The volume at which the sound should be played.
    - `always_scores`: If `true`, editioned card always counts in scoring.
    - `never_scores`: If `true`, editioned card never counts in scoring (supersedes `always_scores`).

## API methods
- `calculate(self, card, context)` [(reference)](https://github.com/Steamodded/smods/wiki/Calculate-Functions)
- `loc_vars, generate_ui` [(reference)](https://github.com/Steamodded/smods/wiki/Localization#Localization-functions)
- `get_p_dollars(self, card) -> number`
    - Gives money when a card with this seal is played.
- `update(self, card, dt)`
    - For actions that happen every frame.
- `draw(self, card, layer)`
	- Draws the sprite and shader of the seal.
