# API Documentation: `SMODS.DynaTextEffect`

This class is used to add effects to text descriptions and other DynaText objects

- **Required parameters:**
  - `key`

## API methods

- `func(dynatext, index, letter)`
  - Used to modify each [letter](#letters), where `index` is the position of the letter in the string and `dynatext` is the DynaText object
- `draw_letter(dynatext, index, letter)`
  - Runs when the [letter](#letters) is being drawn to the screen, where `index` is the position of the letter in the string and `dynatext` is the DynaText object
- `draw_shadow(dynatext, index, letter)`
  - Runs when the [letter](#letters)'s shadow is being drawn to the screen, where `index` is the position of the letter in the string and `dynatext` is the DynaText object
- `draw_override(dynatext)`
  - Replaces the `draw` function of the `dynatext` object entirely

## Letters

Each DynaText letter is a table that has the following properties

- `letter` (`love.graphics.Text`) - A replaceable text object that will get drawn
- `char` (`string`) - The string character this letter represents
- `pop_in` (`number`) - Determines how the letter gradually pops in
- `r` (`number`) - Rotation of the letter in radians, defaults to 0
- `scale` (`number`) - Scale of the letter with the normal size being 1
- `dims` (`{x: integer, y: integer}`) - A table with x and y as letter's dimension. in this case it does NOT modify the size that it is drawn. it instead modifies how far apart each letter are
- `offset` (`{x: integer, y: integer}`) - A table with x and y to specify the letter's offset from the main dynatext alignment
- `colour` (`table`) - The letter's colour. Ignored if `prefix` or `suffix` are set
- `prefix` (`table`) - The letter's colour if it's part of the DynaText's `prefix`.
- `suffix` (`table`) - The letter's colour if it's part of the DynaText's `suffix`. Ignored if `prefix` is set

## Applying effects to text

For your effect to show up in game, you can assign it to formatted text using the *style modifier code* `E:` Example:

```lua
-- Effect code
-- Rotates letters a different amount based on position
SMODS.DynaTextEffect {
    key = "rotating",
    func = function (self, index, letter)
        letter.r = math.sin((G.TIMERS.REAL + index)*1.9443) * math.pi / 7
    end
}
```

```lua
-- In your localization file:
j_modprefix_example = {
  name = "{E:modprefix_rotating}Example",
  text = {
    {
    "{C:chips,E:modprefix_rotating}+#1#{} Chips",
    },
  },
},
```
