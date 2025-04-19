# Running Event Registration System

This project is a FastAPI-based registration system for running events, featuring payment integration with Razorpay and data storage in DynamoDB.

## Features

- User registration for running events
- Payment processing with Razorpay
- Data storage in DynamoDB
- API key authentication
- Logging with loguru
- Containerized application using Docker
- Dependency injection for better code organization

## Prerequisites

- Python 3.9+
- Docker
- AWS account (for DynamoDB)
- Razorpay account

# Running Event Registration System

This project is a FastAPI-based application for managing registrations for running events. It integrates with PhonePe for payment processing and uses AWS DynamoDB for data storage.

## Features

- User registration for running events
- Integration with PhonePe payment gateway
- Data storage in AWS DynamoDB
- Querying registrations by various fields (name, email, phone number, event type)
- Dockerized application for easy deployment
- CI/CD pipeline using GitHub Actions

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.9 or later
* You have a AWS account with DynamoDB access
* You have a PhonePe merchant account with API credentials
* You have Docker and Docker Compose installed (for local development)
