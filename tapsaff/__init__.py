"""
Represent the status of aps-aff for a specified location
"""

import requests

class TapsAff(object):
    """tapsaff object with location"""

    def __init__(self, location):
        """Initialize with a location such as a UK postcode or city"""

        self.location = location

    @property
    def is_taps_aff(self):
        """Returns True if taps aff for this location"""

        request = requests.get('http://www.taps-aff.co.uk/api/%s' % self.location)
        if request.status_code == 200:
            try:
                taps = request.json()['taps']['status']
                if taps == 'aff':
                    return True
                elif taps == 'oan':
                    return False
                else:
                    raise RuntimeError("Unexpected taps value: %s" % taps)
            except ValueError:
                raise RuntimeError("Unexpected response from service")
        else:
            raise IOError("Failure downloading from Api")