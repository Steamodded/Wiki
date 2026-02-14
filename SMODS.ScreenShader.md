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
        - Lower orders are rendered earlier


## API methods
- `should_apply(self) -> boolean`
    - Determines whether a ScreenShader should apply to the screen at any given time. If not defined, defaults to always applying.
- `send_vars(self) -> table`
    - Returns a table of all variables to send to the shader
    - For example, returning `{iTime = G.TIMERS.REAL}` would send the floating point value `iTime`, allowing it to be used in the shader with `extern float iTime;`
    - Note that if you do not use all external variables in the shader, it will crash