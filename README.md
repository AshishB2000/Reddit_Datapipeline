# Stadium List Data Pipeline

## About
This project implements a streamlined data pipeline to gather, process, and analyze posts from the "AAPL" subreddit on Reddit. Leveraging the PRAW library for Reddit API access, the pipeline retrieves posts and associated metadata, which are then securely stored in an Amazon S3 bucket. Using Snowflake for data transformation, the raw Reddit data is structured and loaded into a data warehouse, enabling efficient querying and analysis. Apache Airflow orchestrates the workflow, triggering daily updates to ensure data freshness and reliability. This pipeline provides stakeholders with timely insights into discussions surrounding Apple Inc., facilitating informed decision-making and strategic planning.
## Table of Contents
- [System Architecture](#system-architecture)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Running the Code With Docker](#running-the-code-with-docker)

## System Architecture
-Exreacting data from Reddit using API
-Using Apache Airflow as Orchestrater the ETL process.
-Using PostgreSQL as Temporary storage and metadata management.
-AWS S3 Bucket for storing data.
-Snowflake for data transformation and Data warehousing.



## Requirements
- Python 3.9
- Docker
- AWS Account and Snowflake account.
- Reddit API credentials.


Ensure you have the above prerequisites installed and properly configured on your system before proceeding with the setup and execution of the data pipeline.

## Getting Started
To set up the project on your local machine, follow these steps:

1. **Clone the repository:**
```bash
git clone https://github.com/AshishB2000/Reddit_Datapipeline
