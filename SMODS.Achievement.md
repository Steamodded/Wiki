# API Documentation: SMODS.Achievement
- **Required parameters:**
	- `key`
- **Optional parameters** *(defaults)*:
	- `atlas = 'achievements'`,
    - `pos = {x=1, y=0},`,
    - `earned`: Achievement is considered "earned". Achievement will stay earned on loaded profiles unless `reset_on_startup` is true
    - `reset_on_startup`: Unearns the achievement if already earned on profile load
    - `loc_text`, uses the standard skeleton, omit if using localization files
    ```lua
		{
			name = '',
			description = { '' },
		}
	```
    - `bypass_all_unlocked = false`: Achievement cannot be earned if "Unlock All" button was pressed on current profile
    - `hidden_name = true`: Hides the name of the achievement if not earned
    - `hidden_text`: Hides the description of the achievement if not earned

## API methods
- `unlock_condition(self, args) -> bool`
    - Runs every time `check_for_unlock` is called. Returns true if the achievement should be earned. 