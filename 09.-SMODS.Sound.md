# API Documentation: `SMODS.Sound`
This class allows you to play custom sounds and music tracks or replace existing ones. Your mod must be located in its own subdirectory of the `Mods` folder. The file structure should look something like this:
```bash
Mods
└──Cryptid
	├── Cryptid.lua
	└── assets
		└── sounds
			├── e_mosaic.ogg
			├── music_big.ogg
			└── music_jimball.ogg
```
- **Required parameters:**
	- `key`
    - `path` - the sound file's name, including the extension (e.g. `'music_jimball.ogg'`)
		- Supported file types include `*.ogg`, `*.wav` and `*.mp3`. It is not recommended to use MP3 files.
		- If you want to use different sound files depending on the selected language, you can also provide a table:
		```lua
		path = {
			['default'] = 'my_sound.ogg',
			['nl'] = 'my_sound-nl.ogg',
			['pl'] = 'my_sound_pl.ogg',
		}
		```
- **Optional parameters** *(defaults)*:
    - `pitch = 0.7` - Specify a custom pitch shift for music tracks.
	- `volume = 0.6` - Specify a custom volume for music tracks.
		- These modifiers do not apply to regularly played sounds. Specify them as arguments to `play_sound` instead.
	- `replace` - Behaves like `self:create_replace_sound(replace)`, see below
	- `sync` - For music tracks only - configuration for synchronizing different music tracks.
		- Default behavior: sync with all tracks that aren't configured otherwise.
		- `sync = false`: Do not sync with anything.
		- If provided a table, only try to sync with keys that correspond to a true value, e.g.:
			```lua
			sync = {
				['mymusic1'] = true,
				['mymusic2'] = true,
			}
			```
		- You can use metatables to exclude certain tracks but include everything else:
			```lua
			sync = setmetatable({
				['somemusic1'] = false,
				['somemusic2'] = false,
				['somemusic3'] = false,
			}, { __index = function() return true end })
			```
		- In any case, syncing is only possible when both tracks agree on it. It is recommended synced tracks have the same length

## API methods
- `select_music_track(self) -> number`
	- This function is called each frame to decide what music to play. Return values that are not `nil`, `false` or a number are converted to zero. The music track that returned the highest value is to be played.
		- Your track's sound code must contain the string `music` if you are using this.

## Utility functions
- `create_replace_sound(self, replace)`
	- If `replace` is a string, indefinitely replace it with this one until it is replaced again.
	- If `replace` is a table, the key of the sound being replaced is `replace.key`. Specify a number `replace.times` to temporarily replace it that amount of times. Additional arguments may be passed as `replace.args`.
- [STATIC] `SMODS.Sound:create_stop_sound(key, times)`
	- Supress sounds with the given sound code `times` amount of times or indefinitely.
- [STATIC] `SMODS.Sound:register_global()`
	- Register all sound files found in the `assets/sounds` directory of the current mod. Use the file names without their extensions as keys.
- [STATIC] `SMODS.Sound:get_current_music()`
	- Polls `select_music_track` on all sound objects that have it, returns the key of the music to play.
	- You may override this function to take full control of the played music.

## Vanilla music tracks
The following overview provides a list of music tracks present in the base game and when they play. Custom music with conditions overrides all of these.
- `music1`: default track. Plays when none of the below apply
- `music2`: booster pack music. Plays for all vanilla boosters except Celestial Packs. Plays for all booster packs that have a sparkles effect or don't have a meteor effect.
- `music3`: booster pack music. Plays for Celestial Packs and any other packs with the meteor effect (but no sparkles effect).
- `music4`: shop music. Plays in the shop, outside of booster packs.
- `music5`: boss music. Plays during Boss Blinds.