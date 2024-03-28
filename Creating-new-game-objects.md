# Creating new game objects
Steamodded features APIs for adding different kinds of game objects. Some of them are still new, so they might be unstable in some places. Below, you will find an overview on how to use them.
## Creating jokers
### Example
```lua
-- SMODS.Joker:new(name, slug, config, spritePos, loc_txt, rarity, cost, unlocked, discovered, blueprint_compat, eternal_compat, effect, atlas)
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
* `atlas`: You may specify a custom atlas for your joker. The loader will look for sprites that match the joker's slug automatically, but this option allows you to use one spritesheet for multiple jokers.

### Functions
After registering your joker, it is possible to further define its behavior by declaring these functions on the joker object.
```lua
function SMODS.Jokers.j_example:loc_def(card)
    if card.ability.name == 'Example Joker' then
        return {card.ability.test}
    end
end
function SMODS.Jokers.j_example:set_ability(card, initial, delay_sprites)
    if card.ability.name == 'Example Joker' then
        card.ability.test = card.ability.mult
    end
end
function SMODS.Jokers.j_example:calculate(card, context)
    if (card.ability.name == 'Example Joker') and (context.cardarea == G.jokers) then
        return {
            message = localize{type='variable',key='a_mult',vars={self.ability.mult}},
            mult_mod = self.ability.mult
        }
    end
end
```
* `loc_def` lets you provide localization variables for your joker description. Returning a second value (comma separated) will assign that value to main_end (this allows for compatibility displays like on Blueprint).
* `set_ability` lets you initialize any additional variables you need for your effect to work.
* `calculate` executes your joker's effect. To understand the different contexts you're able to use, it is recommended to have a look at the `Card:calculate_joker` function in the game's code.
* For each function, it is **required** to check for the joker's name, as each function defined this way will be called in the appropriate context. This was done to ensure modders can easily define joker effects in bulk without having to define functions for each joker individually.

## Creating consumables
There are individual creation functions for each consumable type, though they are very similar.
```lua
-- SMODS.Planet:new(name, slug, config, pos, loc_txt, cost, cost_mult, effect, freq, consumeable, discovered, atlas)
local c_example_planet = SMODS.Planet:new('Example Planet', 'example_planet', { hand_type = 'Custom Hand Type' }, {x = 0, y = 0 }, nil, 3, 1, nil, nil, nil, nil, 'my_mod_tarot')
-- SMODS.Tarot:new(name, slug, config, pos, loc_txt, cost, cost_mult, effect, consumeable, discovered, atlas)
local c_example_tarot = SMODS.Tarot:new('Example Tarot', 'example_tarot', { x = 1, y = 0 }, {
   name = 'Example Tarot',
   text = { 'Does nothing?' }
}, 3, 1, nil, nil, nil, 'my_mod_tarot')
-- SMODS.Spectral:new(name, slug, config, pos, loc_txt, cost, consumeable, discovered, atlas)
local c_example_spectral = SMODS.Spectral:new('Example Spectral', 'example_spectral', { x = 2, y = 0}, {
    name = 'Example Spectral',
    text = { 'Does nothing?' }
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
* `freq`: A weight value for planet frequency, defaults to 1 (this is the value *every* Planet in the base game uses)
* `consumeable`: Whether the card is consumeable (spoiler: yes, and it will probably not be functional if it isn't)
* `discovered`: Whether the card is discovered by default (default: false)
* `atlas`: Allows you to specify a custom atlas. Like with jokers, the loader still looks for a custom sprite sheet that matches the card's slug.

### Functions
For all consumable types, functions `use` and `can_use` can be defined with the following headers:
```lua
function SMODS.Tarots.c_example_tarot:can_use(card)
    if card.ability.name == 'Example Tarot' then
        return true
    end
end
function SMODS.Tarots.c_example_tarot:use(card, area, copier)
    if card.ability.name == 'Example Tarot' then
        -- do something
    end
end
```
For Tarots and Spectrals, a `loc_def` function is also recognized and works the same way as it does for jokers. Planets are not expected to need this functionality and get assigned the variables they normally need automatically.

## Creating vouchers, seals and blinds
APIs for these game objects are also added, and this page will be completed with documentation for them soon.