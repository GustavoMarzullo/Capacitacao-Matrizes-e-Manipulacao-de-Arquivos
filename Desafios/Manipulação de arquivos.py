#Desafio da manipulação de arquivos

#abrindo o arquivo
with open("notas.txt","r") as f:
    materia,creditos,nota=[],[],[]
    for linha in f:
        linha=linha[:-1] #remove o último caractere
        campo=linha.split(";")#o que separa os dados
        materia.append(campo[0])
        creditos.append(int(campo[1])) #os créditos são um número inteiro, ou seja, usa-se int
        nota.append(float(campo[2]))   #as notas são números decimais, logo, usa-se float


print("Dados importados:")
print("Matérias:",materia)
print("Créditos:",creditos)
print("Notas:",nota)

#calculando o cr
soma_mult=0 #numerador
soma=0 #denominador
for i in range(len(nota)):
    soma_mult+=creditos[i]*nota[i]
    soma+=creditos[i]
CR=round(soma_mult/soma,2)

#escrevendo o arquivo com a respota
with open("resposta.txt",'w') as f:
    f.write("CR = "+str(CR)+"\n")
    f.write("Maior nota = "+str(max(nota)))
    print("Arquivo salvo com sucesso!")