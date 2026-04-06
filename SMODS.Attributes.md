# API Documentation: SMODS.Attribute
*(Added in 1531zeebee)*

Attributes are able to assigned to different center objects to allow for more advanced polling and effects that require certain attributes. SMODS provides an initial suite of attributes for the vanilla jokers, as well as a couple of empty ones for some scoring methods that the rest of the API provides.
- **Required parameters:**
	- `key`: *does not need to be unique - duplicate keys will be combined*
- **Optional parameters** *(defaults)*:
    - `keys`: Provide a table of keys of centers that have this attribute
    - `alias`: Provide a table of keys of other `SMODS.Attribute` objects that should be treated as the same attribute

If you want to apply attributes in object definitions, add `attributes = {'key1', 'key2', ...}` to the definition.

## Utility functions
- `SMODS.get_attribute_pool(attribute) -> table`
    - Takes a attribute key and returns a table of keys of centers that have that attribute
- `SMODS.add_attribute(attribute_key, object_keys)`
    - Inserts a table of keys into a pre-existing attribute
    - `attribute_key`: key of the attribute to insert into
    - `object_keys`: table of keys of centers to insert into the attribute
- `Card:has_attribute(attribute_key)` *(added in 1606b)*
    - Checks whether a card has a certain attribute or not *(respects aliases)
    - `attribute_key`: key of the attribute to check

# Provided Attributes

Detailed here is a list of attributes that SMODS provides, along with a criteria for what objects should have them. Below is a list of all vanilla jokers and which attributes they have been assigned.

