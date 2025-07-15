# How to install Steamodded on Linux

This guide is for Linux users running the Windows version of Balatro through Steam (via Proton). This includes the Steam Deck. If you're using a standalone Wine setup, the steps will be similar, but some paths may differ.

## Step 1: Installing Lovely
You can follow Lovely's general instructions [here](https://github.com/ethangreen-dev/lovely-injector?tab=readme-ov-file#manual-installation), or instead follow these specific install steps for Balatro (recommended):
1. Download the [latest Lovely release](https://github.com/ethangreen-dev/lovely-injector/releases/latest) for Windows (yes, seriously). This will be `lovely-x86_64-pc-windows-msvc.zip`. If your browser is blocking your download, use Firefox instead.
2. Navigate to your Balatro game directory in your file explorer. This can easily be done by right-clicking the game in Steam, hovering "Manage", and selecting "Browse local files".
3. Open the .zip archive, and extract Lovely's `version.dll` from the archive into the game directory.
4. Set your game's launch options in Steam to `WINEDLLOVERRIDES="version=n,b" %command%`.
5. Launch Balatro through Steam and you should see a second window pop up alongside the game named something like `Lovely x.x.x`. If it does, you have installed Lovely correctly and are ready to proceed to the next section. If it does not, please make sure you have followed the previous steps correctly.

## Step 2: Installing Steamodded
Once you have installed Lovely, you can install Steamodded:
1. Download the [latest Steamodded release](https://github.com/Steamodded/smods/releases/latest) by clicking "Source code (zip)" at the bottom of the page.
2. Extract the downloaded zip file.
3. In your file explorer, navigate to Balatro's save directory: `~/.local/share/Steam/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro`.
  > [!NOTE]
  > This location can differ depending on how you installed Steam:
  > - On systems with a Snap installation of steam the save directory is: `~/snap/steam/common/.local/share/Steam/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro`
  > - On systems with a Flatpack version of steam the save directory is: `~/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro`
  > - On Steam Deck (and some other installations) the save directory is: `~/.steam/steam/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro`
4. Create a folder named `Mods` if it doesn't already exist. Open your `Mods` folder.
5. Inside the extracted zip file, you should find a single directory. Move this interior folder into your `Mods` folder. After moving, it should look like `Mods/smods/<files>`, not `Mods/smods/smods/<files>` or `Mods/<files>`.

You can now install other mods by placing them into the `Mods` folder next to the Steamodded/smods folder. Make sure each mod is in its own subfolder.

## Common issues
Click the line describing your issue to see possible solutions.
<details><summary>The Lovely download failed or was blocked</summary>
Try a different browser. Firefox is known to work. You might need to right click the download and select "allow anyways".
</details>
<details><summary>A second window does not appear when I launch Balatro</summary>

It sounds like Lovely has not been installed correctly. Make sure that:
- Lovely's `version.dll` is in the right folder (it should be in the same folder as the Balatro executable).
- The Balatro launch options in Steam have been set correctly to `WINEDLLOVERRIDES="version=n,b" %command%`.
</details>
<details><summary>The second window appears, but the mods button does not show up in-game</summary>

This means Lovely has been installed correctly, but Steamodded is not installed correctly.
1. Make sure the `Mods` folder is in the right place (it should be under `<SteamLibrary-folder>/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro`, not under `<SteamLibrary-folder>/steamapps/common/Balatro`).
2. Make sure the Steamodded folder is correctly nested. It should look like `Mods/smods/<content>`, not like `Mods/smods/smods/<content>` or `Mods/<content>`, where content is the inner files.
</details>
<details><summary>Steamodded is installed correctly, but my game crashes!</summary>

There is a variety of reasons this can happen. Some of the more common reasons are:
- If you have other mods installed, it's very likely those mods are crashing. Check with the developer(s) of those mods.
- Your Balatro installation could be corrupted. Try verifying your game files on Steam: `Library > Balatro > Properties > Installed Files > Verify integrity of game files`.
- Your Balatro version might be outdated and needs to be updated through steam. Steamodded only supports the latest Steam version of the game.
- If you're trying to continue an existing run and crashing, your run is most likely unrecoverable. Try starting a new run.
</details>

## Updating Steamodded
If you'd like to update Steamodded in the future. Note that you do not need to update Steamodded or Lovely unless you're experiencing issues or new features require it.
- Check if Lovely needs to be updated. Your current version of Lovely is shown in the title of the second window when launching Balatro, and the latest version of Lovely can be found [here](https://github.com/ethangreen-dev/lovely-injector/releases/latest). If Lovely does need to be updated, follow step 1.
- Delete your current Steamodded folder. It might be named `Steamodded`, `smods-1.0.0-beta-0711a`, or something similar.
- Follow the instructions on how to install Steamodded in step 2.

## Uninstalling Steamodded
Delete the `version.dll` file from Balatro's game directory. This will prevent Steamodded and any other mods from loading.
