# API Documentation: `SMODS.Scoring_Parameter`

Used to add new scoring parameters that act like `chips` or `mult` in the base game

- **Required parameters:**
  - `key`
  - `default_value`
    - Default value the parameter takes
- **Optional parameters** *(defaults)*:
  - `colour = G.C.UI_MULT`: Colour of the parameter in the game's UI
  - `calculation_keys`: Valid `calculate` returns for this parameter.
  - `hands`: Defines the values this parameter takes for each Poker Hand.
    - Each value in this table must be in the form `PokerHandKey = { modprefix_key = number, l_modprefix_key = number, s_modprefix_key = number }` where `modprefix_key` (using your mod's prefix and parameter's key) is the starting value that is updated when levelled up, `s_modprefix_key` is the starting value that is used for level up calculations and `l_modprefix_key` is the amount gained when levelled up. The basic formula to calculate the amount is `value = s_value + (level-1) * l_value`.
    - Example:

    ```lua
    -- This parameter is only applied to hands that contain a flush. They all scale the same way
    hands = {
        ["Flush Five"] = {modprefix_key = 1, l_modprefix_key = 5, s_modprefix_key = 1},
        ["Flush House"] = {modprefix_key = 1, l_modprefix_key = 5, s_modprefix_key = 1},
        ["Straight Flush"] = {modprefix_key = 1, l_modprefix_key = 5, s_modprefix_key = 1},
        ["Flush"] = {modprefix_key = 1, l_modprefix_key = 5, s_modprefix_key = 1},
    }
    ```

## API methods

- `modify(self, amount)`
  - Used for custom behaviour when the parameter is modified. Do note that this function **also** updates the UI elements, so if you redefine it you should ensure that you keep this functionality.
  - If not defined, it simply adds `amount` to the current value.
  - Example of custom behaviour:

    ```lua
    -- Parameter that doesn't reset each hand
    modify = function(self, amount)
        self.current = self.current + amount -- update the current value, used for final score calculation
        self.default_value = self.current -- update the default value
        update_hand_text({delay = 0}, {[self.key] = self.current}) -- update the UI
    end
    ```

- `calc_effect(self, effect, scored_card, key, amount, from_edition)`
  - Used for custom behaviour when a calculation key for the parameter is returned in `calculate`.
    - `effect`: Return table for that calculation
    - `scored_card`: Card or object being scored
    - `key`: The return key being calculated
    - `amount`: The value returned for that key
    - `from_edition`: `true` if the effect comes from an edition
  - If not defined, it calls `modify` with the `amount`, juices up the scoring card and plays a default message on it.
  - For more examples of how to use this function, take a look at the `chips` and `mult` Scoring Parameters in `src/game_object.lua`, or `SMODS.calculate_individual_effect` in `src/utils.lua`.

## Util methods

- `SMODS.get_scoring_parameter(key, flames)`
  - Gets the current value for the scoring parameter `key`. `flame` is an flag to get the current value for flame animations.

# API Documentation: `SMODS.Scoring_Calculation`

Used to add new scoring calculation behavious between `chips` and `mult`.

- **Required parameters:**
  - `key`
  - `func(self, chips, mult, flames) -> number`
    - Calculates the current score.
    - `chips` and `mult` are the current value of those parameters and `flames` is `true` when the score is being calculated for flame animations.
    - To obtain any other scoring parameters in this function you can call `SMODS.get_scoring_parameter(key, flames)`. *`flames` must be passed as the second argument for animations to work correctly*
    - Example:

    ```lua
    -- Substraction scoring calculation
    func = function(self, chips, mult, flames)
        return chips - mult
    end
    ```

- **Optional parameters** *(defaults)*:
  - `text = 'X'`: Replaces the "X" symbol on the UI between the chips and mult boxes
  - `colour = G.C.RED`: Sets the colour for the UI symbol
  - `config`: Table for values that persist during the run. You can access it by using `self.config` in the Scoring Calculation's functions, or `G.GAME.current_scoring_calculation.config` anywhere else.
  - `parameters = {'chips', 'mult'}`: A list of scoring parameters this Scoring Calculation applies to, any `calculate` return for any other parameter will be ignored.

## API methods

- `replace_ui(self) -> table`
  - Used to replace the UI for the hand scoring boxes. Returns a [UI node table](https://github.com/Steamodded/smods/wiki/UI-Guide). See `SMODS.GUI.hand_chips_container` in `src/ui.lua` for an example.

- `update_ui(self, container, chip_display, mult_display, operator)`
  - Called when the UI for the scoring boxes is being updated. `container` is the UIElement that contains the entire UI, while `chip_display`, `mult_display` and `operator` are the UIElements for the chip box, mult box and operator symbol respectively.
  - Call `operator.UIBox:recalculate()` to actually update the UI when you do any modification.

## Util methods

- `SMODS.set_scoring_calculation(key)`
  - Sets the current Scoring Calculation. `multiply` (vanilla behaviour), `add` and `exponent` are already defined by SMODS.

- `SMODS.calculate_round_score(flames)`
  - Calculates the current hand score based on the current Scoring Calculation. `flames` is an internal flag used for flame animations.
