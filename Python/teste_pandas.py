import os;

os.system("cls");

import pandas as pd;

#Lendo CSC e carregando DataSet que tem separador com ";"
data = pd.read_csv("./files/GasPricesinBrazil_2004-2019.csv" , sep=';');

#Lendo Excel e carregando DataSet
#excelData = pd.read_excel("./files/GasPricesinBrazil_2004-2019Excel.xlsx");
#print(excelData);

print(data);
print("-----------------------\n\n\n")

# Carregando somente algumas linhas, escolhendo a quantidade dentro do head(quantidade)
print(data.head(10))
print("-----------------------\n\n\n")

#Mostrando informações sobre o DataSet com info();
print(data.info());
print("-----------------------\n\n\n")

#Criando DataSets

meuDataSet = pd.DataFrame({
    "Nome": ["Caio" , "Giovanna" , "Malu" , "Henry"],
    "Idade": [20 , 20 , 5 , 4],
    "Sexo": ["Masculino" , "Feminino" , "Feminino" , "Masculino"]
});

print(meuDataSet);
print(meuDataSet.shape);
print(meuDataSet.info());

print("-----------------------\n\n\n")

print("Exibindo todas as colunas do Dataframe");

print(meuDataSet.columns);

print("-----------------------\n\n\n")

print("Renomeando as colunas");

print(meuDataSet);

print("\n");

meuDataSet = meuDataSet.rename(
    columns= {
        "Nome": "FullName", #Renomeia de Nome para FullNName
        "Idade": "Age",     #Renomeia Idade para Age
        "Sexo": "Gender"    #Renomeia Sexo para Gender
    },
);

print(meuDataSet);

print("-----------------------\n\n\n")

print("SERIES");

# Pegando a COLUNA de ESTADO
# Não precisa do head() apenas fiz isso para pegar apenas 2 linhas
s1 = data["ESTADO"].head(2);

print(s1);

#Criando minha SERIE

s1 = pd.Series(
    [
        "Caio",
        "Giovanna",
        "Malu",
        "Henry"
    ],
    name="Nomes"
);

print(s1);

print("-----------------------\n\n\n")

print("Atribuindo valores para um Dataframe");
