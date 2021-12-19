import turtle
import pandas as pd

screen = turtle.Screen()
entered_states = []
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
x = turtle.Turtle()
x.penup()
x.hideturtle()
states_data = pd.read_csv("50_states.csv")
states_list = states_data.state.to_list()
while len(entered_states) < 50:

    state_name = screen.textinput(title=f"{len(entered_states)}/50 States",
                                  prompt="Enter the name of a state").strip().title()
    if state_name in entered_states:
        print(f"{state_name} was already entered")
    elif state_name in states_list:
        entered_states.append(state_name)
        entered_state_data = states_data[states_data.state == state_name]
        x.goto(int(entered_state_data.x), int(entered_state_data.y))
        x.write(state_name, align="center")
    elif state_name == "Exit":
        break
    else:
        print(f"{state_name} is not a state")

with open("states_to_learn.txt", mode="a") as file:
    file.truncate(0)
    for state in states_list:
        if state not in entered_states:
            file.write(f"{state}\n")


screen.exitonclick()
