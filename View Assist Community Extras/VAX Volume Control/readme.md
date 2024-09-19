# Music Volume Control during Assist & Broadcast
**What this blueprint does:**
When Assist or Broadcast is triggered while music playback is occuring, music volume is stored and decreased by 50% and returns to initial music volume when no STT is detected or when TTS ends.

> [!WARNING]
> This blueprint will eventually be merged into VAX Device Control

> [!important]
> REQUIRES the mediaplayer_device and musicplayer_device in your View Assist device config file to use separate media_player entities. These features rely on using media_player state change as a trigger, so the media players must also be stable, remain available, and display reliable state changes between idle & playing. Remember to also use the mediaplayer_device media_player in Stream Assist.
>
> Must make new automation for each device. 

## Recommended Media Players:
* **musicplayer_device:** [Snapcast](https://play.google.com/store/apps/details?id=de.badaix.snapcast&hl=en_US) (only exposed by Music Assistant) **FREE**
* **mediaplayer_device:** [AirReceiver](https://play.google.com/store/apps/details?id=com.softmedia.receiver&hl=en_US) audio (only exposed by Music Assistant) **$2.99**
<details>

<summary>AirReceiver Setup:</summary>

1) In AirReceiver settings, make sure both Airplay <sub>IOS Media Receiver</sub> and AirTunes Audio <sub>AirPort Express Speaker</sub> are selected. The media_player entity we want to use is only made when both of these are checked.
(You do not need the other options selected for this but they will not harm anything if you choose to).

3) Scroll down and select Advanced Settings.

4) Set AirTunes Audio Latency (ms) to 0(ms)

5) Check AirTunes UI [✓]

The media player entity we want to use will be created by the Music Assistant integration and will be called `media_player.lenovostarview_(last 3 digits of device ip)_audio`  
ex. `media_player.lenovostarview_180_audio`  
This media player has volume controls separate from the android device volume controls, just like the Snapcast media player.
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

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://gist.github.com/Flight-Lab/ed20af4f6f7a4a5258a668317ae61671)

