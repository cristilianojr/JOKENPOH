from tkinter import *
import gamesystem


class CharHud(Frame):
    def __init__(self, master, name, font='Arial 12', foreground='#000000', **kw):
        super(CharHud, self).__init__(master, **kw)

        """Configurações do CharHud"""
        self.life = 1 #
        self.simbol = ('❤', '☠')
        self.text_life = StringVar()
        self.text_life.set(self.simbol[0]*self.life)
        self.font = font
        self.foreground = foreground
        self.background = self['background']
        self.name = name
        """Criação dos Labels de texto"""
        self.label_name = Label(
            self, 
            text=self.name,
            font=self.font,
            foreground=self.foreground,
            background=self.background
        )

        self.label_life = Label(
            self,
            text=self.text_life.get(),
            font=self.font,
            foreground=self.foreground,
            background=self.background
        )

        """Instanciando os Labels"""
        self.label_name.place(x=10, y=10)
        self.label_life.place(x=10, y=50)


    def heal(self):
        """
        Quando chamada, aumenta o Self.life em 1 e verifica se o valor max
        é 8.
        Seta o valor de texto da variável self.label_life 
        """
        self.life += 1
        
        if self.life >= 9:
            self.life = 8

        self.text_life.set(self.simbol[0]*self.life)
        self.label_life['text'] = self.text_life.get()


    def damage(self):
        """
        Diminui o self.life em 1;
        verifica se o valor de self.life é menor que 0, se verdadeiro, 
        seta o valor = 0 e seta a string como morto.
        Dará end game.
        """
        self.life -= 1

        if self.life <= 0:
            self.life = 0
            self.text_life.set(self.simbol[1])
            self.label_life['text'] = self.text_life.get()
            return 

        self.text_life.set(self.simbol[0]*self.life)
        self.label_life['text'] = self.text_life.get()


class Hud(Frame):
    def __init__(self, master, **kwargs):
        """Configurações do Frame"""
        self.bg_color = '#1a1a1a'
        self.fg_color = '#f2f2f2'
        self.height = 105
        super(Hud, self).__init__(master, kwargs, background = self.bg_color, height = self.height)
 
        """                 Imagem de VS
        width = 75
        height = 101
        """
        self.preimg = PhotoImage(file=r'assets\vs.png').zoom(45, 45).subsample(100, 100)
        self.img_vs = Label(self, background=self.bg_color, image=self.preimg)
        self.img_vs.place(x=362, y=0)

        self.player = CharHud(self, 
        name='Cristiliano',
        width=350, 
        height=self.height,
        font='Arial 30',
        foreground=self.fg_color,
        background=self.bg_color
        )

        self.enemy = CharHud(self, 
                name='Bot do TauZ',
                width=350, 
                height=self.height,
                font='Arial 30',
                foreground=self.fg_color,
                background=self.bg_color
                )

        """Instanciando os Huds"""
        self.player.place(x=0, y=0)
        self.enemy.place(x=455, y=0)



    



class PlayerButtons(Frame):
    def __init__(self, master, connect, **kwargs):
        """Configurações do Frame"""
        self.bg_color = '#1a1a1a'
        self.heigth = 200
        self.connect = connect
        self.master = master

        super(PlayerButtons, self).__init__(master, kwargs, background = self.bg_color, height = self.heigth)

        """Proload Assets"""
        self.img_rock = PhotoImage(file=r'assets\rock.png').zoom(150, 150).subsample(100, 100)
        self.img_paper = PhotoImage(file=r'assets\paper.png').zoom(150, 150).subsample(100, 100)
        self.img_scissor = PhotoImage(file=r'assets\scissors.png').zoom(150, 150).subsample(100, 100)

        """Botão Pedra"""
        self.bt_rock = Button(
            self, 
            image=self.img_rock,
            background=self.bg_color,
            command=lambda: self.start_button('rock'),
            bd=0, 

        )

        """Botão Papel"""
        self.bt_paper = Button(
            self, 
            image=self.img_paper,
            background=self.bg_color,
            command=lambda: self.start_button('paper'),
            bd=0, 
        )

        """Botão Tesoura"""
        self.bt_scissor = Button(
            self, 
            image=self.img_scissor,
            background=self.bg_color,
            command=lambda: self.start_button('scissor'),
            bd=0, 
        )

        """Instanciando os Botões"""
        self.bt_rock.place(x=75, y=20)
        self.bt_paper.place(x=330, y=20)
        self.bt_scissor.place(x=575, y=20)

    def start_button(self, player_choice):
        if self.master.on_animation == False:
            self.master.start_game(player_choice)

