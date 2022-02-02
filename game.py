#um rpg de texto curto apenas para teste
import sys
print("                                                 *******")
print("                                 ~             *---*******")
print("                                ~             *-----******* ")
print("                         ~                   *-------*******")
print("                        __      _   _!__     *-------*******")
print("                   _   /  \_  _/ \  |::| ___ **-----********   ~")
print("                 _/ \_/^    \/   ^\/|::|\|:|  **---*****/^\_")
print("              /\/  ^ /  ^    / ^ ___|::|_|:|_/\_******/  ^  \ ")
print("             /  \  _/ ^ ^   /    |::|--|:|---|  \__/  ^     ^\___")
print("           _/_^  \/  ^    _/ ^   |::|::|:|-::| ^ /_  ^    ^  ^   \_")
print("          /   \^ /    /\ /       |::|--|:|:--|  /  \        ^      \ ")
print("         /     \/    /  /        |::|::|:|:-:| / ^  \  ^      ^     \ ")
print("   _Q   / _Q  _Q_Q  / _Q    _Q   |::|::|:|:::|/    ^ \   _Q      ^")
print("  /_\)   /_\)/_/\\)  /_\)  /_\)  |::|::|:|:::|          /_\)")
print("_O|/O___O|/O_OO|/O__O|/O__O|/O__________________________O|/O__________")
print("//////////////////////////////////////////////////////////////////////")
print("///////////////////////WELCOME TO THE FUTURE//////////////////////////")
print("//////////////////////////////////////////////////////////////////////")

# função init ela inicia e sai do programa 
def __init__():
    iniciar=int(input("aperte (1) para inicar/reiniciar o jogo ou (2) para sair= "))
    if iniciar==1:
       nome()
    elif iniciar==2:
        sys.exit()
    else:
       __init__()

def nome():
    nome=input("entre com o seu nome de jogador: ")
    print(nome+ ", seu saldo é= 10.000 ")
    print("use esse dinheiro com sabedoria")
    print( )
    cena1()


# variaveis iniciais
dinheiro=int(10.000)
saldo=int(dinheiro)
bilhete=0

print( )

# cena1 primeiro capitulo da historia
def cena1():
    print("no ano de 2075 a ciencia ja tinha feito grandes descobertas na area de intelicencia artifia, criado novas especies inteligentes meio humano meio animal dentre outras coisas descobriram que a magia realmente existe... /n E para manter esse fragil equilibrio foi criado uma força tarefa especial para combater os novos criminososmas nem sempre eles tão conta e quando isso acontece eles contratam caçadores de recompensa no caso voce, sua missão é capturar vivo ou morto o mafioso e assasino em série jhonny \n")
    print("voce acabara de sair de casa para onde deseja ir? \n 1-bar da cidade \n 2-encontrar seu contado")
    cena1=int(input("digite o numero de sua escolha: ")) #primeira escolha do jogo

    if cena1==1: #se a cena1 for igual a opção 1 vista anteriomente segue-se esse trecho
        print("\n era noite, muitos bebados e vagabundos, almas perdidas na escuridão do mundo, oque voce fara agora? \n 1-beber até cair e esperar algo acontecer \n 2-interrogar as pessoas do bar")
        consequencia1=int(input("digite o numero de sua escolha: ")) #faz referencia a opção1(bar) sendo essa a escolha da consequencia
    
        if consequencia1==1: #se escolhido a consequencia1 tera o dinheiro zerado e reiniciara o game
            saldo=dinheiro-dinheiro
            print("voce ficou bebado e teve a carteira furtada perdendo todo seu dinheiro \n seu saldo atual é de : " + saldo + "\n voce não tem mais dinheiro para continuar a missão \n GAME OVER")
            __init__() #reinicia o jogo

        if consequencia1==2: #se escolhido a consequencia2 vista anteriomente segue-se esse trecho
            saldo=dinheiro+int(1500)
            global bilhete
            bilhete=bilhete+1
            print("todos estavam muito bebados e não ajudaram em nada mas voce furtou umas carteiras \n seu saldo atual é de : " + saldo + "em uma das carteiras voce achou um ingresso para o bordel lux, que fica no submundo, assinado com jn vá verificar \n conseguiu um item especial parabens!!!")
            cena2() #segue para a função cena2
             


    if cena1==2: #se a cena1 for igual a opção 2 vista anteriomente segue-se esse trecho
        print("voce o encontro em um beco escuro, ele exige algo em troca da informação, oque voce fará? \n 1-pagar a ele 2mil \n 2-agredir")
        consequencia2=int(input("digite o numero de sua escolha: "))

    if consequencia2==1: #se a consequencia escolhida foi a consequencia1 segue esse trecho
            saldo=dinheiro-int(2.000)
            print("ele recebe o dinheiro e diz que voce deve ir até o bordel lux que fica no submundo o local pertence a ele!!! \n voce ficou com 8000 coins")      
            cena2() #segue para a função cena2

    elif consequencia2==2: #se a consequencia escolhida foi a consequencia2 segue esse trecho
        print("ele não estava sozinho e voce foi atacado violentamente por trás \n GAME OVER")
        __init__() #reinicia o jogo

