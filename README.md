# Big-Data-Analytics

This repository demonstrates big data processing, visualization, and machine learning using tools such as Hadoop, Spark, Kafka, and Python.

<img src = "https://th.bing.com/th/id/R.8332a2c65eeaecfb365ec3a11e9c2b0e?rik=a86A6oZLes5OWw&riu=http%3a%2f%2ftimesquareit.com%2fimages%2fsl-1.jpg&ehk=VKCM0JR5%2b2hM2HSb%2b%2f6w88WsQFhqxkY3pnZymVms7mo%3d&risl=&pid=ImgRaw&r=0">

## Tools and Technologies ⚙️💻

### 1. [Python](https://www.python.org/)

**Description:**  
Python is a high-level, interpreted programming language known for its readability and versatility. It is widely used in data science for tasks such as data manipulation, analysis, and visualization. Libraries such as Pandas, Matplotlib, and Scikit-Learn provide powerful tools for handling and analyzing large datasets.

### 2. [Hadoop](https://madhurimarawat.github.io/Semester-Notes/Hadoop-Commands.html)

**Description:**  
Hadoop is an open-source framework that allows for the distributed processing of large datasets across clusters of computers using simple programming models. Its core components include the Hadoop Distributed File System (HDFS) for storage and MapReduce for processing data.

### 3. [MapReduce](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)

**Description:**  
MapReduce is a programming model used for processing and generating large datasets with a parallel, distributed algorithm on a cluster. The model consists of two main tasks:

1. **Map:** Processes input data and produces intermediate key-value pairs.
2. **Reduce:** Merges all intermediate values associated with the same key and outputs the final result.

### 4. [Apache Hive](https://hive.apache.org/)

**Description:**  
Apache Hive is a data warehousing and SQL-like query language for Hadoop. It provides a high-level abstraction over Hadoop's complexity by allowing users to write SQL queries (HiveQL) to interact with data stored in HDFS.

### 5. [Apache Spark](https://spark.apache.org/)

**Description:**  
Apache Spark is a fast, open-source processing engine designed for large-scale data processing. It offers high-level APIs in multiple programming languages and modules for SQL, machine learning, and streaming.

### 6. [Apache Kafka](https://kafka.apache.org/)

**Description:**  
Apache Kafka is a distributed streaming platform that enables real-time data pipelines and streaming applications. It is designed for high throughput and fault tolerance, making it ideal for applications that require processing and analyzing continuous streams of data.

### 7. [Matplotlib](https://matplotlib.org/)

**Description:**  
Matplotlib is a comprehensive plotting library for Python that allows users to create static, animated, and interactive visualizations in a variety of formats. It’s widely used for data analysis and scientific computing.

### 8. [Seaborn](https://seaborn.pydata.org/)

**Description:**  
Seaborn is a statistical data visualization library based on Matplotlib. It provides a high-level interface for creating attractive and informative graphics, simplifying the process of creating complex visualizations.

---

## Directory Structure 📂

### Experiment 1

- **Output** 📊  
  This folder contains the output of Experiment 1.
  - `Experiment 1 Output` (e.g., CSV, logs, or results)

### Experiment 2

- **Output** 📊  
  Stores the results and outputs of Experiment 2.
  - `Experiment 2 Output`
- **Commands** 📋  
  A text file listing the commands or steps used during Experiment 2.
  - `commands.docs`

### Experiment 3

- **Codes** 💻  
  This folder contains the code files used for Experiment 3.

  - Python scripts, e.g., `main.py`

- **Output** 📊  
  Experiment 3 output results.
  - `Experiment 3 Output`

### Experiment 4 and onwards

- **Codes** 💻 (If applicable)  
  Contains code files used for the experiment.
