Example of View Assist device configuration using packages.
Includes additional entries needed for some VAX features.

New attributes:
```
adb_device: "media_player.(name)"
fkb_device: "(Fully Kiosk Browser device name)"
```
<!-- sound_device: "media_player.(name) -->

### ADB Setup
- Add integration [Android Debug Bridge](https://www.home-assistant.io/integrations/androidtv)
- Type in Device IP address
  - Recommend reserving IP adress in your network
- Submit
- In your View Assist device config, add:
  - `adb_device: "media_player.(name)"` 
<!-- -->
