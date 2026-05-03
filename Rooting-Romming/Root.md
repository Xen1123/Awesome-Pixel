<h1 align=center>How To Root A Google Pixel! (Pixel 6 And Newer)</h1>
<h4 align=center>This Guide Is Meant For Magisk</h4>

**Prerequisites**
- FIRSTLY!!!!!!! I Am NOT Responsible For Your Hard Bricked Device, This Guide Doesn't Break Your Phone If You Follow It Correctly, If It Just Keeps Rebooting Into Bootloader Fastboot Mode, That's A Soft Brick And Can Be Fixed With This [Tool](https://flash.android.com/) If You Don't Know What To Do.
- Unlock Your Bootloader First!
    - Enable Developer Mode: `Settings` -> `About Phone` -> Scroll Down And Tap Your `Build Number` 7 Times Very Fast Until You're A Developer (It Will Say It At The Bottom As A Toast) -> Go Back To The Main Settings Page -> `System` -> `Developer Options`
        - Enable `OEM Unlocking`, If It Is Greyed Out Or Just Not There, You Are On A Carrier Locked Pixel!
        - Enable `USB Debugging` And Grant Permissions Upon Plugging Your Phone Into Your PC

<h4 align=center>Installing ADB & Fastboot On Linux🐧</h4>

<h5 align=left>For Debian/Ubuntu</h5>

```bash
sudo apt update -y && sudo apt upgrade -y && sudo apt install adb fastboot -y
```

<h5 align=left>For Arch</h5>

```bash
sudo pacman -Syu android-tools --noconfirm
```

<h5 align=left>For Fedora</h5>

```bash
sudo dnf update -y && sudo dnf install android-tools -y
```

<h4 align=center>Installing ADB & Fastboot On Windows🪟</h4>

```batch
winget install Google.PlatformTools
```
Simple, Right?
<h4 align=center>Installing ADB & Fastboot On MacOS🍎</h4>

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
```zsh
brew install --cask android-platform-tools
```

<h4 align=center>Yay! Now You Have The Tools! Time To Get Your Image And Unlock The Phone!!</h4>

- Download Your Stock Firmware [Here](https://developers.google.com/android/images)!
    - Unzip It -> Unzip The Nested Zip Archive -> Give The `vendor_boot` To The Google Pixel Device
        - Download Magisk On The Phone
    - [Click Here](https://github.com/topjohnwu/Magisk/releases/download/v30.7/Magisk-v30.7.apk)!!!
    - Install The App & Open It
         - Select "Install" For Magisk, Not The App; Choose "Select And Patch A File"
            - Patch Your `vendor_boot.img`
                - Transfer It Back To Your Computer, It Should Be Named Like This, `magisk_patched-30700_something.img`

- Reboot Your Phone Into Bootloader Mode
    ```bash
    adb reboot bootloader
    ```
    <h5 align=left>Unlock The Bootloader (THIS WILL WIPE ALL YOUR USER DATA BY PERFORMING A FACTORY RESET - BACKUP ALL DATA FIRST AND COME BACK)</h5>
    
    ```bash
    fastboot flashing unlock
    ```

    Confirm This Part On Your Phone!

- Now Flash Your Image And Reboot!
    ```bash
    fastboot flash init_boot <Your_Patched_Image>
    ```
    ```bash
    fastboot reboot
    ```
- Magisk May Need To Reboot Your Phone or Reinstall Itself From The App Upon Opening, But Then You're Rooted! Here Are Some Modules That Are REALLY Good!
    - [LSPosed/Vector](https://github.com/JingMatrix/Vector/releases/download/v2.0/Vector-v2.0-3021-Release.zip) - Great For Modding Apps!
    - [PixelXpert](https://github.com/siavash79/PixelXpert/releases/download/v5.1.1/PixelXpert.zip) - Great For UI Customization! Keep In Mind It Currently Only Supports Up To Android 16 QPR2 And ONLY Works On Your Pixel Firmware, Not A Custom ROM On A Pixel Or A ROM That Imitates Pixels! (Relies On LSPosed)
    - [ReZygisk](https://github.com/PerformanC/ReZygisk/releases/download/v1.0.0-rc.8/ReZygisk-v1.0.0-rc.8-release.zip) - Better Implementation of Magisk Zygisk, It Is Open Source And Offers Better Root Hiding, Zygisk Is Necessary For Most Modules, Especially LSPosed And LSPosed Dependant, It ALlows The User To Hook Things Into The Android Zygote Process!

<h4 align=center>System Restoration</h4>

- If You Want To Relock Your Bootloader, Make Sure Your Phone Is Completely On Stock Firmware! To Do So, Follow This Guide -
    - Come And Download This Script And Run It While You Are In The Folder of Your Stock Firmware
        - Linux🐧 & MacOS🍎 - [Pixel-Flasher.sh](../Scripts/Pixel-Flasher.sh)
        - Windows🪟 - [Pixel-Flasher.bat (MAY BE INCORRECT, I DON'T USE WINDOWS OR UNDERSTAND BATCH WELL)](../Scripts/Pixel.Flasher.bat)
