import os

import findspark
import pytest


def update_spark_home(spark_home):
    """Set SPARK_HOME with provided path and perform all required
    configuration to make pyspark importable.
    """

    if spark_home is not None:
        spark_home = os.path.abspath(spark_home)
        if not os.path.exists(spark_home):
            raise OSError(
                "SPARK_HOME path specified in config does not exist: %s"
                % spark_home)

    findspark.init(spark_home)


def pytest_addoption(parser):
    parser.addini('spark_home', 'Spark install directory (SPARK_HOME).')


def pytest_configure(config):
    spark_home = config.getini('spark_home')

    if spark_home:
        update_spark_home(spark_home)


@pytest.fixture(scope='session')
def spark_context():
    """Return a SparkContext instance with reduced logging
    (session scope).
    """

    from pyspark import SparkContext

    sc = SparkContext()

    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.OFF)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.OFF)

    yield sc

    sc.stop()


@pytest.fixture(scope='session')
def spark_session():
    """Return a Hive enabled SparkSession instance with reduced logging
    (session scope).

    Available from Spark 2.0 onwards.
    """

    from pyspark import __version__ as spark_version

    if spark_version.startswith('0') or spark_version.startswith('1'):
        raise Exception(
            'The "spark_session" fixture is only available on spark 2.0 '
            'and above. Please use the spark_context fixture and instanciate '
            'a SQLContext or HiveContext from it in your tests.'
        )

    from pyspark.sql import SparkSession

    spark_session = SparkSession.builder.enableHiveSupport().getOrCreate()
    sc = spark_session.sparkContext

    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.OFF)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.OFF)

    yield spark_session

    spark_session.stop()
