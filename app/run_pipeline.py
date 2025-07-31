from helpers import DataProcess
from pathlib import Path

INPUT_PATH = Path('/data') / 'Medicaldataset.csv'
OUTPUT_PATH = Path('/data') / 'CleanedMedicalData.csv'

def run_pipeline():
    process = DataProcess()
    raw_data = process.extract_data(str(INPUT_PATH))
    cleaned_data = process.transform_data(raw_data)
    process.load_data(cleaned_data, str(OUTPUT_PATH))

    print("Data pipeline process complete!")



