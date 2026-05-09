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

Detailed here is a list of attributes that SMODS provides, along with a criteria for what objects should have them. Below is a list of all vanilla objects and which attributes they have been assigned.

## SMODS Attributes
| Attribute Key | When to use | Vanilla Objects |
| ------------- | ----------- | -------------- |
| **mult** | gives +mult at some point of scoring or causes other cards to do so | **Jokers**<br>Joker, Greedy Joker, Lusty Joker, Wrathful Joker, Gluttonous Joker, Jolly Joker, Zany Joker, Crazy Joker, Mad Joker, Droll Joker, Half Joker, Ceremonial Dagger, Mystic Summit, Misprint, Raised Fist, Fibonacci, Abstract Joker, Gros Michel, Even Steven, Scholar, Supernova, Ride the Bus, Green Joker, Red Card, Erosion, Fortune Teller, Flash Card, Popcorn, Spare Trousers, Walkie Talkie, Smiley Face, Swashbuckler, Onyx Agate, Shoot the Moon, Bootstraps<br><br>**Enhancements**<br>Mult Cards, Bonus Cards<br><br>**Editions**<br>Holographic |
| **chips** | gives +chips at some point of scoring or causes other cards to do so | **Jokers**<br>Sly Joker, Wily Joker, Clever Joker, Devious Joker, Crafty Joker, Banner, Scary Face, Odd Todd, Scholar, Runner, Ice Cream, Blue Joker, Hiker, Square Joker, Stone Joker, Bull, Walkie Talkie, Castle, Arrowhead, Wee Joker, Stuntman<br><br>**Enhancements**<br>Bonus Cards, Stone Cards<br><br>**Editions**<br>Foil |
| **xmult** | gives Xmult at some point of scoring or causes other cards to do so | **Jokers**<br>Joker Stencil, Loyalty Card, Steel Joker, Blackboard, Constellation, Cavendish, Card Sharp, Madness, Vampire, Hologram, Baron, Obelisk, Photograph, Lucky Cat, Baseball Card, Ancient Joker, Ramen, Campfire, Acrobat, Throwback, Bloodstone, Glass Joker, Flower Pot, The Idol, Seeing Double, Hit the Road, The Duo, The Trio, The Family, The Order, The Tribe, Driver's License, Canio, Triboulet, Yorick<br><br>**Enhancements**<br>Glass Cards, Steel Cards<br><br>**Editions**<br>Polychrome<br><br>**Vouchers**<br>Observatory |
| **xchips** | gives Xchips at some point of scoring or causes other cards to do so | *none* |
| **score** | gives +score at some point of scoring or causes other cards to do so | *none* |
| **xscore** | gives Xscore at some point of scoring or causes other cards to do so | *none* |
| **blindsize** | gives +blindsize at some point of scoring or causes other cards to do so *(added in 1606b)* | *none* |
| **xblindsize** | gives Xblindsize at some point of scoring or causes other cards to do so *(added in 1606b)* | *none* |
| **balance** | balances mult and chips during scoring or causes other cards to do so *(added in 1606b)* | *none* |
| **swap** | swaps mult and chips during scoring or causes other cards to do so *(added in 1606b)* | *none* |
| **retrigger** | retriggers a card at some point of scoring | **Jokers**<br>Mime, Dusk, Hack, Seltzer, Sock and Buskin, Hanging Chad<br><br>**Seals**<br>Red Seal |
| **scaling** | scales a value on a trigger | **Jokers**<br>Ceremonial Dagger, Seltzer, Ride the Bus, Egg, Runner, Ice Cream, Constellation, Green Joker, Red Card, Madness, Square Joker, Vampire, Hologram, Rocket, Turtle Bean, Obelisk, Flash Card, Lucky Cat, Popcorn, Spare Trousers, Ramen, Castle, Campfire, Throwback, Glass Joker, Wee Joker, Hit the Road, Canio, Yorick |
| **reset** | has a value that resets | **Jokers**<br>Obelisk, Campfire, Hit the Road, Ride the Bus |
| **suit** | trigger is affected by a suit | **Jokers**<br>Greedy Joker, Lusty Joker, Wrathful Joker, Gluttonous Joker, Smeared Joker, Castle, Ancient Joker, Seeing Double, Blackboard, Flower Pot, The Idol, Rough Gem, Bloodstone, Arrowhead, Onyx Agate<br><br>**Consumables**<br>The Star, The Moon, The Sun, The World, Sigil<br><br>**Enhancements**<br>Wild Cards<br><br>**Boss Blinds**<br>The Club, The Goad, The Head, The Window |
| **diamonds** | trigger is affected by diamonds | **Jokers**<br>Greedy Joker, Smeared Joker, Rough Gem<br><br>**Consumables**<br>The Star<br><br>**Boss Blinds**<br>The Window |
| **hearts** | trigger is affected by hearts | **Jokers**<br>Lusty Joker, Smeared Joker, Bloodstone<br><br>**Consumables**<br>The Sun<br><br>**Boss Blinds**<br>The Head |
| **spades** | trigger is affected by spades | **Jokers**<br>Wrathful Joker, Smeared Joker, Arrowhead, Blackboard<br><br>**Consumables**<br>The World<br><br>**Boss Blinds**<br>The Goad |
| **clubs** | trigger is affected by clubs | **Jokers**<br>Gluttonous Joker, Smeared Joker, Onyx Agate, Seeing Double, Blackboard<br><br>**Consumables**<br>The Moon<br><br>**Boss Blinds**<br>The Club |
| **hand_type** | trigger is affected by a specific hand type | **Jokers**<br>Jolly Joker, Zany Joker, Crazy Joker, Mad Joker, Droll Joker, Sly Joker, Wily Joker, Clever Joker, Devious Joker, Crafty Joker, Four Fingers, Supernova, Runner, Superposition, To Do List, Séance, Shortcut, Obelisk, Spare Trousers, The Duo, The Trio, The Family, The Order, The Tribe, Burnt Joker, Card Sharp, Space Joker<br><br>**Consumables**<br>All vanilla Planet Cards<br><br>**Vouchers**<br>Telescope, Observatory<br><br>**Boss Blinds**<br>The Ox, The Mouth, The Eye |
| **hand_level** | effect upgrades or downgrades poker hands | **Jokers**<br>Space Joker, Burnt Joker<br><br>**Consumables**<br>All vanilla Planet Cards<br><br>**Tags**<br>Orbital Tag<br><br>**Boss Blinds**<br>The Arm |
| **rank** | trigger is affected by a specific rank | **Jokers**<br>8 Ball, Raised Fist, Fibonacci, Hack, Even Steven, Odd Todd, Scholar, Sixth Sense, Superposition, Cloud 9, Mail-In Rebate, Walkie Talkie, Wee Joker, The Idol, Hit the Road, Baron, Shoot the Moon, Triboulet<br><br>**Consumables**<br>Strength, Familiar, Grim, Incantation, Ouija |
| **ace** | trigger is affected by aces | **Jokers**<br>Fibonacci, Odd Todd, Scholar, Superposition<br><br>**Consumables**<br>Grim |
| **two** | trigger is affected by 2s | **Jokers**<br>Fibonacci, Hack, Even Steven, Wee Joker<br><br>**Consumables**<br>Incantation |
| **three** | trigger is affected by 3s | **Jokers**<br>Fibonacci, Hack, Odd Todd<br><br>**Consumables**<br>Incantation |
| **four** | trigger is affected by 4s | **Jokers**<br>Hack, Even Steven, Walkie Talkie<br><br>**Consumables**<br>Incantation |
| **five** | trigger is affected by 5s | **Jokers**<br>Fibonacci, Hack, Odd Todd<br><br>**Consumables**<br>Incantation |
| **six** | trigger is affected by 6s | **Jokers**<br>Even Steven, Sixth Sense<br><br>**Consumables**<br>Incantation |
| **seven** | trigger is affected by 7s | **Jokers**<br>Odd Todd<br><br>**Consumables**<br>Incantation |
| **eight** | trigger is affected by 8s | **Jokers**<br>8 Ball, Even Steven, Fibonacci<br><br>**Consumables**<br>Incantation |
| **nine** | trigger is affected by 9s | **Jokers**<br>Odd Todd, Cloud 9<br><br>**Consumables**<br>Incantation |
| **ten** | trigger is affected by 10s | **Jokers**<br>Even Steven, Walkie Talkie<br><br>**Consumables**<br>Incantation |
| **jack** | trigger is affected by Jacks | **Jokers**<br>Hit the Road<br><br>**Consumables**<br>Familiar |
| **queen** | trigger is affected by Queens | **Jokers**<br>Shoot the Moon, Triboulet<br><br>**Consumables**<br>Familiar |
| **king** | trigger is affected by Kings | **Jokers**<br>Baron, Triboulet<br><br>**Consumables**<br>Familiar |
| **face** | trigger is affected by face cards | **Jokers**<br>Scary Face, Pareidolia, Business Card, Ride the Bus, Faceless Joker, Midas Mask, Photograph, Reserved Parking, Smiley Face, Sock and Buskin, Canio<br><br>**Boss Blinds**<br>The Mark, The Mouth |
| **economy** | effect is based around money | **Jokers**<br>Credit Card, Chaos the Clown, Delayed Gratification, Business Card, Egg, Faceless Joker, To Do List, Cloud 9, Rocket, Gift Card, Reserved Parking, Mail-In Rebate, To the Moon, Golden Joker, Trading Card, Golden Ticket, Rough Gem, Matador, Satellite, Astronomer<br><br>**Consumables**<br>The Hermit, Temperance, Immolate<br><br>**Vouchers**<br>Clearance Sale, Liquidation, Reroll Surplus, Reroll Glut, Seed Money, Money Tree<br><br>**Tags**<br>Investment Tag, Handy Tag, Garbage Tag, Coupon Tag, D6 Tag, Speed Tag, Economy Tag<br><br>**Enhancements**<br>Gold Cards, Lucky Cards<br><br>**Seals**<br>Gold Seal |
| **lose_economy** | effect is based around *losing* money | **Consumables**<br>Wraith<br><br>**Boss Blinds**<br>The Ox, The Tooth |
| **generation** | generates another object on a trigger | **Jokers**<br>Marble Joker, 8 Ball, DNA, Sixth Sense, Superposition, Séance, Riff-Raff, Vagabond, Hallucination, Diet Cola, Certificate, Invisible Joker, Cartomancer, Perkeo<br><br>**Consumables**<br>The Fool, The High Priestess, The Emperor, Judgement, Familiar, Grim, Incantation, Wraith, Ankh, Cryptid<br><br>**Tags**<br>Uncommon Tag, Rare Tag, Double Tag, Top-up Tag<br><br>**Seals**<br>Blue Seal, Purple Seal |
| **destroy_card** | destroys another card | **Jokers**<br>Ceremonial Dagger, Madness, Trading Card<br><br>**Consumables**<br>The Hanged Ma, Familiar, Grim, Incantation, Immolate, Ankh, Hex<br><br>**Enhancements**<br>Glass Cards |
| **hands** | effect is based around hands | **Jokers**<br>Loyalty Card, Burglar, Troubadour, Dusk, Acrobat, DNA, Vagabond<br><br>**Vouchers**<br>Grabber, Nacho Tong, Hieroglyph<br><br>**Tags**<br>Handy Tag<br><br>**Boss Blinds**<br>The Needle |
| **discard** | effect is based around discards | **Jokers**<br>Banner, Mystic Summit, Delayed Gratification, Burglar, Faceless Joker, Green Joker, Mail-In Rebate, Drunkard, Trading Card, Ramen, Castle, Merry Andy, Hit the Road, Burnt Joker, Yorick<br><br>**Vouchers**<br>Wasteful, Recyclomancy, Petroglyph<br><br>**Tags**<br>Garbage Tag<br><br>**Boss Blinds**<br>The Hook, The Water<br><br>**Seals**<br>Purple Seal |
| **hand_size** | effect is based around hand size | **Jokers**<br>Juggler, Turtle Bean, Troubadour, Merry Andy, Stuntman<br><br>**Consumables**<br>Ouija, Ectoplasm<br><br>**Vouchers**<br>Paint Brush, Palette<br><br>**Tags**<br>Juggle Tag<br><br>**Boss Blinds**<br>The Manacle |
| **chance** | effect has a chance to happen | **Jokers**<br>8 Ball, Gros Michel, Business Card, Space Joker, Cavendish, Hallucination, Reserved Parking, Bloodstone<br><br>**Consumables**<br>The Wheel of Fortune<br><br>**Enhancements**<br>Glass Cards, Lucky Cards<br><br>**Boss Blinds**<br>The Wheel |
| **mod_chance** | affects other chance rolls | **Jokers**<br>Oops! All 6s |
| **copying** | copies the effect of another card | **Jokers**<br>Blueprint, Brainstorm |
| **full_deck** | effect is based on your full deck | **Jokers**<br>Steel Joker, Cloud 9, Erosion, Stone Joker, Driver's License |
| **passive** | passive bonus from owning the card | **Jokers**<br>Four Fingers, Credit Card, Chaos the Clown, Pareidolia, Splash, Shortcut, To the Moon, Juggler, Drunkard, Troubadour, Smeared Joker, Showman, Oops! All 6s, Astronomer |
| **joker** | related to Joker cards | **Jokers**<br>Abstract Joker, Riff-Raff, Swashbuckler, Invisible Joker, Gift Card<br><br>**Consumables**<br>The Wheel of Fortune, Temperance, Judgement, Ectoplasm, Ankh, Hex<br><br>**Booster Packs**<br>Buffoon Packs<br><br>**Tags**<br>Uncommon Tag, Rare Tag, Negative Tag, Foil Tag, Holographic Tag, Polychrome Tag, Top-up Tag<br><br>**Boss Blinds**<br>Crimson Heart |
| **joker_slot** | related to Joker slots | **Jokers**<br>Joker Stencil<br><br>**Vouchers**<br>Antimatter<br><br>**Editions**<br>Negative |
| **rarity** | related to specific Joker rarities | **Jokers**<br>Riff-Raff, Baseball Card<br><br>**Consumables**<br>Wraith<br><br>**Tags**<br>Uncommon Tag, Rare Tag, Top-up Tag |
| **position** | affected by the position of cards | **Jokers**<br>Blueprint, Ceremonial Dagger, Brainstorm, Hanging Chad, Photograph<br><br>**Consumables**<br>Death |
| **tarot** | related to Tarot cards | **Jokers**<br>8 Ball, Superposition, Vagabond, Hallucination, Fortune Teller, Cartomancer<br><br>**Consumables**<br>The Fool, The Emperor<br><br>**Vouchers**<br>Tarot Merchant, Tarot Tycoon<br><br>**Booster Packs**<br>Arcana Packs<br><br>**Seals**<br>Purple Seal |
| **planet** | related to Planet cards | **Jokers**<br>Astronomer, Constellation, Satellite<br><br>**Consumables**<br>The Fool, The High Priestess<br><br>**Vouchers**<br>Telescope, Observatory, Planet Merchant, Planet Tycoon<br><br>**Booster Packs**<br>Celestial Packs<br><br>**Seals**<br>Blue Seal |
| **spectral** | related to Spectral cards | **Jokers**<br>Sixth Sense, Séance<br><br>**Vouchers**<br>Omen Globe<br><br>**Booster Packs**<br>Spectral Packs |
| **consumable** | related to any consumables | **Jokers**<br>8 Ball, Sixth Sense, Constellation, Superposition, Séance, Vagabond, Gift Card, Hallucination, Fortune Teller, Satellite, Cartomancer, Astronomer, Perkeo<br><br>**Consumables**<br>The Fool, The High Priestess, The Emperor<br><br>**Vouchers**<br>Tarot Merchant, Tarot Tycoon, Planet Merchant, Planet Tycoon<br><br>**Seals**<br>Blue Seal, Purple Seal |
| **consumable_slot** | related to consumable slots | **Vouchers**<br>Crystal Ball |
| **playing_card** | effect adds playing cards to the deck | **Jokers**Marble Joker, DNA, Certificate<br><br>**Consumables**<br>Familiar, Grim, Incantation, Cryptid<br><br>**Vouchers**<br>Magic Trick, Illusion<br><br>**Booster Packs**<br>Standard Packs |
| **enhancements** | related to enhancements | **Jokers**<br>Golden Ticket, Marble Joker, Steel Joker, Vampire, Midas Mask, Stone Joker, Lucky Cat, Glass Joker, Driver's License<br><br>**Consumables**<br>The Magician, The Empress, The Hierophant, The Lovers, The Chariot, Justice, The Devil, The Tower, Familiar, Grim, Incantation<br><br>**Vouchers**<br>Illusion |
| **seals** | related to seals | **Jokers**<br>Certificate<br><br>**Consumables**<br>Talisman, Deja Vu, Trance, Medium |
| **editions** | related to editions *(added in 1606b)* | **Consumables**<br>The Wheel of Fortune, Aura, Ectoplasm, Hex<br><br>**Vouchers**<br>Hone, Glow Up, Illusion<br><br>**Tags**<br>Negative Tag, Foil Tag, Holographic Tag, Polychrome Tag |
| **tag** | related to tags *(added in 1606b)* | **Jokers**<br>Diet Cola<br><br>**Tags**<br>Double Tag |
| **skip** | effect linked to skipping blinds *(added in 1606b)* | **Jokers**<br>Throwback<br><br>**Tags**<br>Speed Tag |
| **modify_card** | modifies playing cards | **Jokers**<br>Pareidolia, Hiker, Vampire, Midas Mask<br><br>**Consumables**<br>The Magician, The Empress, The Hierophant, The Lovers, The Chariot, Justice, Strength, Death, The Devil, The Tower, The Star, The Moon, The Sun, The World, Talisman, Aura, Sigil, Ouija, Deja Vu, Trance, Medium |
| **perma_bonus** | permanently modifies the stats of cards *(added in 1606b)* | **Jokers**<br>Hiker |
| **prevents_death** | effect prevents losing a run | **Jokers**<br>Mr. Bones |
| **boss_blind** | effect linked to boss blinds *(added in 1606b)* | **Jokers**<br>Rocket, Luchador, Matador, Campfire, Chicot<br><br>**Vouchers**<br>Director's Cut, Retcon<br><br>**Tags**<br>Investment Tag, Boss Tag |
| **debuff** | causes cards or Jokers to be debuffed, or is affected by them | **Boss Blinds**<br>The Club, The Goad, The Plant, The Head, The Window, The Pillar, Verdant Leaf, Crimson Heart |
| **face_down** | causes cards or Jokers to be faced down, or is affected by them | **Boss Blinds**<br>The Fish, The House, The Mark, The Wheel, Amber Acorn |
| **large_blind** | causes a Blind to have a larger scoring requirement than default | **Boss Blinds**<br>The Wall, Violet Vessel |
| **ante** | effect changes the ante | **Vouchers**<br>Hieroglyph, Petroglyph |
| **shop** | related to the shop | **Jokers**<br>Chaos the Clown, Flash Card, Astronomer<br><br>**Vouchers**<br>Overstock, Overstock Plus, Clearance Sale, Liquidation, Reroll Surplus, Reroll Glut, Tarot Merchant, Tarot Tycoon, Planet Merchant, Planet Tycoon<br><br>**Tags**<br>Voucher Tag, Coupon Tag, D6 Tag |
| **booster** | related to Booster Packs | **Jokers**<br>Red Card, Hallucination, Astronomer<br><br>**Vouchers**<br>Omen Globe, Telescope<br><br>**Tags**<br>Standard Tag, Charm Tag, Meteor Tag, Buffoon Tag, Ethereal Tag |
| **reroll** | effect is based around rerolling the shop | **Jokers**<br>Chaos the Clown, Flash Card<br><br>**Vouchers**<br>Reroll Surplus, Reroll Glut<br><br>**Tags**<br>D6 Tag |
| **on_sell** | triggers when card is sold | **Jokers**<br>Luchador, Diet Cola, Invisible Joker<br><br>**Boss Blinds**<br>Verdant Leaf |
| **sell_value** | effect is based around sell value of a card | **Jokers**<br>Egg, Swashbuckler, Ceremonial Dagger, Gift Card<br><br>**Consumables**<br>Temperance<br><br>**Vouchers**<br>Clearance Sale, Liquidation |
| **food** | themed on food | **Jokers**<br>Gros Michel, Cavendish, Ice Cream, Ramen, Turtle Bean, Popcorn, Seltzer, Egg, Diet Cola |
| **space** | themed on space | **Jokers**<br>Supernova, Space Joker, Constellation, Rocket, Satellite, Astronomer |

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
| **Ceremonial Dagger** | mult, destroy_card, sell_value, scaling, position |
| **Banner** | discard, chips |
| **Mystic Summit** | mult, discard |
| **Marble Joker** | enhancements, generation, playing_card |
| **Loyalty Card** | xmult, hands |
| **8 Ball** | chance, eight, tarot, consumable, generation, rank |
| **Misprint** | mult |
| **Dusk** | retrigger, hands |
| **Raised Fist** | mult, rank |
| **Chaos the Clown** | reroll, passive, economy, shop |
| **Fibonacci** | three, mult, ace, eight, two, rank, five |
| **Steel Joker** | xmult, full_deck, enhancements |
| **Scary Face** | chips, face |
| **Abstract Joker** | mult, joker |
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
| **Space Joker** | chance, hand_type, space, hand_level |
| **Egg** | food, sell_value, scaling, economy |
| **Burglar** | discard, hands |
| **Blackboard** | xmult, suit, spades, clubs |
| **Runner** | hand_type, chips, scaling |
| **Ice Cream** | food, chips, scaling |
| **DNA** | generation, hands, playing_card |
| **Splash** | passive |
| **Blue Joker** | chips |
| **Sixth Sense** | spectral, consumable, six, generation, rank |
| **Constellation** | xmult, planet, consumable, space, scaling |
| **Hiker** | modify_card, chips, perma_bonus |
| **Faceless Joker** | discard, face, economy |
| **Green Joker** | mult, discard, scaling |
| **Superposition** | ace, hand_type, tarot, consumable, generation, rank |
| **To Do List** | hand_type, economy |
| **Cavendish** | xmult, chance, food |
| **Card Sharp** | xmult, hand_type |
| **Red Card** | mult, scaling, booster |
| **Madness** | xmult, destroy_card, scaling |
| **Square Joker** | chips, scaling |
| **Séance** | spectral, consumable, hand_type, generation |
| **Riff-Raff** | joker, generation, rarity |
| **Vampire** | xmult, modify_card, enhancements, scaling |
| **Shortcut** | hand_type, passive |
| **Hologram** | xmult, scaling |
| **Vagabond** | tarot, consumable, generation, hands |
| **Baron** | xmult, rank, king |
| **Cloud 9** | full_deck, nine, rank, economy |
| **Rocket** | space, scaling, economy, boss_blind |
| **Obelisk** | xmult, hand_type, reset, scaling, hands |
| **Midas Mask** | modify_card, enhancements, face |
| **Luchador** | on_sell, boss_blind |
| **Photograph** | xmult, face, position |
| **Gift Card** | sell_value, economy, joker, consumable |
| **Turtle Bean** | food, hand_size, scaling |
| **Erosion** | mult, full_deck |
| **Reserved Parking** | chance, face, economy |
| **Mail-In Rebate** | discard, rank, economy |
| **To the Moon** | passive, economy |
| **Hallucination** | chance, tarot, consumable, generation, booster |
| **Fortune Teller** | mult, tarot, consumable |
| **Juggler** | hand_size, passive |
| **Drunkard** | discard, passive |
| **Stone Joker** | full_deck, enhancements, chips |
| **Golden Joker** | economy |
| **Lucky Cat** | xmult, enhancements, scaling |
| **Baseball Card** | xmult, joker, rarity |
| **Bull** | chips |
| **Diet Cola** | on_sell, food, generation, tag |
| **Trading Card** | destroy_card, discard, economy |
| **Flash Card** | mult, reroll, scaling, shop |
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
| **Certificate** | seals, generation, playing_card |
| **Smeared Joker** | suit, hearts, passive, diamonds, spades, clubs|
| **Throwback** | xmult, scaling, skip |
| **Hanging Chad** | retrigger, position |
| **Rough Gem** | suit, diamonds, economy |
| **Bloodstone** | xmult, chance, suit, hearts |
| **Arrowhead** | suit, chips, spades |
| **Onyx Agate** | mult, suit, clubs |
| **Glass Joker** | xmult, enhancements, scaling |
| **Showman** | passive |
| **Flower Pot** | xmult, suit |
| **Blueprint** | copying, position |
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
| **Brainstorm** | copying, position |
| **Satellite** | planet, consumable, space, economy |
| **Shoot the Moon** | mult, rank, queen |
| **Driver's License** | xmult, full_deck, enhancements |
| **Cartomancer** | tarot, consumable, generation |
| **Astronomer** | planet, consumable, passive, space, economy, shop, booster |
| **Burnt Joker** | hand_type, discard, hand_level |
| **Bootstraps** | mult |
| **Canio** | xmult, face, scaling |
| **Triboulet** | xmult, rank, queen, king |
| **Yorick** | xmult, discard, scaling |
| **Chicot** | boss_blind | 
| **Perkeo** | generation, consumable | 

