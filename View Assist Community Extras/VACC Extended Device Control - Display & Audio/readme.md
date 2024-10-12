Page is a work in progress

# View Assist Extras - Extended Device Control - Display & Audio

This blueprint extends features for enhanced control of View Assist device display and audio playback. 

> [!note]    
> **Must create a new automation for each device.**
> Some features require edits and/or additions in the View Assist device configuration yaml file. 

__Optional Extended Features Summary:__
- Decreases music volume when triggered by wake-word or broadcast, raises
    music volume when TTS ends.
- Choose and play sound when wake word is detected.
- Choose and play sound when STT detects silence.
- Set music mode when musicplayer_device playing.
- Set normal mode when musicplayer_device idle for set duration.
 
> [!note]
>All features are opt-in and will not work unless the required device config changes are made.

## contains: 

**Extra features that do not require any change to the stock View Assist device config file:**
  * Assist Audio Feedback:
    * Choose and play sound when wake word is detected. (If using, set Stream Assist `STT start media` to `null`)
    * Choose and play sound when STT detects silence. (If Music Duck is activated, then the sound is not played. This is because the voolume returning to normal signifies the end of listening.)

**Extra features that require changes to the stock View Assist device config file:**
* On Home Assistant server startup, Fully Kiosk Browser loads the start URL.  
Requires `fkb_device: ` in config file.  
The `fkb_device: ` will be the name of the device in the Fully Kiosk Browser integration.  
E.g. `fkb_device: "pyramid"`

**Requires the use of separate media players for mediaplayer_device & musicplayer_device:** 
* Auto Music Mode:
    * Set music mode and navigate to music view when the musicplayer_device starts playing. Previously this only happened when playing music using the play music voice command, now this functions when music playback is started from any trigger.
* Music Mode Timeout:
    * Music Mode/View timeout sets normal mode and returns to default home page when music playback has been stopped for a user set amount of time. Previously, this would only happen when using the "stop music" voice command.
* Music Duck:
    * Decreases music volume (by a user selected percentage of the current volume) when triggered by wake-word or broadcast, restores original music volume when TTS ends.


> [!IMPORTANT]
> Most of the extra features REQUIRE the mediaplayer_device and musicplayer_device in your View Assist device config file to use separate media_player entities. These features rely on using media_player state change as a trigger, so the media players must also be stable, remain available, and display reliable state changes between idle & playing. Remember to also use the mediaplayer_device media_player in Stream Assist.

## Recommended Media Players:
* **musicplayer_device:** [Snapcast](https://play.google.com/store/apps/details?id=de.badaix.snapcast&hl=en_US) (only exposed by Music Assistant) **FREE**
* **mediaplayer_device:** [AirReceiver](https://play.google.com/store/apps/details?id=com.softmedia.receiver&hl=en_US) audio (only exposed by Music Assistant) **$2.99**
<details>

<summary>AirReceiver Setup:</summary>

1) In AirReceiver settings, make sure both Airplay <sub>IOS Media Receiver</sub> and AirTunes Audio <sub>AirPort Express Speaker</sub> are selected. The media_player entity we want to use is only made when both of these are checked.
(You do not need the other options selected for this but they will not harm anything if you choose to. I do, however, recommend unchecking them as they will create even more media player entities. One even creates a media server.)

3) Scroll down and select Advanced Settings.

4) Set AirTunes Audio Latency (ms) to 0(ms)

5) Check AirTunes UI [✓]

The media player entity we want to use will be created by the Music Assistant integration and will be called `media_player.lenovostarview_(last 3 digits of device ip)_audio`  
ex. `media_player.lenovostarview_180_audio`  
This media player has volume controls independent from the android device volume controls, just like the Snapcast media player.
Setting the AirTunes Audio Latency to 0(ms) in step \#3 allows for a more responsive feeling TTS.

</details>
<details>

<summary>Other Confirmed Working Media Players:</summary>

* [Fully Kiosk Browser](https://play.google.com/store/apps/details?id=de.ozerov.fully&hl=en_US) media player (exposed by Music Assistant) 
> [!WARNING]
> If using the FKB media player, it must be the one exposed by Music Assistant or it will go unavailable and will not be able to act as a trigger.
>
> The FKB media player seems to have a delay between state changes and audio playback. 
> State will change from idle to playing and then audio playback will begin after a 1-2 second delay.
> Audio playback will end and then state will change from playing to idle after a 1-2 second delay.
> These delays lead to a feeling of decreased responsiveness.


</details>

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://gist.github.com/Flight-Lab/6ddb640f756791d59b6fd9be93375eee)

<!-- 
notes for future edits:
The general concept is to work like an audio mixer. Each channel is individually controllable and can be played at the same time as any of the other channels. This enables you to do something wild like playing music while an alarm rings and assist tells you what the alarm is for, or something more controlled like having your music lower in volume as the alarm increases in volume.  
This also lets you set permanant default levels to each channel or mute certain functions while keeping others enabled.
-->
