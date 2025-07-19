
# Permanent bonuses
Card objects can be given permanent permanent bonuses that allow them to add or subtract score, similar to the vanilla Hiker joker. These are only considered on **playing cards** during the scoring phases. These will not be changed by applying enhancements, copying the card, or similar. Steamodded by default handles all the UI elements for this. These were added in `1.0.0~ALPHA-1428c-STEAMODDED`.

## List of all perma-bonuses
```lua
perma_bonus,      -- permanent chips, from vanilla
perma_mult,
perma_x_chips,
perma_x_mult,

perma_h_chips,
perma_h_mult,
perma_h_x_chips,
perma_h_x_mult,

perma_p_dollars,  -- money on scoring
perma_h_dollars,  -- money on held at end of round (like gold cards)

perma_repetitions, -- retriggers in any context
```

## Re-implementation of Hiker
This function is an example of how to use perma-bonuses in smods, based on the vanilla Hiker joker. See [Calculate Functions](https://github.com/Steamodded/smods/wiki/Calculate-Functions) for more information about `calculate`.
```lua
SMODS.Joker{
    key = "hiker2",
    ...,
    calculate = function(self, card, context)
        if context.individual and context.cardarea == G.play then
            context.other_card.ability.perma_bonus = context.other_card.ability.perma_bonus or 0
            context.other_card.ability.perma_bonus = context.other_card.ability.perma_bonus + card.ability.extra
            return {
                extra = { message = localize('k_upgrade_ex'), colour = G.C.CHIPS },
                card = card
            }
        end
    end
}
```

## Implementation details
Permanent bonuses get added when the playing card gets scored. They happen at the same time as base chips and enhancements, before any edition effects. Permanent bonuses do not change when the player applies enhancements, copies the card, or similar.

Permanent bonuses are scored in the following order:
1. chips (base + enhancement + permanent)
2. mult (enhancement + permanent)
3. xchips (enhancement * permanent)
4. xmult (enhancement * permanent)
5. dollars (seals + permanent)
6. all edition effects
7. all joker effects

Permanent (held) chips get scored at the same time as a playing card's base chips and chips from enhancements. They also show up as a combined number with bonus chips from enhancements in the UI. This is inherited vanilla behaviour. Supports negative values.

Permanent (held) mult gets scored at the same time as a playing card's regular mult and bonus mult from enhancements. It also shows up as a combined number with bonus mult from enhancements. Supports negative values.

Permanent (held) xchips get multiplied with enhancement xchips, showing as a single multiplied number during scoring. Does not support final negative xchips, and will do nothing if end result is negative.

Permanent xmult gets multiplied with enhancement xmult such as glass when scoring, showing as a single multiplied number during scoring. It does show up as a seperate number in the UI when hovering over the card. Does not support final negative xmult, and will do nothing if end result is negative.

Permanent held xmult gets multiplied with enhancement held xmult such as steel when scoring, showing as a single multiplied number during scoring. It does show up as a seperate number in the UI when hovering over the card. It does not support negative values, and will do nothing if scored.

Permanent held dollars only give money on end of round, similar to the gold enhancement.

Permanent repetitions retrigger the card in any context, both when scored or when in hand (Gold cards, Blue seals, etc.).

## Localization
Steamodded by default handles the localization of all perma-bonuses described on this page. These can be overwritten (or translated) by defining:
```lua
card_extra_chips,
card_extra_mult,
card_extra_x_chips,
card_extra_x_mult,

card_extra_h_chips,
card_extra_h_mult,
card_extra_h_x_chips,
card_extra_h_x_mult,

card_extra_p_dollars,
card_extra_h_dollars,

card_extra_repetitions,
```
Simplify define an entry under `descriptions.Other` (see [Localization](https://github.com/Steamodded/smods/wiki/Localization) for more information) such as:
```lua
            card_extra_chips={
                text={
                    "{C:chips}#1#{} extra chips",
                },
            },
```
