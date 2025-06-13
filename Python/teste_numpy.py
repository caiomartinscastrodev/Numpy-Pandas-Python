import os;

os.system("cls");

import numpy as np;

# Criando um array simples
print("-----------------");
print("Array simples");
arr = np.array([1,2,3,4,5,6]);
print(arr);

print("-----------------");
print("Arange normal");
arr2 = np.arange(1 , 7);
print(arr2);

print("Arange com steps de 2 em 2 ou mais");
arr3 = np.arange(1 , 10 , 2);
print(arr2)

print("-----------------");
print("Linspace");
print("Numero entre 0 e 100 4 vezes");
arr4 = np.linspace(0 , 100 , 4);
print(arr4);

print("-----------------");
print("Matrizes e Arrayz com zeros");

print("Array com 5 zeros:\n " + str(np.zeros((5))));

print("Matriz 2D 3:4 de zeros:\n" + str(np.zeros((3,4))));

print("Matriz 3D 3,4,2:\n" + str(np.zeros((3,4,2))))

print("-----------------");

print("Matrizes e Arrayz com UMs");

print("Array com 5 UMs:\n " + str(np.ones((5))));

print("Matriz 2D 3:4 de UMs:\n" + str(np.ones((3,4))));

print("Matriz 3D 3,4,2:\n" + str(np.ones((3,4,2))))

print("-----------------");

print("Matrizes e Arrayz com eye");

print("Array com 5: \n" + str(np.eye(5)));

print("Matriz 2D 3:4:\n" + str(np.eye(3,4)));

print("-----------------");

print("shape-Forma - size-Tamanho - ndim - Numero de colunas");

arrF = np.zeros((3,3,4));
print("size: " + str(arrF.size));
print("shape: " + str(arrF.shape));
print("ndim: " + str(arrF.ndim));

print("-----------------");

print("Concatenando arrays");

a1 = np.array([1,2,3]);
a2 = np.array([4,5,6]);

conc = np.concatenate((a1,a2));
print(conc);
conc = np.concatenate((a2,a1));
print(conc);

print("-----------------");

print("Matriz 4x4 com aleatorios entre 0 e 1");
a = np.random.rand(4,4);
print(a);

print("-----------------");

print("Matriz 5x5 com aleatorios entre 19 e 50")

a = np.random.randint(19 , 51 , size = (5,5));
print(a);

print("-----------------");

print("Filtrando itens de um array");

a = np.random.randint(1 , 10 , size=(7,7));
print("Tudo");
print(a);

print("Maiores que 5");
print(a[a > 5]);

print("Menores que 5");
print(a[a <= 5]);

print("Impares")
print(a[a % 2 != 0]);

print("Pares");
print(a[a % 2 == 0]);

print("-----------------");

print("Operações nos arrays");

a = np.random.randint(1,11 , size=(5,5))
print(a);

print("sum - soma");
print(a.sum())

print("max - maximo");
print(a.max());

print("min - minimo");
print(a.min());

print("mean - media");
print(a.mean());

print("-----------------");

print("Selecionando dados dos arrays");

umD = np.arange(1 , 11);
print(umD);
print("umD[1]: " + str(umD[1]));
print("umD[1:5]: " + str(umD[1:5]));

doisD = np.random.randint(1 , 11 , size=(6,6));
print(doisD);

print("doisD[3 , 3]: \n" + str(doisD[3 , 3]));
print("doisD[0 , 0:3]: \n" + str(doisD[0 , 0:3]));
print("doisD[0:3 , 3:6]: \n" + str(doisD[0:3 , 3:6]));