from tkinter import *
import hudmain
import animframe
import gamesystem
import threading
import replay

class GameWindow(Tk):
    def __init__(self, master=None):
        super(GameWindow, self).__init__(master)
        # Definição tamanho e posição da janela 
        self.width = 800 # Largura
        self.height = 600 # Altura
        self.posx = 350 # Posição de x
        self.posy = 50 # Posição de y

        #Setter Geometria 
        self.geometry(f'{self.width}x{self.height}+{self.posx}+{self.posy}')

        #Definição do título da Janela
        self.title('JohKenPoh')

        #Configurações
        self.configure(background='#1a1a1a') # Cor de fundo geral
        self.resizable(False, False)  # Não permite que o tamanho da janela seja alterado
        
        #Istanciamento dos compartimentos----------------------------------
    
        """ HUD """
        self.hud = hudmain.Hud(self)
        self.hud.pack(side=TOP, fill=BOTH)

        """Central Widget"""
        self.display = animframe.DisplayAnim(None)
        self.display.pack(side=TOP, fill=BOTH)

        """Player Buttons"""
        self.playerbuttons = hudmain.PlayerButtons(self, self.hud) 
        self.playerbuttons.pack(side=BOTTOM, fill=BOTH)

        self.player_choice = ''
        self.ia_choice = ''
        self.v_state = ''
        self.on_animation = False

    def construct_replay(self, state2):
        self.replay = replay.Replay(self, state2)
        self.replay.pack(fill=BOTH, expand=1)
        self.update()
        
    def new_init(self):
        self.replay.destroy()
        """ HUD """
        self.hud = hudmain.Hud(self)
        self.hud.pack(side=TOP, fill=BOTH)

        """Central Widget"""
        self.display = animframe.DisplayAnim(None)
        self.display.pack(side=TOP, fill=BOTH)

        """Player Buttons"""
        self.playerbuttons = hudmain.PlayerButtons(self, self.hud) 
        self.playerbuttons.pack(side=BOTTOM, fill=BOTH)

        self.player_choice = ''
        self.ia_choice = ''
        self.v_state = ''
        self.on_animation = False

        self.update()

    def game_win(self):
        self.hud.destroy()
        self.display.destroy()
        self.playerbuttons.destroy()
        print('win')
        self.construct_replay('win')

    def game_over(self):
        self.hud.destroy()
        self.display.destroy()
        self.playerbuttons.destroy()
        print('lose')
        self.construct_replay('lose')

    
    def start_game(self, player_choice):
        """Define a escolha da IA"""
        self.player_choice = player_choice
        self.ia_choice = gamesystem.ia_chocer()

        """Faz a verificação de vitoria ou derrota"""
        verify_state = gamesystem.battle_verification(player_choice, self.ia_choice)
        self.v_state = verify_state
        """"""
        self.on_animation = True
        """Reservado para a inicialização da animação"""
        t = threading.Thread(target=self.display.battle_animation, args=())
        t.start()
        
        
        """Remoção de pontos dos jogadores"""
        if verify_state == 'victory':
            self.hud.enemy.damage()
        elif verify_state == 'draw':
            pass
        elif verify_state == 'defeat':
            self.hud.player.damage()


