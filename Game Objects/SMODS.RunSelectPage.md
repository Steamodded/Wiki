# `SMODS.RunSelectPage`
*(Added in 26.829)*

Run Select is an integration of the mod Galdur within SMODS itself. This allows for easier customisation of runs before they begin, letting users choose different things that will affect the run. Deck and Stake choice are added by default, but more pages can be added easily.

- **Required parameters:**
    - `key`: The key used to identify your page

- **Optional parameters** *(defaults)*:
    - `page`: Choose a position for your page to appear (1 = before deck, 2 = between deck and stake). Pages automatically get placed after stake selection.
    - `include_deck_preview`: Set to true to automatically include the currently selected deck preview element
    - `include_stake_tower`: Set to true to automatically include the currently selected stake preview element
    - `automatic_preview`: Set to true to automatically add a preview element for your selection
    - `selection_limit`: Set to the number of selections you can make, *(defaults to 1)*
    - `preview_size`: Set to control the number of copies of each choice that are added to the automatic preview, *(defaults to 1 or `stack_size` if defined)*
    - `random_select`: Set to true to automatically include a random button
    - `grid_size`: Set as a table, `{number_of_rows, number_of_columns}`, of dimensions for the automatic selection element, *(defaults to `{2,5}`)*
    - `sprite_size`: Set as a table, `{w = number, h = number}`, to change the size of the cards in the automatic selection element, *(defaults to `{w = G.CARD_W, h = G.CARD_H}`)*
    - `stack_size`: Set to control the number of copies of each selection object that are added to the automatic selection element, *(defaults to 1)*
    - `area_type`: Set as a `CardArea` type to change the type of the `CardAreas` within the automatic selection and preview elements
    - `silent`: Set to true to remove animations from your page
    - `type`: Set to the set of the object to automatically control the selection text

## API methods
- `generate_pool(self) -> table`
	- To determine the pool of objects used in the selection UI. Returns a table of objects
- `set_default(self, choice) -> string`
	- Control what the page has selected when it is first encountered in a session (defaults to last choice)
- `selected_text(self, selection) -> string`
	- Control the text that is displayed in the automatic preview UI
- `quick_start_text() -> string`
	- Control the text that is displayed in the quick start tooltip
	- Use `G.PROFILES[G.SETTINGS.profile].last_choices.modprefix_key` to access the last choice
- `start_run(self, choice)`
	- Execute code after the run is started
- `can_continue(self) -> boolean`
	- Determine whether the user can progress to the next page or not
	- Return `true` to allow progress
- `optional(self) -> boolean`
	- Determine whether the page should be able to be progressed to
	- Return `true` to display the page
- `create_selection_card(self, key, index, area) -> Card`
	- Control how the cards in the selection and preview UIs are created
	- Useful for modifying cards to add extra things to them
- `choose_random(self)`
	- Modify the behaviour of the random button
- `handle_choice(self, choice, remove)`
	- Modify the behaviour of clicking on selections
- `settings(self) -> table`
	- Return a table of UI nodes to be automatically added to the page
	- Useful for adding toggles and sliders
- `definition(self) -> UIElement`
	- Return a custom UI to be used on the page

## Localization
- Random select button: `run_select_MODPREFIX_PAGEKEY_random`
- Next page button: `run_select_MODPREFIX_PAGEKEY`

## Example
Here is an example of a Run Select Page that allows the player to select a Rare Joker to acquire at the beginning of the run if you are playing on Red Deck.

```lua
local mod_prefix = 'eremel_testing' -- Replace with your own prefix
SMODS.RunSelectPage({
    key = 'joker_choice',
    grid_size = {2, 4}, -- Custom grid size
    automatic_preview = true,
    type = 'Joker',
    generate_pool = function(self)
        local pool = {}
        for _, v in ipairs(G.P_CENTER_POOLS.Joker) do
            if v.rarity == 3 then table.insert(pool, v) end
        end
        return pool
    end,
    optional = function(self) -- Only appear if Red Deck is selected
        return SMODS.RunSelect.Setup.choices.deck_choice == 'b_red'
    end,
    quick_start_text = function()
        if not G.PROFILES[G.SETTINGS.profile].last_choices[mod_prefix..'_joker_choice'] then return end -- If no Joker was selected last time, don't add to the tooltip
        return localize({type = 'name_text', set = 'Joker', key = G.PROFILES[G.SETTINGS.profile].last_choices[mod_prefix..'_joker_choice']})
    end,
    start_run = function(self, choice) -- Add the Joker on run start
        G.E_MANAGER:add_event(Event({
            trigger = 'after', delay = 0.7,
            func = function()
                local c = SMODS.add_card({key = choice, skip_materialize = true})
                c:start_materialize()
                return true
            end
        }))
    end,
    set_default = function(self, choice) -- Make sure that the default selection is empty
        return nil
    end,
})
```