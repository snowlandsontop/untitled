game.splash("Let's calculate the area of a trapezoid")
base1 = game.ask_for_number("What is the length of the bottom base in cm")
base2 = game.ask_for_number("What is the length of the top base in cm")
height = game.ask_for_number("What is the height in cm")
area = (base1 + base2) / 2 * height
game.splash("the area of the trapezoid with base" + str(base1) + "cm and another base " + str(base2) + "cm and height " + str(height) + "cm is " + str(area) + "cm^2")