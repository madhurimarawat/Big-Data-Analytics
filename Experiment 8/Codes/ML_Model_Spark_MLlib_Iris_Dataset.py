"""
This script demonstrates how to train a machine learning model using Apache Spark's MLlib 
on the Iris dataset. The script performs the following tasks:

1. Initializes a Spark session for distributed processing.
2. Loads the Iris dataset from the sklearn library.
3. Converts the dataset into a PySpark DataFrame.
4. Preprocesses the data by converting categorical target labels into numeric values and 
   assembling feature columns into a vector.
5. Splits the dataset into training and testing sets.
6. Trains a Decision Tree classifier model on the training data.
7. Makes predictions on the test data.
8. Evaluates the model's performance using accuracy as the metric.
9. Outputs the classification results and a classification report.
10. Stops the Spark session to release resources.

Dependencies:
- PySpark
- Pandas
- scikit-learn
"""

# Importing Required Libraries
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from sklearn.datasets import load_iris
import pandas as pd

# Initialize Spark session
spark = SparkSession.builder.appName("Iris Dataset ML with Spark MLlib").getOrCreate()

# Load Iris dataset using sklearn
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data["target"] = iris.target

# Convert Pandas DataFrame to PySpark DataFrame
df = spark.createDataFrame(data)

# Display dataset information
print("\nDataset Schema:")
df.printSchema()

print("\nFirst 5 rows of the dataset:")
df.show(5)

# Display dataset classes
print("\nClasses in the dataset:")
for index, target_name in enumerate(iris.target_names):
    print(f"Class {index}: {target_name}")

# Feature and Target setup
features = iris.feature_names
target = "target"

# Convert categorical target variable to numeric using StringIndexer (optional for non-numeric targets)
indexer = StringIndexer(inputCol=target, outputCol="label")
df = indexer.fit(df).transform(df)

# Assemble features into a single vector column
assembler = VectorAssembler(inputCols=features, outputCol="features")
df = assembler.transform(df)

# Split data into training and testing sets
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

# Initialize Decision Tree Classifier
dt = DecisionTreeClassifier(featuresCol="features", labelCol="label")

# Train the model
model = dt.fit(train_df)

# Make predictions
predictions = model.transform(test_df)

# Display predictions
print("\nPredictions on test data:")
predictions.select("features", "label", "prediction").show(10)

# Evaluate model performance
evaluator = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="accuracy"
)
accuracy = evaluator.evaluate(predictions)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Classification report
print("\nClassification Report:")
predictions.groupBy("label", "prediction").count().show()

# Stop Spark session
spark.stop()
