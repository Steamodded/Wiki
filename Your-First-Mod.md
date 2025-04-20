# Making Your First Mod
This page is designed to help you find what is needed when first making a mod. If you are just looking on more clarifcation on something specific, you should check the sidebar to see if it's covered, or ask in the [Balatro Discord](https://discord.gg/balatro).

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
  - The best place to find other mods is in the official [Balatro Discord](https://discord.gg/balatro).
- Lovely is a tool that lets you patch the balatro source code, and since it's necessary for Steamodded, Steamodded mods can take advantage of it too. See [Lovely's patch documentation](https://github.com/ethangreen-dev/lovely-injector?tab=readme-ov-file#patches).

# Development Tips
- To quickly restart the game after making mod changes, press and hold `M` or press `Alt + F5`.
- Data can be saved by adding it to `G.GAME`.
