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

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- Git installed on your system

### Setup and Execution

1. Clone the repository

```bash
git clone https://github.com/ricgomez99/data-pipeline.git
cd simple-pipeline
```

2. Ensure Docker Desktop is running on your machine

3. Build and run the pipeline

```bash
docker compose up --build
```

This command will:

- Build the Docker image with all required dependencies
- Create a container from the image
- Mount the data volume
- Execute the pipeline to process the Heart Attack Dataset
- Store the cleaned data in the `data` directory

### Expected Output

After successful execution, you'll find the processed data file `CleanedMedicalData.csv` in the `data` directory.

To stop the container, press `Ctrl+C` or run:

```bash
docker compose down
```
