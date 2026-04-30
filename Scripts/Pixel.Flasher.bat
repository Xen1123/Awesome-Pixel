@echo off
setlocal EnableDelayedExpansion

echo Please Make Sure Your Desired Images Are In The Directory That You're Operating In! Click Any Key To Continue!
pause >nul

:: Rename files, ignoring errors if they don't exist
ren bootloader* bootloader.img >nul 2>&1
ren radio* radio.img >nul 2>&1

:: Reboot commands
adb reboot bootloader >nul 2>&1
:: Windows doesn't have a direct equivalent to Bash's 'timeout' wrapping a command, 
:: but executing it directly generally suffices for this use case.
fastboot reboot bootloader >nul 2>&1

:: Menu prompt
echo.
echo Just Android Images Or The Full Firmware Flash?
echo 1) Android
echo 2) Full Factory
echo.
choice /c 12 /n /m "Please enter 1 or 2: "

if errorlevel 2 goto FullFactory
if errorlevel 1 goto Android

:Android
for %%i in (boot dtbo vendor_boot vbmeta_system vbmeta vbmeta_vendor) do (
    echo Flashing %%i
    fastboot flash %%i %%i.img >nul 2>&1 || echo Failed To Flash %%i
)

fastboot reboot fastboot

for %%i in (system system_ext system_other vendor vendor_dlkm gsa product) do (
    echo Flashing %%i
    fastboot flash %%i %%i.img >nul 2>&1 || echo Failed To Flash %%i
)
goto End

:FullFactory
for %%i in (bootloader radio boot dtbo vendor_boot vbmeta_system vbmeta vbmeta_vendor abl bl1 bl2 bl31 ldfw modem pbl pvmfw tzsw) do (
    echo Flashing %%i
    fastboot flash %%i %%i.img >nul 2>&1 || echo Failed To Flash %%i
)

fastboot reboot fastboot

for %%i in (system product system_ext system_other vendor vendor_dlkm) do (
    echo Flashing %%i
    fastboot flash %%i %%i.img >nul 2>&1 || echo Failed To Flash %%i
)
goto End

:End
echo Done.