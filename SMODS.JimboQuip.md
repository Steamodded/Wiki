# API Documentation: `SMODS.JimboQuip`
JimboQuips allow you to create new pop ups at the end of a run.

- **Required parameters:**
	- `key`,
    - `loc_txt` or localization entry [(reference)](https://github.com/Steamodded/smods/wiki/Localization)
        - For use with localization file, the text should be set as `G.localization.misc.quips[key:lower()]`.
		- `loc_txt` should only contain the text, without key-indexing.
- **Optional parameters** *(defaults)*:
    - `prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)
    - `type`: Whether it's `'win'` or `'loss'` quip. It can be other strings for modded types.
    - `extra`: Table of parameters to customize the key, it can also be a function that returns the appropriate table.
    ```lua
    extra = {
        center = 'j_hanging_chad', -- key of card to show
        particle_colours = { -- table of up to 3 colours for particles
            G.C.GREEN,
            G.C.PURPLE,
            G.C.GOLD
        },
        materialize_colours = { -- table of up to 3 colours for materialize effect
            G.C.GREEN,
            G.C.PURPLE,
            G.C.GOLD
        },
        text_key = 'modprefix_example_quip_newkey', -- key override for the quip
        times = 5, -- number of times to play sounds
        pitch = 1, -- pitch of sounds
        sound = 'voice1', -- string of sound to play, this can also be a table of strings to play simultaneously,
        juice = {0.3, 0.7}, -- table of args to pass into card:juice_up
        delay = 0.13, -- amount to delay the next loop of sounds
    }
    ```

## API methods
- `filter(self, type) -> boolean, table`
    - Allows configuring if the quip is allowed to appear. You can also optionally return a table of extra information. `weight` allows you to control the frequency of your quip being the displayed quip *(default value is 1)*, and `override_base_checks` can be used to stop other quip filters from removing your quip *(more on this later)*.
    - Example:
    ```lua
    filter = function(self, type)
        if next(SMODS.find_card('j_hanging_chad')) then
            return true, {weight = 10}
        end
    end
    ```
- `play_sounds(self, times)`
    - Allows more precise control over the sounds played. This will override any `sounds` defined in the `extra` table.

## Example
Here is an example of one quip object appearing in different situations with different messages.

```lua
SMODS.JimboQuip({
    key = 'black_cat_1',
    extra = {
        center = 'j_ortalab_black_cat',
        particle_colours = {
            G.ARGS.LOC_COLOURS.Ortalab,
            darken(G.ARGS.LOC_COLOURS.Ortalab, 0.5),
            lighten(G.ARGS.LOC_COLOURS.Ortalab, 0.5)
        }
    },
    filter = function(self, type)
        if next(SMODS.find_card('j_ortalab_black_cat')) then
            if type == 'win' then
                self.extra.text_key = self.key..'_win'
                return true, { weight = 10 }
            elseif type == 'loss' then
                self.extra.text_key = self.key..'_loss'
                return true, { weight = 10 }
            end
        end
    end
})
```