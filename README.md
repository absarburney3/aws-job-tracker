# 🚀 AWS Job Application Tracker

A fully serverless, secure job application tracking web app built entirely using the **AWS Management Console** — no CLI, no Terraform.

Built as a hands-on project while preparing for the **AWS Solutions Architect Associate (SAA-C03)** certification.

---

## 🏗️ Architecture

![Architecture Diagram](architecture.png)

---

## ☁️ AWS Services Used

| Service | Purpose | SAA-C03 Domain |
|---|---|---|
| S3 | Private frontend hosting with versioning | Resilient Architectures |
| CloudFront | CDN with OAC + WAF + HTTPS enforcement | Secure Architectures |
| API Gateway | REST API (GET + POST endpoints) | High-Performing Architectures |
| Lambda (Python) | Serverless business logic | Cost-Optimized Architectures |
| DynamoDB | NoSQL database with GSI for status queries | High-Performing Architectures |
| SNS | Email alerts on Interview/Offer status | Event-Driven Architectures |
| CloudWatch | Dashboard + alarms for observability | Operational Excellence |
| IAM | Least-privilege roles for Lambda | Secure Architectures |
| VPC | Custom VPC with public/private subnets across 2 AZs | Resilient Architectures |

---

## 🔐 Security Design Decisions

- **S3 bucket is fully private** — served only through CloudFront using Origin Access Control (OAC), the modern replacement for OAI
- **WAF enabled** on CloudFront distribution at no additional cost — protects against common web vulnerabilities
- **HTTPS enforced** — HTTP automatically redirects to HTTPS via CloudFront viewer protocol policy
- **IAM least-privilege** — Lambda has a dedicated role with only DynamoDB + SNS + CloudWatch Logs permissions
- **No credentials hardcoded** — all AWS service access via IAM roles

---

## 🌐 Network Design

