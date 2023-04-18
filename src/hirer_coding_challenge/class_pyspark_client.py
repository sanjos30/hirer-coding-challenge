#!/usr/bin/python

from pyspark.sql import SparkSession

class SparkClient:
    """ handles all spark related tasks
    """

    def __init__(self, config: dict) -> None:
        self.config = config
        self.debug_dir = "/tmp/spark"
    
    def create_spark_session(self, kwargs:dict):
        try:
            # read config file entries
            master = kwargs.get('spark_conf', {}).get('master', 'local[*]')
            app_name = kwargs.get('spark_conf', {}).get('appname', 'local[*]')
            spark_builder = SparkSession.builder.appName(app_name).master(master)
            return spark_builder.getOrCreate()
        except Exception as e:
            print("An error occurred while creating spark session {}", e)