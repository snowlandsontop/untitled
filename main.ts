game.splash("Let's calculate the area of a trapezoid")
let base1 = game.askForNumber("What is the length of the bottom base in cm")
let base2 = game.askForNumber("What is the length of the top base in cm")
let height = game.askForNumber("What is the height in cm")
let area = (base1 + base2) / 2 * height
game.splash("the area of the trapezoid with base" + base1 + "cm and another base " + base2 + "cm and height " + height + "cm is " + area + "cm^2")
