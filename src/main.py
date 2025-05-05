from pandas import read_csv
from models import UserData
from utils import saida
from pydantic import ValidationError

# Dicionário para armazenar registros com erros e sem erros
registros_com_erros = {}
registros_sem_erros = {}

def main():
    # Ler o arquivo CSV
    try:
        df = read_csv('data/sample.csv')
        print("CSV data read successfully.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    # Validar e processar cada linha
    for index, row in df.iterrows():
        try:
            user_data = UserData(**row.to_dict())
            registros_sem_erros[index] = user_data.dict()  # Armazenando dados válidos
            print(f"Validated data for row {index}: {user_data}")
        
        except ValidationError as e:
            # Armazenando o registro com erro no dicionário
            registros_com_erros[index] = {
                "registro": row.to_dict(),
                "erros": e.errors()  # Captura os erros de validação
            }
            print(f"Validation error for row {index}: {e}")


if __name__ == "__main__":
    main()
    saida(registros_com_erros, registros_sem_erros)

