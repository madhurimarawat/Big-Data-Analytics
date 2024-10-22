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

# Print the entire mapped dataset with values first and species names last
print("\n\n\n====== Mapped Dataset (Values and Species) ======\n\n\n")
for row in rdd.collect():
    sepal_length = row[0]
    sepal_width = row[1]
    petal_length = row[2]
    petal_width = row[3]
    species_num = row[4]  # Assuming the species number is in the last column
    species_name = species_mapping.get(
        species_num, "Unknown"
    )  # Get species name from the mapping

    # Print values followed by the species name
    print(
        f"Sepal Length: {sepal_length}, Sepal Width: {sepal_width}, Petal Length: {petal_length}, Petal Width: {petal_width}, Species: {species_name}"
    )

# Example processing: Calculate the average sepal length by species
species_sepal_length = rdd.map(
    lambda x: (species_mapping.get(x[4], "Unknown"), float(x[0]))
)  # (species, sepal_length)

# Calculate sum and count of sepal lengths for each species
sum_and_count = species_sepal_length.aggregateByKey(
    (0.0, 0),  # Initialize (sum, count)
    lambda acc, val: (acc[0] + val, acc[1] + 1),  # Add value to sum and increment count
    lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1]),  # Merge accumulators
)

# Calculate average sepal length for each species
average_sepal_length = sum_and_count.mapValues(lambda x: x[0] / x[1])

# Print the average sepal length for each species
print("\n\n\n====== Average Sepal Length ======\n\n\n")
for species, avg_length in average_sepal_length.collect():
    print(f"{species}: {avg_length}")


# Calculate and print average for all columns grouped by species
def average_for_species(rdd):
    # Map to (species, (sepal_length, sepal_width, petal_length, petal_width))
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
        ),  # Initialize (sum_length, sum_width, sum_petal_length, sum_petal_width, count)
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
        f"Sepal Length: {averages[0]}, Sepal Width: {averages[1]}, Petal Length: {averages[2]}, Petal Width: {averages[3]}, Species: {species}"
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
