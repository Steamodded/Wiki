# How to install Steamodded on Mac

## Step 1: Installing Lovely
You can follow Lovely's general instructions [here](https://github.com/ethangreen-dev/lovely-injector?tab=readme-ov-file#manual-installation), or instead follow these specific install steps for Balatro (recommended):
1. Download the [latest Lovely release](https://github.com/ethangreen-dev/lovely-injector/releases/latest) for Mac. If you have an M-series CPU (M1, M2, etc.) then this will be `lovely-aarch64-apple-darwin.tar.gz`. If you have an Intel CPU then it will be `lovely-x86_64-apple-darwin.tar.gz`. If you don't know which CPU you have, go to the Apple logo on the top left and press "About this Mac" to view what chip you are using.
2. Navigate to your Balatro game directory in Finder. This can easily be done by right-clicking the game in Steam, hovering "Manage", and selecting "Browse local files".
3. Open the archive, and extract Lovely's `liblovely.dylib` and `run_lovely_macos.sh` files from the archive into the game directory.
4. Launch Balatro by dragging and dropping `run_lovely_macos.sh` onto `Terminal.app` in Applications > Utilities and then pressing enter. You should now see a second window pop up alongside the game named something like `Lovely x.x.x`. If it does, you have installed Lovely correctly and are ready to proceed to the next section. If it does not, please make sure you have followed the previous steps correctly.

## Step 2: Installing Steamodded
Once you have installed Lovely, you can install Steamodded:
1. Download the [latest Steamodded release](https://github.com/Steamodded/smods/releases/latest) by clicking "Source code (zip)" at the bottom of the page.
2. Extract the downloaded zip file.
3. In Finder, navigate to Balatro's save directory: `~/Library/Application Support/Balatro`. If you can't find this folder, try pressing Shift-Command-Period to show hidden files.
4. Create a folder named `Mods` if it doesn't already exist. Open your `Mods` folder.
5. Inside the extracted zip file, you should find a single directory. Move this interior folder into your `Mods` folder. After moving, it should look like `Mods/smods/<files>`, not `Mods/smods/smods/<files>` or `Mods/<files>`.

You can now install other mods by placing them into the `Mods` folder next to the Steamodded/smods folder. Make sure each mod is in its own subfolder.

Note: You cannot run your game through Steam on Mac due to a known bug within the Steam client. You must run it by dragging and dropping `run_lovely_macos.sh` onto `Terminal.app` and pressing enter.

## Common issues
Click the line describing your issue to see possible solutions.
<details><summary>The Lovely download failed or was blocked</summary>
Try a different browser. Firefox is known to work. You might need to right click the download and select "allow anyway".
</details>
<details><summary>I can't find the <code>Library</code> folder in Finder</summary>

Press `Command + Shift + .` (period) or use `Go > Go to Folder...` and enter `~/Library/Application Support/Balatro`.
</details>
<details><summary>MacOS says it "could not verify liblovely.dylib is free of malware" or similar</summary>
Try to either:

- Right-click the file and select "Open" or "Open with" to open the file in another application manually.
- After trying to open it, go to System Settings > Privacy & Security, and look for a message near the bottom about blocked files. Click "Allow Anyway", then try launching it again.
- Run `xattr -rd com.apple.quarantine liblovely.dylib` in the Terminal (for advanced users).
</details>
<details><summary>A second window does not appear when I launch Balatro</summary>

It sounds like Lovely has not been installed correctly. Make sure that:
- Lovely's `liblovely.dylib` and `run_lovely_macos.sh` are in the right folder (it should be in the same folder as the Balatro application).
- You're running the game by dragging and dropping `run_lovely_macos.sh` onto `Terminal.app` and pressing enter, instead of running it through Steam.
</details>
<details><summary>The second window appears, but the mods button does not show up in-game</summary>

This means Lovely has been installed correctly, but Steamodded is not installed correctly.
1. Make sure the `Mods` folder is in the right place (it should be under `~/Library/Application Support/Balatro`, not under `~/Library/Application Support/Steam/SteamApps/common/Balatro`).
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

## Different platforms
Looking to install Steamodded on Windows or Linux? Check [here](https://github.com/Steamodded/smods/wiki).
