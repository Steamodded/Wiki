# `SMODS.Sticker`

- **Required parameters:**
  - `key`
  - `loc_txt` or localization entry [(reference)](https://docs.smods.dev/API%20Documentation/Localization)
    - `loc_txt` should contain a `label` string used for the card's badge text
- **Optional parameters** *(defaults)*:
  - `atlas = 'stickers', pos = { x = 0, y = 0 }` [(reference)](https://docs.smods.dev/Game%20Objects/SMODS.Atlas#applying-textures-to-cards)
  - `config = {}, prefix_config, dependencies, badge_colour, text_colour` [(reference)](https://docs.smods.dev/Game%20Objects/API-Documentation#common-parameters)
    - `config` values will be saved to `card.ability[sticker_key]`
  - `hide_badge`: If set to `true`, no badge is shown for this sticker.
    - `default_compat`: Default compatibility with cards. If `true`, all cards can have this sticker unless otherwise specified.
    - `compat_exceptions`: Array of keys of centers that have non-default compatibility with this sticker.
      - `default_compat = true`: sticker cannot be applied to centers in `compat_exceptions`
      - `default_compat = false`: sticker can only be applied to centers in `compat_exceptions`
    - `sets`, list of pools that this sticker is allowed to be applied on, format:

 ```lua
  {
   Joker = true
  }
 ```

  - `rate = 0.3`: Chance of the sticker applying on an eligible card
  - `needs_enable_flag`: If set to `true`, this sticker requires `G.GAME.modifiers['enable_'..self.key]` to be `true` before it can be applied.
  - `always_scores`: If `true`, cards with this sticker always count in scoring.
  - `never_scores`: If `true`, cards with this sticker never count in scoring (supersedes `always_scores`).
  - `replace_base_card`: If `true`, don't draw base card sprite or give base card chips. *(added in (RELEASE))*
  - `no_rank`: If `true`, cards with this sticker have no rank. *(added in (RELEASE))*
  - `no_suit`: If `true`, cards with this sticker have no suit. *(added in (RELEASE))*
  - `any_suit`: If `true`, cards with this sticker count as any suit. *(added in (RELEASE))*
  - `shatters`: If `true`, cards with this sticker break on destruction like a Glass Card. *(added in (RELEASE))*

## API methods

- `calculate(self, card, context)` [(reference)](https://docs.smods.dev/API%20Documentation/Calculate-Functions)
- `loc_vars` [(reference)](https://docs.smods.dev/API%20Documentation/Localization#Localization-functions)
  - Due to some constraints, the functionality of `loc_vars` on stickers is limited. Out of all possible return values, only `vars`, `key` and `set` are supported.
- `should_apply(self, card, center, area, bypass_roll) -> bool`
  - Returns true if the sticker can be applied to the card.
  - `bypass_roll` skips the RNG check and only looks for compatibility
  - If this function is redefined it will ignore all optional parameter flags listed above. You can call and store the return of `SMODS.Sticker.should_apply(self, card, center, area, bypass_roll)` in this function to retain the default functionality.
- `apply(self, card, val)`
  - Handles applying and removing the sticker
  - By default, sets `card.ability[self.key]` to `config` if it exists and `val` is truthy or to `val` otherwise.
  - It is recommended to not redefine this function. If you still need to, you can call `SMODS.Sticker.apply(self, card, val)` in this function to retain the default functionality.
- `draw(self, card, layer)`
  - Draws the sprite and shader of the sticker.

### Sticker methods

- `Card:add_sticker(sticker, bypass_check)`
 Use this function to add a sticker to a card
  - `sticker`, `key` of sticker as a string
  - `bypass_check`, *boolean*

- `Card:remove_sticker(sticker)`
 Use this function to remove a sticker from a card
  - `sticker`, `key` of sticker as a string
