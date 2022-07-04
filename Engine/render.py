import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def render_air(size, character, playerx, playery):
    size = size + 1
    print(f"Bumble Bee Engine v1.0")
    print(f"Debug Info: Size = {size-1} Character = {character} Playerx = {playerx} Playery = {playery}")
    for y in range(size):
        for x in range(size):
            if x == playerx and y == playery:
                print(character, end="")
            else:
                print(" ", end="")
        print("") # DO NOT REMOVE IT IS VERY NECCECARY