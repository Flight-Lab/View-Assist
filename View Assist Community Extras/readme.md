Lorem Ipsum.
<!--
View Assist Extras


What is it?

View Assist Extras (VAX) are a collection of edited files for the View Assist project. 
These edited files offer additional features unavailable with the stock VA setup.
The VAX files will behave exactly as the stock VA files do unless explicitly switched on from the blueprint input page, and/or have the additional prerequisite attributes needed in the VA device config file. 
The VA device config file is best setup as a package, containing the template sensor, timers, and group.


Additional Features

Features with a check do not require any changes to the stock VA device attributes
Features with a musical note require separate media players for music and TTS playback
features with a star require the creation of new attributes or other addition to the VA device package
Features specific to Fully Kiosk Browser will have a blue F. The intention will be duplicate the feature for wall panel.
^subtext this somewhere^


Blueprints:
  device control
    features
      * The ability to use a toggle to choose between default intent view
      * On Home Assistant server startup, Fully Kiosk Browser loads the start URL. 
        Requires `fkb_device: ` in config file.
      * Set music mode and navigate to music view when the musicplayer_device starts playing. 
        Previously this only happened when playing music using the play music voice command, now this functions when music playback is started from any trigger.
      * Music Mode/View timeout sets normal mode and returns to default home page when music playback has been stopped for a set amount of time. 
        Previously, this would only happen when using the "stop music" voice command. This feature can be disabled by setting music timeout to 0.
  device functions
    features
  
View Assist device config file
  explain idea behind each attribute
    ^collapse section^
  packages


media player notes:


please ignore this, I need to structure and build out but don't have the time. This is an extremely rough and unfinished outline.


-->
