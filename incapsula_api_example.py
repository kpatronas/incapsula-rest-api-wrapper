#!/usr/bin/env python
import requests
import time
import sys
from incapsula import *

if __name__ == '__main__':

    # Create the stats object
    s = incapsula(api_id='1234567890', api_key='1234567890')

    # Example of the stats api using custom timeranges
    # More info at https://my.incapsula.com/api/docs/v1/data
    try:
        print s.stats(account_id='111111',
                      site_id='222222',
                      stats = 'visits_timeseries',
                      start='1-06-2017 00:00:00',
                      end='3-06-2017 00:00:00',
                      time_range='custom')
    except Exception as ex:
        print ex
