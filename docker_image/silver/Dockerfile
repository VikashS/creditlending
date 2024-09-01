FROM openjdk:11-jre-slim

LABEL authors="vikashsingh"

# Install Python and necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Install PySpark
RUN pip3 install pyspark==3.3.1

# Copy the PySpark script
COPY calling_silver_script.py /app/calling_silver_script.py

# Set the working directory
WORKDIR /app

# Define the entry point
ENTRYPOINT ["python3", "calling_silver_script.py"]
