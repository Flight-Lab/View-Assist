# View Assist Extras Device Control
### Controls Device Display & Audio

> [!CAUTION] 
> ## **This is an edited version of Dinki's View Assist Device Control Automation. This version includes community made features and is __not__ supported by Dinki and the View Assist team.**

> [!IMPORTANT]
> Most of the extra features REQUIRE mediaplayer_device and musicplayer_device to use separate media_player entities. These features rely on using media_player state change as trigger, so the media players should be stable, remain available, and display reliable state changes between idle & playing.

## Recommended Media Players:
* **musicplayer_device:** [Snapcast](https://play.google.com/store/apps/details?id=de.badaix.snapcast&hl=en_US) (only exposed by Music Assistant) **FREE**
* **mediaplayer_device:** [AirReceiver](https://play.google.com/store/apps/details?id=com.softmedia.receiver&hl=en_US) audio (only exposed by Music Assistant) **$2.99**

> [!IMPORTANT]
> Remember to make this change in your View Assist configuration file and use the same mediaplayer_device media_player in Stream Assist.

<details>

<summary>other Confirmed Working Media Players:</summary>

* [Fully Kiosk Browser](https://play.google.com/store/apps/details?id=de.ozerov.fully&hl=en_US) media player (exposed by Music Assistant) 
> [!WARNING]
> If using the FKB media player, it must be the one exposed by Music Assistant or it will go unavailable and will not be able to act as a trigger.
>
> The FKB media player seems to have a delay between state changes and audio playback. 
> State will change from idle to playing and then audio playback will begin after a 1-2 second delay.
> Audio playback will end and then state will change from playing to idle after a 1-2 second delay.
> These delays lead to a feeling of decreased responsiveness.


</details>


## New section of blueprint input page labeled Extras contains:

# Extra features that do not require separate media_players:
* The ability to use a toggle to choose between default intent view and @mr.picc010's intent pop-up. (intent pop-up uses BrowserMod)

# Checks if separate media_players are used in Extras inputs and automatically enables the following features: 
* Set music mode and navigate to music view when media player used for musicplayer_device starts playing music. Previously this only happened when playing music using the play music voice command, now this functions when music playback is started from any trigger.
* Music Mode/View timeout sets normal mode and returns to default home page when music playback has been stopped for a set amount of time. Previously, this would only happen when using the "stop music" voice command. This feature can be disabled by setting music timeout to 0.
