import requests
import time
import sys

__author__ = "Kostas Patronas"
__copyright__ = "Copyright 2017"
__license__ = "GNU"
__version__ = "1.0.0"
__maintainer__ = "Kostas Patronas"
__email__ = "kpatronas@gmail.com"
__status__ = "Production"


class stats:

    def __init__(self, api_id=None, api_key=None):
        '''
        Input api_id, api_key
        '''
        self.error_flag = False
        self.error_msg = []
        self.error_must_exit = False
        self.debug = True
        self.incapsula_stats_url = 'https://my.incapsula.com/api/stats/v1'

        if api_id is None:
            self.error_msg.append('No parameter is given for api_id')
            self.error_flag = True
            self.error_must_exit = True

        if api_key is None:
            self.error_msg.append('No parameter is given for api_key')
            self.error_flag = True
            self.error_must_exit = True

        if self.error_flag:
            self.__die(must_die=self.error_must_exit)

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
            self.error_msg.append(
                '%s is not a valid date, valid pattern: %s' %
                (date_time, pattern))
            self.error_must_exit = True
            self.__die(must_die=self.error_must_exit)

    def __die(self, must_die):
        '''
        Print errors to stderr and die
        '''
        for err in self.error_msg:
            sys.stderr.write('Error: %s \n' % (err))
        if must_die:
            sys.exit(1)

    def visits_timeseries(self,
                          account_id=None,
                          time_range=None,
                          start=None,
                          end=None,
                          site_id=None,
                          granularity=None):
        '''
        Get Number of visits by type (Humans/Bots) over time
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='visits_timeseries',
                             granularity=granularity)
        return r

    def hits_timeseries(self,
                        account_id=None,
                        time_range=None,
                        start=None,
                        end=None,
                        site_id=None,
                        granularity=None):
        '''
        Get Number of hits by type (Humans/Bots/Blocked) over
        time and per second
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='hits_timeseries',
                             granularity=granularity)
        return r

    def bandwidth_timeseries(self,
                             account_id=None,
                             time_range=None,
                             start=None,
                             end=None,
                             site_id=None,
                             granularity=None):
        '''
        Get Amount of bytes (bandwith) and bits per second (throughput)
        transferred via the Incapsula network from clients to proxy
        servers and vice-versa over time.
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='bandwidth_timeseries',
                             granularity=granularity)
        return r

    def requests_geo_dist_summary(self,
                                  account_id=None,
                                  time_range=None,
                                  start=None,
                                  end=None,
                                  site_id=None,
                                  stats=None,
                                  granularity=None):
        '''
        Get Total number of requests routed via the Incapsula network by
        datacenter location
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='requests_geo_dist_summary',
                             granularity=granularity)
        return r

    def visits_dist_summary(self,
                            account_id=None,
                            time_range=None,
                            start=None,
                            end=None,
                            site_id=None,
                            granularity=None):
        '''
        Get Total number of visits per client application and country
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='visits_dist_summary',
                             granularity=granularity)
        return r

    def caching(self,
                account_id=None,
                time_range=None,
                start=None,
                end=None,
                site_id=None,
                granularity=None):
        '''
        Get Total number of requests and bytes that were cached by the
        Incapsula network
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='caching',
                             granularity=granularity)
        return r

    def caching_timeseries(self,
                           account_id=None,
                           time_range=None,
                           start=None,
                           end=None,
                           site_id=None,
                           granularity=None):
        '''
        Get Number of requests and bytes that were cached by the
        Incapsula network, with one day resolution, with info regarding
        the caching mode (standard or advanced)
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='caching_timeseries',
                             granularity=granularity)
        return r

    def threats(self,
                account_id=None,
                time_range=None,
                start=None,
                end=None,
                site_id=None,
                granularity=None):
        '''
        Get Total number of threats by type with additional information
        regarding security rules configuration
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='threats',
                             granularity=granularity)
        return r

    def incap_rules(self,
                    account_id=None,
                    time_range=None,
                    start=None,
                    end=None,
                    site_id=None,
                    granularity=None):
        '''
        Get List of incapRules with total number of reported incidents
        for each rule
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='incap_rules',
                             granularity=granularity)
        return r

    def incap_rules_timeseries(self,
                               account_id=None,
                               time_range=None,
                               start=None,
                               end=None,
                               site_id=None,
                               granularity=None):
        '''
        Get List of incapRules with a series of reported incidents for
        each rule with the specified granularity
        '''
        r = self.__get_stats(account_id=account_id,
                             time_range=time_range,
                             start=start,
                             end=end,
                             site_id=site_id,
                             stats='incap_rules_timeseries',
                             granularity=granularity)
        return r

    def __get_stats(self,
                    account_id=None,
                    time_range=None,
                    start=None,
                    end=None,
                    site_id=None,
                    stats=None,
                    granularity=None):
        '''
        Private generic function to get statistics
        '''
        if start:
            start = int(self.__date2epochms(date_time=start)) * 1000
        if end:
            end = int(self.__date2epochms(date_time=end)) * 1000
        try:
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
        except requests.exceptions.RequestException as ex:
            print ex
            sys.exit(1)
