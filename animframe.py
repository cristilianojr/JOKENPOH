from tkinter import *
import time


class DisplayAnim(Canvas):
    def __init__(self, master, **kwargs):
        """Configurações do Frame"""
        self.bg_color = '#b3b3ff'
        self.heigth = 300
        self.master = master
        super(DisplayAnim, self).__init__(master, kwargs, highlightthickness=0, relief='ridge', background = self.bg_color, height = self.heigth, bd=0)

        """Seta o background do display"""
        self.bg_preimage = PhotoImage(file=r'assets\bg_image_anim.png')
        print(self.bg_preimage.width(), self.bg_preimage.width())
        self.bg_image = self.create_image(400, 150, image=self.bg_preimage)

        """Imagens base dos botões"""
        self.rockimg = PhotoImage(file=r'assets\rockm.png')#.zoom(250, 250).subsample(100, 100),
        self.paperimg = PhotoImage(file=r'assets\paperm.png')#.zoom(250, 250).subsample(100, 100),
        self.scissorimg =PhotoImage(file=r'assets\scissorsm.png')#.zoom(250, 250).subsample(100, 100)
        """Vs do meio do game"""
        self.midleimg = PhotoImage(file=r'assets\vs.png')#.zoom(250, 250).subsample(100, 100)
        """Vs do meio do game"""
        self.vict_img = PhotoImage(file=r'assets\Victorystate.png')
        self.draw_img = PhotoImage(file=r'assets\drawstate.png')
        self.def_img = PhotoImage(file=r'assets\defeatstate.png')

        """Qual a sua escolha? Pergunta feita antes de cada chamada"""
        self.wyimg = PhotoImage(file=r'assets\whatyoourchoice.png')
        self.wychoice = self.create_image(400,150, image=self.wyimg)

    def player_img(self):
        """Define qual imagem usar"""
        if self.master.player_choice == 'rock':
            return self.rockimg
        elif self.master.player_choice == 'scissor':
            return self.scissorimg
        if self.master.player_choice == 'paper':
            return self.paperimg

    def ia_img(self):
        """Define qual imagem usar"""
        if self.master.ia_choice == 'rock':
            return self.rockimg
        elif self.master.ia_choice == 'scissor':
            return self.scissorimg
        if self.master.ia_choice == 'paper':
            return self.paperimg

    def state_img(self):
        """Define qual imagem usar"""
        if self.master.v_state == 'victory':
            return self.vict_img
        elif self.master.v_state == 'draw':
            return self.draw_img
        if self.master.v_state == 'defeat':
            return self.def_img

    def battle_animation(self):
        time.sleep(1)
        self.delete(self.wychoice)
        self.playerc = self.create_image(-200, 150, image=self.player_img())
        self.iac = self.create_image(1000, 150, image=self.ia_img())
        
        vel = 3.5
        distance = 100
        for i in range(0, distance):
            self.move(self.playerc, vel, 0) 
            self.move(self.iac, -vel, 0) 
            time.sleep(0.01)
        self.midanim = self.create_image(400, 150, image=self.midleimg)
        time.sleep(2)
        self.canvas_state = self.create_image(400, 150, image=self.state_img())
        time.sleep(2)
        self.delete(self.playerc)
        self.delete(self.iac)
        self.delete(self.midanim)
        self.delete(self.canvas_state)
        self.wychoice = self.create_image(400,150, image=self.wyimg)
        self.master.on_animation = False

        if self.master.hud.player.life <= 0:
            self.master.game_over()
        elif self.master.hud.enemy.life <= 0:
            self.master.game_win()
        else:
            pass
        
