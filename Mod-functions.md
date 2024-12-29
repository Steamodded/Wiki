# Mod functions
## `mod.config_tab`
Your mod can have an optional config page that is accessed through the Mods menu. 

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

### Creating a Config Tab
To create a **config tab**, use this block of code.
	```lua
	SMODS.current_mod.config_tab = function()
		return {n = G.UIT.ROOT, config = {
			-- config values here, see 'Building a UI' page
		}, nodes = {
			-- work your UI wizardry here, see 'Building a UI' page
		}}
	end
	```

## `mod.extra_tabs`
You may want to create additional pages besides your config tab.

### Creating Additional Tabs
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

## `mod.custom_collection_tabs`
This sets up additional collection pages to be accessed through the 'Other' button.
```lua
SMODS.current_mod.custom_collection_tabs = function()
	return {
		{
			button = UIBox_button({
				button = 'your_collection_something', -- calls `G.FUNCS.your_collection_something` when pressed, define accordingly
				id = 'your_collection_something',
				label = {localize('b_your_label')}, -- or pass a string directly instead of using `localize`
				count = G.DISCOVER_TALLIES['something'], -- optional; should have numeric 'tally' and 'of' values (for discovery counts)
				minw = 5, -- optional; minimum width of your button
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

## Advanced Mod descriptions
Default mod descriptions defined within your mod's metadata supports basic text wrapping, but no further formatting like changing the colour and scale of text or inserting variables, as well as localization. By using [Localization files](https://github.com/Steamopollys/Steamodded/wiki/Localization#localization-files-recommended), you can create a description for your mods with support for all the formatting of other descriptions. Your description should be placed in `G.localization.descriptions.Mod[mod_id]`.

### `mod.description_loc_vars`
To change your description dynamically through variables and alternate keys or specify a default text colour and scale, you can define this function on your mod object.
```lua
SMODS.current_mod.description_loc_vars = function(self)
	return {
		vars = { 'some var', colours = {HEX('123ABC') }}, -- text variables (e.g. #1#) and colour variables (e.g. {V:1})
		key = 'alternate_key', -- Get description from G.localization.descriptions.Mod[key] instead
		scale = 1.1, -- Change text scale, default 1
		text_colour = HEX('1A2B3C'), -- Default text colour if no colour control is active
		background_colour = HEX('9876547F')
	}
end
```

## In-game functionality
You may want to have some functionality happen with your mod installed independently of some other object being present. For cases like this, defining these mod-scope functions is a good alternative to destructively modifying the underlying vanilla function and helps preserve compatibility with other mods.

### `mod.reset_game_globals(run_start)`
Set up global game values that reset each round, similar to vanilla jokers like Castle, The Idol, Ancient Joker, and Mail-In Rebate. `run_start` indicates if the function is being called at the start of the run.