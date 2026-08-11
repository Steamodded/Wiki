# Text Styling

Balatro includes a very basic formatting syntax for styling and formatting displayed text in-game. Where supported, text can be styled with the use of *style modifier codes* included within the text string. For example, the text string:

<table>
 <tr> </tr> <!-- Empty row to manipulate the background colour of the next table row -->
 <tr>
  <td>

   ```pas
   {C:blue}+1{} hand
   ```

  </td>
  <td>

  produces
  <br>
  </td>
  <td>
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_+1_hand_dark.svg">
    <img  height=32 width=128 alt="+1 hand" src="/_static/Assets/Text-Styling/example_+1_hand_light.svg">
   </picture>
   <br>
  </td>
 </tr>
</table>

Most SMODS objects that display description text will parse and style text strings automatically when loading from [localization files](https://docs.smods.dev/API%20Documentation/Localization#localization-files-recommended) or [`loc_txt`](https://docs.smods.dev/API%20Documentation/Localization#loc_txt). This includes the text strings of descriptions for Achievements, Consumables, Decks, Jokers, Vouchers, and more.

Style modifiers are not additive - text will only be styled by the modifiers contained within the previous set of curly braces. Using empty braces `{}` will reset text styling for text after it.

Additionally, multiple modifiers can be [combined](#combinations) in a single set of curly braces. For example, the text string:

<table>
 <tr> </tr> <!-- Empty row to manipulate the background colour of the next table row -->
 <tr>
  <td>

   ```pas
   {X:mult,C:white}X0.5{}
   ```

  </td>
  <td>

  produces
  <br>
  </td>
  <td>
   <img src="/_static/Assets/Text-Styling/example_X0.5.svg" height=32 width=128 alt="X0.5">
   <br>
  </td>
 </tr>
</table>

Valid style modifiers are as follows:
<table>
 <tr>
  <td>
   <a href="#text-colour-modifiers-cv"><b>Text colour</a>
  </td>
  <td>
   <code>{C:<i>colour</i>}</code>/<code>{V:<i>colour</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#background-colour-modifiers-xb"><b>Background colour</a>
  </td>
  <td>
   <code>{X:<i>colour</i>}</code>/<code>{B:<i>colour</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#text-motion-modifier-e"><b>Text motion</a>
  </td>
  <td>
   <code>{E:<i>motion-index</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#text-hover-tooltip-modifier-t"><b>Text hover tooltip</a>
  </td>
  <td>
   <code>{T:<i>tooltip-key</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#text-scale-modifier-s"><b>Text scale</a>
  </td>
  <td>
   <code>{s:<i>scale</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#text-underline-strikethrough-and-overline-modifiers-ustov"><b>Text underline</a>
  </td>
  <td>
   <code>{u:<i>colour</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#text-underline-strikethrough-and-overline-modifiers-ustov"><b>Text strikethrough</a>
  </td>
  <td>
   <code>{st:<i>colour</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#text-underline-strikethrough-and-overline-modifiers-ustov"><b>Text overline</a>
  </td>
  <td>
   <code>{ov:<i>colour</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#text-outline-modifier-o"><b>Text overline</a>
  </td>
  <td>
   <code>{O:<i>colour</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#text-font-modifier-f"><b>Font</a>
  </td>
  <td>
   <code>{f:<i>font</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#text-button-modifier-button"><b>Button</a>
  </td>
  <td>
   <code>{button:<i>function-key</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <a href="#ui-element-insertion-element"><b>UI Element</a>
  </td>
  <td>
   <code>{element:<i>element-index</i>}</code>
  </td>
 </tr>
 <tr>
  <td>
   <b>No modifiers</b> (use default styling)
  </td>
  <td>
   <code>{}</code>
  </td>
 </tr>
</table>

> [!IMPORTANT]
> Modifiers are **case sensitive** - make sure to refer to this list for the appropriate capitalization.

---

## Text colour modifiers `{C:}`/`{V:}`

<code>{C:<i>colour</i>}</code> or <code>{V:<i>colour</i>}</code> changes the color of the text, where *`colour`* is one of the following:

- the **key** of a colour defined in [`G.ARGS.LOC_COLOURS`](#loc_colours-table),

- a 6-digit **RGB hex code** or an 8-digit **RGBA hex code**, or

- the index of a custom colour provided as an entry in the [`loc_vars`](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) `vars.colours` table. See [Localization](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) for more details.

> [!NOTE]
> This functionality was added by Steamodded in (RELEASE). In older versions and in vanilla Balatro, `{C:}` only supports the first option, and `{V:}` only supports the third option.

### Examples

<!--- Single-indented table is necessary for code blocks to function properly -->
<table>
 <tr>
  <td> Text string </td> <td> <code>loc_vars</code> </td> <td> Result </td>
 </tr>
 <tr>
  <td colspan=2>
<!-- Code blocks require a preceding empty line when inside HTML tables -->

   ```pas
   {C:mult}+4{} Mult
   ```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_+4_Mult_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_+4_Mult_light.svg" height=32 width=128 alt="+4 Mult">
   </picture>
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td colspan=2>

```pas
{C:attention}1{} free {V:green}Reroll{}
```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_1_free_Reroll_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_1_free_Reroll_light.svg" height=32 width=128 alt="1 free Reroll">
   </picture>
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td>

   ```pas
   {C:green}#1# іn #2#{} chance
   ```

  </td>
  <td>

   ```lua
   vars = {
     G.GAME.probabilities.normal, -- 1
     card.ability.extra.odds      -- 6
   }
   ```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_1_in_6_chance_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_1_in_6_chance_light.svg" height=32 width=128 alt="1 in 6 chance">
   </picture>
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td colspan=2>

   ```pas
   {C:ff00ff}FF00FF{}
   ```

  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_FF00FF.svg" height=32 width=128 alt="FF00FF">
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td>

   ```pas
   {V:2}#2#{} suit{}
   ```

  </td>
  <td>

   ```lua
   vars = {
     'Spade',
     'Heart',
     'Club',
     'Diamond',
     colours = {
       G.C.SUITS.Spades,
       G.C.SUITS.Hearts,
       G.C.SUITS.Clubs,
       G.C.SUITS.Diamonds
     }
   }
   ```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_Heart_suit_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_Heart_suit_light.svg" height=32 width=128 alt="Heart suit">
   </picture>
  </td>
 </tr>
</table>

## Background colour modifiers `{X:}`/`{B:}`

<code>{X:<i>colour</i>}</code> or <code>{B:<i>colour</i>}</code> sets the background color of the text, where *`colour`* is one of the following:

- the **key** of a colour defined in [`G.ARGS.LOC_COLOURS`](#loc_colours-table),

- a 6-digit **RGB hex code** or an 8-digit **RGBA hex code**, or

- the index of a custom colour provided as an entry in the [`loc_vars`](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) `vars.colours` table. See [Localization](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) for more details.

> [!NOTE]
> This functionality was added by Steamodded in (RELEASE). In older versions and in vanilla Balatro, `{X:}` only supports the first option. `{B:}` is not supported by vanilla Balatro; in older Steamodded versions, it only supports the third option.

These modifiers are usually combined with a text colour modifier to make <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_X3_Mult_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_X3_Mult_light.svg" height=24 width=128 alt="X3 Mult" align="center">
</picture> labels.

The `{X:}` modifier uniquely strips all whitespace from the styled text, so text like <code>{X:gold}&nbsp;W&nbsp;I&nbsp;D&nbsp;E&nbsp;{}</code> is rendered as <img src="/_static/Assets/Text-Styling/example_WIDE.svg" height=24 width=128 alt="WIDE" align="center">. This can be helpful for improving the readability of otherwise dense strings. The `{B:}` modifier instead leaves the styled text's whitespace unmodified.

### Examples

<table>
 <tr>
  <td> Text string </td> <td> <code>loc_vars</code> </td> <td> Result </td>
 </tr>
 <tr>
  <td colspan=2>

   ```pas
   {B:mult,C:white}X3{} Mult{}
   ```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_X3_Mult_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_X3_Mult_light.svg" height=32 width=128 alt="X3 Mult">
   </picture>
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td colspan=2>

   ```pas
   {X:chips,C:white} X 1 . 5 {} Chips{}
   ```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_X1.5_Chips_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_X1.5_Chips_light.svg" height=32 width=128 alt="X1.5 Chips">
   </picture>
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td>

   ```pas
   {X:mult,C:white} X#1# {}
   ```

  </td>
  <td>

  ```lua
  vars = {
    card.ability.extra.xmult -- 0.5
  }
  ```

  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_X0.5.svg" height=32 width=128 alt="X0.5">
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td colspan=2>

   ```pas
   {B:00ff00}00FF00{}
   ```

  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_00FF00.svg" height=32 width=128 alt="00FF00">
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td>

   ```pas
   {B:1,V:2}Oh no!{} Anyway...
   ```

  </td>
  <td>

   ```lua
   vars = {
     colours = {
       {1, 0, 0, 1}, --#FF0000
       {0, 0, 0, 1}  --#000000
     }
   }
   ```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_Oh_no_Anyway_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_Oh_no_Anyway_light.svg" height=32 width=128 alt="Oh no! Anyway...">
   </picture>
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td>

   ```pas
   {B:1,V:2}#1#{B:2,C:1}#2#{}
   ```

  </td>
  <td>

   ```lua
   vars = {
     'Spa',
     'rts',
     colours = {
       G.C.SUITS.Spades,
       G.C.SUITS.Hearts,
     }
   }
   ```

  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_Spa-rts.svg" height=32 width=128 alt="Sparts">
  </td>
 </tr>
</table>


## Text motion modifier `{E:}`

`{E:1}` applies a pop-in effect when the text is first displayed, and a floating animation to each letter in the text.

`{E:2}` applies a bumping animation to each letter in sequence.

`{E:}` is fully compatible with background modifiers `{X:}` and `{B:}` *(Added by Steamodded)*. In vanilla Balatro, if background modifiers are set, `{E:1}` will only show a pop-in effect with no motion, and `{E:2}` will be ignored.

You can also apply a custom effect using [SMODS.DynaTextEffect](https://docs.smods.dev/Game%20Objects/SMODS.DynaTextEffect), in that case the modifier should be `{E:modprefix_key}`.

### Examples

<table>
 <tr>
  <td> Text string </td> <td> Result </td>
 </tr>
 <tr>
  <td>

   ```pas
   {C:green,E:1}probabilities{}
   ```

  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_probabilities.svg" height=32 width=128 alt="probabilities">
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td>

   ```pas
   {E:2}Joker{}
   ```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_Joker_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_Joker_light.svg" height=32 width=128 alt="Joker">
   </picture>
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td>

   ```pas
   {C:red,E:2}self destructs{}
   ```

  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_self_destructs.svg" height=32 width=128 alt="self destructs">
  </td>
 </tr>
</table>

## Text hover tooltip modifier `{T:}`

<code>{T:<i>tooltip-key</i>}</code> adds tooltip functionality to the text, which displays a small tooltip UI above the text when the text is hovered over. If `tooltip-key` can be the name of a key found in either `G.P_CENTERS` or `G.P_TAGS` or a description found in `G.localization.descriptions.Other` *(Added in 1814a)*. In the latter case, you can supply additional information as follows: <code>{T:[key=<i>tooltip-key</i>;set=<i>set-key</i>;1=<i>var1</i>;2=<i>var2</i>;...]}</code> *(Added in (RELEASE))*. The *set-key* is used to specify a set in `G.localization.descriptions` to pull from, and the variables *var1*, *var2*, etc. are used to supply any localization variables in the text.

> [!NOTE]
> The same effect can be achieved using <code>{T:<i>tooltip-key</i>,T_set:<i>set-key</i>,T_vars=<i>var1</i>;<i>var2</i>;...}</code> *(added in 1814a)*.

### Examples

<table>
 <tr>
  <td> Text string </td> <td> Result </td>
 </tr>
 <tr>
  <td>
   <br><br>

   ```pas
   {C:tarot,T:v_crystal_ball}Crystal Ball{}
   ```

  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_Crystal_Ball_animated.svg" height=15 width=1280 alt="Crystal Ball with Tooltip Animation">
  </td>
 </tr>
 <tr>
  <td>
   <br><br>

   ```pas
   "Shop can have {C:perishable,T:[key=perishable;1=5;2=5]}Perishable{} Jokers"
   ```

  </td>
  <td>
   TBD
  </td>
 </tr>
 <tr>
  <td>
   <br><br>

   ```pas
   "{T:[key=bl_arm;set=Blind]}The Arm{}"
   ```

  </td>
  <td>
   TBD
  </td>
 </tr>
</table>

## Text scale modifier `{s:}`
>
> [!IMPORTANT]
> This modifier requires the **lowercase** `s`, unlike other modifiers which must be UPPERCASE.

<code>{s:<i>scale</i>}</code> changes the size of the text.

*`scale`* is a decimal value where the default size is 1.0.

Vanilla Balatro only uses `s:0.8`, `s:0.85` and `s:1.1` text scales.

### Examples

<table>
 <tr>
  <td> Text string </td> <td> Result </td>
 </tr>
 <tr>
  <td>

  ```pas
  {s:0.8}0.8 {s:1.0}1.0 {s:1.1}1.1{}
  ```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_0.8_1.0_1.1_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_0.8_1.0_1.1_light.svg" height=35 width=128.2 alt="0.8 1.0 1.1">
   </picture>
  </td>
 </tr>
</table>

## Text underline, strikethrough and overline modifiers `{u:}`/`{st:}`/`{ov:}`
>
> [!NOTE]
> These modifiers are added by Steamodded and are not supported by vanilla Balatro.
> *(Added in (RELEASE))*

> [!IMPORTANT]
> These modifiers must be **lowercase**, unlike other modifiers which must be UPPERCASE.

### Basic usage

<code>{u:<i>colour</i>}</code>, <code>{st:<i>colour</i>}</code> and <code>{ov:<i>colour</i>}</code> respectively add an underline, strikethrough, or underline to the text. The width of the line is 10% of the text's height.

*`colour`* sets the colour of the line, where *`colour`* is one of the following:
- the **key** of a colour defined in [`G.ARGS.LOC_COLOURS`](#loc_colours-table),

- a 6-digit **RGB hex code** or an 8-digit **RGBA hex code**, or

- the index of a custom colour provided as an entry in the [`loc_vars`](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) `vars.colours` table. See [Localization](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) for more details.

### Advanced usage

By supplying a table to the text modifier, it is possible to customize the lines further: <code>{u:[c=<i>colour</i>;s=<i>size</i>]}</code>. *size* is a decimal value with a default of `0.1`. It indicates the thickness of the line relative to the height of the text. It is **required** to specify a *colour*.

### Examples

<table>
 <tr>
  <td> Text string </td> <td> Result </td>
 </tr>
 <tr>
  <td>

  ```pas
  {u:red}Underlined text!
  ```

  </td>
  <td align="center">
   TBD
  </td>
 </tr>
 <tr></tr>
 <tr>
  <td>

  ```pas
  {st:[c=green;s=0.2]}Thick strikethrough text!
  ```

  </td>
  <td align="center">
   TBD
  </td>
 </tr>
 <tr></tr>
 <tr>
  <td>

  ```pas
  {ov:[c=blue;s=0.05]}Thin overlined text!
  ```

  </td>
  <td align="center">
   TBD
  </td>
 </tr>
</table>

## Text outline modifier `{O:}`
>
> [!NOTE]
> This modifier is added by Steamodded and is not supported by vanilla Balatro.
> *(Added in (RELEASE))*

### Basic usage

<code>{O:<i>colour</i>} adds an outline to the text.

*`colour`* sets the colour of the line, where *`colour`* is one of the following:

- the **key** of a colour defined in [`G.ARGS.LOC_COLOURS`](#loc_colours-table),

- a 6-digit **RGB hex code** or an 8-digit **RGBA hex code**, or

- the index of a custom colour provided as an entry in the [`loc_vars`](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) `vars.colours` table. See [Localization](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) for more details.

### Advanced usage

By supplying a table to the text modifier, it is possible to customize the outline further: <code>{O:[c=<i>colour</i>;s=<i>size</i>]}</code>. *size* is a decimal value with a default of `1.0`. It indicates the thickness of the outline. **Due to implementation constraints, large *size* values may lead to unexpected results.** It is **required** to specify a *colour*.

### Examples

<table>
 <tr>
  <td> Text string </td> <td> Result </td>
 </tr>
 <tr>
  <td>

  ```pas
  {O:red}Outlined text!
  ```

  </td>
  <td align="center">
   TBD
  </td>
 </tr>
 <tr></tr>
 <tr>
  <td>

  ```pas
  {C:blue,O:[c=green;s=0.6]}Thinner outline!
  ```

  </td>
  <td align="center">
   TBD
  </td>
 </tr>
</table>

## Text font modifier `{f:}`
>
> [!NOTE]
> This modifier is added by Steamodded and is not supported by vanilla Balatro.

> [!IMPORTANT]
> This modifier requires the **lowercase** `f`, unlike other modifiers which must be UPPERCASE.

<code>{f:<i>font</i>}</code> changes the font of the text.

*`font`* is a f value ranging from `1` to `9` in vanilla, to add [custom fonts](https://docs.smods.dev/Game%20Objects/SMODS.Font) you need to set the value as the font's full key (`modname_font`).

### Examples

<table>
 <tr>
  <td>Text string</td>
  <td>Font Name</td>
  <td>Assigned Language</td>
  <td>Result</td>
 </tr>

 <tr>
  <td>

   ```pas
{f:1}Hello{}
```

  </td>
  <td>m6x11 plus</td>
  <td>Default</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_1_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_1_light.svg" height=35 width=128.2 alt="Hello">
   </picture>
  </td>
 </tr>

 <tr>
  <td>

   ```pas
{f:2}Hello, 你好{}
```

  </td>
  <td>Noto Sans SC Bold</td>
  <td>Simplified Chinese</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_2_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_2_light.svg" height=35 width=128.2 alt="Hello, 你好">
   </picture>
  </td>
 </tr>

 <tr>
  <td>

   ```pas
{f:3}Hello, 您好{}
```

  </td>
  <td>Noto Sans TC Bold</td>
  <td>Traditional Chinese</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_3_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_3_light.svg" height=35 width=128.2 alt="Hello, 您好">
   </picture>
  </td>
 </tr>

 <tr>
  <td>

   ```pas
{f:4}Hello, 안녕하세요{}
```

  </td>
  <td>Noto Sans KR Bold</td>
  <td>Korean</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_4_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_4_light.svg" height=35 width=128.2 alt="Hello, 안녕하세요">
   </picture>
  </td>
 </tr>

 <tr>
  <td>

   ```pas
{f:5}こんにちは{}
```

  </td>
  <td>Noto Sans JP Bold</td>
  <td>Japanese</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_5_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_5_light.svg" height=35 width=128.2 alt="こんにちは">
   </picture>
  </td>
 </tr>

 <tr>
  <td>

   ```pas
{f:6}Hello, Здравствуйте{}
```

  </td>
  <td>Noto Sans Bold</td>
  <td>Russian</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_6_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_6_light.svg" height=35 width=128.2 alt="Hello, Здравствуйте">
   </picture>
  </td>
 </tr>

 <tr>
  <td>

   ```pas
{f:7}Hello{}
```

  </td>
  <td>m6x11 plus</td>
  <td>None*</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_7_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_7_light.svg" height=35 width=128.2 alt="Hello">
   </picture>
  </td>
 </tr>

 <tr>
  <td>

   ```pas
{f:8}Hello{}
```

  </td>
  <td>Go Noto Current Bold</td>
  <td>All1**</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_8_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_8_light.svg" height=35 width=128.2 alt="Hello">
   </picture>
  </td>
 </tr>

 <tr>
  <td>

   ```pas
{f:9}Hello{}
```

</td>
  <td>Go Noto CJK Core</td>
  <td>All2**</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_9_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_9_light.svg" height=35 width=128.2 alt="Hello">
   </picture>
  </td>
 </tr>

 <tr>
  <td>

   ```pas
{f:modprefix_fontkey}Hello{}
```

  </td>
  <td><a href="https://docs.smods.dev/Game%20Objects/SMODS.Font">Custom Font</a> (example: Comic Sans MS)</td>
  <td>Custom</td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_font_hello_10_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_font_hello_10_light.svg" height=35 width=128.2 alt="Hello">
   </picture>
  </td>
 </tr>
</table>

*It differs from the default font from the parameters `TEXT_HEIGHT_SCALE = 0.9` and `TEXT_OFFSET = {x=10,y=15}`

**These are the language names given in the original `game.lua` file.

## Text button modifier `{button:}`
>
> [!NOTE]
> This modifier is added by Steamodded and is not supported by vanilla Balatro.
> *(Added in 1501a)*

> [!IMPORTANT]
> This modifier requires the **lowercase** `button`, unlike other modifiers which must be UPPERCASE.

<code>{button:<i>function-key</i>}</code> allows text to be clickable.

*`function-key`* is the key of the callback function for the button. The function will be under `G.FUNCS['function-key']`.

### Examples

<table>
 <tr>
  <td> Text string </td> <td> Result </td>
 </tr>
 <tr>
  <td>

  ```pas
  {button:modprefix_function}Click me!
  ```

  </td>
  <td align="center">
   TBD
  </td>
 </tr>
</table>

## UI element insertion `{element:}`
>
> [!NOTE]
> This modifier is added by Steamodded and is not supported by vanilla Balatro.
> *(Added in 1531zeebee)*

> [!IMPORTANT]
> This modifier requires the **lowercase** `element`, unlike other modifiers which must be UPPERCASE.

> [!IMPORTANT]
> Unlike other modifiers, this modifier does not affect the text string after it. Instead, the UI element is inserted directly **at** the position of the modifier.

<code>{element:<i>index</i>}</code> inserts a [UI element](https://docs.smods.dev/Guides/UI-Guide)  provided as an entry in the [`loc_vars`](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) `vars.elements` table. Instances of `Node` (e.g. `CardArea`, `Sprite`, `UIBox`) are automatically wrapped in an object node. See [Localization](https://docs.smods.dev/API%20Documentation/Localization#loc_vars) for more details.

*`index`* is the array index of the element entry in the `vars.elements` table.

### Examples
<!--- Single-indented table is necessary for code blocks to function properly -->
<table>
 <tr>
  <td> Text string </td> <td> <code>loc_vars</code> </td> <td> Result </td>
 </tr>
 <tr>
  <td>

   ```pas
   {element:1} <-- Cool sprite
   ```

  </td>
  <td>

   ```lua
   vars = {
     elements = {
       { n=G.UIT.R, config = { align="cm" }, nodes = {
        { n=G.UIT.O, config= { object =
            SMODS.create_sprite(0, 0, 20, 20, "modprefix_atlaskey", {x = 0, y = 0})
        } }
      } },
     }
   }
   ```

  </td>
  <td align="center">
   TBD
  </td>
 </tr>
</table>

## Combinations

Most style codes can be combined within one set of curly braces, like `{X:mult,C:white}`.

- All combinations that aren't explicitly listed here are valid.

- `{C:}` and `{V:}` are exclusive - if both are used, `{C:}` will be ignored.

- `{X:}` and `{B:}` are exclusive - if both are used, `{X:}` will be ignored.

- `{element:}` does not interact with any other modifiers. Any additional modifiers will function as if `{element:}` wasn't present.

- **In vanilla Balatro only**, the text motion modifier `{E:}` is incompatible with background modifiers `{X:}` and `{B:}` - if background modifiers are set, `{E:1}` will only show a pop-in effect with no motion, and `{E:2}` will be ignored. Modern versions of Steamodded fully lift this restriction.

### Examples

<table>
 <tr>
  <td> Text string </td> <td> <code>loc_vars</code> </td> <td> Result </td>
 </tr>
 <tr>
  <td colspan=2>

   ```pas
   {X:mult,C:white}X0.5{}
   ```

  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_X0.5.svg" height=32 width=128 alt="X0.5" align="center">
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td colspan=2>

   ```pas
   {C:edition,E:1,s:2}YOU WIN!{}
   ```

  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_YOU_WIN!.svg" height=48 width=256 alt="YOU WIN!">
  </td>
 </tr>
 <tr> </tr> <!--- Empty row to ensure all codeblock rows have the same background colour -->
 <tr>
  <td>

   ```pas
   {s:0.8}({V:1,s:0.8}lvl.#1#
   {s:0.8}){} Level up{}
   ```

  </td>
  <td>

   ```lua
   vars = {
     G.GAME.hands[card.config.hand_type].level,
     colours = {
       G.C.HAND_LEVELS[math.min(7,
         G.GAME.hands[card.config.hand_type].level
       )]
     }
   }
   ```

  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_lvl.2_Level_up_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_lvl.2_Level_up_light.svg" height=32 width=256 alt="(lvl.2) Level up)">
   </picture>
  </td>
 </tr>
</table>

## Named colours dictionary (`G.ARGS.LOC_COLOURS`)

<a name="loc_colours"></a>

<a name="loc_colours-table"></a>
<table>
 <tr>
  <td><b> Colour </td> <td><b> Key </td> <td><b> Value </td> <td align="center"><b> Example </td> <td align="center"><b> Note </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.RED.svg" height=32 width=32 alt="#FE5F55FF">
  </td>
  <td>
   <code><b>red</code>
  </td>
  <td>
   <code>G.C.RED</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_+1_discard_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_+1_discard_light.svg" height=24 width=128 alt="+1 discard">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.MULT.svg" height=32 width=32 alt="#FE5F55FF">
  </td>
  <td>
   <code><b>mult</code>
  </td>
  <td>
   <code>G.C.MULT</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_+4_Mult_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_+4_Mult_light.svg" height=24 width=128 alt="+4 Mult">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.BLUE.svg" height=32 width=32 alt="#009DFFFF">
  </td>
  <td>
   <code><b>blue</code>
  </td>
  <td>
   <code>G.C.BLUE</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_+1_hand_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_+1_hand_light.svg" height=24 width=128 alt="+1 hand">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.CHIPS.svg" height=32 width=32 alt="#009DFFFF">
  </td>
  <td>
   <code><b>chips</code>
  </td>
  <td>
   <code>G.C.CHIPS</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_+50_Chips_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_+50_Chips_light.svg" height=24 width=128 alt="+50 Chips">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.GREEN.svg" height=32 width=32 alt="#4BC292FF">
  </td>
  <td>
   <code><b>green</code>
  </td>
  <td>
   <code>G.C.GREEN</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_1_in_6_chance_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_1_in_6_chance_light.svg" height=24 width=128 alt="1 in 6 chance">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.MONEY.svg" height=32 width=32 alt="#F3B958FF">
  </td>
  <td>
   <code><b>money</code>
  </td>
  <td>
   <code>G.C.MONEY</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_Earn_$4_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_Earn_$4_light.svg" height=24 width=128 alt="Earn $4">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.GOLD.svg" height=32 width=32 alt="#EAC058FF">
  </td>
  <td>
   <code><b>gold</code>
  </td>
  <td>
   <code>G.C.GOLD</code>
  </td>
  <td align="center">
  <img src="/_static/Assets/Text-Styling/example_Android.svg" height=24 width=128 alt="Earn $4">
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.FILTER.svg" height=32 width=32 alt="#FF9A00FF">
  </td>
  <td>
   <code><b>attention</code>
  </td>
  <td>
   <code>G.C.FILTER</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_+1_hand_size_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_+1_hand_size_light.svg" height=24 width=128 alt="+1 hand size">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.PURPLE.svg" height=32 width=32 alt="#8867A5FF">
  </td>
  <td>
   <code><b>purple</code>
  </td>
  <td>
   <code>G.C.PURPLE</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_Purple_Seal.svg" height=24 width=128 alt="Purple Seal">
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.WHITE.svg" height=32 width=32 alt="#FFFFFFFF">
  </td>
  <td>
   <code><b>white</code>
  </td>
  <td>
   <code>G.C.WHITE</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_Joker_dark.svg" height=24 width=128 alt="Joker">
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.UI.TEXT_INACTIVE.svg" height=32 width=32 alt="#88888899">
  </td>
  <td>
   <code><b>inactive</code>
  </td>
  <td>
   <code>G.C.UI.TEXT_INACTIVE</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_Must_have_room.svg" height=24 width=128 alt="(Must have room)">
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.SUITS.Spades.svg" height=32 width=32 alt="#403995FF/#4F31B9FF">
  </td>
  <td>
   <code><b>spades</code>
  </td>
  <td>
   <code>G.C.SUITS.Spades</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_suit_Spades.svg" height=24 width=128 alt="Spades">
  </td>
  <td align="center" rowspan=4>
   Suit colours<br>affected by<br>High Contrast<br>setting
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.SUITS.Hearts.svg" height=32 width=32 alt="#F03464FF/#F83B2FFF">
  </td>
  <td>
   <code><b>hearts</code>
  </td>
  <td>
   <code>G.C.SUITS.Hearts</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_suit_Hearts.svg" height=24 width=128 alt="Hearts">
  </td>
 </tr>
  <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.SUITS.Clubs.svg" height=32 width=32 alt="#235955FF/#008EE6FF">
  </td>
  <td>
   <code><b>clubs</code>
  </td>
  <td>
   <code>G.C.SUITS.Clubs</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_suit_Clubs.svg" height=24 width=128 alt="Clubs">
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.SUITS.Diamonds.svg" height=32 width=32 alt="#F06B3FFF/#E29000FF">
  </td>
  <td>
   <code><b>diamonds</code>
  </td>
  <td>
   <code>G.C.SUITS.Diamonds</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_suit_Diamonds.svg" height=24 width=128 alt="Diamonds">
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.SECONDARY_SET.Tarot.svg" height=32 width=32 alt="#A782D1FF">
  </td>
  <td>
   <code><b>tarot</code>
  </td>
  <td>
   <code>G.C.SECONDARY_SET.Tarot</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_Tarot_card_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_Tarot_card_light.svg" height=24 width=128 alt="Tarot card">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.SECONDARY_SET.Planet.svg" height=32 width=32 alt="#13AFCEFF">
  </td>
  <td>
   <code><b>planet</code>
  </td>
  <td>
   <code>G.C.SECONDARY_SET.Planet</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_Planet_card_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_Planet_card_light.svg" height=24 width=128 alt="Planet card">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.SECONDARY_SET.Spectral.svg" height=32 width=32 alt="#4584FAFF">
  </td>
  <td>
   <code><b>spectral</code>
  </td>
  <td>
   <code>G.C.SECONDARY_SET.Spectral</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_Spectral_card_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_Spectral_card_light.svg" height=24 width=128 alt="Spectral card">
   </picture>
  </td>
  <td> </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.EDITION.svg" height=32 width=32 alt="EDITION">
  </td>
  <td>
   <code><b>edition</code>
  </td>
  <td>
   <code>G.C.EDITION</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_YOU_WIN!.svg" height=24 width=128 alt="YOU WIN!">
  </td>
  <td align="center" rowspan=2>
   Animated colours
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.DARK_EDITION.svg" height=32 width=32 alt="DARK EDITION">
  </td>
  <td>
   <code><b>dark_edition</code>
  </td>
  <td>
   <code>G.C.DARK_EDITION</code>
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_Add_Negative_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_Add_Negative_light.svg" height=24 width=128 alt="Add Negative">
   </picture>
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.RARITY.Common.svg" height=32 width=32 alt="#009DFFFF">
  </td>
  <td>
   <code><b>common</code>
  </td>
  <td>
   <code>G.C.RARITY.Common</code>
  </td>
  <td align="center">
   <picture>
    <img src="/_static/Assets/Text-Styling/example_common_light.svg" height=16 width=128 alt="Common">
   </picture>
  </td>
  <td align="center" rowspan=3>
   Added by<br>Steamodded
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.RARITY.Uncommon.svg" height=32 width=32 alt="#4BC292FF">
  </td>
  <td>
   <code><b>uncommon</code>
  </td>
  <td>
   <code>G.C.RARITY.Uncommon</code>
  </td>
  <td align="center">
   <picture>
    <img src="/_static/Assets/Text-Styling/example_uncommon_light.svg" height=16 width=128 alt="Uncommon">
   </picture>
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.RARITY.Rare.svg" height=32 width=32 alt="#FE5F55FF">
  </td>
  <td>
   <code><b>rare</code>
  </td>
  <td>
   <code>G.C.RARITY.Rare</code>
  </td>
  <td align="center">
   <picture>
    <img src="/_static/Assets/Text-Styling/example_rare_light.svg" height=16 width=128 alt="Rare">
   </picture>
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.RARITY.Legendary.svg" height=32 width=32 alt="#B26CBBFF">
  </td>
  <td>
   <code><b>legendary</code>
  </td>
  <td>
   <code>G.C.RARITY[4]</code> (vanilla)<br> <code>G.C.RARITY.Legendary</code> (SMODS)
  </td>
  <td align="center">
   <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/_static/Assets/Text-Styling/example_Legendary_Joker_dark.svg">
    <img src="/_static/Assets/Text-Styling/example_Legendary_Joker_light.svg" height=24 width=128 alt="Legendary Joker">
   </picture>
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.SECONDARY_SET.Enhanced.svg" height=32 width=32 alt="#8389DDFF">
  </td>
  <td>
   <code><b>enhanced</code>
  </td>
  <td>
   <code>G.C.SECONDARY_SET.Enhanced</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_Enhancement.svg" height=24 width=128 alt="Enhancement">
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.UI.TEXT_DARK.svg" height=32 width=32 alt="#4F6367FF">
  </td>
  <td>
   <b>default
  </td>
  <td>
 <code>G.C.UI.TEXT_DARK</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_Joker_light.svg" height=24 width=128 alt="Joker">
  </td>
  <td> </td>
 <tr>
  <td>
   <img src="/_static/Assets/Colour-Icons/G.C.DYN_UI.DARK-none.svg" height=32 width=32 alt="#1E2B2DFF"><br><img src="/_static/Assets/Colour-Icons/G.C.DYN_UI.DARK-cerulean.svg" height=32 width=32 alt="#055481FF">
  </td>
  <td>
   <b>blind
  </td>
  <td>
 <code>G.C.DYN_UI.DARK</code>
  </td>
  <td align="center">
   <img src="/_static/Assets/Text-Styling/example_blind_none_light.svg" height=16 width=128 alt="No Blind"><br><img src="/_static/Assets/Text-Styling/example_blind_cerulean_light.svg" height=16 width=128 alt="Cerulean Bell">
  </td>
  <td align="center">
   Added by<br>Steamodded<br>
   since <code>1.0.0~BETA-1531zeebee</code>
  </td>
 </tr>
</table>

This dictionary is initially assigned by the `loc_colour` function in `functions/misc_functions.lua`.

Steamodded automatically adds additional entries to `LOC_COLOURS` for all custom objects in:

- [SMODS.Rarity](https://docs.smods.dev/Game%20Objects/SMODS.Rarity)
- [SMODS.Gradient](https://docs.smods.dev/Game%20Objects/SMODS.Gradient)
- [SMODS.ConsumableType](https://docs.smods.dev/Game%20Objects/SMODS.Center/SMODS.Consumable)
- [SMODS.Suit](https://docs.smods.dev/Game%20Objects/SMODS.Rank-and-SMODS.Suit#api-documentation-smodssuit)

which can be used as colour keys in the same way by `{C:}`/`{V:}` and `{X:}`/`{B:}`. When referring to custom Rarity, Gradient or Suit colours added by SMODS, the key must be prefixed with the [mod prefix](https://docs.smods.dev/API%20Documentation/Mod-Metadata#metadata).
