_This guide is missing any contexts added by RetriggerAPI_

# __Evaluate play flow__
### 1. Populate `scoring_hand` with cards that are scored
### 2. Get base `hand_chips` and `mult` from the played **poker hand**
### 3. For each joker, call `eval_card` with context:
```lua
cardarea = G.jokers
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
before = true
-- This evaluation call looks for `level_up` effects
```
### 4. Reset `hand_chips` and `mult` based off any `level_up` effects
### 5. Check to see if a **blind** affects the base mult and chips and set accordingly
### 6. Iterate through each card in the `scoring_hand`
a) if the card is debuffed, stop

b) call `eval_card` with context:
```lua      
repetition_only = true
cardarea = G.play
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
repetition = true
-- This evaluation call looks for `repetitions` effects in **seals***
```
c) iterate through `G.jokers.cards` calling `eval_card` with context:
```lua
cardarea = G.play
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
other_card = scoring_hand[i] -- this card is the current playing card
repetition = true
-- This evaluation call looks for `repetitions` effects in **jokers**
```
d) for each `repetition`
+ call `eval_card` with context:
    ```lua
    cardarea = G.play
    full_hand = G.play.cards
    scoring_hand = scoring_hand
    scoring_name = text
    -- This evaluation finds base values in the playing card or edition and is saved in `effects`
    ```
+ iterate through `G.jokers.cards` calling `calculate_joker` with context:
    ```lua
    cardarea = G.play
    full_hand = G.play.cards
    scoring_hand = scoring_hand
    scoring_name = text
    poker_hands = poker_hands
    other_card = scoring_hand[i] -- this card is the current playing card
    individual = true
    -- Checks for effects on individual cards in played hand
    ```
+ iterate through `effects` and look for:
    ```lua
    chips
    mult
    p_dollars
    dollars
    extra.mult_mod
    extra.chip_mod
    extra.swap
    extra.func
    x_mult
    edition.chip_mod
    edition.mult_mod
    edition.x_mult_mod
    ```
### 7. Iterate through each card in `G.hand.cards`
a) establish the repetition loop `reps`

b) call `eval_card` with context:
```lua
cardarea = G.hand
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
-- evaluates any scoring effects from a card, saved in `effects` (this might be enhancement calc)
```
c) iterate through `G.jokers.cards` calling `calculate_joker` with context:
```lua
cardarea = G.hand
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
other_card = G.hand.cards[i]
individual = true
-- This evaluation checks for joker effects on cards held in the **hand** saved in `effects`
```
d) begin checks for hand doubling
+ call `eval_card` with context:
    ```lua
    repetition_only = true
    cardarea = G.hand
    full_hand = G.play.cards
    scoring_hand = scoring_hand
    socring_name = text
    poker_hands = poker_hands
    repetition = true
    card_effects = effects
    -- This evaluation checks for `repetitions` effects in **seals**
    ```
+ iterate through `G.jokers.cards` calling `eval_card` with context:
    ```lua
    cardarea = G.hand
    full_hand = G.play.cards
    scoring_hand = scoring_hand
    scoring_name = text
    poker_hands = poker_hands
    other_card = G.hand.cards[i]
    repetition - true
    card_effects = effects
    -- This evaluation checks for `repetitions` effects in **jokers**
    ```
e) iterate through `effects` and look for:
```lua
dollars
h_mult
x_mult
message
```
### 8. Iterate through each card in `G.jokers.cards` and `G.consumeables.cards`
a) call `eval_card` with the context:
```lua
cardarea = G.jokers
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
edition = true
-- This evaluation checks for `chip_mod` and `mult_mod` from **editions**
```
b) call `eval_card` with context:
```lua
cardarea = G.jokers
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
joker_main = true
-- This evaluation checks for `mult_mod`, `chip_mod` and `Xmult_mod` from **jokers**
```
c) iterate through each card in `G.jokers.cards` and call `calculate_joker` with context:
```lua
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
other_joker = _card
-- This evaluation checks for `mult_mod`, `chip_mod` and `Xmult_mod` from **joker** on **joker** interactions
```
d) check for any `x_mult_mod` in `edition_effects` from **8a**
### 9. Call `G.GAME.selected_back:trigger_effect` with context `final_scoring_step`
### 10. Set chips and mult accordingly
### 11. Iterate through `scoring_hand`
a) iterate through `G.jokers.cards` and call `calculation_joker` with context:
```lua
destroying_card = scoring_hand[i]
full_hand = G.play.cards
-- This evaluation checks to see if a **joker** destroys a played card
```
b) Glass card calculation

c) set `card.destroyed` as `true` and populate `cards_destroyed`
### 12. Iterate through `G.jokers.cards` and call `eval_card` with context:
```lua
cardarea = G.jokers
remove_playing_cards = true
removed = cards_destroyed
-- This evaluation checks to see if a **joker** has an effect on a removed card
```
### 13. Remove destroyed cards
### 14. **IF** the hand is debuffed
a) set `mult` and `hand_chips` to 0

