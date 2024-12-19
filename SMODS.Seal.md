# API Documentation: `SMODS.Seal`
- **Required parameters:**
	- `key`,
- **Optional parameters** *(defaults)*:
	- `loc_txt`, Skeleton:
    ```lua
        {
			name = '',
            label = '', -- used for badge labels
			text = { '' },
		}
    ```
    - `atlas = 'centers'`
    - `pos = { x = 0, y = 0 }`
    - `discovered = false`
    - `badge_colour = [white]`
    - `sound = { sound = 'gold_seal', per = 1.2, vol = 0.4 }`: The sound that should play when the seal is applied to a card.
        - `sound`: The key of the sound to play.
        - `per`: The pitch at which the sound should be played.
        - `vol`: The volume at which the sound should be played.

## API methods
- `loc_vars(self, info_queue, card) -> {vars ?= table, key ?= string }`
    - Allows adding additional tooltips to cards with seals. `vars` are passed to the seal's main description. Returning a `key` changes the localization entry (in set `Other`) to use for the description.
    - The description tooltip is added to `info_queue` before this gets called. `info_queue[#info_queue] = nil` can be used to remove it in case you want to replace it with something else entirely.
- `calculate(self, card, context)`
    - Used for common seal effects during the scoring phase. You may need to add more context calls to `Card:calculate_seal()`.
- `get_p_dollars(self, card) -> number`
    - Gives money when a card with this seal is played.
- `update(self, card, dt)`
    - For actions that happen every frame.
- `draw(self, card, layer)`
	- Draws the sprite and shader of the seal.
