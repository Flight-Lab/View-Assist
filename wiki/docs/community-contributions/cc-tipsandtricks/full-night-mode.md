---
title: Full night mode
sidebar_position: 2
---
​
​
If you have a View Assist satellite on your nightstand, you might want it to turn off the screen fully. Here's a way to do that on Android:
1. First, install and configure the Home Assistant companion app. You need this to enable sending notifications to your satellite (or use webpanel to switch apps: https://wallpanel.xyz/docs/launch-external-apps). Make sure to enable the continuous connection to Home Assistant. We like using the companion app because it will continue to show the View Assist dashboard until the screen times out (see below).
2. Optionally install any app you want to use during the night. For example, you might want to use a night clock app. If you just want the screen black you don't need to install an extra app.
3. Configure your satellite Android's settings to turn off the screen after X time. Don't worry, webpanel will make sure your screen is still on during the day so you can continue to use View Assist normally.
4. Write a "bedtime" script or automation or add steps similar to the examples below to what you already have.

- this step calls the `notify` service for your satellite (`kiosk_1` in this example) and starts the NightClock free app (`de.program_co.nightclockfree`) app:**
```
- alias: Start night clock on Kiosk 1
  action: notify.mobile_app_view_assist_kiosk_1
  metadata: {}
  data:
    message: command_launch_app
    data:
      package_name: de.program_co.nightclockfree
```
 - this step cals the `notify` service on another satellite (`kiosk_2` in this example and starts the Home Assistant Companion app (`io.homeassitant.companion.android`):**
```
- alias: Start HA app on Kiosk 2 so screen can time out
  action: notify.mobile_app_view_assist_kiosk_2
  metadata: {}
  data:
    message: command_launch_app
    data:
      package_name: io.homeassistant.companion.android
```

  Since after switching apps, it's up to the app to keep the screen on your screen will turn off after the configured time if you switch to the companion app.

5. In your wake-up script/automation do the reverse, keeping in mind that if your screen has turned off, you need to turn it on otherwise you won't be able to see webpanel again. Here we only turn on the screen explicitly on `kiosk_2` since we know it off and the NightClock free kept the screen on on `kiosk_1` so no need to activate it explicitly. Then, we activate webpanel on all View Assist satellites:
```
- action: notify.mobile_app_view_assist_kiosk_2
    metadata: {}
    data:
      message: command_screen_on
    alias: Turn Kiosk 2 screen back on
  - action: notify.viewassistkiosks
    metadata: {}
    data:
      message: command_launch_app
      data:
        package_name: xyz.wallpanel.app
    alias: Start Wallpanel on both Kiosks
```
​
