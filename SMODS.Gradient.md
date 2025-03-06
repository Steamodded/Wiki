# API Documentation: `SMODS.Gradient`
This class helps create colours that change over time between two or more specified endpoint colours. A gradient can be used at any point where a colour is expected.
- **Required parameters:**
	- `key`
    - `colours`: An array of two or more colours for the gradient to interpolate between.
        - Each element must be provided as an array of four numerical values between 0 and 1, representing the red, green, blue and opacity values. Beside specifying such a table directly, you can also use a colour present in `G.C` (e.g. `G.C.RED`) or generate a colour from a hex code (e.g. `HEX('ABCDEF')`).
- **Optional parameters** *(defaults)*:
    - `cycle = 10`: Amount of time (in seconds) for the gradient to cycle through all colours.
    - `interpolation = 'trig'`: Determines how to interpolate between colours.
        - `'trig'`: Interpolate using a sine wave.
        - `'linear'`: Interpolate linearly, at a constant rate.

## API methods
- `update(self, dt)`
    - The default implementation of this function fulfills the above specifications. If your use case requires more control than this implementation provides, you can use a modified `update` function to add your functionality. 