# Import
import pyspark
from pyspark.sql.functions import col
from pyspark.sql import functions as f
from delta import *


def read_data():
    builder = pyspark.sql.SparkSession.builder.appName("creditLending") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    stocks_df = spark.read.option("multiline", "true") \
        .json("../datalake/bronze_layer/stocks.json")
    clients_df = spark.read.csv("../datalake/bronze_layer/Clients.csv", header=True, inferSchema=True)
    collaterals_df = spark.read.csv("../datalake/bronze_layer/Collaterals.csv", header=True, inferSchema=True)

    # save to silver layer
    stocks_df.write.mode(saveMode="overwrite").format("delta").save("../datalake/silver_layer/stocks-table")
    clients_df.write.mode(saveMode="overwrite").format("delta").save("../datalake/silver_layer/client-table")
    collaterals_df.write.mode(saveMode="overwrite").format("delta").save("../datalake/silver_layer/collaterals-table")


if __name__ == "__main__":
    read_data()
