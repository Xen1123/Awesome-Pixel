from pathlib import Path
import time
import shutil
import sys
import subprocess
import os
import getpass

print(r"""
 ____ _____  _______ _     
|  _ \_ _\ \/ / ____| |    
| |_) | | \  /|  _| | |    
|  __/| | /  \| |___| |___ 
|_|  |___/_/\_\_____|_____|

""")

print("Pixel Flasher - A tool to flash Pixel devices with ease.")
print("GitHub: https://github.com/Xen1123")
fastboot_path = shutil.which("fastboot")
if not fastboot_path:
    print("Error: fastboot not found in PATH. Please install Android Platform Tools and ensure fastboot is accessible.")
    sys.exit(1)
adb_path = shutil.which("adb")
if not adb_path:
    print("Error: adb not found in PATH. Please install Android Platform Tools and ensure adb is accessible.")
    sys.exit(1)
username = getpass.getuser()
confirm = input(f"Hello {username}! Would You Like To Flash Everything, Or Just Android Files Like System, Vendor, Etc? [Type Answer As Spelt In Suggestion!] (All/Android): ")
if confirm.lower() == "all":
    print("Flashing Everything!")
    print("Please Rename radio To `radio.img`, do the same with bootloader!")
    subprocess.run([
        "adb", "reboot", "bootloader"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run([
        "fastboot", "reboot", "bootloader"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    images = [
        "radio", "bootloader", "vbmeta", "dtbo", "boot", "abl", "abl1", "bl2", "bl31", "gsa", "ldfw", "modem", "pbl", "pvmfw", "tzsw", "vbmeta_system", "vbmeta_vendor", "vendor_dlkm"
    ]
    for img in images:
        img_path = Path(f"{img}.img")
        if img_path.exists():
            print(f"Flashing {img}_a . . .")
            subprocess.run([
                "fastboot", "flash", f"{img}_a", img_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Flashing {img}_b . . .")
            subprocess.run([
                "fastboot", "flash", f"{img}_b", img_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print(f"Warning: {img}.img not found, skipping.")
        subprocess.run([
            "fastboot", "reboot", "fastboot"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        part = [
            "system", "vendor", "product", "system_ext", "odm", "product", "system_other", "vendor_dlkm"
        ]
        for p in part:
            img_path = Path(f"{p}.img")
            if img_path.exists():
                print(f"Flashing {p} . . .")
                subprocess.run([
                    "fastboot", "flash", p, img_path
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                print(f"Warning: {p}.img not found, skipping.")
        subprocess.run([
            "fastboot", "reboot"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
elif confirm.lower() == "android":
    subprocess.run([
        "adb", "reboot", "fastboot"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run([
        "fastboot", "reboot", "fastboot"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Flashing Android Files!")
    part = [
        "boot", "dtbo", "vendor_boot", "vbmeta", "vbmeta_system", "vbmeta_vendor", "system", "vendor", "product", "system_ext", "odm", "product", "system_other", "vendor_dlkm"
    ]
    for p in part:
        img_path = Path(f"{p}.img")
        if img_path.exists():
            print(f"Flashing {p} . . .")
            subprocess.run([
                "fastboot", "flash", p, img_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print(f"Warning: {p}.img not found, skipping.")
    subprocess.run([
        "fastboot", "reboot"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
else:
    print("Invalid Option, Exiting.")
    sys.exit(0)