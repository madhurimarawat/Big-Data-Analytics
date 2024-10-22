from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test Spark").getOrCreate()

data = [("Hello, Spark!",)]

df = spark.createDataFrame(data, ["message"])

df.show()
spark.stop()
