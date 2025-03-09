# API Documentation: `SMODS.Tab`
## `SMODS.Tab`
This class offers a standardized way of extending tab-based info dialogs such as `Run Info` or `Deck Info`, as well as the ability to quickly set up new tab-based dialogs.
- **Required parameters:**
    - `key`
    - `tab_group`: The name of the group to add the tab to. Tabs in the same tab group will be displayed on the same UIBox.
    - `order`: Sets the order. `Tab` objects in a group are displayed left to right from lowest to highest order.
    - `func(self)`: Handles generating the contents of the `Tab`. Must return a UI table starting from a G.UIT.ROOT element.
- **Optional parameters** *(defaults)*:
    - `chosen = false`: Whether the tab is the one initially selected in the tab group. The leftmost (lowest order) tab with chosen set to true is the default tab.
    - `is_visible(self, args)`:  If undefined or nil, the tab is always visible. Otherwise must be a function that returns true if the tab should be visible. Args are the table of arguments passed to the tab group function.
    - `prefix_config, dependencies` [(reference)](https://github.com/Steamodded/smods/wiki/API-Documentation#common-parameters)

## Creating a new tab-based dialog

A new dialog box similar to Run Info can be created from all injected `Tab` objects of the same `tab_group` with this helper function:

`SMODS.generate_tabs_uibox(tab_group, args)`
- `tab_group`: The name of the tab_group to render.
- `args`: A table of contextual arguments to pass to the `is_visible` function of each `Tab`.

This function returns UIBox table, which can then be rendered as an overlay menu:

```
G.FUNCS.overlay_menu{definition = SMODS.generate_tabs_uibox(tab_group, args)}
```
