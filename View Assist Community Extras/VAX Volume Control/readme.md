# Music Volume Control during Assist & Broadcast

> [!CAUTION] 
> ## **This is __NOT__ an official View Assist blueprint and therefor is NOT supported by Dinki and the View Assist team.**

> [!WARNING]
> This blueprint will eventually be merged into [VAX Device Control](https://github.com/Flight-Lab/View-Assist/blob/Extras/View%20Assist%20Community%20Extras/VAX%20Device%20Control/readme.md)

## Functionality Overview:  
When triggered by wake word or the Broadcast automation during music playback, the music volume is reduced by 50%.  
If no speech-to-text (STT) is detected or when text-to-speech (TTS) finishes, the volume is reset to its original level. 

* Includes option to play a notification sound when STT is not detected and ceases listening. Notification sound does not play when musicplayer_device is playing, because the music volume ducking acts as this signifier.  
**\*Must make new automation for each device.\***

## Prerequisites:
To use this blueprint, the mediaplayer_device and musicplayer_device must be separate media_player entities in your View Assist device configuration. These features rely on state changes as triggers, so media players must be stable, always available, and display reliable state changes between idle and playing. Remember to also use the mediaplayer_device media_player in Stream Assist.

## Recommended Media Players:
* **musicplayer_device:** [Snapcast](https://play.google.com/store/apps/details?id=de.badaix.snapcast&hl=en_US) (only exposed by Music Assistant) **FREE**
* **mediaplayer_device:** [Air Receiver](https://play.google.com/store/apps/details?id=com.softmedia.receiver&hl=en_US) audio (only exposed by Music Assistant) **$2.99**
<details>

<summary>Air Receiver Setup:</summary>

1) In AirReceiver settings, make sure both Airplay <sub>IOS Media Receiver</sub> and AirTunes Audio <sub>AirPort Express Speaker</sub> are selected. The media_player entity we want to use is only made when both of these are checked.
(I recommend unchecking the other options as they will create even more media player entities. One even creates a media server.)

2) Scroll down and select Advanced Settings.

3) Set AirTunes Audio Latency (ms) to 0(ms)

4) Check AirTunes UI [✓]

The media player entity we want to use will be created by the Music Assistant integration and will be named `media_player.lenovostarview_(last 3 digits of device ip)_audio`  
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

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://gist.github.com/Flight-Lab/ed20af4f6f7a4a5258a668317ae61671)

<!-- start.mp3 & end.mp3 were pulled from [this sound pack](https://pixabay.com/sound-effects/menu-buttom-pack-190019/) by [Liécio Rodriguez](https://pixabay.com/users/liecio-3298866/) via [Pixabay](https://pixabay.com/service/license-summary/)--> 

<!-- 
Other potential sounds: 
https://pixabay.com/sound-effects/90s-game-ui-1-185094/  
https://pixabay.com/sound-effects/90s-game-ui-10-185103/  
https://pixabay.com/sound-effects/click-buttons-ui-menu-sounds-effects-button-13-205396/
--> 
