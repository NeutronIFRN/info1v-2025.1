# @cikey 6943fbd0f5dcd750e1c9f233f778734d
# @sid 20251174010019
# @aid V4.2


#begin_inputs
idades = [34, 90, 4, 56, 12, 78, 54, 13, 24, 9]
gen_idades = (i for i in idades)
input = gen_idades.__next__

 #mantenha esse trecho. o input será manipulado aqui.
#end_inputs
maior = 0

for i in range(10):
    idade = input()
    if idade >= 18:
        maior += 1

print(maior)
