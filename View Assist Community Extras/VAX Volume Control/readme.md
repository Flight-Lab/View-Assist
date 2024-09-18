> [!WARNING]
> This blueprint will eventually be merged into VAX Device Control

<!--[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://gist.github.com/Flight-Lab/ed20af4f6f7a4a5258a668317ae61671)-->

Decreases music volume when triggered by wake-word or broadcast, raises music volume when TTS ends. 
Must make new automation for each device. 
Requires the use of separate and unique media_players for mediaplayer_device (recommend using a reliable media_player that does not go unavailable) and musicplayer_device variables in View Assist device config.


### To-Do
- [ ] Store and reset volume levels
