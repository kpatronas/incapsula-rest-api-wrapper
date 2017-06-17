import requests
import time
import sys

__author__ = "Kostas Patronas"
__copyright__ = "Copyright 2017"
__license__ = "GNU"
__version__ = "1.1.0"
__maintainer__ = "Kostas Patronas"
__email__ = "kpatronas@gmail.com"
__status__ = "Production"


class incapsula:

    def __init__(self, api_id=None, api_key=None):
        '''
        Input api_id, api_key
        '''
        self.incapsula_stats_url = 'https://my.incapsula.com/api/stats/v1'

        if api_id is None:
            self.__die(msg='No parameter is given for api_id')

        if api_key is None:
            self.__die(msg='No parameter is given for api_key')

        self.api_id = api_id
        self.api_key = api_key

    def __date2epochms(self, date_time):
        '''
        Convert timestamp to epoch miliseconds
        '''
        pattern = '%d-%m-%Y %H:%M:%S'
        try:
            return int(time.mktime(time.strptime(date_time, pattern)))
        except Exception as ex:
            self.__die(
                msg='%s is not a valid date, valid pattern: %s'%
                (date_time, pattern))

    def __die(self, msg):
        '''
        Print errors to stderr and die
        '''
        sys.stderr.write('Error: %s \n'%(msg))
        sys.exit(1)

    def stats(self,
              account_id=None,
              time_range=None,
              start=None,
              end=None,
              site_id=None,
              stats=None,
              granularity=None):
        '''
        Generic function to get statistics
        '''
        if start:
            start = int(self.__date2epochms(date_time=start)) * 1000
        if end:
            end = int(self.__date2epochms(date_time=end)) * 1000
        parameters = {'api_id': self.api_id,
                      'api_key': self.api_key,
                      'account_id': account_id,
                      'time_range': time_range,
                      'start': start,
                      'end': end,
                      'site_id': site_id,
                      'stats': stats,
                      'granularity': granularity}
        r = requests.post(self.incapsula_stats_url, params=parameters)
        return r.text
