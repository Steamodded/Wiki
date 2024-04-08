# Creating new game objects
Steamodded features APIs for adding different kinds of game objects. Some of them are still new, so they might be unstable in some places. Below, you will find an overview on how to use them.
## Creating jokers
### Example
```lua
-- SMODS.Joker:new(name, slug, config, spritePos, loc_txt, rarity, cost, unlocked, discovered, blueprint_compat, eternal_compat, effect, atlas, soul_pos)
local j_example = SMODS.Joker:new('Example Joker', 'example', { mult = 10 }, {x=0,y=0}, {
    name = 'Example Joker',
    text = { '{C:red}+#1#{} Mult' }
}, 1, 2, true, false, true, true, 'Mult', 'my_mod_jokers')
j_example:register()
```
### Parameters
* `name`: Your Joker's name.
* `slug`: Your Joker's slug, used to index it in any tables it gets registered in. `j_` will automatically be prepended to this, so the actual slug will start with `j_j_` if you input a slug also starting with `j_`.
* `config`: Used for values specific to this Joker, and may allow you to use effects that already exist in the game's code.
* `spritePos`: The joker's position in its spritesheet. Defaults to position 0,0.
* `loc_txt`: The joker's description as it will show up in-game, with a `name` string and a `text` array. Each entry in `text` corresponds to one row of the description. Variables can be used with the format `#n#`, it is explained below how to provide them.
* `rarity`: An integer value between 1 (Common) and 4 (Legendary), to set the Joker's rarity.
* `cost`: The Joker's in-game base cost.
* `unlocked`: Whether this joker is unlocked by default. Specifying an unlock condition is not yet officially supported by Steamodded.
* `discovered`: Whether this joker is discovered by default.
* `blueprint_compat`: Whether the joker can be copied by Blueprint or Brainstorm. You need to account for this in the joker's effect additionally.
* `eternal_compat`: Whether the joker is allowed to be Eternal.
* `effect`: A string value that can be input to use certain base-game effects. You usually won't need it.
* `atlas`: You may specify a custom atlas for your joker. The loader will look for sprites that match the joker's slug automatically, but this option allows you to use one spritesheet for multiple jokers.
* `soul_pos`: Separate front layer sprite position, like for base game Hologram and Legendary jokers.

### Functions
After registering your joker, it is possible to further define its behavior by declaring these functions on the joker object.
```lua
function SMODS.Jokers.j_example.loc_def(card)
    return {card.ability.test}
end
G.localization.descriptions.Other['my_key'] = {
    name = 'My tooltip',
    text = {
        'Fancy text, and',
        'even more fancy text.',
        'Var 1: {C:attention}#1#' -- this will display 10
    }
}
function SMODS.Jokers.j_example.tooltip(card, info_queue)
    info_queue[#info_queue+1] = G.P_CENTERS.m_steel -- Tooltips for enhancements, editions, tags, etc.
    info_queue[#info_queue+1] = { set = 'Other', key = 'my_key', vars = {card.ability.mult} } -- Custom tooltips
end
function SMODS.Jokers.j_example.set_ability(card, initial, delay_sprites)
    card.ability.test = card.ability.mult
end
function SMODS.Jokers.j_example.calculate(card, context)
    if context.cardarea == G.jokers then
        return {
            message = localize{type='variable',key='a_mult',vars={self.ability.mult}},
            mult_mod = self.ability.mult
        }
    end
end
function SMODS.Jokers.j_example.set_badges(card, badges)
    badges[#badges+1] = create_badge('Custom Badge', HEX('FFFFFF'), HEX('000000'), 1.2)
end
```
* `loc_def` lets you provide localization variables for your joker description. Returning a second value (comma separated) will assign that value to main_end (this allows for compatibility displays like on Blueprint).
* `tooltip` is a separate function for Jokers only that allows you to create tooltips by modifying the `info_queue` table.
* `set_ability` lets you initialize any additional variables you need for your effect to work.
* `calculate` executes your joker's effect. To understand the different contexts you're able to use, it is recommended to have a look at the `Card:calculate_joker` function in the game's code.
* `set_badges` allows you to add or modify a Joker's badges (rarity display and editions show up as badges, usually). The `create_badge` function accepts 4 arguments: A label, a background color, a text color, and a text size.
* These functions are only ever executed when your joker is being processed. Thus, it is not needed to validate what joker they are called from.

