musicas = ["Michael Jackson - Billie Jean", "Bee Gees - Stayin' Alive", "Bob Marley - Exodus", "Di Melo - Kilariô", "Maglore - Me Deixa Legal"]

def exibir_menu():
    print("\n<-=JUKEBOX=->\n")
    print("Escolha uma música do menu:")
    
    for i in range(len(musicas)):
        print(f"{i + 1} - {musicas[i]}")

def musica_escolhida(opcoes):
    if 1 <= opcoes <= 5:
        print(f'\nA música escolhida foi {musicas[opcoes - 1]}')
        
        adicionar = int(input(f'''
Você deseja adicionar {musicas[opcoes - 1]} à sua playlist? 
1 - sim 
2 - não 

'''))
        if adicionar == 1:
            print('\nMúsica adicionada com sucesso!')
        else:
            print('\nMúsica não adicionada.')
    else:
        print('A música escolhida não existe')

while True:
    exibir_menu()
    opcoes = int(input("\nDigite o número da música escolhida: "))
    musica_escolhida(opcoes)
    
    continuar = int(input("\nVocê deseja continuar ouvindo? 1 - sim, 2 - não: "))
    if continuar != 1:
        print("\nEncerrando programa...")
        print("PROGRAMA ENCERRADO")
        break
