# Desafio da multiplicação de matrizes

def CriarMatrizZeros(m,n):
    '''Cria uma matriz de zeros de ordem mxn'''
    A=[]
    for i in range(m): 
        temp=[]
        for j in range(n):#em cada loop interno se cria uma vetor de n zeros
            temp.append(0)
        A.append(temp) #em cada loop externo se coloca um vetor de n zeros m vezes 
    return A

def mult(A,B):
    '''Multiplica as matrizes A e B'''
    m,n=len(A),len(A[0]) #tamanho da matriz A
    n2,p=len(B),len(B[0]) #tamanho da matriz B

    if n!=n2: #retorna uma erro se A e B não podem ser multiplicadas (vide definição)
        raise ValueError ('Matrizes incompatíveis')

    #começando a calcular a matriz resultante
    C=CriarMatrizZeros(m,p)
    for i in range(m): #iterando sobre as linhas
        for j in range(p): #iterando sobre os elementos da linha
            soma=0
            for k in range(n): #somatório (vide definição)
                soma+= A[i][k]*B[k][j]
            C[i][j]=soma
    return C

#Testando o código
A=[[1,1],
   [1,-1]]

B=[[5],
   [2]]
print("Primeiro teste")
print("A=",A)
print("B=",B)
print("AB=",mult(A,B))

print("\nSegundo teste")
A=[[1,2,3],
   [4,5,6]]

B=[[7,8],
   [9,10],
   [11,12]]

print("A=",A)
print("B=",B)
print("AB=",mult(A,B))

A=[[1],[2],[3]]
B=[[1,2,3]]
print("\nTerceiro teste")
print("A=",A)
print("B=",B)
print("AB=",mult(A,B))