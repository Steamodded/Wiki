# The `G` Variable

Balatro has a global variable `G` which is the singleton instance of the `Game` class. This list is not comprehensive.

## The Highlights

- `G.E_MANAGER` is the [event manager](https://github.com/Steamodded/smods/wiki/Guide-%E2%80%90-Event-Manager).
- `G.P_CENTERS` holds the game's center objects (prototypes for jokers, consumables, vouchers, decks, enhancements, editions, and boosters). It is indexed with the object's key. For example, `G.P_CENTERS.c_strength` is the center for Strength.
- `G:update(dt)` is called once per frame. This uses `G.STATE` and `G.STATE_COMPLETE` to run a state machine.
- `G.C` holds colors.
- [`G.GAME`](https://github.com/Steamodded/smods/wiki/G#GGAME)

## Everything

- `G.E_MANAGER` is the [event manager](https://github.com/Steamodded/smods/wiki/Guide-%E2%80%90-Event-Manager).
- `G.P_SEALS` holds the seal prototypes, much like `G.P_CENTERS`.
- `G.P_TAGS` holds the tag prototypes, much like `G.P_CENTERS`.
- `G.P_STAKES` holds the stake prototypes, much like `G.P_CENTERS`.
- `G.P_BLINDS` holds the blind prototypes, much like `G.P_CENTERS`.
- `G.P_CARDS` holds the playing card prototypes, much like `G.P_CENTERS`.
- `G.P_CENTERS` holds the game's center objects (prototypes for jokers, consumables, vouchers, decks, enhancements, editions, and boosters). It is indexed with the object's key. For example, `G.P_CENTERS.c_strength` is the center for Strength.
- `G.P_CENTER_POOLS` holds definitions for objects grouped by pool, indexed by numbers. For example, `G.P_CENTER_POOLS.Tag` holds the tags, and `G.P_CENTER_POOLS.Tag[1]` is a specific tag.
- `G.P_JOKER_RARITY_POOLS` is like `G.P_CENTER_POOLS` but for specific joker rarities.
- `G.P_LOCKED` holds every locked object.
- `G:load_profile(_profile)` selects one of the profiles.
- `G:set_language()` initializes localization information.
- `G.ASSET_ATLAS` and `G.ANIMATION_ATLAS` hold sprite atlases that look like the following:
```lua
{
    name = string,
    image = love_image,
    type = string,
    px = number,
    py = number
}
```
- `G:save_progress()` saves the unlocked/discovered/alerted badge state of centers, blinds, tags, and seals.
- `G:save_notify()` saves unlock notifications.
- `G:save_settings()` save `G.SETTINGS`.
- `G:save_metrics()` save `G.METRICS`.
- `G:prep_stage(...)` sets up `G.ROOM`.
- `G:splash_screen()` shows the intro animation.
- `G:main_menu(...)` shows the main menu.
- `G:init_game_object()` return the initial state of `G.GAME`.
- `G:start_run(...)` starts a new run or continues a run in progress. Additionally, it creates the various `CardArea`s needed in game, as well as the UI elements in the HUD.
- `G:update(dt)` is called once per frame. This uses `G.STATE` and `G.STATE_COMPLETE` to run a state machine.
- `G.STATE_COMPLETE` is set to true once the most recent transition in `G.STATE` has been run.
- `G.STATE` holds the current interaction state in the game's state machine.
- `G.STATES` names every possible interaction state in the game's state machine.
- `G.SPEEDFACTOR` is the speed at which `G.TIMERS.TOTAL` runs.
- `G.STEAM` is used to interact with the Steam API.
- `G.DEBUG` can be set to true to view debugging information.
- `G.FILE_HANDLER` manages saving the game every 10 seconds.
- `G:draw()` draws everything in the game.
- `G:set_globals()` initializes many globals within `G`.
- `G.VERSION` is the version string for the current build of the game.
- `G.TIMERS` has various timers that run at different rates and reset at different times. The [event manager](https://github.com/Steamodded/smods/wiki/Guide-%E2%80%90-Event-Manager) uses these, as well as many animations.
- `G.FRAMES.MOVE` holds the current physics frame number.
- `G.FRAMES.DRAW` holds the current frame number.
- `G.SETTINGS` holds the various configuration options:
- - `G.SETTINGS.language` has the current language code. 
- - `G.SETTINGS.GAMESPEED` has the current gamespeed option. 
- - `G.SETTINGS.paused` is set to true when the game is paused. 
- - `G.SETTINGS.CUSTOM_DECK` holds collab selections. 
- `G.COLLABS` is where collabs are defined. 
- `G.METRICS` holds player stats:
```lua
G.METRICS = {
    cards = {
        used = {},
        bought = {},
        appeared = {},
    },
    decks = {
        chosen = {},
        win = {},
        lose = {}
    },
    bosses = {
        faced = {},
        win = {},
        lose = {},
    }
}
```
- `G.PROFILES` holds the save profiles. Typically only `G.PROFILES[G.SETTINGS.profile]` is relevant.
- `G.CARD_W` holds the width of a standard card.
- `G.CARD_H` holds the height of a standard card.
- `G.STAGE` holds the current game screen (menu vs. gameplay).
- `G.STAGE_OBJECTS` tracks which objects belong to the current stage so they can be deleted correctly.
- `G.STAGES` names every possible game screen.
- `G.TAROT_INTERRUPT` holds the state to return to after the current tarot card is done processing.
- `G.ARGS` is used to move data around the game. It does a lot of miscellaneous things.
- `G.FUNCS` primarily holds functions used as callbacks from within UI definitions.
- `G.I` holds every object the engine needs to generically process.
- `G.I.NODE` holds every `Node`, but no subclasses.
- `G.I.MOVEABLE` holds every `Moveable`, but no subclasses.
- `G.I.SPRITE` holds every `Sprite` and `AnimatedSprite`, but no subclasses.
- `G.I.UIBOX` holds every `UIBox`, but no subclasses.
- `G.I.POPUP` holds every drag popup. This appears to be unused.
- `G.I.CARD` holds every `Card`, `Blind`, and `Card_Character`, but no subclasses.
- `G.I.CARDAREA` holds every `CardArea`, but no subclasses.
- `G.I.ALERT` is unused.
- `G.MOVEABLES` holds every moveable.
- `G.ANIMATIONS` holds every `AnimatedSprite`.
- `G.C` holds colors.
- `G.UIT` names every possible type of [UI node](https://github.com/Steamodded/smods/wiki/UI-Guide#node-types).
- `G.handlist` orders the pokers hands from best to worst.
- `G.ROOM` is the UI node for the entire window.
- `G.ROOM_ATTACH` is the moveable for `G.ROOM`.
- `G.CONTROLLER` is the singleton `Controller` object which handles input.
- `G.playing_cards` contains every spawned in playing card, regardless of area.
- `G.HUD` is the HUD's `UIBox`.
- `G.HUD_blind` is the `UIBox` for the blind's information when facing it.
- `G.HUD_tags` is the `UIBox` for tags.
- `G.hand_text_area` is a collection of convenience accessors into `G.HUD`.
```lua
G.hand_text_area = {
    chips = ...,
    mult = ...,
    ante = ...,
    round = ...,
    chip_total = ...,
    handname = ...,
    hand_level = ...,
    game_chips = ...,
    blind_chips = ...,
    blind_spacer = ...
}
```
- `G.MAJORS` appears to be unused.
- `G.MINORS` appears to be unused.
- `G.CANVAS` is the Love canvas the game gets rendered to.
- `G.SEED` is largely inconsequential. You want `G.GAME.pseudorandom.seed` instead.

## `G.GAME`

`G.GAME` holds game state for the current run. This is reset when starting a new run. Note that it is serialized when saving and reloading the game. 

- `G.GAME.won` is true if this run was won.
- `G.GAME.round_scores` holds statistics for the end screen.
- `G.GAME.joker_usage` appears to be unused.
- `G.GAME.consumeable_usage` holds statistics for effects like Fortune Teller and Satellite.
- `G.GAME.hand_usage` holds statistics for effects like Obelisk.
- `G.GAME.last_tarot_planet` holds the Fool card.
- `G.GAME.win_ante` holds the ante at which finisher blinds will appear.
- `G.GAME.stake` holds the currently applied stake.
- `G.GAME.modifiers` holds game rules. These are usually set by stakes or challenges.
- `G.GAME.starting_params`
- `G.GAME.banned_keys` holds keys of objects that aren't allowed to spawn.
- `G.GAME.round` holds the current round number.
- `G.GAME.probabilities.normal` holds the 1 for any 1 in x odds.
- `G.GAME.bosses_used` holds the boss blinds encountered this run to prevent them from spawning again too quickly.
- `G.GAME.pseudorandom` holds the RNG state for the game.
- `G.GAME.pseudorandom.seed` holds the game seed.
- `G.GAME.starting_deck_size` holds the starting deck size used by Erosion.
- `G.GAME.ecto_minus` holds the hand size decrease on Ectoplasm.
- `G.GAME.pack_size` is used to pass a booster's size to the function that creates it.
- `G.GAME.skips` counts the number of skipped blinds.
- `G.GAME.STOP_USE` is set to a number greater than 0 when no inputs should be processed,
- `G.GAME.edition_rate` is a multiplier to the 4% rate of editions spawning.
- `G.GAME.joker_rate` is a weight for jokers spawning in the shop.
- `G.GAME.tarot_rate` is a weight for tarot cards spawning in the shop.
- `G.GAME.planet_rate` is a weight for planets spawning in the shop.
- `G.GAME.spectral_weight` is a weight for spectral cards spawning in the shop.
- `G.GAME.playing_card_rate` is a weight for playing cards spawning in the shop.
- `G.GAME.consumeable_buffer` is used during calculation to prevent too many consumables from being spawned.
- `G.GAME.joker_buffer` is used during calculation by Riff-Raff to prevent too many jokers from being spawned.
- `G.GAME.discount_percent` is set by Clearance Sale and Liquidation.
- `G.GAME.interest_cap` is the amount of money needed to get max interest.
- `G.GAME.interest_amount` is the amount of interest earned per $5.
- `G.GAME.inflation` is used in the Inflation challenge.
- `G.GAME.hands_played` counts played hands.
- `G.GAME.unused_discards` counts unused discards.
- `G.GAME.perishable_rounds` determines how quickly perishable cards perish.
- `G.GAME.rental_rate` determines how expensive rental cards are at the end of a round.
- `G.GAME.blind` is the blind currently being faced off against.
- `G.GAME.chips` is the current total round chips.
- `G.GAME.chips_text` is `G.GAME.chips` as a readable string.
- `G.GAME.voucher_text` appears to be unused.
- `G.GAME.dollars` is the current money amount.
- `G.GAME.max_jokers` tracks Invisible Joker's unlock condition.
- `G.GAME.bankrupt_at` is set to -20 by Credit Card.
- `G.GAME.current_boss_streak` tracks the "most bosses in a row" statistic.
- `G.GAME.base_reroll_cost` is lowered by Reroll Surplus and Reroll Glut.
- `G.GAME.blind_on_deck` is the type of the "up next" blind ("Small", "Big", or "Boss").
- `G.GAME.sort` is the selected hand sorting method.
- `G.GAME.previous_round` appears to be unused.
- `G.GAME.previous_round.dollars` appears to be unused, but tracks the amount of money after the most recent cash out.
- `G.GAME.tags` holds the current tags.
- `G.GAME.tag_tally` is used to give each tag a unique ID number.
- `G.GAME.pool_flags` is used for Gros Michel/Cavendish.
- `G.GAME.used_jokers` holds currently spawned centers to avoid spawning duplicates.
- `G.GAME.used_vouchers` holds vouchers redeemed this run.
- `G.GAME.current_round` holds various transient numbers that rapidly change during gameplay.
- `G.GAME.round_resets` is used to reset `G.GAME.current_round`.
- `G.GAME.round_resets.blind_states` holds the skip status of each blind.
- `G.GAME.round_bonus` gives extra hands and discards for one round. Unused in vanilla.
- `G.GAME.shop.joker_max` holds the number of card slots in the shop.
- `G.GAME.cards_played` tracks playing card statistics.
- `G.GAME.hands` holds poker hand levels and their chip/mult values.