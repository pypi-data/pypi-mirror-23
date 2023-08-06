"""
File: zone.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/bachya/regenmaschine
"""

# -*- coding: utf-8 -*-

import regenmaschine.api as api


class Zones(api.BaseAPI):
    """ An object to list, interact with, etc. zones """

    def __init__(self, *args, **kwargs):
        """ Initialize! """
        self.parent = super(Zones, self)
        self.parent.__init__(*args, **kwargs)

    def all(self, properties=False):
        """ Returns all zones (optionally showing advanced properties) """
        if properties:
            return self.parent.get('zone/properties').body

        return self.parent.get('zone').body

    def get(self, zone_id, properties=False):  # pylint: disable=arguments-differ
        """ Returns information for a specific zone """
        if properties:
            return self.parent.get('zone/{}/properties'.format(zone_id)).body

        return self.parent.get('zone/{}'.format(zone_id)).body

    def simulate(self, zone_data):
        """
        Simulates a zone activity (based on advanced zone properties)
        """
        return self.parent.post('zone/simulate', data=zone_data).body

    def start(self, zone_id, seconds):
        """ Starts a zone for a specific number of seconds """
        return self.parent.post(
            'zone/{}/start'.format(zone_id), data={'time': seconds}).body

    def stop(self, zone_id):
        """ Stops a zone """
        return self.parent.post('zone/{}/stop'.format(zone_id)).body
