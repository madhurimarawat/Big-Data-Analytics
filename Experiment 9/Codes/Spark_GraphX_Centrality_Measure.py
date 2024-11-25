"""
This script demonstrates how to perform simple graph analytics using GraphFrames 
with Apache Spark. It performs the following tasks:

1. Initializes a Spark session for distributed data processing.
2. Creates a DataFrame representing vertices (nodes) with IDs and names.
3. Creates a DataFrame representing edges (relationships) between nodes.
4. Constructs a GraphFrame using the vertices and edges DataFrames.
5. Displays the vertices and edges of the graph.
6. Calculates the degree centrality (number of connections) for each vertex.
7. Performs community detection using connected components analysis.
8. Outputs the degree centrality and connected components results.
9. Stops the Spark session to release resources.

Dependencies:
- PySpark
- GraphFrames
"""

# Importing Required Libraries
from pyspark.sql import SparkSession
from graphframes import GraphFrame

# Step 1: Initialize the Spark session
# This creates a Spark session, which is the entry point for any Spark functionality.
# The app name is set to "Simple Graph Analytics with GraphFrames", and the required
# GraphFrames package is specified through the config option.
spark = (
    SparkSession.builder.appName("Simple Graph Analytics with GraphFrames")
    .config(
        "spark.jars.packages", "graphframes:graphframes:0.6.0-spark3.0-s_2.12"
    )  # Include GraphFrames package
    .getOrCreate()  # Start the session
)

# Step 2: Define vertices (nodes) for the graph
# A DataFrame is created with two columns: 'id' (representing the node identifier)
# and 'name' (the name associated with each node).
vertices = spark.createDataFrame(
    [("1", "Alice"), ("2", "Bob"), ("3", "Charlie"), ("4", "David"), ("5", "Eve")],
    ["id", "name"],  # Define column names for the vertices
)

# Step 3: Define edges (relationships) between the nodes
# A DataFrame is created representing edges in the graph, where each row defines a relationship
# between two nodes (src and dst). These edges represent directed connections from 'src' to 'dst'.
edges = spark.createDataFrame(
    [("1", "2"), ("2", "3"), ("3", "4"), ("4", "5"), ("1", "3")], ["src", "dst"]
)

# Step 4: Construct a GraphFrame
# GraphFrame is a structure that contains both vertices and edges.
# It is created using the vertices and edges DataFrames defined above.
g = GraphFrame(vertices, edges)

# Step 5: Display the vertices of the graph
# The 'vertices.show()' method prints the vertices DataFrame to the console.
# It shows the list of nodes in the graph along with their associated 'id' and 'name'.
print("Vertices:")
g.vertices.show()

# Step 6: Display the edges of the graph
# The 'edges.show()' method prints the edges DataFrame to the console.
# It shows the directed relationships (edges) between nodes, with 'src' as the source and 'dst' as the destination.
print("Edges:")
g.edges.show()

# Step 7: Calculate degree centrality
# Degree centrality is a measure of the number of edges connected to each node.
# It is computed using the 'g.degrees' attribute, which returns a DataFrame containing
# each vertex's ID and its corresponding degree (the number of edges connected to it).
degree = g.degrees
print("\nDegree Centrality:")
degree.show()  # Display the degree centrality for each node

# Step 8: Perform connected components analysis (Community detection)
# The connectedComponents() method assigns each node to a connected component.
# Nodes in the same connected component are part of the same community. This is useful for detecting groups of
# nodes that are connected in some way, even if indirectly.
result = g.connectedComponents()
print("\nConnected Components (Community Detection):")
result.show()  # Display the connected component for each vertex (node)

# Step 9: Stop the Spark session
# Finally, the Spark session is stopped to release any resources that were being used.
# This is good practice to prevent memory leaks or other resource management issues.
spark.stop()
