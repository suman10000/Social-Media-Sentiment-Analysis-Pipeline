📊 Social Media Sentiment Analysis Pipeline

A full-scale modern data engineering pipeline that ingests large-scale social media data, performs sentiment analysis using NLP, processes data with Apache Spark, stores it in Snowflake using a Star Schema warehouse design, applies enterprise-level security controls, and enables advanced analytical insights.

📌 Table of Contents

🚀 Project Overview

🏗 System Architecture

🧠 Key Features

📊 Tech Stack

📁 Project Structure

⚙ Data Pipeline Flow

📈 Analytics Capabilities

🔐 Security & Governance

⚡ Big Data & Streaming

▶ How to Run Locally

📚 What This Project Demonstrates

👨‍💻 Author

🚀 Project Overview

This project implements a real-world scalable sentiment analytics platform designed to:

• Process large-scale Twitter data (1.6M+ records)
• Perform NLP-based sentiment classification
• Build a structured Data Warehouse (Star Schema)
• Execute advanced SQL analytics
• Optimize performance using Snowflake features
• Apply enterprise security principles
• Demonstrate Spark batch & streaming processing

The architecture mirrors production-grade data engineering systems used in modern analytics-driven organizations.

🏗 System Architecture
Raw Social Media Dataset (CSV)
            ↓
Python ETL (Cleaning + NLP Sentiment Analysis)
            ↓
Dimension & Fact Table Construction
            ↓
Snowflake Data Warehouse (Star Schema)
            ↓
Apache Spark Batch Processing
            ↓
Structured Streaming Simulation
            ↓
Advanced SQL Analytics
            ↓
Clustering + Time Travel Optimization
            ↓
Role-Based Access & Secure Views
            ↓
Interactive Analytics & Reporting
🧠 Key Features

✔ Star Schema Data Warehouse Design
✔ Python-based ETL Pipeline
✔ NLP Sentiment Analysis (VADER)
✔ Apache Spark Batch Processing
✔ Structured Streaming Simulation
✔ Advanced SQL (CTE, Window Functions, Ranking)
✔ Snowflake Clustering & Time Travel
✔ Role-Based Access Control (RBAC)
✔ Secure View-based Data Masking
✔ Performance Optimization Strategies

📊 Tech Stack
Layer	Technology
ETL	Python, Pandas, VADER
Big Data	Apache Spark (PySpark)
Warehouse	Snowflake
Analytics	Advanced SQL
Optimization	Clustering, Time Travel
Security	RBAC + Secure Views
Streaming	Structured Streaming Simulation
Version Control	Git & GitHub
📁 Project Structure
Social-Media-Sentiment-Analysis-Pipeline/
│
├── etl.py
├── warehouse_prep.py
├── spark_batch.py
├── spark_streaming.py
│
├── sql/
│   ├── 01_schema_setup.sql
│   ├── 02_advanced_queries.sql
│   ├── 03_optimization.sql
│   └── 04_security.sql
│
├── requirements.txt
├── .gitignore
└── README.md

⚙ Data Pipeline Flow
🔄 Batch ETL
Extract → Clean → Transform → Sentiment Scoring → Load

• Removes noise (URLs, mentions, symbols)
• Applies VADER sentiment scoring
• Generates structured dataset
• Builds surrogate keys for dimensions
• Constructs fact table

🗄 Data Warehouse Layer

Star Schema Implementation:

Fact Table

fact_sentiment

Dimension Tables

dim_user

dim_date

dim_platform

dim_location

Designed for efficient OLAP-style analytical querying.

📈 Analytics Capabilities

Examples of insights generated:

📊 Sentiment distribution by date

📅 Rolling 7-day sentiment average

🏆 Most negative days ranking

📈 Trend analysis using window functions

🔍 Sentiment segmentation by platform/location

⚡ Hybrid Spark + Snowflake analytics

🔐 Security & Governance

Implemented using enterprise design principles:

Role-Based Access Control (RBAC)

Secure View-based column masking

Schema-level privilege management

Separation of administrative roles

Least privilege enforcement model

⚡ Big Data & Streaming
🚀 Apache Spark Batch Processing

• Aggregates sentiment counts
• Computes daily averages
• Handles 1.6M+ records efficiently

🔄 Structured Streaming (Simulation)

• Real-time sentiment aggregation simulation
• Micro-batch processing model
• Continuous sentiment monitoring concept

▶ How to Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Run ETL Pipeline
python etl.py
3️⃣ Generate Warehouse Tables
python warehouse_prep.py
4️⃣ Run Spark Batch Job
py -3.10 spark_batch.py
5️⃣ Run Streaming Simulation
py -3.10 spark_streaming.py
📚 What This Project Demonstrates

This project showcases:

✅ End-to-end Data Engineering pipeline
✅ Cloud Data Warehouse implementation
✅ Big Data processing with Spark
✅ Advanced SQL analytics mastery
✅ Enterprise security design
✅ Performance tuning techniques
✅ Production-style project organization

👨‍💻 Author

Suman Dandapat
Data Engineering & Analytics Enthusiast