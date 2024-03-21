import random 
letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789!@#$%&*()""-+'
senha = ''
def gerarSenha(quantidadeDeLetras:int=6,quantidadeDeSenha:int=1):
    for i in range(quantidadeDeSenha):
        for _ in range(quantidadeDeLetras):
            global senha
            senha += letras[random.randint(0,len(letras)) - 1]
        print(f"Senha{i+1}: {senha}")
        senha = ''
        
a = gerarSenha(10,35)
print()