def converter_unidades(valor, unidade_de_origem, unidade_de_destino):
    # Adicione aqui as fórmulas de conversão para as unidades desejadas
    if unidade_de_origem == "metros" and unidade_de_destino == "pés":
        return valor * 3.281
    elif unidade_de_origem == "quilogramas" and unidade_de_destino == "libras":
        return valor * 2.205
    # Adicione mais conversões conforme necessário
    else:
        return "Conversão não suportada"

print("Conversor de Unidades de Medida")
valor = float(input("Digite o valor: "))
unidade_de_origem = input("Digite a unidade de origem: ")
unidade_de_destino = input("Digite a unidade de destino: ")

resultado = converter_unidades(valor, unidade_de_origem, unidade_de_destino)
print(f"{valor} {unidade_de_origem} é igual a {resultado} {unidade_de_destino}")
