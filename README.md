Credit lending demo

Basic Set up:
=============

Azure AKS to deploy and manage PySpark jobs
Spin up container registry to store Docker Image
Apache Airflow for pipeline orchestration. ( ADF is also good option)
Azure Data Lake Storage with Delta lake support for Storage all the historical/Intermediate and aggregated Data
PySpark  for all data transformation and normalization.
Final data storage is in Either database (Postgres/Azure Synapse for high performance) or Data lake where lower performance can manage
Azure Monitoring and Log Analytics will be monitoring all Data load and jobs.



Code flow:
===========
There will be pyspark job for each layer . 
Each job layer (bronze, silver, gold) is containerized into separate Docker images. These job will store into Azure Container registry .
Use Azure Kubernetes Service to host all Pyspark job and can also host airflow dags.
Once deployed the Airflow job will be triggered sequentially for each layer for kubernetes jobs.
Kubernetes job will be execute pyspark job on aks cluster.
All the job output will be stored in Data lake.