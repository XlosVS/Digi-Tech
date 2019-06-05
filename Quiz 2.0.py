######################################################
# Python program for bluelight quiz
# Coder: Matthew McDermott
# Name: Quiz 2.0.py
# Version: 2.0
# Version 2 contains graphics and mouse clicks to
# answer questions.
# Date 19/05/2019
#
# Before You Run The Program, go onto command prompt and run pip install pygame, and then pip install pgzero
# How my program works:
# (1) Draw GUI on the screen
# (2) Create a list of questions about bluelight
# (3) Test if there are any questions left
# (4a) If NO go to (8) GAME OVER
# (4b) If YES display the question
# (5) Is the answer correct?
# (6a) If NO go to (8) GAME OVER
# (6b) If YES increase score by 1
# (7) reset timer and go to (3)
# (8) Display final score and end program
######################################################

# Import required library
# Pgzrun is basically a simplier version of Pygame,
# which helps create interactive, non-text based
# games
import pgzrun

# Set the screen size (values in pixels)
WIDTH = 1280
HEIGHT = 720

# Create boxes for the interface
# The function Rect takes 4 parameters
#   The first 2 set the top left-hand corner
#   The last 2 set the bottom right-hand corner
main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 275)
answer_box2 = Rect(0, 0, 495, 275)

# Move the boxes to the correct location o the screen
main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)

# Create the true/false answer boxes
answer_boxes = [answer_box1, answer_box2]

# Set the score
score = 0
# Set the timer
time_left = 10

# Create the questions
q1 = ["Blue light from a smart phone keeps you awake",
      "True", "False", "d", "f", 1]

q2 = ["Yellow light is as bad as blue light",
      "True", "False", "d", "f", 2]

q3 = ["Blue light has no negative consequences",
      "True", "False", "d", "f", 2]

q4 = ["100% of phones are recycled or taken to controlled dumps",
      "True", "False", "d", "f", 2]

q5 = ["You can give Apple your broken Apple devices",
      "True", "False", "d", "f", 1]

# Create a list for the questions
questions = [q1, q2, q3, q4, q5]

# Pick a question from the list using the pgzrun function pop()
# which removes the first item froma list and thme makes the secon item
# the top of the list
question = questions.pop(0)

# Creates a function which draws the screen
# The original colours were Dim Grey, Sky Blue, Orange and Black, but I thought that these
# were a bit bland, so I decided to change them to Turquoise, Peru, Navy, Spring Green,
# Azure and Chocolate.
def draw():
    screen.fill("turquoise")
    screen.draw.filled_rect(main_box, "peru")
    screen.draw.filled_rect(timer_box, "navy")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "corn silk")

    screen.draw.textbox(str(time_left), timer_box, color=("spring green"))
    screen.draw.textbox(question[0], main_box, color=("azure"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("chocolate"))
        index = index + 1

# Ends the game
def game_over():
    global question, time_left
    message = "Game over. You got %s out of 5 questions correct" % str(score)
    if score < 5:
        question = [message, "Better Luck", "Next Time", "-", "-", 5]
    else:
        question = [message, "Well", "Done", "-", "-", 5]
    time_left = 0

# Corect answer procedure
# Increases the score by 1
# 
def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()

# Tells what to do when the mouse is clicked
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it correct")
                correct_answer()
            else:
                game_over()
        index = index + 1

# Code for the timer to reset when going onto next question or if it is game over
def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

# Runs the game
clock.schedule_interval(update_time_left, 1.0)
pgzrun.go()
