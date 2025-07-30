# Data Pipeline for Heart Attack Dataset Analysis

A simple ETL (Extract, Transform, Load) data pipeline that processes the Kaggle Heart Attack Dataset.

## Overview

This project implements a data processing pipeline that:

1. **Extracts** data from the Kaggle Heart Attack Dataset (CSV format)
2. **Transforms** the data by:
   - Removing missing values
   - Cleaning column names
   - Performing data validations
3. **Loads** the cleaned data into a new CSV file

## Technologies

- **Python 3.13**: Core programming language
- **Docker**: Container platform for consistent environment management
- **pandas**: Data manipulation and analysis library

## Project Structure

```
simple-pipeline/
├── app/
│   └── pipeline.py    # Main pipeline implementation
├── data/
    └── Medicaldataset.csv            # Directory for input/output data
├── Dockerfile         # Docker image definition
├── compose.yml        # Docker Compose configuration
└── pyproject.toml     # Project dependencies and metadata
```

## Getting Started

Instructions for setting up and running the pipeline will be added soon.
