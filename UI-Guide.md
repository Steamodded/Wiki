# UI Guide

- [Basic Structure](#basic-structure)
  - [Node Types](#node-types)
  - [Node Configuration](#node-configuration)
- [How to Build UI](#how-to-build-ui)
  - [The Basics](#the-basics)
  - [Creating a `UIBox`](#creating-a-uibox)
  - [Interaction](#interaction)
  - [Helper Functions](#helper-functions)
  - [The Details](#the-details)

***

# Basic Structure

The user interface of Balatro most closely resembles the CSS `flexbox` layout, albeit with fewer features.
In Balatro, the basic building block of the UI is `UIElement` (aka. node), which is a table with the following fields:

 - `n`: stands for 'node (type)' and determines how the element will handle its contents
 - `config`: the properties of the node, akin to CSS properties
 - `nodes`: the nodes *inside* this node (aka. children nodes)

A basic example looks like this:

```lua
-- Example node:
{n = G.UIT.C, config = {align = "cm", padding = 0.1}, nodes = {
   {n = G.UIT.T, config = {text = "Hello, world!", colour = G.C.UI.TEXT_LIGHT, scale = 0.5}}
}}
```

Now, these `UIElement` objects would be very finicky to render and update one-by-one.
Therefore, they are packaged into `UIBox` objects.
Each `UIBox` is a complete UI feature like a menu, or a button.
Note that a `UIBox` can have other `UIBox` objects inside it &ndash; a `UIBox` for a menu will usually contain some `UIBox` objects for buttons (among many `UIElement` objects).
Hopefully, all of this will become more clear as this guide continues.

> [!TIP]
> As a metaphor, you can think of `UIElement` as a function, and `UIBox` as a class.<br>
> In reality, both of them are objects, but the structure/hierarchy between them is similar.

## Node Types

The only values that the `n` field can take:

 - `G.UIT.ROOT`: the top-level node of *every* `UIBox`; there's exactly one of these per `UIBox`.
 - `G.UIT.R`: a **Row** node, which arranges its child nodes *horizontally*.
 - `G.UIT.C`: a **Column** node, which arranges its child nodes *vertically*.
 - `G.UIT.T`: a **Text** node, which displays text.<br>
   This node must contain `text`, `colour`, and `scale` in its `config`.
 - `G.UIT.O`: an **Object** node, which displays a special game object.<br>
   Game objects include `Sprite`, `Card`, `CardArea`, `DynaText` (ie. dynamic text), and more.
 - `G.UIT.B`: a **Box** node, which is used as a spacer; it *ignores any child nodes*.
   This node must contain `h` and `w` in its `config`.
 - `G.UIT.S`: a **Slider** node, which contains a slider input.<br>
   You should probably use `create_slider(..)` instead.
 - `G.UIT.I`: a text **Input** node, which contains text input.

*Example*
The following code uses a combination of columns and rows to build up the basic structure of the UI. It can then have other elements added to add content.
```lua
{n = G.UIT.ROOT, config = {r = 0.1, minw = 8, minh = 6, align = "tm", padding = 0.2, colour = G.C.BLACK}, nodes = {
	{n = G.UIT.C, config = {minw=4, minh=4, colour = G.C.MONEY, padding = 0.15}, nodes = {
		{n = G.UIT.R, config = {minw=2, minh=2, colour = G.C.RED, padding = 0.15}, nodes = {
			{n = G.UIT.C, config = {minw=1, minh=1, colour = G.C.BLUE, padding = 0.15}},
			{n = G.UIT.C, config = {minw=1, minh=1, colour = G.C.BLUE, padding = 0.15}}
		}},
		
		{n = G.UIT.R, config = {minw=2, minh=1, colour = G.C.RED, padding = 0.15}, nodes = {
			{n = G.UIT.C, config = {minw=1, minh=1, colour = G.C.BLUE, padding = 0.15}},
			{n = G.UIT.C, config = {minw=1, minh=1, colour = G.C.BLUE, padding = 0.15}}
		}}
	}}
}}
```

![UI Example](https://i.imgur.com/0HMQObb.png)

## Node Configuration

The `config` field expects a table of configuration entries.
There are *a lot* of different keys that the game recognises in different contexts, but there are only a few that you need to know in order to build working UIs:

 - `align`: where the child nodes are placed within the current node; it always consists of *exactly two letters*:<br>
   the first letter is for *vertical* alignment: either `t` for Top, `c` for Center, or `b` for Bottom;<br>
   the second letter is for *horizontal* alignment: either `l` for Left, `m` for Middle, or `r` for Right.
 - `h`, `minh`, `maxh`: the Height of this node (either fixed, minimum, or maximum)
 - `w`, `minw`, `maxw`: the Width of this node (either fixed, minimum, or maximum)
 - `padding`: the extra space inside the edges of the current node.<br>
   Standard values are `0.05` or `0.1`.
 - `r`: the Roundness of corners of the current node.<br>
   Standard value is `0.1`.
 - `colour`: the fill colour of the current node.<br>
   Standard values are stored in the `G.C` table; fully custom values can be used with `HEX("00000000")` (taking RGBA values).<br>
   The British spelling is important!
 - `no_fill`: set to `true` for no fill.
 - `outline`: the thickness of the outline of the current node.<br>
   Standard value is `???`.
 - `outline_colour`: the colour of the outline of the current node.<br>
   See `colour` for possible values, above.
 - `emboss`: how much the current node is *raised* out of its parent node.<br>
   Standard value is `0.05`.
 - `hover`: set to `true` to render the current node as hovering *above* its parent node.
 - `shadow`: set to `true` to render the shadow of the current node; only shows-up under hovering nodes.
 - `juice`: set to `true` to apply the `juice_up` animation to the current node once it loads in.

Some advanced configuration keys include:

 - `id`: set a custom ID to the current node.<br>
   This will allow you to find this specific node via `[UIBOX]:get_UIE_by_ID([ID])`;
   note that you must already know some `UIBox` element that *contains* this node.<br>
   This is only useful in very specific cases, and for simple UIs you should not need to use this.
 - `instance_type`: set the layer that the current node is drawn on, either:<br>
   `NODE`, `MOVEABLE`, `UIBOX` (w/o `attention_text`), `CARDAREA`, `CARD`, `UI_BOX` (w/ `attention_text`), `ALERT`, or `POPUP`<br>
   These are ordered from lowest to highest layer.
 - `ref_table`: a table containing some data that is relevant to the current node.<br>
   This is used to pass data to UI nodes or between UI-related functions.
 - `ref_value`: a string corresponding to a key in the current node's `ref_table`.<br>
   This is always used in conjunction with `ref_table` to access the relevant value by key.
 - `func`: set a function that will be called when the current node is being drawn.<br>
   Its value is a string of the function name; the function itself must be stored in `G.FUNCS`.
 - `button`: set a function that will be called when the current node is clicked on.<br>
   Its value is a string of the function name; the function itself must be stored in `G.FUNCS`.
 - `tooltip`: add a tooltip when the current node is hovered over by a mouse/controller.<br>
   Its value is a table: `{title = "", text = {"Line1", "Line2"}}`.
 - `detailed_tooltip`: similar to tooltip above
 
> [!TIP]
> The **`ref_table`** and **`ref_value`** fields are extremely custom.
> Therefore, whenever you encounter them, you must manually trace what data they access and how it is used.

Configuration options for Text nodes (ie. `G.UIT.T`):

 - `text`: set the string to display.<br>
   Alternatively, you can set text via the `ref_table` and `ref_value` combination; for example:<br>
   `{n=G.UIT.T, config={ref_table = G.GAME.current_round, ref_value = "reroll_cost", scale = 0.75, colour = G.C.WHITE}`
 - `scale`: set a multiplier to text size.
 - `colour`: set the text colour.<br>
   Standard values are `G.C.UI.TEXT_LIGHT`, `G.C.UI.TEXT_DARK`, and `G.C.UI.TEXT_INACTIVE`,<br>
   but all values applicable to `colour` can also go here (see above).
 - `vert`: set to `true` to draw the text vertically (ie. sideways).
 
 > [!TIP]
 > If you want to change the text contents of a `G.UIT.T` interactively, use arguments `ref_table` and `ref_value` instead of `text`. Its text will be updated whenever `ref_table[ref_value]` changes.
 > If you want animated text, use `G.UIT.O` with `DynaText`.
 
Configuration optoins for Object nodes (ie. `G.UIT.O`):

 - `object`: set the object to render.<br>
   This is a literal game object, like `CardArea`.
 - `role`: set the relationship of the object to the UI.<br>
   Its value is a table containing at least: `{role_type = [TYPE]}` where type is either `"Major"`, `"Minor"`, or `"Glued"`.<br>
   You probably don't need to use this.

# How to Build UI

At this point, you should have a general idea about the structure of Balatro's UI.
Here are a few tips to actually making changes to it.

## The Basics

The most important thing to understand is the parent-child relationship between nodes.
A parent Row/Column node will arrange *all of its direct children* in Rows/Columns.
The children will be equally distributed (unless any specific width/height configuration is specified).

```lua
{n=G.UIT.C, config={align = "cm"}, nodes={      -- 0
  {n=G.UIT.R, config={align = "cr"}, nodes={}}, -- 1
  {n=G.UIT.R, config={align = "cm"}, nodes={}}, -- 2
  {n=G.UIT.R, config={align = "cl"}, nodes={}}  -- 3
}}

-- Result:
--   ------------
--   |        1 |
--   ------------
--   |     2    |
--   ------------
--   | 3        |
--   ------------
-- The WHOLE box containing 1,2,3 is Element 0
-- The contents of Elements 1,2,3 will go inside their respective small boxes.
-- The contents of Elements 1/3 will be right/left aligned, due to configuration.
```

```lua
{n=G.UIT.R, config={align = "cm"}, nodes={    -- 0
  {n=G.UIT.C, config={align = "cm"}, nodes={}}, -- 1
  {n=G.UIT.C, config={align = "cm"}, nodes={    -- 2
    {n=G.UIT.R, config={align = "cm"}, nodes={}}, -- 3
    {n=G.UIT.R, config={align = "cm"}, nodes={}}  -- 4
  }}
}}

-- Result:
--   -------------
--   |     |  3  |
--   |  1  |-----|
--   |     |  4  |
--   -------------
-- The WHOLE box is Element 0
-- The row containing 3,4 is Element 2
```

The biggest tip with regards to making a UI is to always **alternate Row nodes and Column nodes for each UI 'level'**.
The way that the UI is drawn, similar to CSS `flexbox`, stretches each UI element either in the Row direction or the Column direction.
Therefore, to make everything center-aligned, you need to stretch UI elements in both directions.

```lua
-- Always alternate Row and Column nodes between UI 'levels' (to keep center alignment):
{n=G.UIT.C, config={}, nodes={
  {n=G.UIT.R, config={}, nodes={
    {n=G.UIT.C, config={}, nodes={...}},
    {n=G.UIT.C, config={}, nodes={...}}
  }},
  {n=G.UIT.R, config={}, nodes={...}},
  {n=G.UIT.R, config={}, nodes={
    {n=G.UIT.C, config={}, nodes={
      {n=G.UIT.R, config={}, nodes={...}},
      {n=G.UIT.R, config={}, nodes={...}},
    }}
  }}
}}
```

## Creating a `UIBox`

A `UIBox` is a very useful tool if you need to create **interactive UIs**,
because a `UIBox` can be updated by deleting it and creating a new `UIBox` with updated values.
This is how Balatro's menus are updated.

It is created via a constructor and then used as a UI Object:

```lua
-- A simple UIBox being created:
local my_menu = UIBox({
   definition = my_menu_function(...),
   config = {type = "cm", ...}
})

-- A UIBox must be placed in an Object node!
local my_menu_node = {n=G.UIT.O, config={object = my_menu}}
```

The vital part of creating a `UIBox` is providing a **definition function**.
This function must simply **return a Root node** (ie. `G.UIT.ROOT`),
although it will most likely contain at least a few child nodes that hold some content.

```lua
function my_menu_function(menu_name)
   return {n=G.UIT.ROOT, config={align = "cm"}, nodes={
      -- Use a Row node to arrange the contents in rows:
      {n=G.UIT.R, config={align = "cm"}, nodes={
         -- Use a wrapper Column node to hold the menu name:
         {n=G.UIT.C, config={align = "cm"}, nodes={
            {n=G.UIT.T, config={text = menu_name, colour = G.C.UI.TEXT_LIGHT, scale = 0.5}}
         }},
         -- Use a wrapper Column node to hold the first menu row:
         {n=G.UIT.C, config={align = "cm"}, nodes={
            -- Menu Row 1 contents...
         }},
         -- Use a wrapper Column node to hold the second menu row:
         {n=G.UIT.C, config={align = "cm"}, nodes={
            -- Menu Row 2 contents...
         }},
         -- Etc...
      }}
   }}
end
```

## Interaction

The last vital component of Balatro's UI is interaction, and it is governed by buttons.
Consider the following button element:

```lua
{n=G.UIT.C, config={button = "my_button", my_data={1, 2, 3}}, nodes={
  {n=G.UIT.T, config={text = "Press Me!", ...}}
}}
```

Once this button is pressed, the game will call `G.FUNCS.my_button(e)`, where `e` is the whole button UI Element. That means you can access `e.config.my_data`, `e.nodes`, etc.

As a last example, here is one possible pattern to update the contents of a `UIBox`:

```lua
function G.FUNCS.my_update_menu(e)
  -- Get the menu UIBox object:
  local my_menu_uibox = e.config.my_data.menu_uibox
  -- Get the parent of the menu UIBox, because we want to delete and re-create the menu:
  local menu_wrap = my_menu_uibox.parent
  
  -- Delete the current menu UIBox:
  menu_wrap.config.object:remove()
  -- Create the new menu UIBox:
  menu_wrap.config.object = UIBox({
    definition = my_menu_function(e.config.my_data),
    config = {parent = menu_wrap, type = "cm"} -- You MUST specify parent!
  })
  -- Update the UI:
  menu_wrap.UIBox:recalculate()
end
```

## Helper Functions

The game's UI elements should ideally be consistent, which is why there are a few helper functions that
create and/or organise `UIBox` elements from templates.
   
```lua
UIBox_button(args)
create_toggle(args)
create_slider(args)
create_text_input(args)
simple_text_container(_loc, args)
create_UIBox_generic_options(args)
create_option_cycle(args)
```

These are not exhaustive, and you will have to figure out exactly how to use them by yourself.
This is meant to be an introductory guide, not Balatro's UI API documentation.

## The Details

The last couple sections may already seem quite complex.
It took hours of exploring the game's UI and experimenting with custom UIs to truly understand the dynamics of it all.
Unfortunately, there are a lot of different functions, tables, keys, and values that are used sporadically,
so the best anyone can do is to try different things and find patterns.

> [!IMPORTANT]
> In reality, the best way to learn Balatro's UI is to **copy its existing UI elements**.
> Everything you could ever need to design/change already exists in the game &ndash; you just need to find where it is defined and then explore how/why it works.

Once again, two good places to get a feel for building UI are [Divvy's Preview](https://github.com/DivvyCr/Balatro-Preview/blob/main/src/Interface.lua) and [Divvy's History](https://github.com/DivvyCr/Balatro-History/tree/main/src/UI) mods.

***
*Guide written by DivvyC, original notes by Eremel*
