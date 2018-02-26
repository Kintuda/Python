nome = input("Digite o nome do aluno: ")
notas = [0,0,0,0]
faltas = [0,0,0,0]
for i in range(len(notas)):
     while True:
        try:
            nota = int(input("Digite a nota do " + str(i+1) + " Bimestre: "))
            falta = int(input("Digite as faltas do " + str(i+1) + " Bimestre: "))
            notas[i] = nota
            faltas[i] = falta
        except ValueError:
            print("Apenas valores numericos")
            continue
        break
mediaNotas  = sum(notas)/4
FaltasTotal = sum(faltas)
if (mediaNotas >= 6 and FaltasTotal < 30):
    status = "Aprovado"
    resultadoFinal = "O aluno " + nome + " foi " + status
else:
    status = "Reprovado"
    resultadoFinal = "O aluno " + nome + " foi " + status
print(resultadoFinal)
print("Média: " + str(mediaNotas))
print("Faltas: " + str(FaltasTotal))