## Vanilla Consumable Attributes

| Tarot Name | Attributes |
| ---------- | ---------- |
| **The Fool** | generation, tarot, planet, consumable |
| **The Magician** | enhancements, modify_card |
| **The High Priestess** | generation, planet, consumable |
| **The Empress** | enhancements, modify_card |
| **The Emperor** | generation, tarot, consumable |
| **The Hierophant** | enhancements, modify_card |
| **The Lovers** | enhancements, modify_card |
| **The Chariot** | enhancements, modify_card |
| **Justice** | enhancements, modify_card |
| **The Hermit** | economy |
| **The Wheel of Fortune** | joker, editions, chance |
| **Strength** | modify_card, rank |
| **The Hanged Man** | destroy_card |
| **Death** | modify_card, position |
| **Temperance** | economy, joker, sell_value |
| **The Devil** | enhancements, modify_card |
| **The Tower** | enhancements, modify_card |
| **The Star** | modify_card, suit, diamonds |
| **The Moon** | modify_card, suit, clubs |
| **The Sun** | modify_card, suit, hearts |
| **Judgement** | generation, joker |
| **The World** | modify_card, suit, spades |

| Planet Name | Attributes |
| ----------- | ---------- |
| *All vanilla Planet Cards* | hand_type, hand_level, space |

