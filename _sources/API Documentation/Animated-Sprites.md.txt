# Animated Sprites

Most `SMODS.Center` objects, such as [SMODS.Joker](https://github.com/Steamodded/smods/wiki/SMODS.Joker), define an `atlas` field with the key to the [SMODS.Atlas](https://github.com/Steamodded/smods/wiki/SMODS.Atlas) that holds its texture (at the xy position defined in the object's `pos` field).
An object can define an *animated* texture by using an `SMODS.Atlas` that defines `atlas_table = "ANIMATION_ATLAS"|"STATE_ATLAS"`, respectively creating an `AnimatedSprite` or a `StateSprite`.

## AnimatedSprite

An `AnimatedSprite` functions like a regular `Sprite`, except its `:animate()` method is called each frame. This allows it to change its texture after some time has elapsed, thus animating it.
By default, an `AnimatedSprite` takes on the `frames` and `fps` arguments defined in its `SMODS.Atlas`' `sprite_args` field, but defining `sprite_args` on an object such as a `SMODS.Joker` allows overriding those default values.

This is the structure of the `sprite_args` table:

- `start_pos: xy position`, the start xy position of the animation. (defaults to object's `pos` field)
- `frames: number`, or `end_pos: xy position`, e.g. `{x=1,y=3}`. (frames may wrap between rows in the texture) (defaults to object's `SMODS.Atlas`' `frames` field)
- `flipped_h/v: boolean`, whether the sprite should be drawn flipped *horizontally* or *vertically*.
- `fps: number`, *frames per second* of the animation. (defaults to object's `SMODS.Atlas`' `fps` field, or `10` (`G.ANIMATION_FPS`))
- `frame_duration: number`, default frame duration, inverse of `fps`, as in; if `fps = 10` and `frame_duration = 2`, each frame takes `1 second / 10 (fps) * 2 (frame_duration) = 0.2 seconds`, for an effective `5` fps. (defaults to `1`)
- `frame_durations: table`, a table of *per-frame* frame duration by index, e.g. `{[2] = 3}` would make the second frame last three times as long.
- `frame_order: string|fun(sprite):integer`, `"linear"`, or `"random"`, or a table defining which frame appears at which index, e.g. `{[1] = 3, [2] = 1, [3] = 2}` (third frame -> first frame -> second frame), or a function returning the frame. (defaults to `"linear"`)

## StateSprite

*Added by SMODS in version 26.829.0*. For `StateSprite`s, most of the above holds, except its `sprite_args` contains a `states` field, which defines a table of states by key:

- *all of the above, behaving as defaults*
- `default_state: [state_key]`, the default state a sprite should start with.
- `states_offset: xy offset`, applied to the start and end positions of a state's animation. (allows reusing state tables for other objects that share the fundamental state structure)
- `states`:
  - `[state_key 1]`: (the arbitrary name of the state, e.g. `moving`)
    - `start_pos: xy position`, same as for `AnimatedSprite`, for this state.
    - `frames: number`, or `end_pos: xy position`, e.g. `{x=1,y=3}`, same as for `AnimatedSprite`, for this state.
    - `flipped_h/v: boolean`, same as for `AnimatedSprite`, for this state.
    - `fps: number`, same as for `AnimatedSprite`, for this state.
    - `frame_duration: number`, same as for `AnimatedSprite`, for this state.
    - `frame_durations: table`, same as for `AnimatedSprite`, for this state.
    - `frame_order: string|fun(sprite):integer`, `"linear"`, same as for `AnimatedSprite`, for this state.
    - *optional* `exit_to: [state_key]|function(state_table, sprite): [state_key]`: if defined, the `StateSprite` automatically changes state to the `state_key` after one iteration.
  - `[state_key 2]`: (the arbitrary name of a second state, e.g. `jumping`)
    - `...`

Each state may define the regular `sprite_args` arguments, taking priority over any values also present in the `sprite_args` table. A `StateSprite`'s state can be changed by calling `:set_state()` on it directly, or `Card:set_sprite_state()` on a card that has a `StateSprite` as its `self.children.center` sprite.
