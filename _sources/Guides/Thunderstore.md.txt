# Packaging on Thunderstore

This guide is designed to explain how Steamodded mods interact with Thunderstore. If you are just looking for information on the process of putting a mod on Thunderstore, checkout [Creating a Package](https://wiki.thunderstore.io/mods/creating-a-package).

## Rules
Thunderstore has a set of rules that mods must follow. You can view them at [Global Rules](https://wiki.thunderstore.io/moderation/global-rules). I wanted to point out a few that might be unexpected for people used to distributing elsewhere.

- Mods should not self update themselves
- Mods should not download and then run code from the internet

Make sure to read all the rules.

## Manifest
Thunderstore packages have a file, manifest.json, which is documented on the [Thunderstore wiki](https://wiki.thunderstore.io/mods/creating-a-package#manifest). This is different than Steamodded's [metadata](https://docs.smods.dev/API%20Documentation/Mod-Metadata/). Keep in mind that these 2 systems are completely seperate, Steamodded doesn't use Thunderstore manifests and Thunderstore doesn't use Steamodded metadata.

### Versioning
Thunderstore has a different versioning system than Steamodded does. In Thunderstore, the versions are in the format x.y.z where x, y and z are all numbers. This more restrictive versioning scheme may not be compatible with how you have been versioning you're mod in the past. In the case your version is not compatible, here are your course of actions:
- Switch to using a versioning compatible with Thunderstore (Recommended)
  - This prevents confusion with versions, when people are using one system or the other.
  - Make sure you don't accidetnally make older versions of your mod considered higher when changing the version number.
- Use a seperate version for Thunderstore and Steamodded.
  - If you do this, it's recommended that the version is based on your Steamodded version to make it easier to switch between.

### Dependancies
Thunderstore has a very basic (relative to Steamodded's) dependancy system. Mods can specifiy exact versions of other mods they depend on. Mod managers will download that version or newer. This is equivalent to Steamodded's >= operator. It is recommended to include your dependancies in both the Thunderstore and Steamodded metadata. 
- Dependancies on Thunderstore will show link to the package on the website, and get mod managers to install them.
- Dependancies on Steamodded will be checked when the game is started, and prevent your mod from loading if it's missing dependancies.
  - Users can still manually install packages from Thunderstore, so they might mess up the dependancies.

The [Thunderstore Wiki](https://wiki.thunderstore.io/mods/creating-a-package#dependencies) has more details about it's dependancy system.

The version string for Steamodded looks like `"Steamodded-Steamodded-X.Y.Z"`. For 1.0.0 beta's, please consult the following chart:

<details><summary>List of Steamodded Beta Versions and Their Corresponding Thunderstore Version</summary>

v26.829.0 and higher are the same on both Thunderstore and Steamodded.

|SMODS Versioning|Thunderstore Versioning|
|--------|------|
|[1.0.0~BETA-0301a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0301a)|[1.301.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.301.0)|
|[1.0.0~BETA-0305c](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0305c)|[1.305.2](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.305.2)|
|[1.0.0~BETA-0312b](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0312b)|[1.312.1](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.312.1)|
|[1.0.0~BETA-0323b](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0323b)|[1.323.1](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.323.1)|
|[1.0.0~BETA-0506a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0506a)|[1.506.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.506.0)|
|[1.0.0~BETA-0509c](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0509c)|[1.509.2](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.509.2)|
|[1.0.0~BETA-0530b](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0530b)|[1.530.1](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.530.1)|
|[1.0.0~BETA-0614a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0614a)|[1.614.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.614.0)|
|[1.0.0~BETA-0711a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0711a)|[1.711.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.711.0)|
|[1.0.0~BETA-0827c](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-0827c)|[1.827.2](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.827.2)|
|[1.0.0~BETA-1016c](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-1016c)|[1.1016.2](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.1016.2)|
|[1.0.0~BETA-1221a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-1221a)|[1.1221.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.1221.0)|
|[1.0.0~BETA-1224a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-1224a)|[1.1224.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.1224.0)|
|[1.0.0~BETA-1501a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-1501a)|[1.1501.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.1501.0)|
|[1.0.0~BETA-1503a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-1503a)|[1.1503.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.1503.0)|
|[1.0.0~BETA-1531zeebee](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-1531zeebee)|[1.1531.999999](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.1531.999999)|
|[1.0.0~BETA-1606b](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-1606b)|[1.1606.1](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.1606.1)|
|[1.0.0~BETA-1620a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-1620a)|[1.1620.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.1620.0)|
|[1.0.0~BETA-1814a](https://github.com/Steamodded/smods/releases/tag/1.0.0-BETA-1814a)|[1.1814.0](https://thunderstore.io/c/balatro/p/Steamodded/Steamodded/v/1.1814.0)|

</details>

## Immutabile Packages
For reliability and stability, once a specific version of a package is successfully uploaded to thunderstore, it cannot be modifed (including README edits). Any changes after that point need a new version.
