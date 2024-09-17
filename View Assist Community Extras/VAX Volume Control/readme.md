> [!WARNING]
> This blueprint will eventually be merged into VAX Device Control

Decreases music volume when triggered by wake-word or broadcast, raises music volume when TTS ends. 
Must make new automation for each device. 
Requires the use of separate and unique media_players for mediaplayer_device (recommend using a reliable media_player that does not go unavailable) and musicplayer_device variables in View Assist device config.


### To-Do
- [ ] Store and reset volume levels
