# `SMODS.Seal`

- **Required parameters:**
  - `key`,
  - `loc_txt` or localization entry [(reference)](https://docs.smods.dev/API%20Documentation/Localization)
    - For use with localization file, the description should be set as `descriptions.Other[key:lower()..'_seal']`.
      - `loc_txt` should contain an additional `label` string. It is used on badges, while `name` is displayed at the top of info boxes. For use with localization files, this label should be set as `misc.labels[key:lower()..'_seal']`.
- **Optional parameters** *(defaults)*:
  - `atlas = 'Joker', pos = { x = 0, y = 0 }` [(reference)](https://docs.smods.dev/Game%20Objects/SMODS.Atlas#applying-textures-to-cards)
  - `config = {}, discovered = false, no_collection, prefix_config, dependencies, badge_colour, text_colour` [(reference)](https://docs.smods.dev/Game%20Objects/API-Documentation#common-parameters)
    - Values in `config` are copied to `card.ability.seal` when the seal is applied to `card`.
  - `attributes`: *(Added in 26.829.0)* Array of Attributes this seal has [(reference)](https://docs.smods.dev/Game%20Objects/SMODS.Attributes/)
  - `badge_colour = HEX('FFFFFF')`
  - `sound = { sound = 'gold_seal', per = 1.2, vol = 0.4 }`: The sound that should play when the seal is applied to a card.
    - `sound`: The key of the sound to play.
    - `per`: The pitch at which the sound should be played.
    - `vol`: The volume at which the sound should be played.
  - `always_scores`: If `true`, cards with this seal always count in scoring.
  - `never_scores`: If `true`, cards with this seal never count in scoring (supersedes `always_scores`).
  - `replace_base_card`: If `true`, don't draw base card sprite or give base card chips. *(added in 26.829.0)*
  - `no_rank`: If `true`, cards with this seal have no rank. *(added in 26.829.0)*
  - `no_suit`: If `true`, cards with this seal have no suit. *(added in 26.829.0)*
  - `any_suit`: If `true`, cards with this seal count as any suit. *(added in 26.829.0)*
  - `shatters`: If `true`, cards with this seal break on destruction like a Glass Card. *(added in 26.829.0)*

## API methods

- `calculate(self, card, context)` [(reference)](https://docs.smods.dev/API%20Documentation/Calculate-Functions)
- `loc_vars, generate_ui` [(reference)](https://docs.smods.dev/API%20Documentation/Localization#Localization-functions)
- `get_p_dollars(self, card) -> number`
  - Gives money when a card with this seal is played.
- `update(self, card, dt)`
  - For actions that happen every frame.
- `draw(self, card, layer)`
  - Draws the sprite and shader of the seal.

## Seal methods

- `Card:set_seal(seal, immediate, silent)`
  - Use this function to set the seal of a card
    - `seal` - `key` of seal as a string, `nil` to remove the seal
    - `immediate` - if `true` applies the seal immediately not creating an event
    - `silent` - if `true` removes sounds