## Creating consumables
### Examples
There are individual creation functions for each consumable type, though they are very similar.
```lua
-- SMODS.Planet:new(name, slug, config, pos, loc_txt, cost, cost_mult, effect, freq, consumeable, discovered, atlas)
local c_example_planet = SMODS.Planet:new('Example Planet', 'example_planet', { hand_type = 'Custom Hand Type' }, {x = 0, y = 0 }, nil, 3, 1, nil, nil, nil, nil, 'my_mod_tarot')
-- SMODS.Tarot:new(name, slug, config, pos, loc_txt, cost, cost_mult, effect, consumeable, discovered, atlas)
local c_example_tarot = SMODS.Tarot:new('Example Tarot', 'example_tarot', {}, { x = 1, y = 0 }, {
   name = 'Example Tarot',
   text = { 'Does nothing?' }
}, 3, 1, nil, nil, nil, 'my_mod_tarot')
-- SMODS.Spectral:new(name, slug, config, pos, loc_txt, cost, consumeable, discovered, atlas)
local c_example_spectral = SMODS.Spectral:new('Example Spectral', 'example_spectral', { mult = 4 }, { x = 2, y = 0 }, {
    name = 'Example Spectral',
    text = { 'Does nothing?', '{C:inactive}Or does it?' }
}, 4, nil, nil, 'my_mod_tarot')
c_example_planet:register()
c_example_tarot:register()
c_example_spectral:register()
```
### Parameters
* `name`: Your card's name.
* `slug`: Your card's slug, used to index it in any tables it gets registered in. `c_` will automatically be prepended to this, so the actual slug will start with `c_c_` if you input a slug also starting with `c_`.
* `config`: Used for values specific to this card, and may allow you to use effects that already exist in the game's code.
* `pos`: The card's position in its spritesheet. Defaults to position 0,0.
* `loc_txt`: The card's description as it will show up in-game, with a `name` string and a `text` array. Each entry in `text` corresponds to one row of the description. Variables can be used with the format `#n#`.
* `cost`: The card's shop cost.
* `cost_mult`: A cost multiplier, does not exist for spectrals and defaults to 1.
* `effect`: A string value that can be input to use certain base-game effects. Defaults to `'Hand Upgrade'` for planets, does not exist for spectrals.
* `freq`: Unused legacy value that exists only on planets for some reason. If you want to use it for something, maybe it will have a purpose.
* `consumeable`: Whether the card is consumeable (spoiler: yes, and it will probably not be functional if it isn't)
* `discovered`: Whether the card is discovered by default (default: false)
* `atlas`: Allows you to specify a custom atlas. Like with jokers, the loader still looks for a custom sprite sheet that matches the card's slug.

### Functions
For all consumable types, functions `use`, `can_use`, `loc_def`, and `set_badges` can be defined as shown below. Additionally, a `calculate` function to be called from `Card:calculate_joker()` can also be defined and is identical in usage to a Joker's `calculate` function.
```lua
function SMODS.Tarots.c_example_tarot.can_use(card)
    -- stop_use and whatnot are handled by the loader, so you don't need to worry about it
    return true
end
function SMODS.Tarots.c_example_tarot.use(card, area, copier)
    -- do something
end
function SMODS.Tarots.c_example_tarot.loc_def(center, info_queue)
    info_queue[#info_queue+1] = { set = 'Other', key = 'my_key' }
    return {}
end
function SMODS.Planets.c_example_planet.set_badges(card, badges)
    -- Override the default 'Planet' badge to have a different text
    badges[1] = create_badge('Exoplanet', G.C.SECONDARY_SET['Planet'], nil, 1.2)
end
function SMODS.Spectrals.c_example_spectral.calculate(card, context)
    if SMODS.end_calculate_context(context) then
        return {
            message = localize{type='variable',key='a_mult',vars={card.ability.mult}},
            mult_mod = card.ability.mult
        }
    end
end
```
The original function responsible for the usage of consumables will not be called if a `use` function has been declared. Tooltips can be made right inside `loc_def` for consumables due to them being processed differently. Note that this difference causes a Joker's `loc_def` function to be passed a `Card` object with an `ability` field, while all other such functions are passed a `center` object with a `config` table that includes similar information.

## Creating vouchers
### Example
```lua
-- SMODS.Voucher:new(name, slug, config, pos, loc_txt, cost, unlocked, discovered, available, requires, atlas)
local v_example = SMODS.Voucher:new('Example', 'example', { extra = 2 }, { x = 0, y = 0 }, {
    name = 'Example',
    text = { '{C:red}+#1#{} discards' },
}, 10, true, false, true, {'v_recyclomancy'}, 'my_mod_voucher')
v_example:register()
```

### Parameters
* `name`: Your voucher's name.
* `slug`: Your voucher's slug, used to index it in any tables it gets registered in. `v_` will automatically be prepended to this, so the actual slug will start with `v_v_` if you input a slug also starting with `v_`.
* `config`: Used for values specific to this voucher.
* `pos`: The voucher's position in its spritesheet. Defaults to position 0,0.
* `loc_txt`: The voucher's description as it will show up in-game, with a `name` string and a `text` array. Each entry in `text` corresponds to one row of the description. Variables can be used with the format `#n#`.
* `cost`: The voucher's shop cost.
* `unlocked`: Whether the voucher is unlocked by default. Unlock conditions are unsupported as of now, so the API will override this value with `true` for the time being.
* `discovered`: Whether the voucher is discovered by default (default: false)
* `available`: Does nothing. If you want to set this to false and manually make your voucher unavailable, why are you creating it in the first place?
* `requires`: A list of vouchers that must be redeemed first before this one can show up.
* `atlas`: Allows you to specify a custom atlas. Like with jokers, the loader still looks for a custom sprite sheet that matches the card's slug.

### Functions
Alongside `loc_def` and `set_badges` functions, which work identically to their consumable counterparts, custom vouchers can define a `redeem` function to be called when the voucher is redeemed:
```lua
function SMODS.Vouchers.v_example.loc_def(center, info_queue)
    return { center.config.extra }
end
function SMODS.Vouchers.v_example.redeem(center_table)
    -- center_table has 2 fields: name (the center's name) and extra (the extra field of the voucher config)
    G.GAME.round_resets.discards = G.GAME.round_resets.discards + center_table.extra
    ease_discard(center_table.extra)
end
```

## Creating seals and blinds
APIs for these game objects are also added, and this page will be completed with documentation for them soon.

# Modifying existing objects present in the base game
## Taking ownership
To use API functions with a vanilla Joker, Consumable, Voucher or Blind, you must first take ownership of it, providing its slug to the `take_ownership` function:
```lua
SMODS.Joker:take_ownership('jolly_joker'):register()
SMODS.Tarot:take_ownership('fool'):register()
-- and so on, you get the point
```
This only works for vanilla objects that have not been registered by a different mod. After doing this, you can use the object as if it were created by your mod through the API. Note that your mod badge will also be displayed on any vanilla objects you take ownership of.