## SMODS Attributes
| Attribute Key | When to use | Vanilla Jokers |
| ------------- | ----------- | -------------- |
| **mult** | gives +mult at some point of scoring | Joker, Greedy Joker, Lusty Joker, Wrathful Joker, Gluttonous Joker, Jolly Joker, Zany Joker, Crazy Joker, Mad Joker, Droll Joker, Half Joker, Ceremonial Dagger, Mystic Summit, Misprint, Raised Fist, Fibonacci, Abstract Joker, Gros Michel, Even Steven, Scholar, Supernova, Ride the Bus, Green Joker, Red Card, Erosion, Fortune Teller, Flash Card, Popcorn, Spare Trousers, Walkie Talkie, Smiley Face, Swashbuckler, Onyx Agate, Shoot the Moon, Bootstraps |
| **chips** | gives +chips at some point of scoring | Sly Joker, Wily Joker, Clever Joker, Devious Joker, Crafty Joker, Banner, Scary Face, Odd Todd, Scholar, Runner, Ice Cream, Blue Joker, Hiker, Square Joker, Stone Joker, Bull, Walkie Talkie, Castle, Arrowhead, Wee Joker, Stuntman |
| **xmult** | gives Xmult at some point of scoring | Joker Stencil, Loyalty Card, Steel Joker, Blackboard, Constellation, Cavendish, Card Sharp, Madness, Vampire, Hologram, Baron, Obelisk, Photograph, Lucky Cat, Baseball Card, Ancient Joker, Ramen, Campfire, Acrobat, Throwback, Bloodstone, Glass Joker, Flower Pot, The Idol, Seeing Double, Hit the Road, The Duo, The Trio, The Family, The Order, The Tribe, Driver's License, Canio, Triboulet, Yorick |
| **xchips** | gives Xchips at some point of scoring | *none* |
| **score** | gives +score at some point of scoring | *none* |
| **xscore** | gives Xscore at some point of scoring | *none* |
| **blindsize** | gives +blindsize at some point of scoring *(added in 1606b)* | *none* |
| **xblindsize** | gives Xblindsize at some point of scoring *(added in 1606b)* | *none* |
| **balance** | balances mult and chips during scoring *(added in 1606b)* | *none* |
| **swap** | swaps mult and chips during scoring *(added in 1606b)* | *none* |
| **retrigger** | retriggers a card at some point of scoring | Mime, Dusk, Hack, Seltzer, Sock and Buskin, Hanging Chad |
| **scaling** | scales a value on a trigger | Ceremonial Dagger, Seltzer, Ride the Bus, Egg, Runner, Ice Cream, Constellation, Green Joker, Red Card, Madness, Square Joker, Vampire, Hologram, Rocket, Turtle Bean, Obelisk, Flash Card, Lucky Cat, Popcorn, Spare Trousers, Ramen, Castle, Campfire, Throwback, Glass Joker, Wee Joker, Hit the Road, Canio, Yorick |
| **reset** | has a value that resets | Obelisk, Campfire, Hit the Road, Ride the Bus |
| **suit** | trigger is affected by a suit | Greedy Joker, Lusty Joker, Wrathful Joker, Gluttonous Joker, Smeared Joker, Castle, Ancient Joker, Seeing Double, Blackboard, Flower Pot, The Idol, Rough Gem, Bloodstone, Arrowhead, Onyx Agate |
| **diamonds** | trigger is affected by diamonds | Greedy Joker, Smeared Joker, Rough Gem |
| **hearts** | trigger is affected by hearts | Lusty Joker, Smeared Joker, Bloodstone |
| **spades** | trigger is affected by spades | Wrathful Joker, Smeared Joker, Arrowhead, Blackboard |
| **clubs** | trigger is affected by clubs | Gluttonous Joker, Smeared Joker, Onyx Agate, Seeing Double, Blackboard |
| **hand_type** | trigger is affected by a specific hand type | Jolly Joker, Zany Joker, Crazy Joker, Mad Joker, Droll Joker, Sly Joker, Wily Joker, Clever Joker, Devious Joker, Crafty Joker, Four Fingers, Supernova, Runner, Superposition, To Do List, Séance, Shortcut, Obelisk, Spare Trousers, The Duo, The Trio, The Family, The Order, The Tribe, Burnt Joker, Card Sharp, Space Joker |
| **rank** | trigger is affected by a specific rank | 8 Ball, Raised Fist, Fibonacci, Hack, Even Steven, Odd Todd, Scholar, Sixth Sense, Superposition, Cloud 9, Mail-In Rebate, Walkie Talkie, Wee Joker, The Idol, Hit the Road, Baron, Shoot the Moon, Triboulet |
| **ace** | trigger is affected by aces | Fibonacci, Odd Todd, Scholar, Superposition |
| **two** | trigger is affected by 2s | Fibonacci, Hack, Even Steven, Wee Joker |
| **three** | trigger is affected by 3s | Fibonacci, Hack, Odd Todd |
| **four** | trigger is affected by 4s | Hack, Even Steven, Walkie Talkie |
| **five** | trigger is affected by 5s | Fibonacci, Hack, Odd Todd |
| **six** | trigger is affected by 6s | Even Steven, Sixth Sense |
| **seven** | trigger is affected by 7s | Odd Todd |
| **eight** | trigger is affected by 8s | 8 Ball, Even Steven, Fibonacci |
| **nine** | trigger is affected by 9s | Odd Todd, Cloud 9 |
| **ten** | trigger is affected by 10s | Even Steven, Walkie Talkie |
| **jack** | trigger is affected by Jacks | Hit the Road |
| **queen** | trigger is affected by Queens | Shoot the Moon, Triboulet |
| **king** | trigger is affected by Kings | Baron, Triboulet |
| **face** | trigger is affected by face cards | Scary Face, Pareidolia, Business Card, Ride the Bus, Faceless Joker, Midas Mask, Photograph, Reserved Parking, Smiley Face, Sock and Buskin, Canio |
| **economy** | effect is based around money | Credit Card, Chaos the Clown, Delayed Gratification, Business Card, Egg, Faceless Joker, To Do List, Cloud 9, Rocket, Gift Card, Reserved Parking, Mail-In Rebate, To the Moon, Golden Joker, Trading Card, Golden Ticket, Rough Gem, Matador, Satellite |
| **generation** | generates another object on a trigger | Marble Joker, 8 Ball, DNA, Sixth Sense, Superposition, Séance, Riff-Raff, Vagabond, Hallucination, Diet Cola, Certificate, Invisible Joker, Cartomancer, Perkeo |
| **destroy_card** | destroys another card | Ceremonial Dagger, Madness, Trading Card |
| **hands** | effect is based around hands | Loyalty Card, Burglar, Troubadour, Dusk, Acrobat, DNA, Vagabond |
| **discard** | effect is based around discards | Banner, Mystic Summit, Delayed Gratification, Burglar, Faceless Joker, Green Joker, Mail-In Rebate, Drunkard, Trading Card, Ramen, Castle, Merry Andy, Hit the Road, Burnt Joker, Yorick |
| **hand_size** | effect is based around hand size | Juggler, Turtle Bean, Troubadour, Merry Andy, Stuntman |
| **chance** | effect has a chance to happen | 8 Ball, Gros Michel, Business Card, Space Joker, Cavendish, Hallucination, Reserved Parking, Bloodstone |
| **joker_slot** | related to Joker slots | Abstract Joker, Joker Stencil |
| **mod_chance** | affects other chance rolls | Oops! All 6s |
| **copying** | copies the effect of another card | Blueprint, Brainstorm |
| **full_deck** | effect is based on your full deck | Steel Joker, Cloud 9, Erosion, Stone Joker, Driver's License |
| **passive** | passive bonus from owning the card | Four Fingers, Credit Card, Chaos the Clown, Pareidolia, Splash, Shortcut, To the Moon, Juggler, Drunkard, Troubadour, Smeared Joker, Showman, Oops! All 6s, Astronomer |
| **joker** | related to Joker cards | Abstract Joker, Riff-Raff, Swashbuckler |
| **tarot** | related to Tarot cards | 8 Ball, Superposition, Vagabond, Hallucination, Fortune Teller, Cartomancer |
| **planet** | related to Planet cards | Astronomer, Constellation, Satellite |
| **spectral** | related to Spectral cards | Sixth Sense, Séance |
| **enhancements** | related to enhancements | Golden Ticket, Marble Joker, Steel Joker, Vampire, Midas Mask, Stone Joker, Lucky Cat, Glass Joker, Driver's License |
| **editions** | related to editions | *none* |
| **seals** | related to seals | Certificate |
| **editions** | related to editions *(added in 1606b)* | *none* |
| **tag** | related to tags *(added in 1606b)* | Diet Cola |
| **skip** | effect linked to skipping blinds *(added in 1606b)* | Throwback |
| **modify_card** | modifies playing cards | Pareidolia, Hiker, Vampire, Midas Mask |
| **perma_bonus** | permanently modifies the stats of cards *(added in 1606b)* | Hiker |
| **prevents_death** | effect prevents losing a run | Mr. Bones |
| **boss_blind** | effect linked to boss blinds *(added in 1606b)* | Luchador, Matador, Chicot |
| **reroll** | effect is based around rerolling the shop | Chaos the Clown, Flash Card |
| **on_sell** | triggers when card is sold | Luchador, Diet Cola, Invisible Joker |
| **sell_value** | effect is based around sell value of a card | Egg, Swashbuckler, Ceremonial Dagger, Gift Card |
| **skip** |  effect is based around skipping a blind | Throwback |
| **tag** |  effect is based around tags | Diet Cola |
| **boss_blind** | effect is based around boss blinds | Rocket, Luchador, Matador, Campfire, Chicot |
| **food** | themed on food | Gros Michel, Cavendish, Ice Cream, Ramen, Turtle Bean, Popcorn, Seltzer, Egg, Diet Cola |
| **space** | themed on space | Supernova, Space Joker, Constellation, Rocket, Satellite, Astronomer |

