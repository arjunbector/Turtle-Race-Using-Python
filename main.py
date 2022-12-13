from turtle import Turtle, Screen
from random import randint 


colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
y_positions=[-70, -40, -10, 20, 50, 80] #Starting positions of the turtles.
is_race_on = False # Flag to know whether race/game is on or not.
screen = Screen()
screen.setup(width=500,height=400)
screen.bgcolor('black')
user_bet = screen.textinput(title='Make Your Bet', prompt=f'Which turtle will win the race? Enter a color\nfrom {colors}:')




all_turtles=[] # Empty list to store all the turtles.



if user_bet in colors: # To check whether the given input color is valid or not.
    is_race_on = True
    for i in range(len(colors)):
        new_turtle = Turtle(shape='turtle') # Creates a new turtle.
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[i])
        all_turtles.append(new_turtle) # Appends the newly formed turtle to the turtles' list.
else:
    print("Please enter a valid colour.")
    


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: # To check whether the a turtle has crossed the finish line.
            is_race_on = False
            wining_color = turtle.pencolor() # Returns the pen color of the turtle that won.
            if wining_color == user_bet:
                print(f'You won! {wining_color.title()} turtle won the race.')
            else:
                print(f'You lose. {wining_color.title()} turtle won the race.')
            break
        
        random_distance = randint(0,10) 
        turtle.forward(random_distance) # Each turtle goes forward by random steps between 0 to 10 (both inclusive)
        


screen.exitonclick()