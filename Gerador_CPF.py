
import random

cpf_para_soma = ''
for _ in range(0,9):
    cpf_para_soma += str(random.randint(0,9))

soma_cpf1 = 0
indice_mult1 = 10
for i in cpf_para_soma:
    soma_cpf1 = soma_cpf1 + (int(i)* indice_mult1) 
    indice_mult1 -= 1
result_soma_cpf = (soma_cpf1*10)%11
digito1 = result_soma_cpf if result_soma_cpf <= 9 else 0



cpf_para_soma2 = cpf_para_soma + str(digito1)
soma_cpf2 = 0
indice_mult2 = 11
for i in cpf_para_soma2:
    soma_cpf2 = soma_cpf2 + (int(i)*indice_mult2)
    indice_mult2 -= 1
result_soma_cpf2 = (soma_cpf2*10)%11
digito2 = result_soma_cpf2 if result_soma_cpf2 <= 9 else 0

digitos = f'{digito1}{digito2}'

cpf_visu="{}.{}.{}-{}".format(
    cpf_para_soma[:3], 
    cpf_para_soma[3:6], 
    cpf_para_soma[6:9], 
    digitos[0:]
    )

print(f'CPF VALIDO: {cpf_visu}')

