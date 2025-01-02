# Creating your first mod
## Metadata
The (new) standard way to specify your mod's metadata is in a separate JSON file in your mod folder, as per the following specification:
```js
// Mods/your_mod/your_mod.json
{
	"id": "your_mod", // [required] ! Must be unique. "Steamodded", "Lovely" and "Balatro" are disallowed.
	"name": "Your Mod", // [required]
	"author": ["You", "Someone else"], // [required]
	"description": "A description of your mod.", // [required] ! To use more advanced typesetting, specify your description as a localization entry at G.localization.descriptions.Mod[id]
	"prefix": "prefix", // [required] ! Must be unique. This prefix is added to the keys of all objects your mod registers. UNLIKE LEGACY HEADERS, THERE IS NO DEFAULT VALUE.
	"main_file": "main.lua", // [required] ! This is the entry point of your mod. The specified file (including .lua extension) will be executed when your mod is loaded.
	"priority": -20, // [default: 0] ! Mods are loaded in order from lowest to highest priority value.
	"badge_colour": "FF230A", // [default: 666665] ! Background colour for your mod badge. Must be a valid hex color with 6 or 8 digits (RRGGBB or RRGGBBAA)
	"badge_text_colour": "ABC123", // [default: FFFFFF] ! Text colour for your mod badge.
	"display_name": "YM", // [default: <name>] ! Displayed text on your mod badge.
	"version": "1.0.0", // ! Must follow a version format of (major).(minor).(patch)(rev). rev starting with ~ indicates a beta/pre-release version.
	"dependencies": [
		"Steamodded (>=1.*)", // Allows any version past a 1.0.0 stable version (but disallows 1.0.0 beta versions)
		"Lovely (>=0.6)", // Allows all versions past 0.6.0 stable, including future beta versions and major version breaks
		"SomeMod (==1.0.*)", // Allows all versions past 1.0.0 stable that are 1.0.x (1.1 and later are disallowed)
		"SomeOtherMod (==1.0.0~)", // Allows 1.0.0 versions of any revision, beta or not.
		"Balatro (==1.0.1m)", // Allows only the specified version and revision.
		"OneMoreMod (>>1.0~g) (<<2~)", // << and >> are used for versions strictly less/greater than the specified one.
		// NOTE: The << operator should be used in combination with the ~ beta wildcard in order to exclude pre-release major version changes.
		"IRanOutOfIdeas (==1.*~)", // Combination of wildcard symbols. All 1.x versions are allowed, including beta.
		"Talisman | TalismanReplacement" // Multiple different mods can be used to fulfill this dependency. May want to use `provides` instead
	], // ! All mods in the list must be installed and loaded (and must fulfill version requirements), else this mod will not load.
	"conflicts": [
		"Talisman (>=1.1) (<<2~)" // Same format as for dependencies, except alternatives (|) are disallowed.
	], // ! No mods in the list (that fulfill version restrictions) may be installed, else this mod will not load.
	"provides": [
		"SomeAPIMod (1.0)"
	], // ! Use this if your mod is able to stand in for a different mod and fulfill dependencies on it. This allows the usage of a different ID so both mods can coexist. If you don't specify a valid version, your mod's version is used instead.
	"dump_loc": false // !! Not for use in distributions. Writes all localization changes made on startup to a file, for conversion from a legacy system.
}
```
Template for copying:
```json
{
	"id": "",
	"name": "",
	"display_name": "",
	"author": [""],
	"description": "",
	"prefix": "",
	"main_file": "",
	"priority": 0,
	"badge_colour": "",
	"badge_text_colour": "",
	"version": "",
	"dependencies": [],
}
```
## File header (outdated)
Using the legacy file header system is still supported, though switching to metadata files is encouraged. Steamodded will recognize your mod in this system only if the first line in your mod file is EXACTLY `--- STEAMODDED HEADER`. If you are transitioning away from using this method, make sure to remove the header to prevent Steamodded from trying to load your mod twice.

Your mod can also contain the following lines. These lines describe information about your mod and how Steamodded should load it.
- Required:
	- `--- MOD_NAME: Example Mod`
	- `--- MOD_ID: ExampleMod` (**Must be unique and without spaces**)
	- `--- MOD_AUTHOR: [You, AnotherDev, AnotherOtherDev]` (**Brackets are required**)
	- `--- MOD_DESCRIPTION: A description of your mod.` (**No line breaks, text is wrapped automatically.**)
- Optional:
	- `--- PRIORITY: -100` (**Negative values go first, positive values go last**)
	- `--- BADGE_COLOR: 123456` or `--- BADGE_COLOUR: ABCDEF`
	- `--- DISPLAY_NAME: Example` (**Shown on mod badges instead of your mod's name**)
	- `--- DEPENDENCIES: [Steamodded>=1.0.0~BETA, Mod1, Mod2>=1.0.0, Mod3<=1.7.5, Mod4>=1.0.0<=2.0]`
	- `--- CONFLICTS: [Mod5, Mod6<=0.9.9, Mod7>=0.6.2, Mod8<=1.0>=0.3.7]`
	- `--- PREFIX: example` (**Must be unique. Defaults to the first 4 letters, lowercase, of your mod's ID.**)
	- `--- VERSION: 1.0.0`
These lines can be specified in any order.

# Useful resources
- Often, something you want to do has already been implemented in the base game. Familiarizing yourself with the game's code is an important step to learn Balatro modding. To get Balatro's source code, extract the game's executable file with [7-zip](https://www.7-zip.org/). For Mac, find `Balatro.love` inside `Balatro.app` and rename it to `Balatro.zip`, then extract `Balatro.zip`.
- It can also be useful to look at code from other mod creators. The best place to find them is in the official [Balatro Discord](https://discord.gg/balatro).