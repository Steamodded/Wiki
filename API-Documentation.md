# API Documentation

- [General Remarks](#general-remarks)
- [Creating an Object](#creating-an-object)
- [Common Parameters](#common-parameters)
	- [`name`](#name)
	- [`loc_txt`](#loc_txt)
	- [`unlocked`](#unlocked)
	- [`discovered`](#discovered)
	- [`no_collection`](#no_collection)
	- [`config`](#config)
	- [`prefix_config`](#prefix_config)
	- [`dependencies`](#dependencies)
	- [`display_size`](#display_size)
	- [`pixel_size`](#pixel_size)
- [Taking Ownership](#taking-ownership)
- [API Functions](#api-functions)

***

## General Remarks
All Steamodded APIs are built on an Object Oriented Programming engine. As such, Steamodded objects share some common methods and parameters, described below.
## Creating an Object
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

## Common Parameters
### `name`
Used by the game to identify certain objects, but Steamodded doesn't use it at all. You can ignore it.

### `loc_txt`
Most objects display a text description, and some objects need to display additional text in the collection and other places. The `loc_txt` field defines these pieces of text. You can find an in-depth explanation of `loc_txt` and other ways to load description strings on [this page](https://github.com/Steamodded/smods/wiki/Localization).

### `unlocked`
Sets the default unlock state of an object. If set to `false`, your object won't be obtainable until it's unlocked; make sure to implement an unlock condition.

### `discovered`
Sets the default discovery state of an object. If set to `true`, your object can be viewed in the collection without needing to find it in a run.

### `no_collection`
If set to `true`, this object will not show up in the collection.

### `config`
Put initial values for your object in `config`. Cards representing your object have an `ability` table, whose initial value is a copy of `config`, but can change during the game. Defaults to `{}` when not specified.
- Only specific keys are copied from `config`; define an `extra` table inside `config` to make sure your initial values aren't lost.
	```lua
	config = {
		extra = {
			custom_value = 10,
			another_value = 'something',
		},
	}
	``` 

### `prefix_config`
Defining this table gives you control over where prefixes should be added to keys you specify. The default behavior is to add a class prefix (if it exists) and your mod prefix.
- Supported keys:
	- `key`
	- `atlas`: Includes all atlas-related fields like `hc_atlas` and `lc_atlas` on suits and ranks
	- `shader`
	- `card_key`
	- `above_stake`
	- `applied_stakes`: Also supports options per index
- Each key can be set to a table or the value `false`. Effects:
	- `mod`: Setting this to `false` removes your mod prefix.
	- `class`: Setting this to `false` removes the class prefix.
	- If `false` is used as the value instead of a table, no prefixes are applied.
- Set `prefix_config = false` to apply no prefixes to any key.
- Example:
	```lua
	{
		prefix_config = {
			key = { mod = false },
			atlas = false, 
			applied_stakes = {
				[1] = { mod = false },
				[3] = false,
			},
		},
	}
	```

### `dependencies`
A list of one or more mod IDs. Your object will only be loaded when all specified mods are present. This is useful for cross-mod compatibility, but not for dependencies that are required for your mod to function properly. In that case, add a dependency to your mod header.

### `display_size`
Changes the display size of cards by scaling them by a factor relative to pixel size (default: `{ w = 71, h = 95 }`). 

### `pixel_size`
Changes how large the sprite of this card is considered, useful for smaller sprites like Half Joker (default: `{ w = 71, h = 95 }`).

## Taking Ownership
You may need to modify vanilla objects or objects from another mod. Use the `take_ownership` function to modify an existing object; then, you can use all of Steamodded's API functions on it. Each key-value pair of the provided table overwrites the object's value, while the rest of the object is left intact. Objects you take ownership of have your mod's badge added to them, unless you suppress this with the `silent` argument.
```lua
SMODS.Joker:take_ownership('joker', -- object key (class prefix not required)
    { -- table of properties to change from the existing object
	cost = 5,
	calculate = function(self, card, context)
		-- more on this later
	end
    },
    true -- silent | suppresses mod badge
)
```

## API Functions
Each class's API functions are explained on that class's Wiki page. The following lists parameter names common to these API functions.
| Identifier 	| Meaning 		|
| :--------- 	| :--------- 	|
| `self`		| The table this method is defined on. This is generally a prototype object that can't keep track of state. |
| `card`		| An instance of the game's `Card` class. Keeps track of state in an `ability` field. |
