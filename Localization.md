# Localization
Steamodded offers multiple ways to load strings for in-game descriptions and other labels into the game. This page offers an overview of each option and when you should use them.

## Localization files (recommended)
This method follows the ways of the base game: instead of attaching descriptions directly to each object, all localization strings for the same language are combined into one file. Each such file should be found in the location `localization/locale.lua` relative to your mod's root directory. `locale` can be the key of any language found in Balatro itself or added through [SMODS.Language](https://github.com/Steamopollys/Steamodded/wiki/SMODS.Language).

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

## `loc_txt`
Alternatively, you can define a `loc_txt` table on each object to create its description. This is more limited than the above option because it does not allow creating multiple descriptions for the same object or strings that don't belong to an object at all. The effort of maintaining translations of your mod while using this method is significantly higher. 

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