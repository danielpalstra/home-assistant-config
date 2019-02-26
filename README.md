# Home Assistant Configuration

[![Build Status](https://travis-ci.org/danielpalstra/home-assistant-config.svg?branch=master)](https://travis-ci.org/danielpalstra/home-assistant-config)

This repository contains my [Home Assistant](https://home-assistant.io/) (hass) configuration. I have installed hass on a [HP Proliant MicroServer Gen8](https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-c03793258) with 16GB RAM and 2 disks of 3 TB. I am currently running Ubuntu 16.04 LTS on the MicroServer and using Docker to deploy Home Assistant.

I try to keep track of the latest Home Assistant versions and update this repository regularly. 

## Deployment

I use [Docker](https://www.docker.com/) ([docker-compose](https://docs.docker.com/compose/)) to deploy Home Assistant. To support the [Xiaomi](https://www.mi.com/global/) bridge I run the container in network: host mode. 

```yaml
version: '3'
services:
  homeassistant:
    container_name: homeassistant
    image: homeassistant/home-assistant:latest
    volumes:
      - /srv/homeassistant/config:/config
      - /etc/localtime:/etc/localtime:ro
    devices:
      - /dev/ttyUSB0:/dev/ttyUSB0
      - /dev/ttyACM0:/dev/ttyACM0
      - /dev/ttyACM1:/dev/ttyACM1
      - /dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_857303138363517161D2-if00:/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_857303138363517161D2-if00
    network_mode: host
    restart: unless-stopped
```

## Other components

Next to a bunch of other stuff I run the following components to make my house smart. 

* [Home Assistant](https://home-assistant.io/)
* [Mosquitto](https://mosquitto.org/) for MQTT messaging
* [Zigbee2MQTT](https://github.com/Koenkk/zigbee2mqtt) to connect Xiaomi devices to MQTT
* [Node-RED](https://nodered.org/) to build complex automations
* [Traefik](https://traefik.io/) as a reverse proxy

## Some of the devices and services that I use with HA

  * [Aeotec Z-Stick Gen5](https://www.amazon.com/dp/B00X0AWA6E/) for Z-Wave control
    * I own a Fibaro Dimmer 2 and a Fibaro Roller shutter which are currently not in use.
  * Multiple [ESP8266](https://en.wikipedia.org/wiki/ESP8266) sensors built on top of [ESPEasy](https://en.wikipedia.org/wiki/ESP8266) and [Tasmota](https://github.com/arendst/Sonoff-Tasmota). I am currently considering moving to [esphomelib](https://esphomelib.com/) instead.
  * [Xiaomi Aqara](https://www.aliexpress.com/item/Original-Xiaomi-Smart-Gateway-2-Intelligent-Web-Wifi-Radio-and-Ringbell-Smart-Window-and-Door-Sensor/32816289388.html) for Zigbee sensors
    * Currently using [temperature/humidity](https://www.gearbest.com/access-control/pp_626702.html), [door/window](https://www.gearbest.com/smart-light-bulb/pp_257677.html), and [human body](https://www.gearbest.com/alarm-systems/pp_659226.html) sensors
  * Presence and security

    * I use a [Tado](https://www.tado.com) smart thermostat to keep our house warm and keep track of who is home.
    * In the future I'll probably move to [OwnTracks](https://home-assistant.io/components/device_tracker.owntracks/),  [Geofency](https://home-assistant.io/components/device_tracker.geofency/) instead of Tado for keeping track of all our iOS devices
    * [iOS app](https://itunes.apple.com/us/app/home-assistant-companion/id1099568401?mt=8)
    * [Ring](https://home-assistant.io/components/ring/) doorbell for spying on the mailman
  * Networking
    * [Multiple Unifi Devices](https://www.ui.com/products/#unifi) for maintaining a stable and secure network
  * Lights and Switches
    * [Philips Hue](https://www2.meethue.com/nl-nl)
    * [Xiaomi Yeelight](https://nl.gearbest.com/smart-lighting/pp_424884.html)
  * Voice assistants
    * [Google Home](https://store.google.com/product/google_home), with [HA Cloud](https://home-assistant.io/components/cloud/)
    * [Amazon Echo Dot](https://www.amazon.com/dp/B01DFKC2SO/) with [HA Cloud](https://home-assistant.io/components/cloud/)
  * Media
    * [Sony Bravia](https://www.home-assistant.io/components/media_player.braviatv/) and [Sony HT ZF 9](https://www.home-assistant.io/components/media_player.songpal/)
    * [Google Cast](https://home-assistant.io/components/media_player.cast/) on my Nvidia Shield TV
  * Notifications:
    * [iOS ](https://home-assistant.io/docs/ecosystem/ios/notifications/basic/) and
  * Weather and Climate related
    * [Tado](https://home-assistant.io/components/ecobee/) for the livingroom which controls the whole house

## Lovelace

I've been using lovelace from the start and using it ever since. Will share some screenshots in the future. 

## Useful links

* [HA cheat sheet](/HASS%20Cheatsheet.md) for miscellaneous tips and tricks.
* [Arsaboo's Home Assistant Config](https://github.com/arsaboo/homeassistant-config) for forming the base of this README :-)