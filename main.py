import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("State game")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in all_states:
        answer_state_data = data[data.state == answer_state]
        print(answer_state_data.x)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(answer_state_data.x[0]), int(answer_state_data.y[0]))
        t.write(answer_state)
        guessed_states.append(answer_state_data)
