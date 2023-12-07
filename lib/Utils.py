from pyspark.sql import SparkSession


def get_spark_session(env):
    if env == "LOCAL":
        return SparkSession.builder \
            .config('spark.driver.extraJavaOptions',
                    '-Dlog4j.configuration=file:log4j.properties') \
            .master("local[2]") \
            .enableHiveSupport() \
            .getOrCreate()
    else:
        return SparkSession.builder \
            .enableHiveSupport() \
            .getOrCreate()


def load_df(spark,type,path):
    return spark.read.format(type).option("inferSchema", "true").option("header", "true").\
        load(path)