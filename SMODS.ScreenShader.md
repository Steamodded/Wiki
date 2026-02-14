# API Documentation: `SMODS.ScreenShader`
This class allows for drawing a shader on the entire screen, rather than just a singular object.
- **Required parameters:**
	- `key`
    - `shader` or `path`
        - `shader` refers to the key of an existing shader, including mod prefix key. `path` refers to the file of a shader similar to the `path` parameter in `SMODS.Shader`
        - Only one of these parameters is required, having both will prioritize `shader` and ignore `path`
- **Optional parameters** *(defaults)*:
    - `order`
        - Defines the order in which ScreenShaders should be rendered, defaults to 0
        - ScreenShaders are rendered in order from lowest to highest.


## API methods
- `should_apply(self) -> boolean`
    - Determines whether a ScreenShader should apply to the screen at any given time. If not defined, defaults to always applying.
- `send_vars(self) -> table`
    - Used to send extra vars to the shader, similar to `SMODS.Shader.send_vars`
    - One major difference between the two, with `SMODS.ScreenShader.send_vars`, you can pass arrays like so
    ```lua
    send_vars = function(self)
        return {
            float_array = {array = {1.5, 2.3, 6.7}},
            vector_array = {array = { {x, y}, {z, w} }}
        }
    end
    ```