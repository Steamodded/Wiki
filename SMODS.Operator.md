# API Documentation: `SMODS.Operator`
This class provides a way to alter the Chip-Mult operator.
- **Required parameters:**
	- `key`
  - `func`: A function that takes two numbers, `chips` and `mult`, and returns the effect of the operator for them. For the base game, this would look something like `function(chips, mult) return chips * mult end`.
  - `node_func`: A function that runs once upon setting the operator to update the node display. This function runs with the context of the parent node for the operator text node.
  
## API methods
- `SMODS.set_operator(name)`
    - Sets the active operator to a currently defined operator.
- `SMODS.calculate_round_score(chips, mult)`
    - Calculates a round score based on a `chips` value, a `mult` value, and the current active operator.

## `G.GAME` values
- `G.GAME.current_operator`
    - Stores the string key of the current operator - you can get it with `SMODS.Operators[G.GAME.current_operator]`.

## Misc.
SMODS itself defines an operator for the vanilla behavior of multiplying Chips and Mult, with a key of `base`. It is defined as follows:
```lua
SMODS.Operator {
    key = "base",
    func = function(chips, mult) return chips * mult end,
    node_func = function(e)
        e.children[1].config.colour = G.C.UI_MULT
        e.children[1].config.text = "X"
        e.children[1].config.text_drawable:set("X")
        e.children[1].UIBox:recalculate()
    end
}
```
