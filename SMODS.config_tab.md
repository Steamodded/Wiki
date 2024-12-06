# The Config Tab
Your mod can have an optional config page that is accessed through the Mods menu. 

- **Setting Up Your Config**
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

- **Creating a Config Tab**
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