# Imagine que você está em uma viagem para os Estados Unidos e precisa converter o valor em reais para dólares. Crie um programa que receba o valor em reais e a taxa de câmbio atual, e exiba o valor equivalente em dólares.
def converter_reais_para_dolares(valor_reais, taxa_cambio):
    """
    Converte um valor em reais para dólares com base na taxa de câmbio fornecida.

    :param valor_reais: Valor em reais a ser convertido
    :param taxa_cambio: Taxa de câmbio atual (reais por dólar)
    :return: Valor equivalente em dólares
    """
    valor_dolares = valor_reais / taxa_cambio
    return valor_dolares

def main():
    print("Conversão de Reais para Dólares")
    
    valor_reais = float(input("Digite o valor em reais: R$ "))
    
    taxa_cambio = 5.6
    
    valor_dolares = converter_reais_para_dolares(valor_reais, taxa_cambio)
    
    print(f"O valor de R$ {valor_reais:.2f} em dólares é: ${valor_dolares:.2f}")

if __name__ == "__main__":
    main()