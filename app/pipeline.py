import os
from helpers import DataProcess

INPUT_PATH = os.path.join('/data', 'Medicaldataset.csv')
OUTPUT_PATH = os.path.join('/data', 'CleanedMedicalData.csv')

def run_pipeline():
    process = DataProcess()
    raw_data = process.extract_data(INPUT_PATH)
    cleaned_data = process.transform_data(raw_data)
    process.load_data(cleaned_data, OUTPUT_PATH)

    print("Data pipeline process complete!")


if __name__ == "__main__":
    run_pipeline()
