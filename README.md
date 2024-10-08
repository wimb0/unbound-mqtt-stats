# unbound-mqtt-stats

## Description

Collects metrics from Unbound and sends them to an MQTT server

## Getting started

Install unbound-control, python3, mosquitto-clients, git.

git clone this repo

### Execute

#### Command line

`python3 -m src.main <MQTT IP> <MQTT User> <MQTT Password> [--no-reset] [--debug]`

optional parameter:

* "--no-reset" ("-nr") avoid to reset unbound statistics
* "--debug" set loglevel to DEBUG

#### Cronjob

`*/5 * * * * cd <PATH> ; python3 -m src.main <MQTT IP> <MQTT User> <MQTT Password> [--no-reset] [--debug]`

### Requirements

* Python 3.8 or higher
* mosquitto-clients
* unbound-control

###
Based on [unbound-statistics-publisher](https://github.com/Qaldak/unbound-statistics-publisher) by [@qaldak](https://github.com/qaldak)
