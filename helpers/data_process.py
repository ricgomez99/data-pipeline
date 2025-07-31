import pandas as pd

class DataProcess:
    def __init__(self) -> None:
        pass

    def extract_data(self, path: str):
        file_data = pd.read_csv(path)

        if not len(file_data):
            raise ValueError('Unable to extract file data')

        return file_data
    
    def transform_data(self, data: pd.DataFrame):
        cleaned_data = data.dropna()
        cleaned_data.columns = [col.strip().lower().replace(" ", "_") for col in cleaned_data.columns ]

        return cleaned_data
    
    def load_data(self, data: pd.DataFrame, output_path: str):
        if not len(data):
            raise ValueError('No data available for loading into CSV file')
        
        data.to_csv(output_path, index=False)