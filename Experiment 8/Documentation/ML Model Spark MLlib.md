<div style='text-align:center; color: #00B050'>
<h1 style='font-size: 16pt'>Author: Madhurima Rawat</h1>

<h2 style='font-size: 14pt'>Machine Learning Model Training with Spark MLlib</h2>

<h3 style='font-size: 12pt'>Train machine learning models on 
large datasets using Spark's MLlib library, and evaluate model performance using 
techniques such as cross-validation and model selection.</h3>
</div>

<h2 style='color: #00B050;'>Introduction</h2>
<p>
Machine learning enables systems to learn and improve from data without explicit programming. Spark MLlib, a scalable machine learning library, allows you to process large datasets efficiently. It offers tools for classification, regression, clustering, and more, making it an ideal choice for big data machine learning tasks.
</p>

<h2 style='color: #00B050;'>Prerequisites</h2>
<p>
Before starting, ensure you have the following installed:
</p>
<ul>
    <li>Apache Spark (version 3.0 or later)</li>
    <li>Python (version 3.6 or later)</li>
    <li>PySpark library</li>
    <li>An IDE or notebook environment (e.g., Jupyter Notebook or PyCharm)</li>
</ul>

<h2 style='color: #00B050;'>Steps to Set Up</h2>
<ol>
    <li>Install Apache Spark and set it up in your environment.</li>
    <li>Install the PySpark library using <code>pip install pyspark</code>.</li>
    <li>Download or access the Iris dataset. This example uses the dataset from its online source.</li>
</ol>

<h2 style='color: #00B050;'>Code</h2>

```python
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
print(f"\nModel Accuracy: {accuracy \* 100:.2f}%")

# Classification report

print("\nClassification Report:")
predictions.groupBy("label", "prediction").count().show()

# Stop Spark session

spark.stop()
```

<h2 style='color: #00B050;'>Explanation</h2>
<p>
<strong>Step 1:</strong> A Spark session is created to interact with the Spark framework. The <code>appName</code> identifies the application.<br>
<strong>Step 2:</strong> The Iris dataset is loaded, and column names are assigned for clarity.<br>
<strong>Step 3:</strong> Data preprocessing involves converting string labels to numeric using <code>StringIndexer</code> and assembling feature columns into a vector using <code>VectorAssembler</code>.<br>
<strong>Step 4:</strong> The dataset is split into training and testing subsets.<br>
<strong>Step 5:</strong> A Decision Tree Classifier is initialized for classification tasks.<br>
<strong>Step 6:</strong> Hyperparameter tuning is performed using <code>CrossValidator</code> with a parameter grid.<br>
<strong>Step 7:</strong> Model performance is evaluated on the test dataset using accuracy as the metric.<br>
<strong>Step 8:</strong> The Spark session is stopped to release resources.
</p>

### Spark MLlib and Explanation of Outputs

Apache Spark is a powerful, open-source distributed computing system that allows for the processing of large datasets quickly. It supports both batch and real-time data processing and provides several libraries for data analytics, including MLlib, which is Spark's machine learning library. Spark's ability to scale on clusters and its integration with Hadoop's distributed file system (HDFS) make it a top choice for big data processing. MLlib contains various algorithms for classification, regression, clustering, and collaborative filtering, and provides utilities for data preprocessing, feature extraction, and model evaluation.

#### Output and Explanation:

1. **Dataset Schema**:

   ```plaintext
   root
    |-- sepal length (cm): double (nullable = true)
    |-- sepal width (cm): double (nullable = true)
    |-- petal length (cm): double (nullable = true)
    |-- petal width (cm): double (nullable = true)
    |-- target: long (nullable = true)
   ```

   The schema describes the structure of the dataset:

   - The dataset contains five columns: four numerical feature columns (`sepal length (cm)`, `sepal width (cm)`, `petal length (cm)`, `petal width (cm)`) and one target column (`target`), which is a categorical variable representing the class of each iris flower.

2. **First 5 Rows of the Dataset**:

   ```plaintext
   +-----------------+----------------+-----------------+----------------+------+
   |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|target|
   +-----------------+----------------+-----------------+----------------+------+
   |              5.1|             3.5|              1.4|             0.2|     0|
   |              4.9|             3.0|              1.4|             0.2|     0|
   |              4.7|             3.2|              1.3|             0.2|     0|
   |              4.6|             3.1|              1.5|             0.2|     0|
   |              5.0|             3.6|              1.4|             0.2|     0|
   +-----------------+----------------+-----------------+----------------+------+
   only showing top 5 rows
   ```

   The first five rows of the dataset are displayed. Each row contains the measurements for the iris flowers' sepals and petals, as well as the target class. The target value `0` corresponds to the species "setosa."

3. **Classes in the Dataset**:

   ```plaintext
   Class 0: setosa
   Class 1: versicolor
   Class 2: virginica
   ```

   The dataset contains three classes of iris flowers:

   - `0`: Setosa
   - `1`: Versicolor
   - `2`: Virginica

4. **Predictions and Evaluations**:

   ```plaintext
   +-----------------+-----+----------+
   |         features|label|prediction|
   +-----------------+-----+----------+
   |[4.6,3.1,1.5,0.2]|  0.0|       0.0|
   |[4.8,3.4,1.6,0.2]|  0.0|       0.0|
   |[4.9,3.1,1.5,0.1]|  0.0|       0.0|
   |[5.4,3.7,1.5,0.2]|  0.0|       0.0|
   |[4.6,3.6,1.0,0.2]|  0.0|       0.0|
   |[5.0,3.0,1.6,0.2]|  0.0|       0.0|
   |[5.0,3.2,1.2,0.2]|  0.0|       0.0|
   |[5.4,3.4,1.5,0.4]|  0.0|       0.0|
   |[4.4,3.2,1.3,0.2]|  0.0|       0.0|
   |[5.0,3.5,1.3,0.3]|  0.0|       0.0|
   +-----------------+-----+----------+
   only showing top 10 rows
   ```

   The predictions show the predicted class (`prediction`) for each instance based on the features (`features`) of the iris flowers. For example, the first row's features correspond to the class `0.0` (Setosa), and the model predicted the same class.

5. **Model Accuracy**:

   ```plaintext
   Model Accuracy: 100.00%
   ```

   The model achieved 100% accuracy on the test dataset, meaning all predictions were correct.

6. **Classification Report**:
   ```plaintext
   +-----+----------+-----+
   |label|prediction|count|
   +-----+----------+-----+
   |  0.0|       0.0|   13|
   |  1.0|       1.0|    8|
   |  2.0|       2.0|   13|
   +-----+----------+-----+
   ```
   This table shows the distribution of predictions across the different classes. It confirms that the model correctly predicted all the instances for each class. The counts show how many instances of each class were predicted correctly, further validating the model's perfect accuracy.

### Additional Insights:

- The **Decision Tree Classifier** used in the model is a supervised learning algorithm. It splits the dataset into branches based on feature values and class labels, ultimately making predictions by following these decision paths.
- **Cross-validation** and **hyperparameter tuning** can further enhance model performance, though not covered in this basic example.
- **Accuracy**, though important, should be complemented with other evaluation metrics like precision, recall, and F1 score, especially in imbalanced datasets.

In conclusion, this Spark MLlib example demonstrates how to use Spark's distributed framework for machine learning on large datasets, process data efficiently, train a model, and evaluate its performance on a classification task with great accuracy.
