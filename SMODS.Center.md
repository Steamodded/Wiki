# API Documentation: `SMODS.Center`
`SMODS.Center` is the superclass for everything the game considers to be a "center". It is not recommended to use it to create an object directly; always use the appropriate subclass.
## `SMODS.Joker`
- **Required parameters:**
	- `key`,
- **Optional parameters** *(defaults)*:
	- `loc_txt`, Skeleton:
	```lua
		{
			name = '',
			text = { '' },
		}
	```
	- `config = {}`,
	- `rarity = 1` (`1` = Common, `2` = Uncommon, `3` = Rare, `4` = Legendary)
	- `pos = { x = 0, y = 0 }`,
	- `atlas = 'Joker'`,
	- `cost = 3`,
	- `unlocked = true`,
	- `discovered = false`,
	- `blueprint_compat = false` (**Purely cosmetic, you need to define your Joker's blueprint behavior in code**),
	- `eternal_compat = true`,
	- `perishable_compat = true`,
	- `<sticker>_compat` for any modded stickers

## `SMODS.Consumable`
- **Required parameters:**
	- `key`,
	- `set` (`'Tarot'`, `'Planet'`, `'Spectral'`, or any modded consumable type),

- **Optional parameters** *(defaults)*:
	- `loc_txt`, default skeleton
	- `config = {}`
	- `pos = { x = 0, y = 0 }`
	- `atlas = 'Tarot'`
	- `cost = 3`
	- `unlocked = true`
	- `discovered = false`
	- `hidden` for legendary consumables like The Soul. For further customization:
		- `soul_set = 'Spectral'`, legendaries may appear when a card of either their own set or this one are being generated.
		- `soul_rate = 0.003`, determines how likely this legendary is to replace each card in a pack
		- `can_repeat_soul`, allows repeats of this card as if Showman were present

## `SMODS.Voucher`
- **Required parameters:**
	- `key`,
- **Optional parameters** *(defaults)*:
	- `loc_txt`, default skeleton
	- `config = {}`
	- `pos = { x = 0, y = 0 }`
	- `atlas = 'Voucher'`
	- `cost = 10`
	- `unlocked = true`
	- `discovered = false`
	- `requires`: specify a list of one or more vouchers by their **full key** (e.g. `'v_grabber'` for vanilla vouchers, or `'v_pref_myvoucher'` for a modded voucher from the mod with prefix `'pref'`)

## `SMODS.Back` (formerly `SMODS.Deck`)
- **Required parameters:**
	- `key`,
- **Optional parameters** *(defaults)*:
	- `loc_txt`, default skeleton
	```
	- `config = {}`,
	- `pos = { x = 0, y = 0 }`,
	- `atlas = 'centers'`,
	- `unlocked = true`,
	- `discovered = false`,

## `SMODS.Booster`
- **Required parameters:**
	- `key`
- **Optional parameters** *(defaults)*:
	- `loc_txt`, Skeleton:
	```lua
		{
			name = '',
			group_name = '', -- Pack group text while a pack is being opened, omit if using group_key
			text = { '' },
		}
	```
	- `atlas = 'Booster'`
	- `pos = { x = 0, y = 0 }`
	- `config = { extra = 3, choose = 1 }`: `extra` is the amount of cards in the pack, `choose` is the amount of choices.
	- `discovered = false`
	- `weight = 1`: Determines how frequently the pack appears in the shop.
	- `cost = 4`
	- `group_key`: Key to the group name (bottom text while on the pack opening screen) of this booster. Draws from `G.localization.misc.dictionary['k_booster_group'..group_key]`.
	- `draw_hand = false`: If this is `true`, draw playing cards to hand when this pack is opened.
	- `kind`: Used for grouping packs together. For example, this can be used in `get_pack()` to generate a booster pack of a given type.

## API methods
### All centers
- `set_ability(self, card, initial, delay_sprites)`
	- Set up initial ability values or manipulate sprites in an advanced way.
- `add_to_deck(self, card, from_debuff)`
	- Modify the game state when this card is obtained.
	- Jokers are considered added when they become undebuffed (in this case, `from_debuff` will be true).
- `remove_from_deck(self, card, from_debuff)`
	- Modify the game state when this card is sold, destroyed, or otherwise removed.
	- Jokers are considered removed when debuffed (in this case, `from_debuff` will be true).
- `in_pool(self, args) -> bool, { allow_duplicates = bool }`
	- Define custom logic for when a card is allowed to spawn. A card can spawn if `in_pool` returns true and all other checks are met.
	- `allow_duplicates` allows this card to spawn when one already exists, even without Showman.
	- When called from `generate_card_ui`, the `_append` key is passed as `args.source`.
- `update(self, card, dt)`
	- For actions that happen every frame.
- `set_sprites(self, card, front)`
	- For advanced sprite manipulation that happens when a card is created or loaded.
- `load(self, card, card_table, other_card)`
	- For modifications to sprites or the card itself when a run is reloaded.
- `loc_vars(self, info_queue, card) -> { vars ?= table, main_start ?= table, main_end ?= table, key ?= string, replace_debuff ?= bool }`
	- Pass variables (`vars`) to card descriptions.
	- Add tooltips by appending to `info_queue`.
	- You can force the use of a different description entirely (`key`).
	- Add additional text to the start or end of a card description with `main_start` or `main_end`.
- `generate_ui(self, info_queue, card, desc_nodes, specific_vars, full_UI_table)`
	- The default implementation of this function acts as a wrapper of `loc_vars`. For advanced UI implementations, define this function directly.
- `locked_loc_vars(self, info_queue, card) -> { vars ?= table }`
	- Pass variables (`vars`) to descriptions of locked cards.
	- Tooltips can be configured by appending to `info_queue`.
- `check_for_unlock(self, args) -> bool`
	- Configure unlock conditions. Refer to the function `check_for_unlock` in Balatro's code for more information.
- `set_badges(self, card, badges)`
	- Add additional badges, leaving existing badges intact. This function doesn't return; add badges by appending to `badges`.
	- Avoid overwriting existing elements. It will cause text to appear on the top left corner of your screen instead.
- `set_card_type_badge(self, card, badges)`
	- Same as `set_badges`, but bypasses creation of the card type / rarity badge, allowing you to replace it with a custom one.

### Specific to certain subclasses
- `Consumable.use(self, card, area, copier)`
	- Defines the behavior of a consumable when used.
- `Consumable.can_use(self, card) -> bool`
	- Determines whether a consumable is currently able to be used.
- `Consumable.keep_on_use(self, card) -> bool`
	- Allows a used card to stay where it is instead of getting destroyed.
- `Joker.calculate(self, card, context) -> table`
	- All Joker effects that are tied to specific in-game actions happen here. Refer to the function `Card:calculate_joker(context)` in Balatro's source code to learn more about `context` and how this function works.
	- Some common calculation contexts include:
		- `context.joker_main`: The main scoring phase for Jokers, after playing cards have finished scoring.
		- `context.before`: Effects that trigger before playing cards are scored (e.g. Midas Mask)
		- `context.after`: Effects that trigger when a hand has finished scoring (e.g. Ice Cream melting)
		- `context.individual`: Effects that operate on each card separately. An additional check for the card area is needed to avoid extra triggers.
	- Consumables may also make use of this function, however only `context.joker_main` timing is supported.
- `Joker.calc_dollar_bonus(self, card) -> number`
	- For awarding money at the end of the round (e.g. Delayed Gratification, Cloud Nine)
- `Back.apply(self)`
	- Apply modifiers at the start of a run.
- `Back.trigger_effect(self, args)`
	- Used for effects that happen during a run, like Plasma Deck's effect.
- `Voucher.redeem(self)`
	- Defines the behavior of a Voucher when redeemed.
- `Booster.create_card(self, card, i) -> table|Card`
	- Creates the cards inside of the booster pack. `card` is the booster pack card, `i` is the position of the card to be generated. If the returned table is not a `Card`, it is passed into `SMODS.create_card`.
- `Booster.update_pack(self, dt)`
	- Handles booster pack UI when opened. 
- `Booster.ease_background_colour(self)`
	- Changes background colour. 
- `Booster.particles(self)`
	- Handles particle effects. 
- `Booster.create_UIBox(self) -> table`
	- Returns the booster's UIBox. 

## Utility functions
- `SMODS.Booster:take_ownership_by_kind(kind, obj, silent)`
	- Finds all booster packs with matching `kind` and applies `SMODS.Booster:take_ownership()` to each one with arguments `obj` and `silent` passed through.
