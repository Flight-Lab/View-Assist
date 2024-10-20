# View Assist Extras Device Functions <sub>v 1.2.2 e 0.1.0</sub>
 **description**  
> [!CAUTION] 
> ## **This is an edited version of Dinki's View Assist Device Functions blueprint. This version includes community made features and is __NOT__ supported by Dinki and the View Assist team.**

> [!IMPORTANT]
> o

If using stock View Assist device config, this blueprint behaves exactly the same way as the stock Device Functions Blueprint.  
Features are unlocked automatically when View Assist device config uses different media players for mediaplayer_device & musicplayer_device, and when an adb_device is added.  
If View Assist device config does not use separate media players, Music Player & TTS Player volume commands cannot be triggered.  
If View Assist device config does not contain an adb_device, default volume controls will continue to target mediaplayer_device.
If using separate media players, there is the option to target musicplayer_device with the default voice commands while musicplayer_device is playing.


New features:

* voice commands for Music Player volume
* voice commands for TTS Player volume
* Default volume voice commands target adb_device (if it exists). This controls the device's volume the same way the hardware buttons do.
* Option to target musicplayer_device with the default voice commands while musicplayer_device is playing.

recommend using media players that have volume control independent from the device volume
Examples: 
* Snapcast
* Air Receiver airtunes audio


[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://gist.github.com/Flight-Lab/054a12df123f8b179feb4af7d90443c8)


To-Do:     
[ ] type real readme
