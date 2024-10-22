<div style='text-align:center; color: #00B050'>
<h1 style="font-size: 16pt">Author: Madhurima Rawat</h1>
<h2 style="font-size: 14pt">Large-Scale Data Analysis Using Apache Spark</h2>

<h3 style="font-size: 12pt">Performing distributed data processing with Apache Spark, leveraging RDD operations like filtering, mapping, and aggregation for efficient analysis of big data</h3>
</div>

---

### Table of Contents

1. [Introduction to Apache Spark](#introduction-to-apache-spark)
2. [Setting Up Apache Spark](#setting-up-apache-spark)
   1. [Download and Install Spark](#download-and-install-spark)
   2. [Configure Environment Variables](#configure-environment-variables)
   3. [Test Spark Installation](#test-spark-installation)
3. [Understanding Spark RDDs](#understanding-spark-rdds)
4. [Basic Operations on RDDs](#basic-operations-on-rdds)
   1. [Filtering](#filtering)
   2. [Mapping](#mapping)
   3. [Aggregation](#aggregation)
5. [Complete Code Example for Iris Dataset](#complete-code-example-iris)

---

<a name="introduction"></a>

## 1. Introduction

### **Apache Spark: Powerful Open-Source Processing Engine**

Apache Spark is an open-source, distributed data processing engine designed for large-scale data processing. It is known for its speed, ease of use, and its ability to handle sophisticated analytics, such as machine learning and graph processing. Spark operates on a cluster of machines, enabling parallel processing of tasks across datasets, making it ideal for handling massive amounts of data.

#### **Key Features of Apache Spark**:

- **Speed**: Spark processes data in memory, significantly improving performance compared to traditional disk-based systems like Hadoop's MapReduce. It can be up to 100x faster for large-scale data processing.
- **Ease of Use**: It provides high-level APIs in popular languages like Python, Scala, and Java. The APIs allow developers to process data efficiently without dealing with complex distributed systems.
- **Advanced Analytics**: Spark includes libraries for SQL queries (Spark SQL), machine learning (MLlib), graph processing (GraphX), and streaming data (Spark Streaming), making it a versatile tool for analytics.

#### **Real-Life Example: Big Data Analysis in Retail**:

A major retail company like Amazon can use Apache Spark to analyze millions of transactions every day to understand customer purchasing behavior. By processing data in real-time, Spark helps detect trends, such as popular products, buying patterns, and potential inventory issues. For instance, if a product starts selling out rapidly, Spark can trigger an automatic restocking process based on sales trends, reducing the risk of running out of stock.

---

<a name="setting-up-apache-spark"></a>

## Setting Up Apache Spark

The setup instructions remain the same as previously detailed for setting up Spark, configuring environment variables, and testing installation.

---

<a name="understanding-spark-rdds"></a>

## Understanding Spark RDDs

RDDs (Resilient Distributed Datasets) are the fundamental units of Spark, providing fault tolerance and allowing data to be processed in a distributed fashion. They are immutable and can be created from external datasets or in-memory collections.

---

<a name="basic-operations-on-rdds"></a>

## Basic Operations on RDDs

For the iris dataset (`encoded_iris.csv`), which contains the columns:
`['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']`

Let's explore how we can perform basic operations such as filtering, mapping, and aggregation on this dataset.

---

<a name="filtering"></a>

### Filtering

We can filter rows based on specific conditions. For example, we might want to filter flowers with a sepal length greater than 5.

```python
# Load data into RDD
iris_rdd = sc.textFile("encoded_iris.csv")

# Split the data by commas and filter for flowers with sepal
# length greater than 5
filtered_rdd = iris_rdd.map(lambda line:
line.split(",")).filter(lambda x: float(x[0]) > 5)

# Collect and print the filtered data
print("Filtered data (Sepal Length > 5):")
print(filtered_rdd.collect())
```

**Explanation:**

- **Loading the Data**: The `sc.textFile` method reads the data from the specified CSV file into an RDD (`iris_rdd`).
- **Mapping and Filtering**: The `map` function splits each line by commas, and the `filter` function selects only those records where the sepal length (first column) is greater than 5.
- **Collecting Results**: The `collect` method gathers the filtered results from all partitions and prints them.

---

<a name="mapping"></a>

### Mapping

Let's say we want to convert the `species` column to a more descriptive name based on the integer code.

```python
# Map function to convert species integer codes to their
# respective names
species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
mapped_rdd = iris_rdd.map(lambda line:
line.split(",")).map(lambda x: (float(x[0]),
float(x[1]), float(x[2]), float(x[3]),
species_mapping[int(x[4])]))

# Collect and print the transformed data
print("Mapped data with species names:")
print(mapped_rdd.collect())
```

**Explanation:**

- **Species Mapping**: A dictionary (`species_mapping`) is created to map integer codes to species names.
- **Double Mapping**: The first `map` splits the lines into individual columns, while the second `map` converts the values to their appropriate types (floats for the numeric columns and string for species) using the mapping dictionary.
- **Collecting Results**: The transformed data with species names is collected and printed.

---

<a name="aggregation"></a>

### Aggregation

Let's compute the average sepal width across all flowers in the dataset.

```python
# Aggregate the sum of sepal widths and the count of records
sum_and_count = mapped_rdd.map(lambda x: (x[1], 1))
.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]))

# Calculate average sepal width
average_sepal_width = sum_and_count[0] / sum_and_count[1]
print(f"Average sepal width: {average_sepal_width}")
```

**Explanation:**

- **Mapping for Aggregation**: The `map` function creates pairs of `(sepal_width, 1)` for each record.
- **Reducing to Calculate Sum and Count**: The `reduce` function aggregates the sums and counts of sepal widths.
- **Calculating Average**: The average is computed by dividing the total width by the count of records.

---

<a name="complete-code-example-iris"></a>

## Complete Code Example for Iris Dataset

Here’s a complete example that loads the iris dataset, performs filtering, maps values, and aggregates data.

```python
from pyspark import SparkContext, SparkConf

# Initialize SparkContext
conf = SparkConf().setAppName("Iris Data Analysis")
sc = SparkContext(conf=conf)

# Load the encoded Iris dataset
data = sc.textFile("encoded_iris.csv")

# Split the CSV lines into columns
rdd = data.map(lambda line: line.split(","))

# Get the header (first row)
header = rdd.first()

# Remove the header from the RDD
rdd = rdd.filter(lambda line: line != header)

# Print the entire encoded Iris dataset
print("\n\n\n\nEntire encoded Iris dataset:\n\n\n\n")
for row in rdd.collect():  # Collect and print all rows of the dataset
    print(row)  # Each row is printed as a list


# Create a dictionary to map species numbers to names
species_mapping = {"0": "Setosa", "1": "Versicolor", "2": "Virginica"}

# Print the entire mapped dataset with values
# first and species names last
print("\n\n\n====== Mapped Dataset (Values and Species) ======\n\n\n")
for row in rdd.collect():
    sepal_length = row[0]
    sepal_width = row[1]
    petal_length = row[2]
    petal_width = row[3]

    # Assuming the species number is in the last column
    species_num = row[4]
    species_name = species_mapping.get(
        species_num, "Unknown"
    )  # Get species name from the mapping

    # Print values followed by the species name
    print(
        f"Sepal Length: {sepal_length}, Sepal Width: {sepal_width},
        Petal Length: {petal_length},
        Petal Width: {petal_width}, Species: {species_name}"
    )

# Example processing: Calculate the average sepal length by species
species_sepal_length = rdd.map(
    lambda x: (species_mapping.get(x[4], "Unknown"), float(x[0]))
)  # (species, sepal_length)

# Calculate sum and count of sepal lengths for each species
sum_and_count = species_sepal_length.aggregateByKey(
    (0.0, 0),  # Initialize (sum, count)

    # Add value to sum and increment count
    lambda acc, val: (acc[0] + val, acc[1] + 1),
    lambda acc1, acc2: (acc1[0] + acc2[0],
    acc1[1] + acc2[1]),  # Merge accumulators
)

# Calculate average sepal length for each species
average_sepal_length = sum_and_count.mapValues(lambda x: x[0] / x[1])

# Print the average sepal length for each species
print("\n\n\n====== Average Sepal Length ======\n\n\n")
for species, avg_length in average_sepal_length.collect():
    print(f"{species}: {avg_length}")


# Calculate and print average for all columns grouped by species
def average_for_species(rdd):
    # Map to (species, (sepal_length, sepal_width,
    # petal_length, petal_width))
    species_values = rdd.map(
        lambda x: (
            species_mapping.get(x[4], "Unknown"),
            (float(x[0]), float(x[1]), float(x[2]), float(x[3])),
        )
    )

    # Sum and count for each species
    sum_and_count_all = species_values.aggregateByKey(
        (
            0.0,
            0.0,
            0.0,
            0.0,
            0,
        ),

        # Initialize (sum_length, sum_width,
        # sum_petal_length, sum_petal_width, count)

        lambda acc, val: (
            acc[0] + val[0],
            acc[1] + val[1],
            acc[2] + val[2],
            acc[3] + val[3],
            acc[4] + 1,
        ),
        lambda acc1, acc2: (
            acc1[0] + acc2[0],
            acc1[1] + acc2[1],
            acc1[2] + acc2[2],
            acc1[3] + acc2[3],
            acc1[4] + acc2[4],
        ),
    )

    # Calculate averages for all columns for each species
    average_all_columns = sum_and_count_all.mapValues(
        lambda x: (x[0] / x[4], x[1] / x[4], x[2] / x[4], x[3] / x[4])
    )

    return average_all_columns


# Calculate average for all columns grouped by species
average_values_by_species = average_for_species(rdd)

# Print average values for all columns by species
print("\n\n\n====== Average Values for All Columns by Species ======\n\n\n")

for species, averages in average_values_by_species.collect():
    print(
        f"Sepal Length: {averages[0]}, Sepal Width: {averages[1]},
        Petal Length: {averages[2]},
        Petal Width: {averages[3]}, Species: {species}"
    )

# Count number of instances per species
species_count = rdd.map(
    lambda x: (species_mapping.get(x[4], "Unknown"), 1)
).reduceByKey(lambda a, b: a + b)

# Print species counts
print("\n\n\n====== Count of Instances per Species ======\n\n\n")
for species, count in species_count.collect():
    print(f"{species}: {count}")

# Stop SparkContext
sc.stop()
```

**Explanation:**

- **Initialization**: The Spark context is initialized, and the dataset is loaded.
- **Data Processing**:
  - **RDD Creation**: The dataset is split into columns.
  - **Header Removal**: The header row is filtered out.
  - **Average Calculation**: The average sepal length is calculated by species using the `aggregateByKey` function.
  - **Comprehensive Averages**: A separate function calculates and prints average values for all columns grouped by species, ensuring clarity in data processing.
- **Final Output**: The script outputs the average values, providing insights into the dataset.

---

### Conclusion

This document provides an overview of how to analyze the Iris dataset using Apache Spark, leveraging RDD operations for efficient distributed data processing. The examples demonstrated filtering, mapping, and aggregating techniques, crucial for any large-scale data analysis.
