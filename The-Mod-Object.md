# The Mod Object
Every mod that's found and registered by Steamodded is converted into a "Mod" object during the loading process. These are tables containing metadata and additional information that can be accessed and modified through the `SMODS.Mods` table, or by `SMODS.current_mod` when your mod is being loaded.

- [Mod Fields](#mod-fields)
	- ["Lovely" mods](#lovely-mods)
	- ["Meta" mods](#meta-mods)

- [Mod Config](#mod-config)
	- [Setting Up Your Config](#setting-up-your-config)
	- [`mod.save_mod_config`](#modsave_mod_configmod)

- [Optional Features](#optional-features)
	- [Available Features](#available-features)
	- [`mod.optional_features`](#modoptional_features)

- [Customizing Mod Page UI](#customizing-mod-page-ui)
	- [`mod.description_loc_vars`](#moddescription_loc_vars)
	- [`mod.custom_ui`](#modcustom_ui)

- [Additional Tabs](#additional-tabs)
	- [`mod.custom_collection_tabs`](#modcustom_collection_tabs)
	- [`mod.extra_tabs`](#modextra_tabs)

- [In-Game Functionality](#in-game-functionality)
	- [`mod.reset_game_globals(run_start)`](#modreset_game_globalsrun_start)
	- [`mod.set_ability_reset_keys() -> table`](#modset_ability_reset_keys---table)
	- [`mod.set_debuff(card) -> boolean|"prevent_debuff"`](#modset_debuffcard---booleanprevent_debuff)

- [Other](#other)
	- [`mod.debug_info`](#moddebug_info)

***

## Mod Fields
These are the values that can be created from the mod's metadata:
- `id` - The mod's ID. Accessing this mod through `SMODS.Mods` or from calling `SMODS.find_mod` requires knowing the mod's ID.
- `name` - The mod's name.
- `display_name` - The mod's display name. This is the text used for the mod badge.
- `description` - The mod's description.
- `priority` - Priority of the mod. Mods are sorted by this value.
- `badge_colour` - HEX color of the mod badge.
- `badge_text_colour` - HEX color of the text within the mod badge.
- `prefix` - The mod's prefix.
- `version` - The mod's version.
- `main_file` - The entry file of the mod.
- `config_file` - The config file of this mod. By default set to `"config.lua"`.
- `author` - List of mod authors.
- `dump_loc` - Flag that indicate for SMODS to dump all localization changes into a file.
- `dependencies` - Table of the mod's dependencies.
- `conflicts` - Table of the mod's conflicts.
- `provides` - Table of the mods that this mod can provide.
- `lovely` - Mods that have a `lovely.toml` file or a `lovely` folder in their directory have this flag enabled. You can use this to verify if your mod was able to load lovely patches

### "Lovely" Mods
Folders within the mod directiry that have a `lovely.toml` file or a `lovely` folder are considered "Lovely" mods. These are registered as regular mods, with default information set up and a `lovely_only` flag. 

### "Meta" Mods
Meta mods are created by Steamodded manually, as they are not a mod. These have the `"meta_mod"` flag set to `true`. These are used to allow targeting certain versions of Lovely or Balatro.

The current list of meta mods are Steamodded, Lovely, and Balatro.

***

## Mod Config
Your mod can have an optional config table and a page to modify it, accessible through the Mods menu. 

### Setting Up Your Config
Create the structure of your config in a file named `config.lua` stored in your mod directory. SMODS will take this and assign it as the config for your mod, handling modifications and reloading internally. Your `config.lua` file should follow a structure like this:
```lua
return {
	["setting_1"] = true,
	["setting_2"] = {
		["option_1"] = 50,
		["option_2"] = 3,
		["option_3"] = false,
	}
}
```

You can access your config inside your mod by using this set up `local config = SMODS.current_mod.config`. Following this, using `config.setting_1` would give you the value of setting_1 in your config.

### `mod.save_mod_config(mod)`
If you want the mod config to be handled differently from how SMODS saves mod configs, you can define this function. It will be called when SMODS goes to save your mod's config rather than the default `SMODS.save_mod_config` function. 

***

## Optional Features
Steamodded comes with additional opt-in features that requires mods to manually turn them on. 

### Available Features
- **`quantum_enhancements`** - Enables "Quantum Enhancement" contexts. Cards can count as having multiple enhancements at once. 
- **`retrigger_joker`** - Enables "Joker Retrigger" contexts. Jokers can be retriggered by other jokers or effects. 
- **`post_trigger`** - Enables "Post Trigger" contexts. Allows calculating effects after a Joker has been calculated. 
- **`cardareas`** - Table of features that would add 
	- **`deck`** - Adds `G.deck` to CardArea checks, allowing cards within the deck to be included in calculation.
	- **`discard`** - Adds `G.discard` to CardArea checks, allowing discarded cards to be included in calculation.

### `mod.optional_features`
To enable any of the optional features, you can define `optional_features` for your mod
```lua
-- optional features enabled via table
SMODS.current_mod.optional_features = {
	quantum_enhancements = true, -- will enable "Quantum Enhancement"
	-- Add any other features to enable here.
	cardareas = {}
}

-- optional features enabled via table
-- Returns a table of features to enable.
SMODS.current_mod.optional_features = function()
	return {
		quantum_enhancements = true,
		-- ...
		cardareas = {}
	}
end
```

***

## Customizing Mod Page UI
The UI elements within on your mod page can be individually customized.

### Mod Description
Default mod descriptions defined within your mod's metadata supports basic text wrapping, but no further formatting like changing the colour and scale of text or inserting variables, as well as localization. By using [Localization files](https://github.com/Steamodded/smods/wiki/Localization#localization-files-recommended), you can create a description for your mods with support for all the formatting of other descriptions. Your description should be placed in `G.localization.descriptions.Mod[mod_id]`.

#### `mod.description_loc_vars`
To change your description dynamically through variables and alternate keys or specify a default text colour and scale, you can define this function on your mod object. This function behaves like [`loc_vars`](https://github.com/Steamodded/smods/wiki/Localization#loc_vars) on other objects.
```lua
SMODS.current_mod.description_loc_vars = function(self)
	return {
		vars = {
			'some var', -- text variables (e.g. #1#)
			colours = { HEX('123ABC') } -- colour variables (e.g. {V:1})
		},
		key = 'alternate_key', -- Get description from G.localization.descriptions.Mod[key] instead
		scale = 1.1, -- Change text scale, default 1
		text_colour = HEX('1A2B3C'), -- Default text colour if no colour control is active
		background_colour = HEX('9876547F')
	}
end
```

#### `mod.custom_ui`
This function can be used to manipulate your mod's description tab arbitarily. It receives a table of nodes as an argument, you can modify this table to insert additional elements or modify existing ones. See also: [Building a UI](https://github.com/Steamodded/smods/wiki/UI-Guide).

### Additional Tabs
You can also create additional tabs to to display in your Mod's menu.

#### Creating a Config Tab
To create a **config tab**, use this block of code. This will add a tab with the displayed name "Config".
```lua
SMODS.current_mod.config_tab = function()
	return {n = G.UIT.ROOT, config = {
		-- config values here, see 'Building a UI' page
	}, nodes = {
		-- work your UI wizardry here, see 'Building a UI' page
	}}
end
```

#### `mod.custom_collection_tabs`
This sets up additional collection pages to be accessed through the 'Other' button.
```lua
SMODS.current_mod.custom_collection_tabs = function()
	return {
		{
			button = UIBox_button({
				-- calls `G.FUNCS.your_collection_something` when pressed, define accordingly
				button = 'your_collection_something', 
				id = 'your_collection_something',
				-- Displayed label on the button (using non-localized strings also works)
				label = {localize('b_your_label')},
				-- optional; should have numeric 'tally' and 'of' values (for discovery counts)
				count = G.DISCOVER_TALLIES['something'], 
				-- optional; minimum width of your button
				minw = 5,
			})
		},
		-- add more buttons here
	}
end
G.FUNCS.your_collection_something()
	G.SETTINGS.paused = true
  	G.FUNCS.overlay_menu{
    	definition = create_UIBox_your_collection_something(), -- this is the actual UI definition function
  	}
end
-- define `create_UIBox_your_collection_something()` to create the collection, see 'Building a UI'
```

#### `mod.extra_tabs`
To create **additional tabs**, use this block of code.
```lua
SMODS.current_mod.extra_tabs = function()
	return {
		{
			label = 'My Label',
			tab_definition_function = function()
				-- works in the same way as mod.config_tab
				return {n = G.UIT.ROOT, config = {
					-- config values here, see 'Building a UI' page
				}, nodes = {
					-- work your UI wizardry here, see 'Building a UI' page
				}}
			end,
		},
		-- insert more tables with the same structure here
	}
end
```

***

## In-game Functionality
You may want to have some functionality happen with your mod installed independently of some other object being present. For cases like this, defining these mod-scope functions is a good alternative to destructively modifying the underlying vanilla function and helps preserve compatibility with other mods.

### `mod.reset_game_globals(run_start)`
Set up global game values that reset each round, similar to vanilla jokers like Castle, The Idol, Ancient Joker, and Mail-In Rebate. `run_start` indicates if the function is being called at the start of the run.

### `mod.set_ability_reset_keys() -> table`
When a card's `ability` table is changed (such as calling `Card:set_ability()` on it), all previous fields are transferred from the previous `ability` table with set exceptions. This function returns a table of strings corresponding to fields that should not persist. 

### `mod.set_debuff(card) -> boolean|"prevent_debuff"`
This function is called when a card is being checked for if it should be debuffed. 
- Returning `false` or `nil` will not debuff the card. 
- Returning `true` will debuff the card. 
- Returning `"prevent_debuff"` will force to card to not be debuffed, and all other effects that would normally debuff this card are ignored.

## Other 
### `mod.debug_info`
This is a property that can be set by mods to display debug information on the crash screen.
- Setting this to a string will display that string under your mod in the crash screen.
- Setting this to a table of strings will display a list with each key and its value under your mod in the crash screen.
```lua
-- Will display "Foo" under your mod
SMODS.current_mod.debug_info = "Foo"

-- Will display "Bar: Baz" under your mod
SMODS.current_mod.debug_info = {Bar = "Baz"}
```