# @cikey 6943fbd0f5dcd750e1c9f233f778734d
# @sid 20251174010019
# @aid V2.4


#begin_inputs
valor_compra = float(input("Digite o  valor da compra: "))
#end_inputs
valor_avista = valor_compra * 0.91
prestacao_5x = valor_compra / 5
prestacao_10x = (valor_compra * 1.17) / 10
print(f"{valor_avista:.1f}")
print(f"{prestacao_5x:.1f}")
print(f"{prestacao_10x:.1f}")