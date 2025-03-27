import turtle
import pandas
import sys

screen = turtle.Screen()
screen.title("U.S. state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.tracer(0)
e = turtle.Turtle()
e.penup()
e.goto(0, 300)
e.pendown()
e.hideturtle()
e.write("Enter Exit to exit")
screen.update()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answered_state = []
while len(answered_state) < 50:
    answer = screen.textinput(title= "U.S. state game",prompt="Enter the name of the us: ").title()
    if answer in all_states and answer not in answered_state:
        answered_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(state_data.x.values[0], state_data.y.values[0])
        t.pendown()
        t.write(answer)
    if answer == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in answered_state:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in answered_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        sys.exit()
screen.exitonclick()