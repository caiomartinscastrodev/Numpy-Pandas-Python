name = "Caio Martins Castro";

# Mostrando do 0 caracter até o 6
print(name[0:6])

# Exibindo a quantidade de caracteres
print(len(name))

# Cortar os espaços extras de inicio e fim do caracter
wrongName = "    Caio Martins Castro    ";
print("Quantidade de caracteres: " + str(len(wrongName.strip())));

# Usando Upper e Split
teste = "Testando".upper().split('T');
print(teste);

# Usando o Replace
womanName = "Giovanna Pereira Silva";
womanName = womanName.replace(" " , "-");
print(womanName);

#Contains e Não Contains
t1 = "Caio";
t2 = "Caio Martins Castro";
res = t1 not in t2;
print(res);

