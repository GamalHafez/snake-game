# The game loop
from turtle import screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

window = Screen()
window.setup(width = 800, height = 800)
window.bgcolor("black")
window.tracer(0)
window.title("Snake Game")

snake = Snake()
food = Food()
score = Scoreboard()

def user_control():
    window.listen()
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.right, "Right")
    window.onkey(snake.left, "Left")

user_control()
game_continue = True

while game_continue:
    snake.move()
    window.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.random_appear()
        snake.extend()
        score.increase_score()

    if ( snake.head.xcor() > 375 or
    snake.head.xcor() < -375 or
    snake.head.ycor() > 375 or
    snake.head.ycor() < -375
    ):
        food.remove_from_screen()
        score.end_game()       
        game_continue = False

    for square in snake.squares[:-1]:
        if snake.head.distance(square) < 10:
            score.end_game()
            game_continue = False
            break          




another_try = window.textinput("AGAIN..", "Another try?\nType 'y' if yes, or anything to exit").lower()
if another_try == 'y':
    window.clear()
    exec(open(__file__).read())