b) iterate through `G.jokers.cards` calling `eval_card` with context:
```lua
cardarea = G.jokers
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
debuffed_hand = true
-- This evaluation checks to see if a **joker** has an effect on playing a debuffed hand
```
### 15. Multiply the `hand_chips` and `mult` and add to the current score
### 16. Iterate through `G.jokers.cards` calling `eval_card` with context:
```lua
cardarea = G.jokers
full_hand = G.play.cards
scoring_hand = scoring_hand
scoring_name = text
poker_hands = poker_hands
after = true
-- This evaluation checks for **joker** effects after the hand is scored
```

# Other joker calculations
## End of round
1) Iterate through `G.jokers.cards` calling `calculate_joker` with context:```
end_of_round = true
game_over = game_over -- true or false``` *This evaluation checks for `saved` effects*
**rental** and **perishable** calculations also happen here
2) If the game is not over, iterate through `G.hand.cards`
    i) establish the repetition loop `reps`
    ii) calculate `get_end_of_round_effect` on the current card with no context
        *This evaluation looks for `h_dollars`*
    iii) call `eval_card` with context:```
end_of_round = true
cardarea = G.hand
repetition = true
repetition_only = true``` *This evaluation looks for `repetitions` effects from **seals***

    iv) call `eval_card` with context:```
cardarea = G,hand
other_card = G.hand.cards[i]
repetition = true
end_of_round = true
card_effects = effects``` *This evaluation looks for `repetitions` effects from **jokers***

    v) iterate through `effects` and look for:```
h_dollars
extra```

## Discard cards from highlighted
1) iterate through `G.hand.cards` calling `eval_card` with context:```
pre_discard = true
full_hand = G.hand.highlighted
hook = hook``` *This evaluation looks for **cards** that do something to a discarded hand before it is discarded*
2) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
pre_discard = true
full_hand = G.hand.highlighted
hook = hook``` *This evaluation looks for **jokers** that do something to a discarded hand before it is discarded*
3)  iterate through `G.hand.cards` calling `eval_card` with context:```
discard = true
full_hand = G.hand.highlighted``` *This evaluation looks for `remove` effects from **cards** when it is discarded*
4) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
discard = true
other_card = G.hand.highlighted[i]
full_hand = G.hand.highlighted``` *This evaluation looks for `remove` effects from **jokers** when a card is discarded*
5) if there are any **destroyed** cards in the discarded cards, call `calculate_joker` with context:```
cardarea = G.jokers
remove_playing_cards = true
removed = destroyed_cards``` *This evaluation checks to see if a **joker** has an effect on a removed card*
## New round
1) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
setting_blind = true
blind = G.GAME.round_resets.blind``` *This evaluation checks to see if a **joker** has an effect when a blind is selected
## Use consumeable
1) When a consumeable removes a card, iterate through `G.jokers.cards` calling `calculate_joker` with contet:```
remove_playing_cards = true
removed = destroyed_cards```
## Open a booster
1) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
open_booster = true
card = self```
## Redeem voucher
1) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
buying_card = true
card = self```
## Calculate joker
1) if joker is *Blueprint* or *Brainstorm* call `calculate_joker` with the same context
## Update draw to hand
1) on the first hand of a round, iterate through `G.jokers.cards` calling `calculate_joker` with context `first_hand_drawn = true`
## Use card
1) If card is consumeable, iterate through `G.jokers.cards` calling `calculate_joker` with context:```
using_consumeable = true
consumeable = card```
## Sell joker
1) When a joker is sold, call `calculate_joker` with context `selling_self = true`
## Sell card
1) If selling card, iterate through `G.jokers.cards` calling `calculate_joker` with context:```
selling_card = true
card = card```
## Buy from shop
1) When buying a joker, call `calculate_joker` with context:```
buying_card = true
card = c1```
2) iterate through `G.jokers.cards` calling `calculate_joker` with context:```
buying_card = true
card = c1```
## Toggle shop
1) If leaving the shop, iterate through `G.jokers.cards` calling `calculate_joker` with context `ending_shop = true`
## Reroll shop
1) If rerolling the shop, iterate through `G.jokers.cards` calling `calculate_joker` with context `reroll_shop = true`
## Skip booster
1) If skipping a booster pack, iterate through `G.jokers.cards` calling `calculate_joker` with context `skipping_booster = true`
## Skip blind
1) If skipping a blind, iterate through `G.jokers.cards` calling `calculate_joker` with context `skip_blind = true`
## Playing card added
1) When adding a playing card, iterate through `G.jokers.cards` calling `calculate_joker` with context:```
playing_card_added = true
cards = cards```