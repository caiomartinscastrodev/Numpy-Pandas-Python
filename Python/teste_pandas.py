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

# Salvando uma copia
# Caso eu coloque apenas bkp_estado = data["ESTADO"]; eu não estou salvando os dados, apenas estou salvando a referencia

bkp_estado = data["ESTADO"].copy();

#Modificando todos os valores
data["ESTADO"] = "SP";

print(data.head());
print(bkp_estado.head());

#Mudando novamete para o backup
data["ESTADO"] = bkp_estado;

print(data.head());

nrow = data.shape[0];
ncol = data.shape[1]

print(nrow);
print(ncol);

print("-----------------------\n\n\n")


#Criando novas colunas

print("Criando novas colunas");

data["NOVA COLUNA"] = "DEFAULT";
print(data.head());

print("-----------------------\n\n\n")


# Selecionando por indices

print("Selecionando por indices\n");

print(data.head(1));
# Selecionando pelo indice
print(data.iloc[1])
# Selecionando por uma lista de indices
print(data.iloc[[7,8,9]]);

print("-----------------------\n\n\n")

# Selecionando Colunas e LINHAS
print("Selecionando coluna e UMA linha\n");

print(data["ESTADO"][0]);

print("\nSelecionando coluna e VARIAS linhas\n");

print(data["ESTADO"][0:3]);

print("\nSelecionando coluna e VARIAS linhas EXPECIFICAS\n");

print(data["ESTADO"][[0,3,5,7]]);

print("-----------------------\n\n\n")

print("Selecionando LINHA e UMA COLUNA\n");

print(data.iloc[0]["ESTADO"]);

print("\nSelecionando LINHA e VARIAS colunas\n");

print(data.iloc[0][["ESTADO" , "REGIÃO"]]);

print("\nSelecionando VARIAS LINHA e VARIAS COLUNAS\n");

print(data.iloc[0:3][["ESTADO" , "REGIÃO"]])

print("\nOU\n");

print(data.iloc[[0,1,2]][["ESTADO" , "REGIÃO"]]);

print("-----------------------\n\n\n")

print("Deletando colunas | Salvando o DataFrame");

print(data.columns);

del data["Unnamed: 0"];
print(data.columns);

#data.to_csv("./files/Dataframe.csv" , sep=";");

print("-----------------------\n\n\n")

print("Filtrando dados");

df = pd.read_csv("./files/Dataframe.csv" , sep=";");
print(df.columns);

# Filtro direto
print(df[df["ESTADO"] == "SAO PAULO"]);


# Filtro com &

print(df[(df["ESTADO"] == "RIO DE JANEIRO") & (df["PRODUTO"] == "GASOLINA COMUM")]);

# Filtro com |

print(df[(((df["ESTADO"] == "SAO PAULO") | (df["ESTADO"] == "RIO DE JANEIRO")) & (df["PRODUTO"] == "GASOLINA COMUM"))]);

print("-----------------------\n\n\n")

print("Convertendo dados");

df_prev1 = df.copy();

print(df_prev1.info());

df_prev1["DATA INICIAL"] = pd.to_datetime(df_prev1["DATA INICIAL"]);
df_prev1["DATA FINAL"] = pd.to_datetime(df_prev1["DATA FINAL"]);

print(df_prev1.info());

df_prev1["PREÇO MÍNIMO DISTRIBUIÇÃO"] = pd.to_numeric(df_prev1["PREÇO MÍNIMO DISTRIBUIÇÃO"] , errors="coerce");
df_prev1["PREÇO MÉDIO DISTRIBUIÇÃO"] = pd.to_numeric(df_prev1["PREÇO MÉDIO DISTRIBUIÇÃO"] , errors="coerce");
df_prev1["PREÇO MÁXIMO DISTRIBUIÇÃO"] = pd.to_numeric(df_prev1["PREÇO MÁXIMO DISTRIBUIÇÃO"] , errors="coerce");
df_prev1["PREÇO MÍNIMO REVENDA"] = pd.to_numeric(df_prev1["PREÇO MÍNIMO REVENDA"] , errors="coerce");
df_prev1["PREÇO MÉDIO REVENDA"] = pd.to_numeric(df_prev1["PREÇO MÉDIO REVENDA"] , errors="coerce");
df_prev1["PREÇO MÁXIMO REVENDA"] = pd.to_numeric(df_prev1["PREÇO MÁXIMO REVENDA"] , errors="coerce");

print(df_prev1.info())

#print(df_prev1[df_prev1["PREÇO MÍNIMO DISTRIBUIÇÃO"].isnull()]["PREÇO MÍNIMO DISTRIBUIÇÃO"]);

print("-----------------------\n\n\n")

print("Tirando valores vazios");

# Preenchendo qualquer valor NULL com 0
df_t1 = df_prev1.copy();
df_t1 = df_t1.fillna(0);
print(df_t1.info())

# Preenchendo valores expecificos NULL com 0
df_t2 = df_prev1.copy();
df_t2 = df_t2.fillna(
    value={
        "PREÇO MÍNIMO DISTRIBUIÇÃO": 0,
        "PREÇO MÉDIO DISTRIBUIÇÃO": 0,
        "PREÇO MÁXIMO DISTRIBUIÇÃO": 0
    }
);
print(df_t2.info());

# Removendo qualquer series/registro/linnha que tenha null

df_t3 = df_prev1.copy();
df_t3 = df_t3.dropna();
print(df_t3.info())
