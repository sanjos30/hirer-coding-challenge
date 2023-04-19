import pytest
import sys
from pyspark.sql import SparkSession
sys.path.insert(0, '../')
from src.hirer_coding_challenge.class_pyspark_client import SparkClient

@pytest.fixture(scope="module")
def spark():
    spark = SparkSession.builder.appName("test").master("local").getOrCreate()
    yield spark
    spark.stop()

@pytest.fixture(scope="module")
def spark_client():
    config = {
        "spark_conf": {
            "master": "local",
            "appname": "test"
        }
    }
    spark_client = SparkClient(config)
    yield spark_client

def test_create_spark_session(spark, spark_client):
    session = spark_client.create_spark_session({})
    assert isinstance(session, SparkSession)
    assert session.version == spark.version
