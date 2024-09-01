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

    normalized_stocks_df = spark.read.option("multiline", "true") \
        .json("../datalake/bronze_layer/stocks.json")
    clients_df = spark.read.csv("../datalake/bronze_layer/Clients.csv", header=True, inferSchema=True)
    collaterals_df = spark.read.csv("../datalake/bronze_layer/Collaterals.csv", header=True, inferSchema=True)
    normalized_stocks_df.show()

    combined_df = clients_df.join(collaterals_df, clients_df.client_id == collaterals_df.client, "inner")
    combined_df.show()
    collateral_status_df = combined_df.join(normalized_stocks_df, combined_df.stock_id == normalized_stocks_df.stock_id,
                                            "left") \
        .groupBy("client_id") \
        .agg(f.sum(col("savings")+col("cars")+col("current_price")).alias("Total_asset_value")

    )

    collateral_status_df.show()
    collateral_status_df.write.mode(saveMode="overwrite").format("delta").save("../datalake/silver_layer/delta-table")


if __name__ == "__main__":
    read_data()
