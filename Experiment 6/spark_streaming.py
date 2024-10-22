from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, from_json, count, min, max, mean
from pyspark.sql.types import StructType, StructField, StringType, FloatType

# Initialize Spark Session with reduced log output
spark = SparkSession.builder.appName("Real-Time Rainfall Data Processing").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")  # Set log level to ERROR to suppress INFO logs

# Read stream from Kafka topic 'rainfall_data'
kafka_stream = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "rainfall_data")
    .load()
)

# Deserialize the JSON data
schema = StructType(
    [
        StructField("division", StringType(), True),
        StructField("year", StringType(), True),
        StructField("jan", FloatType(), True),
        StructField("feb", FloatType(), True),
        StructField("mar", FloatType(), True),
        StructField("apr", FloatType(), True),
        StructField("may", FloatType(), True),
        StructField("jun", FloatType(), True),
        StructField("jul", FloatType(), True),
        StructField("aug", FloatType(), True),
        StructField("sep", FloatType(), True),
        StructField("oct", FloatType(), True),
        StructField("nov", FloatType(), True),
        StructField("dec", FloatType(), True),
        StructField("annual", FloatType(), True),
        StructField("jan_feb", FloatType(), True),
        StructField("mar_may", FloatType(), True),
        StructField("jun_sep", FloatType(), True),
        StructField("oct_dec", FloatType(), True),
    ]
)

# Parse the value column
parsed_stream = (
    kafka_stream.selectExpr("CAST(value AS STRING) ")
    .select(from_json(col("value"), schema).alias("data"))
    .select("data.*")
)

# Show column names and schema
parsed_stream.printSchema()

# Calculate descriptive statistics: count, min, max, mean, etc.
descriptive_stats = parsed_stream.groupBy("division").agg(
    count("*").alias("count"),
    min("annual").alias("min_annual_rainfall"),
    max("annual").alias("max_annual_rainfall"),
    mean("annual").alias("mean_annual_rainfall"),
)

# Write the descriptive statistics to the console
query = descriptive_stats.writeStream.outputMode("complete").format("console").start()

# Await termination (uncomment if we want it to run indefinitely)
query.awaitTermination()
