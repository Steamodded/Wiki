# Building a UI
UIs are built up of a series of `UIBox` that contain other elements. The basic build up of a UI Element is like so.
```lua
{n = G.UIT.C, 
config = {
	-- config values here, see below
},
nodes = {
	-- further nodes
}}
```
The `n` value defines which type of element you are creating. The following list contains the available options which will be explained in detail later.
`G.UIT.ROOT, G.UIT.R, G.UIT.C, G.UIT.T, G.UIT.O, G.UIT.B`
The `config` table allows you to define certain aspects of your element. There is a list of available options below.
The `nodes` table contains the UI elements that are contained within your element.

## Types of Nodes
	- **ROOT**
	The `ROOT` element is the outer wrapper for your UI Elements.
	- **R**
	A **row** element. Contains other nodes that are arranged horizontally.
	- **C**
	A **column** element. Contains other nodes that are arranged vertically.

	- **T**
	A **text** element. Used to display text on the screen.
		- must contain `text`, `scale` in `config`
	- **O**
	An **object** element. Contains a game object, such as a `Sprite`, a `CardArea` or a `DynaText`.
	- **B**
	A **box** element. Used as a spacer or to draw a coloured box. *Ignores any internal nodes*
		- must contain `h` and `w` in `config`

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

_Image example to be added later_

## Config
There are lots of values you can set in the config of each element. They will help you manipulate your element as required.

**General Config**

- `align` - controls where elements inside are aligned
- *Made up of two letters. The first letter can be `t`, `c`, or `b` and controls the vertical alignment. The second letter can be `l`, `m` or `r` and controls the horizontal alignment.*
- `h`/`w`/`minh`/`maxh`/`minw`/`maxw` - controls the height and width of the element
- `maxh`/`maxw` - set limits on the height and width of elements inside your element
- `padding` - adds spacing inside the edges of your element
- `r` - rounds the corners of your element
- `colour` - set the fill colour of your element
- `no_fill`
- `outline` - set the thickness of the outline of your element
- `outline_colour` - set the colour of the outline of your element
- `emboss` - set the thickness of the emboss at the bottom of your element
- `id` - set the id of your element, used to access your element with `UIBox:get_UIE_by_ID(id, node)`
- `instance_type` - sets the layer your element is drawn on
  - Options include `NODE`, `MOVEABLE`, `UIBOX` *(with no `attention_text`)*, `CARDAREA`, `CARD`, `UI_BOX` *(with `attention_text = true`)*, `ALERT`, `POPUP`. Layered from left to right.
- `shadow` - turn the shadow of your element on or off
- `tooltip` - adds a simple tooltip to your element that is shown on hover `tooltip = {title = "", text = {"", ""}, filler}`
- `detailed_tooltip` - adds a detailed tooltip, like the ones from `info_queue` to your element that is shown on hover
- `juice` - applies the `juice_up` animation to the element when it loads in

- `func` - set a function that is called when your element is being drawn. The function must be stored in `G.FUNCS`
- `button` - set a function that is called when your element is clicked on *(turns your element into a button)* The function must be stored in `G.FUNCS`
- `hover` - defines whether the button has a hover effect or not *(defaults to `false`)*
- `one_press` - defines whether the button can only be pressed one time or not *(defaults to `false`)*
- `can_collide` - defines whether the button can be collided with by the mouse *(defaults to `true`)*

**G.UIT.T config**
- `text` - the text string to display
- `scale` - a scalar value for your text **required**
- `vert` - defines whether the text is displayed vertically or not *(defaults to false)*
- `ref_table` - a table that contains your text
- `ref_value` - the key for the text in the table

**G.UIT.O config**
- `object` - used exclusively in `G.UIT.O` to provide the object to the element
- `role` - used to set the role of the object
  - can be `{role_type = 'Major'}`, `{role_type = 'Minor'}`, `{role_type = 'Glued'}`
  - there are some other options you can define here

`focus_args` - I think these are used for handling controllers

I don't know what these other ones really do or are for*
`mid` - The game sets it as **true** sometimes but I don't know why
`group` - can be referenced by some functions such as `UIBox:remove_group(node, group)`
`res`

### Useful Functions
The game provides some useful helper functions to create different UI elements. They are:
```lua
create_slider(args)
create_toggle(args)
create_option_cycle(args)
create_text_input(args)
UIBox_button(args)
simple_text_container(_loc, args)
create_UIBox_generic_options(args)
```