


If using stock View Assist device config, this blueprint behaves exactly the same way as the stock Device Functions Blueprint.
Features are unlocked automatically when View Assist device config uses different media players for mediaplayer_device & musicplayer_device, and when an adb_device is added.
If View Assist device config does not use separate media players, Music Player & can not be triggered.
If View Assist device config does not contain an adb_device, default volume controls will continue to target mediaplayer_device.

New features:

* voice commands for Music Player volume
* voice commands for TTS Player volume
* Default volume voice commands target adb_device (if it exists). This controls the devices volume the same way the hardware buttons do.
