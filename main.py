import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states_List = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                            "name?").title()
    if user_answer in states_List:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer)



screen.exitonclick()
