import time
import pandas as pd
from kafka import KafkaProducer
import json

# Load the dataset
df = pd.read_csv("rainfall in india 1901-2015.csv")

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)

# Send data to Kafka topic 'rainfall_data'
for index, row in df.iterrows():
    data = {
        "division": row["DIVISION"],
        "year": row["YEAR"],
        "jan": row["JAN"],
        "feb": row["FEB"],
        "mar": row["MAR"],
        "apr": row["APR"],
        "may": row["MAY"],
        "jun": row["JUN"],
        "jul": row["JUL"],
        "aug": row["AUG"],
        "sep": row["SEP"],
        "oct": row["OCT"],
        "nov": row["NOV"],
        "dec": row["DEC"],
        "annual": row["ANNUAL"],
        "jan_feb": row["Jan-Feb"],
        "mar_may": row["Mar-May"],
        "jun_sep": row["Jun-Sep"],
        "oct_dec": row["Oct-Dec"],
    }

    producer.send("rainfall_data", value=data)

# Ensure all messages are sent before closing
producer.flush()
producer.close()
