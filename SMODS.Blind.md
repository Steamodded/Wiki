# API Documentation: `SMODS.Blind`
- **Required parameters:**
	- `key`
- **Optional parameters** *(defaults)*:
	- `loc_txt`, Skeleton:
	```lua
		{
			name = '',
			text = { '' },
		}
	```
	- `dollars = 5`: Amount of money obtained when defeated.
	- `mult = 2`: Required score relative to the Ante's Base score.
	- `boss`: Marks this Blind as a Boss Blind and specifies on which Antes it can appear (`{ min = 1, max = 10 }`). `max` is an artifact and is not functional. Use `in_pool` instead for advanced conditions.
		- `boss.showdown`: Marks this Blind as a Final Boss Blind that shows up on every multiple of the winning Ante. `min` is ignored, use `in_pool` to restrict spawning.
	- `boss_colour`: Sets the background colour to use while playing this Blind (e.g. `HEX('56789A')`)
	- `pos = { x = 0, y = 0 }`
		- The `y` value determines the row to use for the animation.
	- `atlas = 'blind_chips'`
	- `discovered = false`
	- `debuff = {}`: Configure vanilla Blind effects with these fields:
		- Disallowing hands in full:
			- `hand = { ['Hand Type'] = true}` for a specific set of hands,
			- `h_size_ge = n`, must play at least `n` cards,
			- `h_size_le = n`, must play at most `n` cards.
		- Debuffing cards:
			- `suit = 'Hearts'` for one specific suit,
			- `value = '2'` for one specific rank,
			- `nominal = n` for all ranks scoring `n` base chips,
			- `is_face = true` for all face cards.
		- Note that these effects are ignored if you specify a `debuff_hand` or `debuff_card` function respectively.
	- `ignore_showdown_check`: Enabling this allows `in_pool` to be evaluated regardless of whether a showdown Boss Blind was requested or not.
	- `vars = {}`: variables for the Blind's description in the collection. Fallback if `collection_loc_vars` isn't set.

## API methods
In all of the following methods, use the global variable `G.GAME.blind` to
refer to the current blind. (The base game uses `self` to refer to the current blind in `Blind:fff()`.)
- `set_blind(self)`
	- Effects that activate when this Blind is selected
- `disable(self)`
	- Reverting effects when this Blind gets disabled
- `defeat(self)`
	- Reverting effects when this Blind is defeated
- `drawn_to_hand(self)`
	- Effects that activate when cards are drawn to hand
- `press_play(self)`
	- Effects that activate when a hand is played
- `recalc_debuff(self, card, from_blind) -> bool`
	- Determines what cards should be debuffed by this Blind
- `debuff_hand(self, cards, hand, handname, check) -> bool`
	- Determines if a hand is disallowed by this Blind
- `stay_flipped(self, area, card) -> bool`
	- Determines what cards are drawn face down
- `modify_hand(self, cards, poker_hands, text, mult, hand_chips) -> number, number, bool`
	- Used for modifications on the base score of played hands. Expected return values in order are:
		- The modified value of `mult`
		- The modified value of `hand_chips`
		- A boolean value indicating whether any values were changed
- `get_loc_debuff_text(self) -> string`
	- Allows modifying text displayed for debuff warnings on invalid hands
- `loc_vars(self) -> { vars ?= table, key ?= string }`
	- Used for passing variables to Blind descriptions. If you need access to multiple descriptions, you can specify a `key` to a different description.
- `collection_loc_vars(self) -> { vars ?= table, key ?= string }`
	- Used for passing variables to Blind descriptions when viewing the collection. If not defined, the game will use the `vars` field on your object.
- `in_pool(self) -> bool`
	- For implementing advanced restrictions on when a Blind may appear in a run. This puts `boss.min` and `boss.max` restrictions out of effect.
	- Unless `ignore_showdown_check` is set, this function will not be evaluated in the following cases:
		- A showdown Boss Blind should appear, but this Blind is a regular Boss Blind.
		- A regular Boss Blind should appear, but this Blind is a showdown Boss Blind.