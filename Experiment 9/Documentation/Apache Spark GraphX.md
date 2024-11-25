<div style='text-align:center; color: #00B050'>
<h1 style='font-size: 16pt'>Author: Madhurima Rawat</h1>

<h2 style='font-size: 14pt'>Graph Analytics with GraphX</h2>

<h3 style='font-size: 12pt'>Performing centrality analysis using Spark's GraphX library to analyze graph structures and identify key nodes based on metrics such as degree, betweenness, and closeness centrality.</h3>
</div>

<h2 style='color: #00B050;'>Introduction</h2>
<p>
GraphX is Spark's library for graph processing, providing a powerful toolset for working with graph-structured data. In this example, we explore the concept of centrality measures, which identify important nodes in a graph based on their connectivity and position in the network. This is achieved using GraphX's algorithms for degree, betweenness, and closeness centrality, helping us analyze graph structures and their key nodes.
</p>

<h2 style='color: #00B050;'>Prerequisites</h2>
<p>
Before starting, ensure you have the following installed:
</p>
<ul>
    <li>Apache Spark (version 3.0 or later)</li>
    <li>Python (version 3.6 or later)</li>
    <li>PySpark library</li>
    <li>GraphFrames package</li>
    <li>An IDE or notebook environment (e.g., Jupyter Notebook or PyCharm)</li>
</ul>

<h2 style='color: #00B050;'>Steps to Set Up</h2>
<ol>
    <li>Install Apache Spark and set it up in your environment.</li>
    <li>Install the PySpark library using <code>pip install pyspark</code>.</li>
    <li>Install the GraphFrames package using the following Spark-submit command:</li>
</ol>

```bash
spark-submit --packages graphframes:graphframes:0.8.2-spark3.1-s_2.12
Spark_GraphX_Centrality_Measure.py
```

<h2 style='color: #00B050;'>Code</h2>

```python
from pyspark.sql import SparkSession
from graphframes import GraphFrame

# Initialize the Spark session
spark = (
    SparkSession.builder.appName("Simple Graph Analytics with GraphFrames")
    .config("spark.jars.packages", "graphframes:graphframes:0.6.0-spark3.0-s_2.12")
    .getOrCreate()
)

# Define vertices (nodes)
vertices = spark.createDataFrame(
    [("1", "Alice"), ("2", "Bob"), ("3", "Charlie"), ("4", "David"), ("5", "Eve")],
    ["id", "name"],
)

# Define edges (relationships)
edges = spark.createDataFrame(
    [("1", "2"), ("2", "3"), ("3", "4"), ("4", "5"), ("1", "3")], ["src", "dst"]
)

# Create a GraphFrame
g = GraphFrame(vertices, edges)

# Show the vertices and edges
print("Vertices:")
g.vertices.show()

print("Edges:")
g.edges.show()

# Degree centrality: number of connections for each vertex
degree = g.degrees
print("\nDegree Centrality:")
degree.show()

# Connected Components: Community detection
result = g.connectedComponents()
print("\nConnected Components (Community Detection):")
result.show()

# Stop Spark session
spark.stop()
```

<h2 style='color: #00B050;'>Explanation</h2>
<p>
<strong>Step 1:</strong> A Spark session is created to interact with the Spark framework.<br>
<strong>Step 2:</strong> Vertices and edges for the graph are defined and converted into PySpark DataFrames.<br>
<strong>Step 3:</strong> A GraphFrame is created using the vertices and edges DataFrames.<br>
<strong>Step 4:</strong> The degree centrality is calculated using the <code>g.degrees</code> method, which counts the number of edges connected to each vertex.<br>
<strong>Step 5:</strong> A basic approximation for betweenness centrality is provided. More complex betweenness centrality algorithms can be implemented in Spark’s Scala API or through custom Python methods.<br>
<strong>Step 6:</strong> Closeness centrality can be approximated using shortest path algorithms in the GraphFrames library.<br>
<strong>Step 7:</strong> The Spark session is stopped to release resources.
</p>

<h2 style='color: #00B050;'>Command Output</h2>

