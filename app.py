import os

restaurantes = [
                {'nome':'beira-mar bc', 'categoria':'brasileira', 'ativo':False},
                {'nome':'brava', 'categoria':'portuguesa', 'ativo':False},
                {'nome':'bucanas', 'categoria':'bebidas', 'ativo':False}
                ]


def exibir_nome_programa():
    '''Responsavel por exibir o nome inicial do programa'''

    print('sabor express\n')

def exibir_subtitulo(texto):
    '''Exibi um subtitutlo passando um texto a ele'''

    os.system('cls')
    print(texto)

def encerrar_app():   
    '''encerra o app saindo do console''' 

    exibir_subtitulo('app encerrado! \n')  

def voltar_menu():
      '''Volta ao menu digitando uma tecla'''

      input('\n   digite uma tecla para voltar \n')
      main() 

def opcao_invalida():
    '''Avisa quando uma ocpao nao é valida voltando ao menu'''

    exibir_subtitulo('esta opcao é invalida!\n')  
    voltar_menu()  

def mostrar_opcoes():
    '''Mostra as opcoes do app'''

    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar restaurante')
    print('4. sair\n')

def listar_restaurantes():
    '''Responsavel por listar os restaurante em ordem no console'''

    print(f'{'Nome restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}\n')
    for cadastro_restaurantes in restaurantes:
        nome_Restaurante = cadastro_restaurantes['nome']
        categoria = cadastro_restaurantes['categoria']
        ativo = 'Esta ativo' if cadastro_restaurantes['ativo'] else 'Nao esta ativo' 
        print(f'.{nome_Restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')

def alterar_estado_restaurante():
    '''Altera o estado do restaurante entre ativo ou inativo'''

    exibir_subtitulo('alternando estado do restaurante')
    nome_restaurante = input('Nome do restaurante que deseja alterar o estado - ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
    mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso!'
    print(mensagem)

    if not restaurante:
        print('O restaurante nao foi encotrado')
    
def escolher_opcoes():
    '''Responsavel por executar determinadas acoes ao digitar uma opcao no console'''

    try:
        opcao_escolhida = int(input('escolha uma opcao --> '))
        print(f'\nVoce escolheu a opcao {opcao_escolhida} ')

        if opcao_escolhida == 1:            
            exibir_subtitulo('\ncadastro de restaurantes!\n')
            cadastro_restaurantes = input('Digite o nome do restaurante | ')

            categoria = input(f'Digite a categoria do {cadastro_restaurantes} | ')

            dados_do_restaurante = {'nome': cadastro_restaurantes,
                                    'categoria':categoria,
                                    'ativo':False                                    
                                    }
            restaurantes.append(dados_do_restaurante)
            print(f'\nO restaurante "{cadastro_restaurantes}" foi cadastrado com a categoria de "{categoria}"! ')
            voltar_menu()

        elif opcao_escolhida == 2:            
            exibir_subtitulo('listando restaurantes - \n')
            listar_restaurantes()
            voltar_menu()

        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
            voltar_menu()
        elif opcao_escolhida == 4:
            print('sair')
            
            encerrar_app()
        else:
            opcao_invalida()
    except:    
        opcao_invalida()

def main():
    '''Principal funcao do app, aonde possui tudo que é principal na tela inicial'''
    
    os.system('cls')
    exibir_nome_programa()
    mostrar_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()