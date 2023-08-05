"""The hello command."""


from json import dumps, loads
import requests
import datetime as dt
try:
    from urllib.parse import urlencode
except ImportError:
     from urllib import urlencode
from .base import Base
from . import utils

class Counts(Base):

    def run(self):
        token = utils.get_saved_token()
        if token == False:
            return

        params =    (  
                        ('feed',self.options["<feeds>"]),
                        ('bins',self.options.get("bins") or '1h'),
                        ('starttime', self.options["--starttime"] or (dt.datetime.utcnow() - dt.timedelta(days=7)).isoformat() + 'Z'),
                        ('endtime', self.options["--endtime"] or dt.datetime.utcnow().isoformat() + 'Z'),
                        ('class', self.options["--class"] or 'pedestrian')
                    )
        r = requests.get(self.request_url + '/b/counts?' + urlencode(params), headers={ 'Authorization': 'JWT ' + token })
        is_expired = utils.check_if_expired(r)
        if not is_expired:
            print(dumps(loads(r.text), indent=4, sort_keys=True))
