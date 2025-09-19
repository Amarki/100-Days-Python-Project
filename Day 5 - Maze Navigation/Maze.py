
'''
Day 5 - Writing code on Reeborg's World to have a robot navigate a maze through Python.
Link to Reeborg World problem: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Summary: Code has robot check along walls and follows along it, only turning right when it can and left when it absolutely has to (such as in dead ends). 
'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()  
    

while not at_goal():
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
