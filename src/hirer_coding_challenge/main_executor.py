#!/usr/bin/python

from .helper import read_spark_config_file
from .constants import SPARK_CONFIG_PATH, DATA_FILE_FOLDER_PATH
from .class_pyspark_client import SparkClient
from .answers import answers as a

def execute_main():
    """ purpose of this function is to answer all the 12 questions for the technical coding challenge.
        All the questions are considered to be equivalent of a job and this funtion is responsible to 
        execute all the 12 jobs. This is done in 2 steps:
            1. reading raw data (json) into a spark dataframe
            2. answer all the questions
    """

    # create the spark session from the config file
    spark_conf = read_spark_config_file(SPARK_CONFIG_PATH)
    spark = SparkClient(config={}).create_spark_session(spark_conf)

    dataframe = spark.read.json(DATA_FILE_FOLDER_PATH)
    print(dataframe.printSchema())

    print("Data read OK")

    
    for i in dir(a):
        item = getattr(a,i)
        if callable(item):
            item()

if __name__ == '__main__':
    execute_main()