## Vanilla Joker Attributes

| Joker Name | Attributes |
| ---------- | ---------- |
| **Joker** | mult |
| **Greedy Joker** | mult, suit, diamonds |
| **Lusty Joker** | mult, suit, hearts |
| **Wrathful Joker** | mult, suit, spades |
| **Gluttonous Joker** | mult, suit, clubs |
| **Jolly Joker** | mult, hand_type |
| **Zany Joker** | mult, hand_type |
| **Mad Joker** | mult, hand_type |
| **Crazy Joker** | mult, hand_type |
| **Droll Joker** | mult, hand_type |
| **Sly Joker** | hand_type, chips |
| **Wily Joker** | hand_type, chips |
| **Clever Joker** | hand_type, chips |
| **Devious Joker** | hand_type, chips |
| **Crafty Joker** | hand_type, chips |
| **Half Joker** | mult |
| **Joker Stencil** | joker_slot, xmult |
| **Four Fingers** | hand_type, passive |
| **Mime** | retrigger |
| **Credit Card** | passive, economy |
| **Ceremonial Dagger** | mult, destroy_card, sell_value, scaling |
| **Banner** | discard, chips |
| **Mystic Summit** | mult, discard |
| **Marble Joker** | enhancements, generation |
| **Loyalty Card** | xmult, hands |
| **8 Ball** | chance, eight, tarot, generation, rank |
| **Misprint** | mult |
| **Dusk** | retrigger, hands |
| **Raised Fist** | mult, rank |
| **Chaos the Clown** | reroll, passive, economy |
| **Fibonacci** | three, mult, ace, eight, two, rank, five |
| **Steel Joker** | xmult, full_deck, enhancements |
| **Scary Face** | chips, face |
| **Abstract Joker** | joker_slot, mult, joker |
| **Delayed Gratification** | discard, economy |
| **Hack** | three, retrigger, four, two, rank, five |
| **Pareidolia** | modify_card, passive, face |
| **Gros Michel** | chance, mult, food |
| **Even Steven** | mult, ten, four, eight, two, six, rank |
| **Odd Todd** | three, ace, seven, chips, nine, rank, five |
| **Scholar** | mult, ace, chips, rank |
| **Business Card** | chance, face, economy |
| **Supernova** | mult, hand_type, space |
| **Ride the Bus** | mult, face, reset, scaling |
| **Space Joker** | chance, hand_type, space |
| **Egg** | food, sell_value, scaling, economy |
| **Burglar** | discard, hands |
| **Blackboard** | xmult, suit, spades, clubs |
| **Runner** | hand_type, chips, scaling |
| **Ice Cream** | food, chips, scaling |
| **DNA** | generation, hands |
| **Splash** | passive |
| **Blue Joker** | chips |
| **Sixth Sense** | spectral, six, generation, rank |
| **Constellation** | xmult, planet, space, scaling |
| **Hiker** | modify_card, chips, perma_bonus |
| **Faceless Joker** | discard, face, economy |
| **Green Joker** | mult, discard, scaling |
| **Superposition** | ace, hand_type, tarot, generation, rank |
| **To Do List** | hand_type, economy |
| **Cavendish** | xmult, chance, food |
| **Card Sharp** | xmult, hand_type |
| **Red Card** | mult, scaling |
| **Madness** | xmult, destroy_card, scaling |
| **Square Joker** | chips, scaling |
| **Séance** | spectral, hand_type, generation |
| **Riff-Raff** | joker, generation |
| **Vampire** | xmult, modify_card, enhancements, scaling |
| **Shortcut** | hand_type, passive |
| **Hologram** | xmult, scaling |
| **Vagabond** | tarot, generation, hands |
| **Baron** | xmult, rank, king |
| **Cloud 9** | full_deck, nine, rank, economy |
| **Rocket** | space, scaling, economy, boss_blind |
| **Obelisk** | xmult, hand_type, reset, scaling, hands |
| **Midas Mask** | modify_card, enhancements, face |
| **Luchador** | on_sell, boss_blind |
| **Photograph** | xmult, face |
| **Gift Card** | sell_value, economy |
| **Turtle Bean** | food, hand_size, scaling |
| **Erosion** | mult, full_deck |
| **Reserved Parking** | chance, face, economy |
| **Mail-In Rebate** | discard, rank, economy |
| **To the Moon** | passive, economy |
| **Hallucination** | chance, tarot, generation |
| **Fortune Teller** | mult, tarot |
| **Juggler** | hand_size, passive |
| **Drunkard** | discard, passive |
| **Stone Joker** | full_deck, enhancements, chips |
| **Golden Joker** | economy |
| **Lucky Cat** | xmult, enhancements, scaling |
| **Baseball Card** | xmult |
| **Bull** | chips |
| **Diet Cola** | on_sell, food, generation, tag |
| **Trading Card** | destroy_card, discard, economy |
| **Flash Card** | mult, reroll, scaling |
| **Popcorn** | mult, food, scaling |
| **Spare Trousers** | mult, hand_type, scaling |
| **Ancient Joker** | xmult, suit |
| **Ramen** | xmult, food, discard, scaling |
| **Walkie Talkie** | mult, ten, four, chips, rank |
| **Seltzer** | retrigger, food, scaling |
| **Castle** | suit, discard, chips, scaling |
| **Smiley Face** | mult, face |
| **Campfire** | xmult, reset, scaling, boss_blind |
| **Golden Ticket** | enhancements, economy |
| **Mr. Bones** | prevents_death |
| **Acrobat** | xmult, hands |
| **Sock and Buskin** | retrigger, face |
| **Swashbuckler** | mult, joker, sell_value |
| **Troubadour** | hand_size, passive, hands |
| **Certificate** | seals, generation |
| **Smeared Joker** | suit, hearts, passive, diamonds, spades, clubs|
| **Throwback** | xmult, scaling, skip |
| **Hanging Chad** | retrigger |
| **Rough Gem** | suit, diamonds, economy |
| **Bloodstone** | xmult, chance, suit, hearts |
| **Arrowhead** | suit, chips, spades |
| **Onyx Agate** | mult, suit, clubs |
| **Glass Joker** | xmult, enhancements, scaling |
| **Showman** | passive |
| **Flower Pot** | xmult, suit, hands |
| **Blueprint** | copying |
| **Wee Joker** | two, chips, rank, scaling |
| **Merry Andy** | hand_size, discard |
| **Oops! All 6s** | mod_chance, passive |
| **The Idol** | xmult, suit, rank |
| **Seeing Double** | xmult, suit, clubs |
| **Matador** | economy, boss_blind |
| **Hit the Road** | xmult, jack, discard, reset, rank, scaling |
| **The Duo** | xmult, hand_type |
| **The Trio** | xmult, hand_type |
| **The Family** | xmult, hand_type |
| **The Order** | xmult, hand_type |
| **The Tribe** | xmult, hand_type |
| **Stuntman** | hand_size, chips |
| **Invisible Joker** | on_sell, generation |
| **Brainstorm** | copying |
| **Satellite** | planet, space, economy |
| **Shoot the Moon** | mult, rank, queen |
| **Driver's License** | xmult, full_deck, enhancements |
| **Cartomancer** | tarot, generation |
| **Astronomer** | planet, passive, space |
| **Burnt Joker** | hand_type, discard |
| **Bootstraps** | mult |
| **Canio** | xmult, face, scaling |
| **Triboulet** | xmult, rank, queen, king |
| **Yorick** | xmult, discard, scaling |
| **Chicot** | boss_blind | 
| **Perkeo** | generation | 
