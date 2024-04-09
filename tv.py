class Tv():
    def __init__(self):
        self.ligado=False
        self.volume= 99
        self.canal= 0


    def ligar(self):
        print('A TV esta deligada.')
        ligar= int(input('Digite 1 para ligara a TV:'))
        if(ligar!=1):
            self.ligar()
        else:
            self.ligado=True
            print('A TV ligou')
            print('Canais disponiveis: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10')
            escolhercanal=int(input('Qual canal você quer assistir?'))
            if(escolhercanal>10 or escolhercanal<1):
                print('Canal invalido')
                self.escolherCanal()
            else:
                self.canal= escolhercanal
                self.getInfo()



    def desligada(self):
        print('A TV esta desligada!')
        self.ligado= False
        return
    
    
    def volumeMudo(self):
        self.volume=0
        self.getInfo()


    def aumentarVolume(self):
        if (self.volume>=100):
            print(f'Volume {self.volume} é o maximo')
            self.getInfo()
        else: 
            self.volume= self.volume+1
            self.getInfo()

    
    def diminuirVolume(self):
        if (self.volume<=0):
            print('A Tv esta no mudo')
            self.getInfo()
        else:
            self.volume= self.volume-1
            self.getInfo()


    def escolherCanal(self):
        print('Canais disponiveis: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10')
        escolhercanal=int(input('Qual canal você quer assistir?'))
        if(escolhercanal>10 or escolhercanal<1):
            print('Canal invalido')
            self.escolherCanal()
        else:
            self.canal= escolhercanal
            self.getInfo()


    def canalAnterior(self):
        if (self.canal<=1):
            print('Não tem canal anterior')
            self.getInfo()
        else:
            self.canal= self.canal-1
            self.getInfo()


    def proximoCanal(self):
        if(self.canal>=10):
            print('Ultimo canal da lista')
            self.getInfo()
        else:
            self.canal= self.canal+1
            self.getInfo()


    def mostraCanal(self):
        if(self.canal==0):
            print('Canal invalido')
            print('Tela azul')
        else:
            print('Está reproduzindo o canal', self.canal)


    def mostraVolume(self):
        if(self.volume==0):
            print('TV esta no modo mudo')
        else:
            print('O volume esta em', self.volume)


    def getInfo(self):
        print('')
        print('-*'*30)
        self.mostraCanal()
        self.mostraVolume()
        print('-*'*30)
        print('')
        self.main()


    def menu(self):
        print('1- Escolher de canal')
        print('2- Proximo canal')
        print('3- Canal anterior')
        print('4- Aumentar volume')
        print('5- Diminuir volume')
        print('6- TV modo silencioso')
        print('7- Delsigar TV')
        escolha= int(input('Qual sua escolha?'))
        if(escolha==1):
            self.escolherCanal()
        elif(escolha==2):
            self.proximoCanal()
        elif(escolha==3):
            self.canalAnterior()
        elif(escolha==4):
            self.aumentarVolume()
        elif(escolha==5):
            self.diminuirVolume()
        elif(escolha==6):
            self.volumeMudo()
        elif(escolha==7):
            self.desligada
        else:
            print('Opção invalida, voltando para informações')
            self.getInfo()


    def main(self):
        print('O que você deseja fazer')
        print('1- Menu')
        print('2- Desligar')
        escolha= int(input('Digite aqui:'))
        if(escolha==1):
            self.menu()
        elif(escolha==2):
             self.desligada()
        else:
            print('Opção invalida, tente novamente!!')
            self.main()

   

tv1= Tv()
tv1.ligar()