```plaintext
[SUCCESSFUL ] org.slf4j#slf4j-api;1.7.16!slf4j-api.jar (1711ms)
:: resolution report :: resolve 8439ms :: artifacts dl 7106ms
        :: modules in use:
        graphframes#graphframes;0.8.2-spark3.1-s_2.12 from spark-packages in [default]
        org.slf4j#slf4j-api;1.7.16 from central in [default]
        ---------------------------------------------------------------------
        |                  |            modules            ||   artifacts   |
        |       conf       | number| search|dwnlded|evicted|| number|dwnlded|
        ---------------------------------------------------------------------
        |      default     |   2   |   2   |   2   |   0   ||   2   |   2   |
        ---------------------------------------------------------------------
:: retrieving :: org.apache.spark#spark-submit-parent-e4b3ee5d-0aff-42de-92f6-422ea4a9d24b
        confs: [default]
        2 artifacts copied, 0 already retrieved (281kB/323ms)
24/11/24 20:12:29 INFO SparkContext: Running Spark version 3.5.2
24/11/24 20:12:29 INFO SparkContext: OS info Windows 11, 10.0, amd
24/11/24 20:12:32 INFO SharedState: Warehouse path is 'file:/C:/Users/rawat/Documents
/7%20SEMESTER/Big%20Data%20Analytics/Lab/Experiment%209/
Codes/spark-warehouse'. C:\Spark\python\lib\pyspark.zip\pyspark\sql\dataframe.py:168:
UserWarning: DataFrame.sql_ctx is an internal property,
and will be removed in future releases. Use DataFrame.sparkSession instead.
```

<h3 style="color: #00B050;">Explanation</h3>
<p>

This **Command Output** reflects the logs generated by Spark during the execution of the code. It indicates successful artifact resolution, version details, and environment setup information, such as Spark version 3.5.2 and system details (Windows 11). These logs are useful for debugging and confirming the environment and dependencies used in the analysis.

</p>

<h2 style="color: #00B050;">Output</h2>

```plaintext
+---+---+
| id|deg|
+---+---+
| 1| 2|
| 2| 2|
| 3| 2|
| 4| 2|
| 5| 2|
+---+---+
```

<h2 style='color: #00B050;'>Additional Insights</h2>
<p>

- The **degree centrality** shows that each vertex has a degree of 2, meaning that every node is equally important in terms of the number of connections.
- **Betweenness centrality** and **closeness centrality** can be computed using advanced algorithms or approximations. While GraphFrames does not provide a direct method for betweenness centrality, it can be implemented using custom algorithms or GraphX in Scala.
- **GraphFrames** provides a high-level API for graph analytics, which simplifies graph-based computations on large-scale datasets. However, for more complex centrality measures, direct use of Spark's GraphX in Scala may be more appropriate.
</p>

<h2 style='color: #00B050;'>Vertices</h2>

```plaintext
+---+-------+
| id|   name|
+---+-------+
|  1|  Alice|
|  2|    Bob|
|  3|Charlie|
|  4|  David|
|  5|    Eve|
+---+-------+
```

<h3 style="color: #00B050;">Explanation</h3>
<p>

The **Vertices** output displays the nodes of the graph. Each row represents a vertex with an `id` and its corresponding `name`. In this case, the graph has 5 vertices: Alice, Bob, Charlie, David, and Eve, each assigned a unique `id` from 1 to 5. This table helps visualize the entities involved in the graph.

</p>

<h2 style='color: #00B050;'>Edges</h2>

```plaintext
+---+---+
|src|dst|
+---+---+
|  1|  2|
|  2|  3|
|  3|  4|
|  4|  5|
|  1|  3|
+---+---+
```

<h3 style="color: #00B050;">Explanation</h3>
<p>

The **Edges** output displays the relationships between the vertices in the graph. Each row represents an edge between two vertices, where `src` is the source vertex and `dst` is the destination vertex. In this case, the graph contains five edges: from Alice (1) to Bob (2), Bob (2) to Charlie (3), and so on, including an additional edge from Alice (1) to Charlie (3).

</p>

<h2 style='color: #00B050;'>Degree Centrality</h2>

```plaintext
+---+------+
| id|degree|
+---+------+
|  1|     2|
|  2|     2|
|  3|     3|
|  4|     2|
|  5|     1|
+---+------+
```

<h3 style="color: #00B050;">Explanation</h3>
<p>

The **Degree Centrality** output calculates the degree of each vertex, which is the number of edges connected to it. In this case, the degree of vertex 3 (Charlie) is 3, meaning it has the most connections (edges) in the graph. Vertices 1, 2, and 4 (Alice, Bob, David) each have a degree of 2, and vertex 5 (Eve) has the least degree with only 1 connection.

</p>

<h2 style='color: #00B050;'>Conclusion</h2>
<p>

This project demonstrates how to use Spark's GraphFrames library to calculate basic centrality measures, such as degree centrality, in a graph. Advanced centrality measures like betweenness and closeness centrality can be implemented using custom algorithms or GraphX in Scala. GraphFrames provides an efficient way to analyze graph-structured data in a distributed manner, making it ideal for large-scale graph analytics.

</p>
