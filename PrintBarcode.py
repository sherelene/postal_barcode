import turtle


# defining the helper functions
def start(title):
    # initializing the turtle object (pen)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.width(4)
    turtle.title(title)
    turtle.penup()
    turtle.left(180)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(180)
    turtle.pendown()


# function that draws the |
def print_one():
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.pendown()


# function that draws the .
def print_zero():
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.forward(15)
    turtle.left(90)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.pendown()


# function that will print the barcode
def print_barcode(bar_code, zip_code):
    title = "Zip Code: " + zip_code  # title of the canvas
    start(title)  # sets up the canvas so pen can go left to right
    print_one()  # draws the initial start 1
    for num in bar_code:  # calls the helper functions to draw the barcode depending on their encoding
        if num == "0":
            print_zero()
        else:
            print_one()
    print_one()  # draws the stop 1
    turtle.done()  # prevents the canvas from closing on its own


def zip_encoding(zip_code):
    # Create a dictionary for all digits and their encoded numbers
    bar_dict = {1: "00011", 2: "00101", 3: "00110", 4: "01001", 5: "01010",
                6: "01100", 7: "10001", 8: "10010", 9: "10100", 0: "11000"}

    # Loops through zip code and joins all the binary digits together
    bar_code = ''.join([bar_dict[int(num)] for num in zip_code])

    # Calls function that will draw the barcode
    print_barcode(bar_code, zip_code)