| Spectral Name | Attributes |
| ------------- | ---------- |
| **Familiar** | generation, rank, jack, queen, king, face, playing_card, destroy_card, enhancements |
| **Grim** | generation, rank, ace, playing_card, destroy_card, enhancements |
| **Incantation** | generation, rank, two, three, four, five, six, seven, eight, nine, ten, playing_card, destroy_card, enhancements |
| **Talisman** | modify_card, seals |
| **Aura** | modify_card, editions |
| **Wraith** | generation, joker, rarity, lose_economy |
| **Sigil** | modify_card, suit |
| **Ouija** | modify_card, rank, hand_size |
| **Ectoplasm** | joker, editions, hand_size |
| **Immolate** | destroy_card, economy |
| **Ankh** | generation, joker, destroy_card |
| **Deja Vu** | modify_card, seals |
| **Ectoplasm** | joker, editions, destroy_card |
| **Trance** | modify_card, seals |
| **Medium** | modify_card, seals |
| **Cryptid** | generation, playing_card |
| **The Soul** | *none* |
| **Black Hole** | *none* |

*(The Soul and Black Hole don't have attributes yet because the system doesn't yet support soulable objects.)*

## Vanilla Booster Pack Attributes

| Booster Pack Name | Attributes |
| ----------------- | ---------- |
| **Arcana Pack** | tarot |
| **Celestial Pack** | planet |
| **Standard Pack** | playing_card |
| **Buffoon Pack** | joker |
| **Spectral Pack** | spectral |

