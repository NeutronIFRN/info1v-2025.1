# @cikey 6943fbd0f5dcd750e1c9f233f778734d
# @sid 20251174010019
# @aid V4.3


#begin_inputs
mes = 1
#end_inputs
meses = [
    "janeiro",
    "fevereiro",
    "marco",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]
if 1 <= mes <= 12:
    print(meses[mes - 1])
else:
    print("mes invalido")