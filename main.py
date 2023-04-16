import turtle
from turtle import Turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        my_turtle = Turtle()
        my_turtle.penup()
        my_turtle.hideturtle()
        state_data = data[data.state == answer_state]
        my_turtle.goto(int(state_data.x), int(state_data.y))
        my_turtle.write(answer_state)
        scoreboard.increase_score()
