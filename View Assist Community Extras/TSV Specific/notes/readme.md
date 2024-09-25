> [!warning]
> Mass disorganized info dump 🤷‍♂️

Many thanks to Electimon and Deadman for the Lineage 15.1 build, and PGale for the guide
https://github.com/pgale/lineage_15.1_Installation_TSV



ADB persistent on reboot: 
  `adb shell setprop persist.adb.tcp.port 5555`


## ADB Commands for Screen Brightness Control

**Auto brightness mode on:**
```settings put system screen_brightness_mode 1```
**Auto brightness mode off:**
```settings put system screen_brightness_mode 0```
**Auto brightness mode set brightness:**
```settings put system screen_auto_brightness_adj {value between -1 and 1}```
**Manual brightness mode set brightness:**
```settings put system screen_brightness {value between 0 and 255}```

## Screen Brightness Info Dumping
Auto brightness doesn't actually adjust the brightness automatically, but it does allow setting the minimum brightness even lower than in manual brightness mode. Conversely, manual brightness mode allows setting the maximum brightness to be even higher than in auto brightness mode. (Thanks to @thejeffcooper  for this tip).

Based on some quick testing: (on further testing the auto brightness kind of barely works so these numbers aren't exactly correct. testing was done in a dark room)
- Auto brightness 0.13 is equivalent to manual brightness 0
- Auto brightness 1 is equivalent to manual brightness 73

Launching or reloading the Fully Kiosk Browser app turns off auto brightness and sets brightness to maximum.

When Browser Mod `light.{deviceID}_screen` entity is switched off, a  black filter is placed over the screen while the screen and backlight remains on. This allows for a pseudo touch to wake ability and for Assist to keep functioning with the screen "off." Combining this with screen auto brightness set to minimum gets you the lowest possible brightness output while still keeping Assist functioning. 
-# (For me, this is still too bright for night time bedroom use but it's still less bright than if I open my window shade to a degree comparable to the 8" screen size).
Further, the Browser Mod `light.{deviceID}_screen` entity is "dimmable." Adjusting this entity's brightness does not affect the device backlight but adjusts the transparency of the black filter. 
With `light.{deviceID}_screen` set to 100%, the black filter transparency = 100%. Dimming decreases the transparency of the black filter.


Courtesy of @SemiColon:
"Unsure if anyone has found this yet, but in order to detect the Hardware Mic and Camera switches, you can read the following files:

/sys/devices/soc/soc:gpio_keys/camera_switches
Camera Enabled/Shutter Open: 1
Camera Disabled/Shutter Closed: 0
/sys/devices/soc/soc:gpio_keys/mute_switches
Mic Enabled: 0
Mic Disabled: 1

Could use this to drive the Mute entity in HA, and detect the status of the Camera. 
Unfortunately, they are GPIO pins, so there is no linux/android events associated with the files changing. I was able to use Tasker with the tick event, to check the file every few seconds."

Magisk/root can be achieved by either replacing the boot.img in the zip with `boot_los15_20240602.img` (after renaming it to `boot.img`), or flash this boot.img  in QFIL's partition manager after flashing lineage.



<!--
[Android 11](https://github.com/phhusson/treble_experimentations/releases/download/v313/system-roar-arm-aonly-vanilla.img.xz)

[Android 10](https://github.com/phhusson/treble_experimentations/releases/download/v222/system-quack-arm-aonly-vanilla.img.xz)

Endlessvoid's notes:
"Auto-brightness doesn't work
Recents button doesn't work (on A11 only, works fine on A10)
Tap to wake doesn't work
Wifi MAC isn't pulling from hardware (can be set manually with adb)
Wifi won't connect to WPA3
Scaling is too large by default (adjustable in developer options)
Potentially some issues with the proximity sensor (not experienced first-hand)"

Deadman's instructions:
"A11 Go Gapps Kingston firmware package

From testing you don't need to flash the debug firmware before doing these steps, it was tested on a fresh out of box unit as well.

Install instructions:

Unplug power and then hold vol + and - before plugging it in to boot to edl directly or adb reboot edl
Flash the combined firmware with qfil (Same instructions as flashing debug firmware just use rawprogram0.xml instead of rawprogram_unsparse.xml)
Unplug power and then hold Vol+ before plugging it in to boot to recovery directly
Use volume keys to navigate to the factory reset option and select it
Reboot and after a few minutes you will see the duck boot animation and then the Google setupwizard

Features/changes:

Kernel with GPU OC (850mhz), Wifi fix, selinux permissive enabled for now
a11 gogapps GSI with gsm/ims permissions removed
Vendor with updated wifi module, edited fstab to remove resource partition mounting, removed qcom-factory permission
New rawprogram0, patch0, gpt_main0/gpt_backup0 from @mrhand for larger system and userdata partitions
Userdata_1.img as just userdata.img
Stock recovery pulled from newer firmware so volume keys work to move/select

Bugs (If you find some let me know and I'll add):
No Auto Brightness currently  (Needs a treble vendor overlay to turn it on WIP)
Recents button doesn't work  (Needs a treble vendor overlay to turn it on WIP)

Download:
https://s3.us-east-1.wasabisys.com/filestash-buk/lenovo-thinksmart-view/combined_kingston_a11_gogapps.7z

Qfil flashing instructions 
https://xdaforums.com/t/cd-18781y-lenovo-thinksmart-view-bootloader-firmware-zoom-teams-conversion-normal-android.4426029/#:~:text=Flashing%20the%20Lenovo%20firmware

If you don't want Go gapps you can replace the system.img with a different gsi. Also be aware this can easily be reversed by flashing the debug firmware again. It will repartition your device back to the stock layout."

-->
