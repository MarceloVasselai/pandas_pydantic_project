from typing import List
import pandas as pd
from src.models import DataModel

def read_csv(file_path: str) -> List[DataModel]:
    df = pd.read_csv(file_path)
    return [DataModel(**row) for index, row in df.iterrows()]

def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    # Example conversion logic (customize as needed)
    df['boolean_field'] = df['boolean_field'].astype(bool)
    df['date_field'] = pd.to_datetime(df['date_field'])
    df['float_field'] = df['float_field'].astype(float)
    return df

def validate_data(df: pd.DataFrame) -> List[DataModel]:
    validated_data = []
    for index, row in df.iterrows():
        try:
            validated_data.append(DataModel(**row))
        except Exception as e:
            print(f"Validation error for row {index}: {e}")
    return validated_data