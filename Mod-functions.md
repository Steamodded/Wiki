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

## Advanced Mod descriptions
Default mod descriptions defined within your mod's metadata supports basic text wrapping, but no further formatting like changing the colour and scale of text or inserting variables, as well as localization. By using [Localization files](https://github.com/Steamodded/smods/wiki/Localization#localization-files-recommended), you can create a description for your mods with support for all the formatting of other descriptions. Your description should be placed in `G.localization.descriptions.Mod[mod_id]`.

### `mod.description_loc_vars`
To change your description dynamically through variables and alternate keys or specify a default text colour and scale, you can define this function on your mod object. This function behaves like [`loc_vars`](https://github.com/Steamodded/smods/wiki/Localization#loc_vars) on other objects.
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

### `mod.ui_config`
You can define this table in your mod object to change the colours of its menu.
```lua
SMODS.current_mod.ui_config = {
	colour = G.C.L_BLACK, -- Main UI box
    bg_colour = {G.C.GREY[1], G.C.GREY[2], G.C.GREY[3], 0.7}, -- Background
    back_colour = G.C.ORANGE, -- Back button
    tab_button_colour = G.C.BOOSTER, -- Tabs buttons
	outline_colour = G.C.JOKER_GREY, -- Main UI box outline
	author_colour = G.C.JOY.XYZ, -- Author text
	author_bg_colour = G.C.CLEAR, -- Author box background
	author_outline_colour = G.C.JOKER_GREY, -- Author box outline
    collection_bg_colour = {G.C.GREY[1], G.C.GREY[2], G.C.GREY[3], 0.7}, -- Collection background (Defaults to bg_colour)
    collection_back_colour = G.C.ORANGE, -- Collection background (Defaults to back_colour)
	collection_outline_colour = G.C.JOKER_GREY, -- Collection background (Defaults to outline_colour)
    collection_option_cycle_colour = G.C.RED, -- Collection option cycle button
}
```

### `mod.custom_ui`
This function can be used to manipulate your mod's description tab arbitarily. It receives a table of nodes as an argument, you can modify this table to insert additional elements or modify existing ones. See also: [Building a UI](https://github.com/Steamodded/smods/wiki/UI-Guide).

## `mod.debug_info`
This is a property that can be set by mods to show debug information on the crash screen.
- Setting this to a string will display that string under your mod in the crash screen.
- Setting this to a table of strings will display a list with each key and its value under your mod in the crash screen.

## In-game functionality
You may want to have some functionality happen with your mod installed independently of some other object being present. For cases like this, defining these mod-scope functions is a good alternative to destructively modifying the underlying vanilla function and helps preserve compatibility with other mods.

### `mod.reset_game_globals(run_start)`
Set up global game values that reset each round, similar to vanilla jokers like Castle, The Idol, Ancient Joker, and Mail-In Rebate. `run_start` indicates if the function is being called at the start of the run.
