# unbound-mqtt-stats

## Description

Collects metrics from Unbound and sends them to an MQTT server

## Getting started

Install python3, mosquitto-clients, git.

git clone this repo

### Execute

#### Command line

`python3 main.py <MQTT IP> <MQTT User> <MQTT Password> [--no-reset] [--debug]`

optional parameter:

* "--no-reset" ("-nr") avoid to reset unbound statistics
* "--debug" set loglevel to DEBUG

#### Cronjob

`*/5 * * * * python3 <PATH>/main.py <MQTT IP> <MQTT User> <MQTT Password> [--no-reset] [--debug]`

### Requirements

* Python 3.8 or higher
* mosquitto-clients
