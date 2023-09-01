from datetime import datetime

def calcular_idade(data_de_nascimento):
    hoje = datetime.now()
    data_de_nascimento = datetime.strptime(data_de_nascimento, "%Y-%m-%d")
    idade = hoje - data_de_nascimento
    anos = idade.days // 365
    meses = (idade.days % 365) // 30
    dias = (idade.days % 365) % 30
    return anos, meses, dias

data_de_nascimento = input("Digite sua data de nascimento (AAAA-MM-DD): ")
anos, meses, dias = calcular_idade(data_de_nascimento)
print(f"Você tem {anos} anos, {meses} meses e {dias} dias de idade.")