## Vanilla Voucher Attributes

| Voucher Name | Attributes |
| ------------ | ---------- |
| **Overstock** | shop |
| **Overstock Plus** | shop |
| **Clearance Sale** | shop, economy, sell_value |
| **Liquidation** | shop, economy, sell_value |
| **Hone** | editions |
| **Glow Up** | editions |
| **Reroll Surplus** | shop, economy, reroll |
| **Reroll Glut** | shop, economy, reroll |
| **Crystal Ball** | consumable_slot |
| **Omen Globe** | spectral, booster |
| **Telescope** | planet, booster, hand_type |
| **Observatory** | xmult, planet, hand_type |
| **Grabber** | hands |
| **Nacho Tong** | hands |
| **Wasteful** | discard |
| **Recyclomancy** | discard |
| **Tarot Merchant** | shop, tarot, consumable |
| **Tarot Tycoon** | shop, tarot, consumable |
| **Planet Merchant** | shop, planet, consumable |
| **Planet Tycoon** | shop, planet, consumable |
| **Seed Money** | economy |
| **Money Tree** | economy |
| **Blank** | *none* |
| **Antimatter** | joker_slot |
| **Magic Trick** | playing_card |
| **Illusion** | playing_card, enhancements, editions, seals |
| **Hieroglyph** | ante, hands |
| **Petroglyph** | ante, discard |
| **Director's Cut** | boss_blind |
| **Retcon** | boss_blind |
| **Paint Brush** | hand_size |
| **Palette** | hand_size |

