# Localization
Steamodded offers multiple ways to load strings for in-game descriptions and other labels into the game. This page offers an overview of each option and when you should use them.

- [Localization Files](#localization-files-recommended)
    - [Adding your descriptions](#adding-your-descriptions)
    - [Migrating to localization files](#migrating-to-localization-files)
- [`loc_txt`](#loc_txt)
- [`mod.process.loc_text`](#modprocessloc_text)
- [Text Formatting](#text-formatting)
- [Localization Functions](#localization-functions)
    - [`loc_vars`](#loc_vars)
    - [`locked_loc_vars`](#locked_loc_vars)
    - [`generate_ui`](#generate_ui-advanced)

***

## Localization Files (recommended)
This method follows the ways of the base game: instead of attaching descriptions directly to each object, all localization strings for the same language are combined into one file. Each such file should be found in the location `localization/<locale>.lua` or `localization/<locale>.json` relative to your mod's root directory. `<locale>` can be the key of any language found in Balatro itself or added through [SMODS.Language](https://github.com/Steamodded/smods/wiki/SMODS.Language).

- `default`: Used as a fallback when no text was found for the selected language.
- `de`: German
- `en-us`: English
- `es_419`: Spanish (Latin America)
- `es_ES`: Spanish (Spain)
- `fr`: French
- `id`: Indonesian
- `it`: Italian
- `ja`: Japanese
- `ko`: Korean
- `nl`: Dutch
- `pl`: Polish
- `pt_BR`: Portuguese
- `ru`: Russian
- `zh_CN`: Chinese (simplified)
- `zh_TW`: Chinese (traditional)

The following is a skeleton for the base structure of a localization file. Entries without content may be omitted. Each found localization string is copied into `G.localization` when the languages are matching.
```lua
return {
    descriptions = {
        Back={},
        Blind={},
        Edition={},
        Enhanced={},
        Joker={},
        Other={},
        Planet={},
        Spectral={},
        Stake={},
        Tag={},
        Tarot={},
        Voucher={},
    },
    misc = {
        achievement_descriptions={},
        achievement_names={},
        blind_states={},
        challenge_names={},
        collabs={},
        dictionary={},
        high_scores={},
        labels={},
        poker_hand_descriptions={},
        poker_hands={},
        quips={},
        ranks={},
        suits_plural={},
        suits_singular={},
        tutorial={},
        v_dictionary={},
        v_text={},
    },
}
```
### Adding your descriptions
A localization file containing a single description may look something like this:
```lua
return {
    descriptions = {
        -- this key should match the set ("object type") of your object,
        -- e.g. Voucher, Tarot, or the key of a modded consumable type
        Joker = {
            -- this should be the full key of your object, including any prefixes
            j_mod_joker = {
                name = 'Name',
                text = {
                    'This is the first line of this description',
                    'This is the second line of this description',
                },
                -- only needed when this object is locked by default
                unlock = {
                    'This is a condition',
                    'for unlocking this card',
                },
            },
            -- multiple line name and multiple description box example
            j_mod_multi_joker = {
                name = {
                    'First line of name',
                    'Second line of name',
                },
                text = {
                    {
                       'First line of box 1',
                       'Second line of box 1',
                    },
                    {
                       'First line of box 2',
                       'Second line of box 2',
                    }
		}
            },
        },
    },
}
```

### Migrating to localization files
If you've been using `loc_txt` and wish to switch to using localization files, disable as many other mods as possible (if you have cross-mod content, you may wish to reconfigure it so it can load even with the other mod disabled), add `"dump_loc": true` to [your mod's metadata](https://github.com/Steamodded/smods/wiki/Mod-Metadata), and launch Balatro once. Steamodded will create a `dump.lua` file in your mod's localization folder, containing all modified localization entries. Remove any extraneous entries (e.g. from other mods you couldn't disable due to being dependencies) and rename this file to `en-us.lua`.

Remember to remove the `dump_loc` entry when finished!

## `loc_txt`
Alternatively, you can define a `loc_txt` table on each object to create its description. This is more limited than localization files because it does not allow creating multiple descriptions for the same object or strings that don't belong to an object at all. The effort of maintaining translations of your mod while using this method is significantly higher. 

You can provide a single table for every language, or provide a subtable for each language. If the currently selected language isn't provided, the `default` subtable, the English (`'en_us'`) subtable, or `loc_txt` itself will be used as defaults, in that order. Refer to your object's documentation for what fields need to go in `loc_txt`.

The following are examples of valid `loc_txt` tables:
-
```lua
{ name = 'Name', text = { 'This is example text' } }
```
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
        name = 'Name',
        text = { 'A moderately long', 'description of', 'your effect.' },
    }
}
```
-
```lua
{
    -- The simplest option: use a single table
    label = 'Label',
    name = 'Name',
    text = { 'A moderately long', 'description of', 'your effect.' },
}
```

## `mod.process.loc_text`
Finally, it is possible to define additional localization strings even when not using localization files. Because the localization sometimes gets reloaded in-game, this can't be done by simply adding the strings to `G.localization` upon loading your mod. Instead, you should define a function on your mod object that puts the strings you need into place. It should look something like this:
```lua
SMODS.current_mod.process_loc_text = function()
    G.localization.misc.labels.mod_mylabel = 'My Label' -- assigning to G.localization directly
    SMODS.process_loc_text(G.localization.misc.labels, 'mod_anotherlabel', { -- Util function to handle multiple languages.
        ['en-us'] = 'English label',
        ['de'] = 'Deutsches Label',
        ['it'] = 'Etichetta italiana',
    })
end
```

# Text Formatting
```lua
{
    name = 'Example name',
    text = {
        'This is {C:attention}coloured{} text',
        '{s:0.8}This is scaled down, {s:1.5}this is scaled up',
        'This text can {V:1}change colours{}!',
        'This is {E:1}floating DynaText',
        'This is {E:2}spaced out DynaText',
        '{X:mult,C:white} X#1# {} Mult',
        '{T:v_telescope}This will display a tooltip when hovered',
    },
}
```

# Localization Functions
To create dynamic descriptions, you need to create functions that define how they behave.
## `loc_vars`
`loc_vars` functions are a simple to use but versatile tool for any type of description.
```lua
SMODS.Consumable {
    -- `self`: The object this function is being called on (the card prototype)
    -- `info_queue`: A table that stores tooltips to be displayed alongside the description
    -- `card`: The card being described. If no card is available because this is for a tooltip,
    -- a fake table that looks like a card will be provided (See: duck typing)
    -- NOTE: card may belong to a different class depending on what object this is defined on;
    -- e.g. a `Tag` is passed if this is defined on a `SMODS.Tag` object.
    loc_vars = function(self, info_queue, card)
        -- Add tooltips by appending to info_queue
        info_queue[#info_queue+1] = G.P_CENTERS.m_stone -- Add a description of the Stone enhancement
        info_queue[#info_queue+1] = G.P_CENTERS.j_stone -- Add a description of Stone Joker
        -- all keys in this return table are optional
        return {
            vars = {
                card.ability.extra.mult, -- replace #1# in the description with this value
                card.ability.extra.mult_gain, -- replace #2# in the description with this value
                colours = {
                    G.C.SECONDARY_SET.Tarot, -- colour text formatted with {V:1}
                    HEX(card.ability.extra.colour_string), -- colour text formatted with {V:2}
                },
            },
            key = self.key..'_alt', -- Use an alternate description key (pulls from G.localization.descriptions[self.set][key])
            set = 'Spectral', -- Use an alternate description set (G.localization.descriptions[set][key or self.key])
            scale = 1.2, -- Change the base text scale of the description
            text_colour = G.C.RED, -- Change the default text colour (when no other colour is being specified)
            background_colour = G.C.BLACK, -- Change the default background colour
            main_start = nil, -- Table of UIElements inserted before the main description (-> "Building a UI")
            main_end = nil, -- Table of UIElements inserted after the main description
        }
    end,
}
```

## `locked_loc_vars`
This function is called for descriptions of locked cards. It behaves identically to regular `loc_vars`.

## `generate_ui` *(advanced)*
The base implementation of this function acts as a wrapper to `loc_vars`. Overriding it allows you to freely define the UI of a card description. Function signature:
```lua
    {
        generate_ui = function(self, info_queue, card, desc_nodes, specific_vars, full_UI_table)
            -- `self`, `info_queue`, `card`: See loc_vars
            -- `desc_nodes`: A table to place UIElements into to be displayed in the current description box
            -- `specific_vars`: Variables passed from outside the current `generate_ui` call. Can be ignored for modded objects
            -- `full_UI_table`: A table representing the main description box. 
            -- Mainly used for checking if this is the main description or a tooltip, or manipulating the main description from tooltips.
            -- This function need not return anything, its effects should be applied by modifying desc_nodes
        end,
    }
```
