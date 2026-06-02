# API Documentation: `SMODS.Shader`
- **Required parameters:**
	- `key`
	- `path`: The file name of your shader. Shaders must be stored in `assets/shaders/` and be a `.fs` file.
		- The shader's `key`, file name (without extension) and the shader name used in the GLSL file **must be identical.**

### API methods
- `send_vars(sprite, @nullable card) -> table`
	- Used to send extra vars to the shader. Card may be `nil` if shader is not applied to a Card. Returned table entries are sent to the shader via `Shader:send(key, value)`. Usage example may be found in `example_mods/Mods/EditionExamples` - [here](https://github.com/Steamodded/examples/blob/master/Mods/EditionExamples/EditionExamples.lua#L126) and [here](https://github.com/Steamodded/examples/blob/master/Mods/EditionExamples/assets/shaders/gold.fs#L24)


#### Working with Shaders
[ionized.fs](https://github.com/Steamodded/examples/blob/master/Mods/EditionExamples/assets/shaders/ionized.fs) has shader code explanation with comments.
For a general guide, look at [LOVE2D introduction to shaders](https://blogs.love2d.org/content/beginners-guide-shaders).

If you want to see vanilla Balatro shaders, unzip the Balatro.exe and go to `resources/shaders` folder.

To see values for default externs, check out `engine/sprite.lua` -> `Sprite:draw_shader`.


#### Useful shaders resources
- [The book of shaders](https://thebookofshaders.com) - beginner friendly introduction to shaders.
- [GLSL Editor](https://patriciogonzalezvivo.github.io/glslEditor/) - preview your fragment shaders live.
- [GLSL Image Processing System](https://github.com/kajott/GIPS/releases) - preview your fragment shaders live. The program additionally provides some built-in shaders as examples.
- [Inigo Quilez articles](https://iquilezles.org/articles/) - in-depth articles on algorithms and techniques you could use in shaders. A lot of those are for 3D, but there's some 2D stuff as well.
- [Shadertoy](https://www.shadertoy.com) - tons of shaders from other people to learn from. A lot of them are pretty complex and 3D, but you can find simple 2D ones.

Note: in all resources the language is slightly different from LOVE2D shaders language, but the logic works the same way.

# API Documentation: `SMODS.ScreenShader`
*(Added in 1501a)*

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
- `draw(self, shader, canvas)`
    - Allows freely drawing on a canvas for more advanced control than directly applying the shader to it. *(added in 1620a)*