## Vanilla Tag Attributes

| Tag Name | Attributes |
| -------- | ---------- |
| **Uncommon Tag** | generation, joker, rarity |
| **Rare Tag** | generation, joker, rarity |
| **Negative Tag** | joker, editions |
| **Foil Tag** | joker, editions |
| **Holographic Tag** | joker, editions |
| **Polychrome Tag** | joker, editions |
| **Investment Tag** | economy, boss_blind |
| **Voucher Tag** | shop |
| **Boss Tag** | boss_blind |
| **Standard Tag** | booster |
| **Charm Tag** | booster |
| **Meteor Tag** | booster |
| **Buffoon Tag** | booster |
| **Handy Tag** | economy, hands |
| **Garbage Tag** | economy, discard |
| **Ethereal Tag** | booster |
| **Coupon Tag** | economy, shop |
| **Double Tag** | generation, tag |
| **Juggle Tag** | hand_size |
| **D6 Tag** | economy, shop, reroll |
| **Top-up Tag** | generation, joker, rarity |
| **Speed Tag** | economy, skip |
| **Orbital Tag** | hand_level |
| **Economy Tag** | economy |

## Vanilla card modifier Attributes

| Enhancement Name | Attributes |
| ---------------- | ---------- |
| **Bonus Card** | chips |
| **Mult Card** | mult |
| **Wild Card** | suit |
| **Glass Card** | xmult, chance, destroy_card |
| **Steel Card** | xmult |
| **Stone Card** | chips |
| **Gold Card** | economy |
| **Lucky Card** | mult, economy, chance |

