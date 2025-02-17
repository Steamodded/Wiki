Welcome to the Steamodded wiki! The following pages form an assembly of documentation and guides for Steamodded.
# How to install Steamodded
## Step 1: Anti-virus setup
*Skip ahead to step 2 if you are not using any anti-virus software.*

Steamodded relies on a runtime code injector in order to modify the game. Because it functions similarly to a Trojan, it is often **incorrectly** flagged as malware by anti-virus systems. Rest assured that Lovely is **not malicious** in any way. It is fully open source, so you can convince yourself that it works exactly as promised and does nothing else. You can even build it yourself if you're still unsure. In order to get Lovely running properly, you will have to whitelist Balatro's installation folder in whatever anti-virus software you may be using. You may also need to temporarily disable real-time protection to avoid having files deleted while moving them around.
### Example: steps for Windows Defender
Differences may occur if you're using different software.
1. Navigate to the game's directory by right-clicking the game in Steam, hovering "Manage", and selecting "Browse local files". Copy the file path of this directory.
2. Open Windows Security and navigate to `Virus & threat protection > Manage settings`.
3. Disable `Real-time protection`.
4. Scroll down to `Add or remove exclusions` and confirm if prompted.
5. Add a folder exclusion. When an explorer window opens, paste the path you copied in step 1 into the address bar and confirm.

## Step 2: Installing Lovely
Now you're ready to install the **Lovely injector**. Please follow the installation instructions for your operating system [here](https://github.com/ethangreen-dev/lovely-injector?tab=readme-ov-file#manual-installation), then return to this page and continue with Step 3. If your browser is blocking your download, use Firefox instead.

## Step 3: Installing Steamodded
**If you previously installed Steamodded without Lovely,** you must first remove that installation by verifying your game files on Steam: `Library > Balatro > Properties > Installed Files > Verify integrity of game files`.

### Method (3a): Direct download
*This method requires no further tools. If you know what Git is, skip ahead to Method (3b).*
1. Click [here](https://github.com/Steamodded/smods/archive/refs/heads/main.zip) to download the latest source code. (*No up-to-date releases exist as of now. This guide will be updated when they do.*)
2. Extract the download zip file.
3. In your file explorer, navigate to Balatro's save directory: **Windows:** `%AppData%/Balatro`; **Mac:** `~/Library/Application Support/Balatro`; **Linux (WINE/Proton):** `~/.local/share/Steam/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro`.
  > [!IMPORTANT]
  > On Windows systems, just paste `%AppData%/Balatro` into the explorer path bar or the run dialog to open the folder. `%AppData%` has special meaning and you do not need to manually replace it.
  > <details>
  > <summary>Click me for Example Video</summary>
  > 
  > [Screencast_20241231_162107.webm](https://github.com/user-attachments/assets/12b76bed-fb0b-4e49-ae57-4ca12b6f1727)
  > 
  > </details>

  > [!NOTE]
  > On Linux systems with a snap installation of Steam, the save directory is slightly different: `~/snap/steam/common/.local/share/Steam/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro`
4. Create a folder named `Mods` if it doesn't already exist. Open your `Mods` folder.
5. Inside the extracted zip file, you should find a directory named `smods-main`. Move this interior folder into your `Mods` folder. Ensure there is more than a single folder inside.
6. To update Steamodded later, delete the `smods-main` folder and repeat steps 1-5.

### Method (3b): Using the command line
*This method requires [Git](https://git-scm.com/downloads). If you have completed Method (3a), please skip this step. Your installation is complete.*
1. Navigate to Balatro's save directory: **Windows:** `cd %AppData%/Balatro`; **Mac:** `cd ~/Library/Application Support/Balatro`; **Linux (WINE/Proton):** `cd ~/.local/share/Steam/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro`.

2. Paste the following lines: 
```shell
mkdir Mods
cd Mods
git clone https://github.com/Steamodded/smods.git

```
3. To update Steamodded later, navigate back to the `smods` directory and run `git pull`.
