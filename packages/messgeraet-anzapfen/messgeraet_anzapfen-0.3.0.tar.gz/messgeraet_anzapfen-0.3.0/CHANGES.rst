=========
Changelog
=========

Version 0.1
===========

- typo +metadaten
- led implemented, restructured the code and prepared for sensorplugins
- fertig bis auf led
- enable star import to keep the main.py simple(er-ish)
- add configtemplate
- sensors to own subdir
- new sensor
- parser for tables ready
- rename dir

Version 0.2
===========

- move sensor econsens3 to own repo
- reformat output of --print-known-sensors

Version 0.3
===========

- pep8/pylint wants self.data and self.config in the init of Sensor
- remove data/conttable.htm and move it to sensor_econsens3 repo
- use new blinking pattern for leds
- rename config entries
- improve logformat
- add timeout while sending data to logserver
- rename key
- add token manipulation tool, add token usage to anzapfen
