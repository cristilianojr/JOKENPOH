import random
from tkinter import PhotoImage


"""
Esse arquivo define os estados do game

"""


def ia_chocer():
    """IA faz a escolha de um numero aleatório"""
    posibility = ['rock', 'paper', 'scissor']
    value = posibility[random.randint(0, 2)]
    return value

def battle_verification(player_choice, ia_choice):
    state_victoryorlose = ''
    if player_choice == 'rock':
        if ia_choice == 'rock':
            state_victoryorlose = 'draw'
        elif ia_choice == 'scissor':
            state_victoryorlose = 'victory'
        elif ia_choice == 'paper':
            state_victoryorlose = 'defeat'
    elif player_choice == 'scissor':
        if ia_choice == 'rock':
            state_victoryorlose = 'defeat'
        elif ia_choice == 'scissor':
            state_victoryorlose = 'draw'
        elif ia_choice == 'paper':
            state_victoryorlose = 'victory'
    elif player_choice == 'paper':
        if ia_choice == 'rock':
            state_victoryorlose = 'victory'
        elif ia_choice == 'scissor':
            state_victoryorlose = 'defeat'
        elif ia_choice == 'paper':
            state_victoryorlose = 'draw'
    return state_victoryorlose 











