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

while len(entered_states) < 50:

    state_name = screen.textinput(title=f"{len(entered_states)}/50 States", prompt="Enter the name of a state").title()
    if state_name in entered_states:
        print(f"{state_name} was already entered")
    elif state_name in states_data.state.to_list():
        entered_states.append(state_name)
        entered_state_data = states_data[states_data.state == state_name]
        x.goto(int(entered_state_data.x), int(entered_state_data.y))
        x.write(state_name, align="center")
    else:
        print(f"{state_name} is not a state")

screen.exitonclick()
