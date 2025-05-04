from pandas import read_csv
from models import UserData
from pydantic import ValidationError

def main():
    # Read the CSV file 
    try:
        df = read_csv('data/sample.csv')
        print("CSV data read successfully.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    # Validate and process each row
    for index, row in df.iterrows():
        try:
            user_data = UserData(**row.to_dict())
            print(f"Validated data for row {index}: {user_data}")
        except ValidationError as e:
            print(f"Validation error for row {index}: {e}")

if __name__ == "__main__":
    main()