- **Documentation** 📝  
  This folder contains the documentation related to each experiment. It includes both Markdown (`.md`) and PDF formats for easy reference. Markdown is converted to PDF using [md2pdf](https://md2pdf.netlify.app/).
  - `documentation.md`
  - `documentation.pdf`
- **Dataset** 📁 (If applicable)  
  Stores the datasets used in the experiment. If an experiment involves a dataset, place it here for easy access.
  - e.g., `dataset.csv`
- **Output** 📊  
  Stores the output of the experiment.
  - `Experiment X Output` (with the relevant experiment number)

---

## Example Layout:

```
Big-Data-Analytics/
│
├── Experiment 1/
│   ├── Output/ 📊
│   │   └── Experiment 1 Output
│
├── Experiment 2/
│   ├── Output/ 📊
│   │   └── Experiment 2 Output
│   ├── Commands/ 📋
│   │   └── commands.docs
│
├── Experiment 3/
│   ├── Codes/ 💻
│   │   └── main.py
│   ├── Output/ 📊
│   │   └── Experiment 3 Output
│
├── Experiment 4/
│   ├── Codes/ 💻
│   │   └── process_data.py
│   ├── Documentation/ 📝
│   │   ├── documentation.md
│   │   └── documentation.pdf
│   ├── Output/ 📊
│   │   └── Experiment 4 Output
│
├── Experiment 5/
│   ├── Dataset/ 📁
│   │   └── data.csv
│   ├── Documentation/ 📝
│   │   ├── documentation.md
│   │   └── documentation.pdf
│   ├── Output/ 📊
│   │   └── Experiment 5 Output
│
└── Experiment 6/
    ├── Dataset/ 📁
    │   └── stream_data.json
    ├── Documentation/ 📝
    │   ├── documentation.md
    │   └── documentation.pdf
    ├── Output/ 📊
    │   └── Experiment 6 Output
```

---

### Explanation of Folders:

- **Codes Folder (💻):**  
  Contains the source code used for the experiment. If the experiment involves running scripts or programs, the corresponding code files go here.

- **Dataset Folder (📁):**  
  This folder stores the dataset used in an experiment. If a dataset is involved (like a `.csv`, `.json`, or any data file), it will be placed here.

- **Output Folder (📊):**  
  Stores the outputs/results generated by the experiments. This might include processed data, logs, or result files. Each experiment’s output is stored separately with a relevant name.

- **Documentation Folder (📝):**  
  Contains the documentation of each experiment, provided in both `.md` and `.pdf` formats. The Markdown file is converted to PDF using the provided link for Markdown to PDF conversion.

- **Commands File (📋):**  
  A text file documenting the specific commands or steps used in the experiment, especially useful for command-line operations.

---

## Table Of Contents 📔 🔖 📑

### 1. [Hadoop Installation](https://github.com/madhurimarawat/Big-Data-Analytics/tree/main/Experiment%201)

**Description:**  
This experiment involves the installation and setup of Hadoop on your system. It covers the necessary configurations to get Hadoop up and running, enabling exploration of its capabilities for handling large-scale data processing tasks.

### 2. [Data Exploration with Hadoop](https://github.com/madhurimarawat/Big-Data-Analytics/tree/main/Experiment%202)

**Description:**  
In this experiment, we use Hadoop to explore large-scale datasets stored in the Hadoop Distributed File System (HDFS). Basic operations such as file listing, data reading, and summary statistics are performed to understand the structure and content of the datasets.

### 3. [SQL Queries with Hive](https://github.com/madhurimarawat/Big-Data-Analytics/tree/main/Experiment%203)

**Description:**  
This experiment uses Apache Hive to run SQL queries on datasets stored in HDFS. We perform various SQL operations, such as filtering, joining, and aggregating large datasets to extract meaningful insights.

### 4. [Word Count with MapReduce](https://github.com/madhurimarawat/Big-Data-Analytics/tree/main/Experiment%204)

**Description:**  
The classic MapReduce word count algorithm is implemented to count the frequency of words in a large text corpus stored in HDFS. This experiment demonstrates the Map and Reduce functions’ structure for processing large volumes of text data.

### 5. [Data Analysis with Apache Spark](https://github.com/madhurimarawat/Big-Data-Analytics/tree/main/Experiment%205)

**Description:**  
In this experiment, Apache Spark is used to analyze large datasets. You will load data into Spark Resilient Distributed Datasets (RDDs) and perform operations such as filtering, mapping, and aggregation, showcasing Spark's efficiency in big data processing.

### 6. [Streaming Analytics with Kafka and Spark](https://github.com/madhurimarawat/Big-Data-Analytics/tree/main/Experiment%206)

**Description:**  
This experiment sets up a data streaming pipeline using Apache Kafka to ingest real-time data. Apache Spark Streaming processes this data, demonstrating how real-time analytics can be performed on live data feeds.

### 7. [Data Visualization with Python and Matplotlib](https://github.com/madhurimarawat/Big-Data-Analytics/tree/main/Experiment%207)

**Description:**  
In this experiment, Python and the Matplotlib library are used to visualize insights from large datasets. Various types of plots, such as histograms, scatter plots, and time series visualizations, are created to communicate findings effectively.

## Additional Resources

- **Detailed Documentation:** A Word document explaining each command used in the experiments.
- **Output Document:** A document showcasing the outputs and results for each experiment.

## Thanks for Visiting 😄

- Drop a 🌟 if you find this repository useful.<br><br>
- If you have any doubts or suggestions, feel free to reach me.<br><br>
  📫 How to reach me: &nbsp; [![Linkedin Badge](https://img.shields.io/badge/-madhurima-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/madhurima-rawat/) &nbsp; &nbsp;
  <a href ="mailto:rawatmadhurima@gmail.com"><img src="https://github.com/madhurimarawat/Machine-Learning-Using-Python/assets/105432776/b6a0873a-e961-42c0-8fbf-ab65828c961a" height=35 width=30 title="Mail Illustration" alt="Mail Illustration📫" > </a><br><br>
- **Contribute and Discuss:** Feel free to open <a href= "https://github.com/madhurimarawat/Big-Data-Analytics/issues">issues 🐛</a>, submit <a href = "https://github.com/madhurimarawat/Big-Data-Analytics/pulls">pull requests 🛠️</a>, or start <a href = "https://github.com/madhurimarawat/Big-Data-Analytics/discussions">discussions 💬</a> to help improve this repository!
