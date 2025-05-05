# Função para formatar a saída de cada registro
def formatar_registro(index, erro_info):
    registro = erro_info["registro"]
    erros = erro_info["erros"]

    # Formatar a string de erros
    erros_formatados = ", ".join([f"{erro['loc'][0]}: {erro['msg']}" for erro in erros])
    
    return f"Registro na linha {index}: Nome: {registro['name']}, Idade: {registro['age']}, Erros: {erros_formatados}"

def saida(registros_com_erros, registros_sem_erros):
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
