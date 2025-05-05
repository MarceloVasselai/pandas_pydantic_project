from pandas import read_csv
from models import UserData
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

# Função para formatar a saída de cada registro
def formatar_registro(index, erro_info):
    registro = erro_info["registro"]
    erros = erro_info["erros"]

    # Formatar a string de erros
    erros_formatados = ", ".join([f"{erro['loc'][0]}: {erro['msg']}" for erro in erros])
    
    return f"Registro na linha {index}: Nome: {registro['name']}, Idade: {registro['age']}, Erros: {erros_formatados}"


if __name__ == "__main__":
    main()
    
    # Imprimindo registros com erros
    print("\nRegistros com erros:")
    if registros_com_erros:
        for chave, valor in registros_com_erros.items():
            print(f"Row {chave}: {valor['registro']} - Erro foi: {valor['erros']}")
    else:
        print("Nenhum registro com erro encontrado.")

    # Imprimindo registros sem erros
    print("\nRegistros sem erros:")
    if registros_sem_erros:
        for chave, valor in registros_sem_erros.items():
            print(f"Row {chave}: {valor}")
    else:
        print("Nenhum registro válido encontrado.")

    # Total de Registros
    print(f"total de registros lidos: ", len(registros_com_erros) + len(registros_sem_erros))
    print(f"total de registros com erros: ", len(registros_com_erros))
    print(f"total de registros sem erros: ", len(registros_sem_erros))

    # Usando map para formatar todos os registros
    registros_formatados = map(lambda item: formatar_registro(item[0], item[1]), registros_com_erros.items())
    # Imprimindo todos os registros formatados
    print("\n".join(registros_formatados))