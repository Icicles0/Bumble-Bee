import Engine.render as render

def basicMovement(size, character, playerx, playery):
    while True:
        render.render_air(size, character, playerx, playery)
        movement = input()
        if movement == "w":
            playery = playery - 1
        elif movement == "s":
            playery = playery + 1
        elif movement == "a":
            playerx = playerx - 1
        elif movement == "d":
            playerx = playerx + 1

        if playery < 0:
            playery = playery + 1
        elif playery > size - 1:
            playery = playery - 1
        if playerx < 0:
            playerx = playerx + 1
        elif playerx > size - 1:
            playerx = playerx - 1
        render.clear()