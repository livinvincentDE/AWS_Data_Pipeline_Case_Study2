# 🚀 Serverless Data Pipeline on AWS

## 📌 Overview

This project demonstrates a fully serverless data pipeline using AWS services to process and analyze data.

---
## ⚙️ Tech Stack

![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)
![Amazon DynamoDB](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white)
![Amazon EventBridge](https://img.shields.io/badge/Amazon%20EventBridge-FF4F8B?style=for-the-badge&logo=amazonaws&logoColor=white)

---

## 🧱 Architecture

EventBridge → Lambda → S3 (partitioned) → DynamoDB

![Architecture Diagram](architecture/architecture.png)

---

## 🔄 Features

* Serverless ETL processing
* Scheduled execution using EventBridge
* Partitioned data storage in S3
* KPI storage in DynamoDB
* NDJSON data handling

---

## 📂 Project Structure

* `lambda/` → Lambda function code
* `data/` → Sample input data
* `architecture/` → Architecture diagram
* `screenshots/` → Output proof

---

## 📊 Output

* Partitioned data in S3
* Metrics stored in DynamoDB

---

## 💡 Key Learnings

* Built event-driven serverless pipelines
* Handled real-world data formats (NDJSON)
* Implemented IAM-based security
* Designed scalable architecture

---

## 🚀 Future Enhancements

* Athena integration
* Dashboard visualization
* Data quality checks

---

## 👨‍💻 Author

Livin Vincent
