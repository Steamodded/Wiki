# Making Your First Mod
This page is designed to help you find what is needed when first making a mod. If you are just looking on more clarification on something specific, you should check the sidebar to see if it's covered, or ask in the [Balatro Discord](https://discord.gg/balatro).

# First Steps
If you haven't already, Install Steamodded. Method A is recommended due to easier updating and being on the latest dev branch.
### Method A: using the command line
*This method requires [Git](https://git-scm.com/downloads). If you do not have git, skip to method B.*
1. Install lovely according to the [instructions](https://github.com/ethangreen-dev/lovely-injector?tab=readme-ov-file#manual-installation).
2. Navigate to Balatro's save directory: `cd %AppData%/Balatro`
3. Paste the following lines:
```shell
mkdir Mods
cd Mods
git clone https://github.com/Steamodded/smods.git
```
4. To update Steamodded later, navigate back to the `smods` directory and run `git pull`.
### Method B: manual installation
*If you have completed Method A, please skip this step. Your installation is complete.*

Follow the manual installation instructions on how to install smods as a user at the [home page](https://github.com/Steamodded/smods/wiki).

# Useful resources
A list of resources that might be useful when developing your own mod.
## Existing mods
It can be useful to look at code from other mod creators.
- You can find example implementations of the vanilla Jokers using Steamodded [here](https://github.com/nh6574/VanillaRemade) (Work In Progress)
- The best place to find more mods is in the official [Balatro Discord](https://discord.gg/balatro).
- Steamodded has some [Example Mods](https://github.com/Steamodded/examples/tree/master/Mods).
## Steamodded documentation
- Check out the [Mod Metadata](https://github.com/Steamodded/smods/wiki/Mod-Metadata) page for how to get your mod detected by Steamodded.
- Check out the [API Documentation](https://github.com/Steamodded/smods/wiki/API-Documentation) page for information on the basics of Steamodded's api.
- For adding content, check the **Game Objects** part of the sidebar, which lists every object SMODS can create.
## Other resources
- [The Lua Reference Manual](https://www.lua.org/manual/5.1/) and [Programming in Lua](https://www.lua.org/pil/contents.html) are very useful resources to familiarize yourself with Lua (the game's programming language).
- Often, something you want to do has already been implemented in the base game. Familiarizing yourself with the game's code is an important step to learn Balatro modding. To get Balatro's source code, extract the game's executable file with [7-zip](https://www.7-zip.org/). For Mac, find `Balatro.love` inside `Balatro.app` and rename it to `Balatro.zip`, then extract `Balatro.zip`. A handful of vanilla jokers have been reimplemented in a [Steamodded example mod](https://github.com/Steamodded/examples/tree/master/Mods/ExampleJokersMod) for reference.
- Lovely is a tool that lets you patch Balatro's source code. Steamodded mods can take advantage of it too. See [Lovely's patch documentation](https://github.com/ethangreen-dev/lovely-injector?tab=readme-ov-file#patches).

# Development Tips
- To quickly restart the game after making mod changes, press and hold `M` or press `Alt + F5`.
- Data can be saved by adding it to `G.GAME`.
