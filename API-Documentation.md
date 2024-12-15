# API Documentation
## General remarks
All Steamodded APIs are built on an Object Oriented Programming engine. As such, Steamodded objects share some common methods and parameters, described below.
### Creating an object
Create an object by calling a class, for example `SMODS.Joker`, with a single table parameter. Each class may have required fields and may provide some default values.

Your table must have a `key` field, which must be a unique string. Don't worry about collisions with other mods&mdash;your mod's prefix will always be prepended to `key`. With a few exceptions, you don't have to worry about this.
```lua
-- Skeleton for creating an object
SMODS.Class {
	key = 'key',
	other_param = 0,
	loc_txt = {
		-- ...
	},
}
``` 

### Common parameters
- `name`: Used by the game to identify certain objects, but Steamodded doesn't use it at all. You can ignore it.
- `loc_txt`: Most objects display a text description, and some objects need to display additional text in the collection and other places. The `loc_txt` field defines these pieces of text. You can provide a single table for every language, or provide a subtable for each language. If the currently selected language isn't provided, the `default` subtable, the English (`'en_us'`) subtable, or `loc_txt` itself will be used as defaults, in that order. Refer to your object's documentation for what fields need to go in `loc_txt`.

	The following are examples of valid `loc_txt` tables:
	- `{ name = 'Name', text = { 'This is example text' } }`
	-
	```lua
		{
			['en-us'] = {
				name = 'Name',
				text = { 'Example', 'text', 'on', 'five', 'lines'},
			},
			['fr'] = {
				-- French translation
			},
			['nl'] = {
				-- Dutch translation
			},
			['default'] = {
				-- a different default text
				-- leave this empty to allow
				-- custom languages to provide
				-- their own translation
			}
		}
	```
	-
	```lua
	{
		['en-us'] = {
			-- Sometimes, more text is required than just a name and a description
			label = 'Label',
			description = {
				name = 'Name',
				text = { 'A moderately long', 'description of', 'your effect.' }
			}
		}
	}
	```
	-
	```lua
	{
		-- The simplest option: use a single table
		label = 'Label',
		description = {
			name = 'Name',
			text = { 'A moderately long', 'description of', 'your effect.' }
		}
	}
	```
- `unlocked`: Sets the default unlock state of an object. If set to `false`, your object won't be obtainable until it's unlocked; make sure to implement an unlock condition.
- `discovered`: Sets the default discovery state of an object. If set to `true`, your object can be viewed in the collection without needing to find it in a run.
- `config`: Put initial values for your object in `config`. Cards representing your object have an `ability` table, whose initial value is a copy of `config`, but can change during the game.

	Only specific keys are copied from `config`; define an `extra` table inside `config` to make sure your initial values aren't lost.
```lua
config = {
	extra = {
		custom_value = 10,
		another_value = 'something',
	},
}
```
- `raw_atlas_key` (optional): Parameter for all objects with an `atlas` field. Your mod prefix won't be prepended to `atlas` if this is set; it's needed if you want to reference an atlas from the base game or another mod.
- `dependencies` (optional): A list of one or more mod IDs. Your object will only be loaded when all specified mods are present. This is useful for cross-mod compatibility, but not for dependencies that are required for your mod to function properly. In that case, add a dependency to your mod header.

### Taking ownership
You may need to modify vanilla objects or objects from another mod. Use the `take_ownership` function to modify an existing object; then, you can use all of Steamodded's API functions on it. Each key-value pair of the provided table overwrites the object's value, while the rest of the object is left intact.
```lua
SMODS.Joker:take_ownership('joker', {
	cost = 5,
	calculate = function(card, context)
		-- more on this later
	end
})
```

### API functions
Each class's API functions are explained on that class's Wiki page. The following lists parameter names common to these API functions.
| Identifier 	| Meaning 		|
| :--------- 	| :--------- 	|
| `self`		| The table this method is defined on. This is generally a prototype object that can't keep track of state. |
| `card`		| An instance of the game's `Card` class. Keeps track of state in an `ability` field. |