| Edition Name | Attributes |
| ------------ | ---------- |
| **Foil** | chips |
| **Holographic** | mult |
| **Polychrome** | xmult |
| **Negative** | joker_slot |

| Seal Name | Attributes |
| --------- | ---------- |
| **Red Seal** | retrigger |
| **Blue Seal** | generation, planet, consumable |
| **Gold Seal** | economy |
| **Purple Seal** | generation, tarot, consumable, discard |

## Vanilla Blind Attributes

| Blind Name | Attributes |
| ---------- | ---------- |
| **Small Blind** | *none* |
| **Big Blind** | *none* |
| **The Hook** | discard |
| **The Ox** | lose_economy, hand_type |
| **The House** | face_down |
| **The Wall** | large_blind |
| **The Wheel** | face_down, chance |
| **The Arm** | hand_level |
| **The Club** | debuff, suit, clubs |
| **The Fish** | face_down |
| **The Psychic** | *none* |
| **The Goad** | debuff, suit, spades |
| **The Water** | discard |
| **The Window** | debuff, suit, diamonds |
| **The Manacle** | hand_size |
| **The Eye** | hand_type |
| **The Mouth** | hand_type |
| **The Plant** | debuff, face |
| **The Serpent** | *none* |
| **The Pillar** | debuff |
| **The Needle** | hands |
| **The Head** | debuff, suit, hearts |
| **The Tooth** | lose_economy |
| **The Flint** | *none* |
| **The Mark** | face_down, face |
| **Amber Acorn** | face_down, joker |
| **Verdant Leaf** | debuff, on_sell |
| **Violet Vessel** | large_blind |
| **Crimson Heart** | debuff, joker |
| **Cerulean Bell** | *none* |