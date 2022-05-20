
prova1 = int(input('Digite a nota 1:'))
trabalho = int(input('Digite a nota do trabalho:'))
prova2 = int(input('Digite a nota 2:'))


media =((prova1*2)+trabalho+(prova2*2))/5

if media >= 6:
    print('Aluno aprovado!') 

else:
    if media >= 3:
        print('Aluno recuperação!')
    else:
        print('Aluno reprovado!') 


