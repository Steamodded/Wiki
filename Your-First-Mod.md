# Making Your First Mod
This page is designed to help you find what is needed when first making a mod. If you are just looking on more clarifcation on something specific, you should check the sidebar to see if it's covered, or ask in the [Balatro Discord](https://discord.gg/balatro).

## **If you are looking to start making a mod its reccomended to use a IDE. here is a list of commonly used IDE programs:**

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio](https://visualstudio.microsoft.com/)
- [NotePad++](https://notepad-plus-plus.org/)

# First Steps 
- If you haven't already [Install Steamodded](https://github.com/Steamodded/smods/wiki).
- Checkout the [Mod Metadata](https://github.com/Steamodded/smods/wiki/Mod-Metadata) page for how to get your mod detected by Steamodded.
- Checkout the [API Documentation](https://github.com/Steamodded/smods/wiki/API-Documentation) page for information on the basics of Steamodded's api.
- For adding content, check the **Game Objects** part of the sidebar, which lists every object SMODS can create.

# Useful resources
- [The Lua Reference Manual](https://www.lua.org/manual/5.1/) and [Programming in Lua](https://www.lua.org/pil/contents.html) are very useful resources to familarize yourself with lua (the game's programming language).
- Often, something you want to do has already been implemented in the base game. Familiarizing yourself with the game's code is an important step to learn Balatro modding. To get Balatro's source code, extract the game's executable file with [7-zip](https://www.7-zip.org/). For Mac, find `Balatro.love` inside `Balatro.app` and rename it to `Balatro.zip`, then extract `Balatro.zip`. A handful of vanilla jokers have been reimplemented in a [Steamodded example mod](https://github.com/Steamodded/examples/tree/master/Mods/ExampleJokersMod) for reference.
- It can also be useful to look at code from other mod creators.
  - Steamodded has some [Example Mods](https://github.com/Steamodded/examples/tree/master/Mods).
  - You can find example implementations of the vanilla Jokers using Steamodded [here](https://github.com/nh6574/VanillaRemade) (Work In Progress)
  - The best place to find other mods is in the official [Balatro Discord](https://discord.gg/balatro).
- Lovely is a tool that lets you patch the balatro source code, and since it's necessary for Steamodded, Steamodded mods can take advantage of it too. See [Lovely's patch documentation](https://github.com/ethangreen-dev/lovely-injector?tab=readme-ov-file#patches).

# Development Tips
- To quickly restart the game after making mod changes, press and hold `M` or press `Alt + F5`

# If you are unsure where to start here is a list of the classes added by Steamodded that are sorted by their complexity to code
___
## Useful Info for developing and Debugging
- [API Documentation](https://github.com/Steamodded/smods/wiki/API-Documentation)
- [Calculation Functions](https://github.com/Steamodded/smods/wiki/Calculate-Functions)
- [Event Manager](https://github.com/Steamodded/smods/wiki/Guide-%E2%80%90-Event-Manager)
- [Localization](https://github.com/Steamodded/smods/wiki/Localization)
- [Logging](https://github.com/Steamodded/smods/wiki/Logging)
- [Perma-bonuses](https://github.com/Steamodded/smods/wiki/Perma-bonuses)
- [Utility Functions](https://github.com/Steamodded/smods/wiki/Utility)
___
## Basic and Simple to use SMODS Classes
- [SMODS.Atlas](https://github.com/Steamodded/smods/wiki/SMODS.Atlas)
- [SMODS.Back](https://github.com/Steamodded/smods/wiki/SMODS.Back)
- [SMODS.Blind](https://github.com/Steamodded/smods/wiki/SMODS.Blind)
- [SMODS.Consumable](https://github.com/Steamodded/smods/wiki/SMODS.Consumable)
- [SMODS.Enhancment](https://github.com/Steamodded/smods/wiki/SMODS.Enhancement)
- [SMODS.Gradient](https://github.com/Steamodded/smods/wiki/SMODS.Gradient)
- [SMODS.Joker](https://github.com/Steamodded/smods/wiki/SMODS.Joker)
- [SMODS.Keybind](https://github.com/Steamodded/smods/wiki/SMODS.Keybind)
- [SMODS.Rank](https://github.com/Steamodded/smods/wiki/SMODS.Rank-and-SMODS.Suit#api-documentation-smodsrank)
- [SMODS.Rarity](https://github.com/Steamodded/smods/wiki/SMODS.Rarity)
- [SMODS.Suit](https://github.com/Steamodded/smods/wiki/SMODS.Rank-and-SMODS.Suit#api-documentation-smodssuit)
___
## Intermediate SMODS Classes
- [Switching from Loc_txt to using Localization](https://github.com/Steamodded/smods/wiki/Mod-functions#advanced-mod-descriptions)
- [SMODS.Booster](https://github.com/Steamodded/smods/wiki/SMODS.Booster)
- [SMODS.Challenge](https://github.com/Steamodded/smods/wiki/SMODS.Challenge)
- [SMODS.ConsumableType](https://github.com/Steamodded/smods/wiki/SMODS.ObjectType#api-documentation-smodsconsumabletype)
- [SMODS.PokerHand](https://github.com/Steamodded/smods/wiki/SMODS.PokerHand)
- [SMODS.Seal](https://github.com/Steamodded/smods/wiki/SMODS.Seal)
- [SMODS.Sound](https://github.com/Steamodded/smods/wiki/SMODS.Sound)
- [SMODS.Stake](https://github.com/Steamodded/smods/wiki/SMODS.Stake)
- [SMODS.Sticker](https://github.com/Steamodded/smods/wiki/SMODS.Sticker)
- [SMODS.https](https://github.com/Steamodded/smods/wiki/SMODS.https)
___
## Advance SMODS Classes
- [Adding a Config for your mod](https://github.com/Steamodded/smods/wiki/Mod-functions#modconfig_tab)
- [SMODS.DrawStep](https://github.com/Steamodded/smods/wiki/SMODS.DrawStep)
- [SMODS.ObjectType](https://github.com/Steamodded/smods/wiki/SMODS.ObjectType#api-documentation-smodsobjecttype)
- [SMODS.Tag](https://github.com/Steamodded/smods/wiki/SMODS.Tag)
- [SMODS.Voucher](https://github.com/Steamodded/smods/wiki/SMODS.Voucher)
___
## Expert SMODS Classes
- [Creating UI's outside of your mods config](https://github.com/Steamodded/smods/wiki/UI-Guide)
- [SMODS.Edition](https://github.com/Steamodded/smods/wiki/SMODS.Edition)
- [SMODS.Shader](https://github.com/Steamodded/smods/wiki/SMODS.Edition#smodsshader)
___
## Other SMODS Classes and Meathods
- [SMODS.Achievement](https://github.com/Steamodded/smods/wiki/SMODS.Achievement)
- [SMODS.DeckSkin](https://github.com/Steamodded/smods/wiki/SMODS.DeckSkin)
- [SMODS.Language](https://github.com/Steamodded/smods/wiki/SMODS.Language)
- [Text Styling](https://github.com/Steamodded/smods/wiki/Text-Styling)
