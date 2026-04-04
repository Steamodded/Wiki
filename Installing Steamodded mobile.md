# How to install Steamodded on Android/iOS

> [!IMPORTANT]
> The official Balatro Discord has a longstanding rule against the discussion of modding non-desktop platforms. If you need support with your installation on Android or iOS, please ask on the [Steamodded Discord](https://discord.gg/kU8cqCqwy3) server instead.
> [!IMPORTANT]
> In order to play with mods on Android or iOS, you must own and have access to the **Steam version** of Balatro. The versions of the game available on the Google Play Store and the Apple App Store **are not and will never be supported** by Steamodded.

## Step 1: Lovely Mobile Maker
1. Visit the [Lovely Mobile Maker](https://lmm.shorty.systems/) website on a device with access to the files of your Balatro installation on Steam.
2. Follow all of the steps provided on the website. Make sure to expand any info boxes along the way; they contain important information.
3. **When installing for the first time:** After installing the game on your mobile device, run it once to allow initialization of the save directory.

## Step 2: Installing Steamodded
Once you've used Lovely Mobile Maker and installed the app on your mobile device, you can install Steamodded.
1. Download the [latest Steamodded release](https://github.com/Steamodded/smods/releases/latest) by clicking "Source code (zip)" at the bottom of the page.
2. Extract the downloaded zip file.
3. In your file explorer, navigate to your mods folder.
  <details><summary>Mods folder on Android</summary>
  - Unfortunately, most Android file managers are inadequate for managing your Mods folder. It is recommended to use [Material Files](https://github.com/zhanghai/MaterialFiles) (Install on [Google Play](https://play.google.com/store/apps/details?id=me.zhanghai.android.file) or [F-Droid](ttps://f-droid.org/packages/me.zhanghai.android.files)) for this purpose.
  - After installing Material Files, you can then open the hamburger menu on the top left > Add Storage... > External Storage > the hamburger menu on the top left > Balatro > Use this folder > allow. </p>
  - This will add a new folder to the sidebar with your game saves. Navigate to <code>ASET/Mods</code> within this folder to access your mods folder.
  </details>
  <details><summary>Mods folder on iOS</summary>
  - In <code>On My iPhone/iPad</code>, navigate to <code>Balatro/game/Mods</code> to access your mods folder.
  </details>

  > [!NOTE]
  > If you chose a custom name for your app in Lovely Mobile Maker, replace any mentions of the game name Balatro in this step with your custom name.
4. Inside the extracted zip file, you should find a single directory. Move this interior folder into your `Mods` folder. After moving, it should look like `Mods/smods/<files>`, not `Mods/smods/smods/<files>` or `Mods/<files>`.

You can now install other mods by placing them into the `Mods` folder next to the Steamodded/smods folder. Make sure each mod is in its own subfolder.

## Step 3: Recommended Mods
- The default mouse controls of the Steam version are not very mobile-friendly. It is recommended to install [Silk Touch](https://github.com/HuyTheKiller/SilkTouch) or [Sticky Fingers](https://github.com/eramdam/sticky-fingers) to control the game more like the native mobile version.
- [Mobile Patches](https://github.com/WilsontheWolf/MobilePatches/archive/refs/heads/master.zip) is a mod that changes a few things in balatro to work better on mobile devices. Each patch is in a different file and can be deleted if you do not want it. If you are experiencing certain issues (see below!), **you must install this!**

## Common issues
Click the line describing your issue to see possible solutions.
<details><summary>The app download failed or was blocked</summary>

- Try a different browser. Firefox is known to work. You might need to right click the download and select "allow anyways".
- If you use any anti-virus software, it might be easiest to temporarily turn it off entirely, and re-enable it after you have finished installing.
</details>
<details><summary>Steamodded is installed correctly, but my game crashes!</summary>

There is a variety of reasons this can happen. Some of the more common reasons are:
- If you have other mods installed, it's very likely those mods are crashing. Check with the developer(s) of those mods.
- Your Balatro installation could be corrupted. Try verifying your game files on Steam: `Library > Balatro > Properties > Installed Files > Verify integrity of game files`. Then, follow step 1 again to build a new app with the clean files.
- Your Balatro version might be outdated and needs to be updated through Steam. Steamodded only supports the latest Steam version of the game. After a game update, you should follow step 1 again to update your mobile app to the latest version.
- If you're trying to continue an existing run and crashing, your run is most likely unrecoverable. Try starting a new run.
</details>
<details><summary>When I lauch the game, it is mostly covered in black!</summary>

- This is a common issue mostly observed on Google Pixel devices. To fix it, please install [Mobile Patches](https://github.com/WilsontheWolf/MobilePatches/archive/refs/heads/master.zip).
</details>

## Updating Steamodded
If you'd like to update Steamodded in the future. Note that you do not need to update Steamodded or Lovely unless you're experiencing issues or new features require it.
- Delete your current Steamodded folder. It might be named `Steamodded`, `smods-1.0.0-beta-0711a`, or something similar.
- Follow the instructions on how to install Steamodded in step 2.
- If you're experiencing any crashes or mods failing to load due to Lovely not being up to date, follow step 1 again to update.

## Uninstalling Steamodded
It is not possible to uninstall Lovely from a Lovely Mobile Maker build. To install Steamodded or any other mods, remove them from your mods folder.
