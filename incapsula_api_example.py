#!/usr/bin/env python
import requests
import time
import sys
from incapsula import stats

if __name__ == '__main__':

    # Create the stats object
    s = stats(api_id='1234567890', api_key='1234567890')

    # Example of the stats api using custom timeranges
    # More info at https://my.incapsula.com/api/docs/v1/data
    print s.visits_timeseries(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')
    print s.hits_timeseries(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')
    print s.bandwidth_timeseries(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')
    print s.requests_geo_dist_summary(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')
    print s.visits_dist_summary(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')
    print s.caching(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')
    print s.caching_timeseries(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')
    print s.threats(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')
    print s.incap_rules(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')
    print s.incap_rules_timeseries(account_id='111111', site_id='222222', start='1-06-2017 00:00:00', end='3-06-2017 00:00:00', time_range='custom')

    # Example of the stats api using pre-defined timeranges
    # More info at https://my.incapsula.com/api/docs/v1/data
    print s.visits_timeseries(account_id='111111', site_id='222222', time_range='today')
    print s.hits_timeseries(account_id='111111', site_id='222222', time_range='today')
    print s.bandwidth_timeseries(account_id='111111', site_id='222222', time_range='today')
    print s.requests_geo_dist_summary(account_id='111111', site_id='222222', time_range='today')
    print s.visits_dist_summary(account_id='111111', site_id='222222', time_range='today')
    print s.caching(account_id='111111', site_id='222222', time_range='today')
    print s.caching_timeseries(account_id='111111', site_id='222222', time_range='today')
    print s.threats(account_id='111111', site_id='222222', time_range='today')
    print s.incap_rules(account_id='111111', site_id='222222', time_range='today')
    print s.incap_rules_timeseries(account_id='111111', site_id='222222', time_range='today')
