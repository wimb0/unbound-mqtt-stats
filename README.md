# unbound-mqtt-stats

## Description

Collects metrics from Unbound and sends them to an MQTT server

## Getting started

### Execute

#### Command line

`python3 -m src.main <MQTT IP> <MQTT User> <MQTT Password>[--no-reset] [--debug]`

optional parameter:

* "--no-reset" ("-nr") avoid to reset unbound statistics
* "--debug" set loglevel to DEBUG

#### Cronjob

`05 0 * * * cd <PATH> ; python3 -m src.main <MQTT IP> <MQTT User> <MQTT Password>[--no-reset] [--debug]`

### Requirements

* Python 3.8 or higher
* 
