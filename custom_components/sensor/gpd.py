import requests
from datetime import timedelta

from homeassistant.const import CONF_URL, TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle

# https://home-assistant.io/developers/platform_example_sensor/
# https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/components/binary_sensor/nest.py
# https://github.com/cyberjunky/home-assistant-custom-components/blob/master/sensor/solarportal.py

SENSOR_PREFIX = 'Trash '
TRASH_TYPES = [{1: "rest"}, {3: "gft"}, {87: "papier"}]
MIN_TIME_BETWEEN_UPDATES = timedelta(hours=1)


def setup_platform(hass, config, add_devices, discovery_info=None):

    # """Setup the sensor platform."""
    url = config.get(CONF_URL)
    data = TrashCollectionSchedule(url, TRASH_TYPES)

    devices = []
    for trash_type in TRASH_TYPES:
        for t in trash_type.values():
            devices.append(TrashCollectionSensor(t, data))
    add_devices(devices)


class TrashCollectionSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, name, data):
        """Initialize the sensor."""
        self._state = None
        self._name = name
        self.data = data

    @property
    def name(self):
        """Return the name of the sensor."""
        return SENSOR_PREFIX + self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self.data.update()
        for d in self.data.data:
            if d['shortcode'] == self._name:
                self._state = d['pickup_date']


class TrashCollectionSchedule(object):

    def __init__(self, url, trash_types):
        self._url = url
        self._trash_types = trash_types
        self.data = None

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        response = requests.get(self._url)
        content = response.json()
        tschedule = []
        for item in content:
            for id in self._trash_types:
                if int(item['id']) in id.keys():
                    trash = {}
                    trash['shortcode'] = (next(iter(id.values())))
                    trash['id'] = item['id']
                    trash['pickup_date'] = item['ophaaldatum']
                    tschedule.append(trash)
        self.data = tschedule
