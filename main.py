#hhttps://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turnRight():
    for i in range(0, 3):
        turn_left()

while not at_goal():
    #Se destra e davanti sono disponibili
    if right_is_clear and front_is_clear():
        move()  
    #Se posso andare a destra
    elif right_is_clear():
        turnRight()
        move()
    #Quando ho un muro sulla destra vado dritto
    elif front_is_clear() and wall_on_right():
        move()
    #Quando ho un muro davanti ed a destra, vado a sinistra
    elif not front_is_clear() and wall_on_right():
        turn_left()
        move()