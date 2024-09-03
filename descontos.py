#calculadora de descontos em python 

valor_produto = float(input("Digite o valor bruto do produto para aplicar desconto"))

percentual_desconto = float(input("Quantos % Deseja aplicar ?"))


#VERIFICA SE O PERCENTUAL DE DESCONTO ESTÁ DENTRO DOS LIMITES ACEITAVEIS (0-100%)

if percentual_desconto < 0 or percentual_desconto > 100:
    print("Desconto valido na compra acima de 100$")
else:
    
#CALCULA O VALOR DE DESCONTO
    desconto = valor_produto *(percentual_desconto / 100)

#CALCULA O VALOR FINAL DA CONTA 
valor_final = valor_produto - desconto

#IMPRIMIR O RESULTADO
print(f"O Deconto de {percentual_desconto}% foi aplicado no valor de {valor_produto} e ficou no valor de {valor_final}$")