print( )

#cena2 segundo capitulo da história
def cena2():
    print("voce chega no submundo um local perigoso em baixo da area mais pobre da cidade \n após falar com um hibrido de lobo e pedir informção voce logo se encontra na frente do bordel, havia dois segurancas na porta. oque voce fará? \n 1-tentar invadir na força bruta \n 2-criar confusao e entrar escondido \n 3-entregar bilhete")
    consequencia1=int(input("digite o numero da opção desejada: "))

    if consequencia1==1: #reinicia a cena2
        print("voce tentou invadir na força bruta mas foi impedido pelos seguranças. tente outra vez")
        cena2() #chama a cena2

    if consequencia1==2: #segue para a cena3
        print("voce criou uma confusao na rua fazendo os seguranças se distrairem, voce usa suas habilidades e invadi sem ser visto")
        cena3() #chama a cena3

    if consequencia1==3 and bilhete==1: #segue para a cena3
        print("voce se aproxima e entrega o bilhete a o seguranca, o mesmo lhe deixa entrar sem problema")
        cena3() #chama a cena3
    else:
        print("voce não tem o bilhete, foi agredido e jogado na rua")
        cena2() #chama a cena2

print( )

#cena3 segundo capitulo da historia
def cena3():
    print("dentro do bordel voce encontra uma escada e um elevador, o escritorio fica no decimo andar. escada ou elevador? \n 1-para elevador \n 2-para escada")
    consequencia1=int(input("digite o numero de sua escolha: "))
    print( )

    if consequencia1==1: #referente a opção1/elevador
        print("voce o encontrou, ele estava de costa olhando a cidade inferior \n jhonny- eu esperava alguem mais capacitado para essa missão suicida, recomendo que vá embora enquando ainda tem suas pernas \n 1-não foi dificil encontrar voce da mesma forma nao sera dificil acabar com sua raça \n 2-eu vou ganhar uma boa grana com voce")
        fala1=int(input("digite o numero de sua escolha: "))

        if fala1==1: #se escolhido fala1 segue o trecho abaixo
            print("jhonny-vejo que voce escolheu a morte \n jhonny se vira e puxa uma katana negra a mesma soltava faisca o que significava que ela estava eletrificada, oque voce fara? \n 1-fugir \n 2-enfrentar")
            consequencia1=int(input("digite o numero de sua escolha: "))
            if consequencia1==1:
                print("após voltar para casa voce recebe um link de video do youtube após clicar voce se depara com seu video fugindo da batalha com efeito de penas e sons de galinha \n voce virou um sucesso no youtube com esse video mas um fracasso nesse jogo, tente outra vez e tome cuidado para não botar um ovo ;D")
                __init__
        if fala1==2: #se escolhido fala2 segue o trecho abaixo
            print("johnny-voce chegou longe porque ao invés de lutarmos voce não se une a mim? voce tera muito dinheiro e tudo oque mais puder imaginar \n 1-aceitar \n 2-negar e atacar")
            consequencia1=int(input("digite o numero de sua escolha: "))

            if consequencia1==1: #zera o jogo sem luta
                print("o trato foi feito, voce se corrompeu e se transformou naquilo que jurou destruir, mas agora é rico e o braço direito de johnny")
                __init__() #fim de jogo

            elif consequencia1==2: #se escolhido a consequencia2 gera luta
                print("voces lutam por alguns mas ele não tem chance e voce acaba o levando a justiça e se torna muito famoso \n MISSÃO CONCLUIDA COM SUCESSO")

    if consequencia1==2: #referente a opção 2/ escada
        print("voce demorou muito para subir toda a escadaria e seu alvo que estava no topo pegou o elevador para descer e saiu do prédio \n nem sempre o caminho mais longo é o melhor lhe daremos outra chance :p")
        cena3()

__init__()