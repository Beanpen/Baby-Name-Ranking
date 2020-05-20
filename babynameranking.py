def quit_program(input):
    if input in ['quit', 'Quit', 'q', 'Q']:
        wn.clear()
        wn.bgcolor("black")
        tt.home()
        tt.color('white')
        tt.write('BYEBYE', font=('Arial', 100, 'normal'))
        return True
    return False



def drawBar(t, height, colume_num):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.penup()
    t.forward(5)
    t.pendown()
    if height != 0:
        t.write('  ' + find_year(colume_num))
    else:
        t.write('Out of rank', font=("Arial", 10, "normal"))
    t.left(90)
    t.forward(height)
    if height != 0:
        t.write('  ' + str(height), font=("Arial", 18, "normal"))
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape


def stripe_write(turtle, string):
    from itertools import cycle
    FONT = ('Arial', 36, 'normal')
    COLORS = ["red", "blue", "orange", "yellow", 'black', 'white']
    color = cycle(COLORS)

    for character in string:
        turtle.color(next(color))
        turtle.write(character, move=True, font=FONT)


def find_min(numbers):
    # initialize min_value and min_index
    min_value = 100000000000000000
    min_index = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            continue

        if int(numbers[i]) <= min_value:
            min_value = int(numbers[i])
            min_index = i + 2
            continue

    return (min_value, min_index)


def find_year(colume_number):
    if colume_number is 2:
        return ('1900-1909')
    if colume_number is 3:
        return ('1910-1919')
    if colume_number is 4:
        return ('1920-1929')
    if colume_number is 5:
        return ('1930-1939')
    if colume_number is 6:
        return ('1940-1949')
    if colume_number is 7:
        return ('1950-1959')
    if colume_number is 8:
        return ('1960-1969')
    if colume_number is 9:
        return ('1970-1979')
    if colume_number is 10:
        return ('1980-1989')
    if colume_number is 11:
        return ('1990-1999')
    if colume_number is 12:
        return ('2000-2009')


bn = open('Baby_Names.data.txt', 'r')
lines = bn.readlines()

def get_most_popular_decade(bn,name):
    year = -1
    numbers = -1
    for line in lines:
        # strip and split
        line = line.strip()
        line = line.split(' ')
        # if line[0] == name then return then call find_min and return most popular decade
        if user_name == line[0]:
            numbers = []
            for i in range(1, len(line)):
                numbers.append(int(line[i]))
            (min_value, min_index) = find_min(numbers)
            year = find_year(min_index)
            return year, numbers
    return year, numbers


import turtle
wn = turtle.Screen()  # Set up the window and its attributes
wn.setup(1000, 1000)
tt = turtle.Turtle()

# keep getting names until user wants to quit
while True:
    # background setting
    wn.clear()
    wn.bgcolor('lightblue')

    # write colorful title
    tt.goto(-350, 0)
    try:
        stripe_write(tt, "WELCOME TO NAME \nPOPULARITY TEST!")
    except:
        pass

    # ask the user their name
    user_name = wn.textinput('Welcome', 'What\'s your name?')
    try:
        user_name = user_name[0].upper() + user_name[1:].lower()
    except:
        continue

    # get the polularity
    (year, numbers) = get_most_popular_decade(lines, user_name)

    # check if the user enters 'quit' or not
    do_quit_program = quit_program(user_name)
    if do_quit_program:
        break

    if year == -1:
        # you have a unique name
        # ask them if they want to try another
        answer = 0
        while answer not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
            answer = wn.textinput('Enter Q to exit', 'WOW! That is a unique name! We could not find any data about it...'
                                         'However, do you want to try it with another name?(Y/N)')
        if answer in ['Yes', 'yes', 'y', 'Y']:
            continue
        else:
            wn.bgcolor("black")
            tt.home()
            tt.color('white')
            tt.write('BYEBYE', font=('Arial', 100, 'normal'))
            break
    else:
        wn.clear()

        # set the screen
        xs = numbers
        maxheight = max(xs)
        numbars = len(xs)
        border = 50
        wn.setworldcoordinates(0 - border, 0 - border, 40 * numbars + border, maxheight + border)
        wn.bgcolor("lightblue")

        # set some attributes
        tt.color("white")
        tt.fillcolor("blue")
        tt.pensize(3)
        tt.speed('fastest')
        tt.penup()
        tt.home()

        counter = 1
        for a in xs:
            counter += 1
            drawBar(tt, a, counter)

        # print out info_1
        a = wn.textinput('Press any key to continue', 'This dataset records the rank of baby name for a particular decade. '
                 '\nA rank of 1 was the most popular and ranking go all the way down to 1000. '
                 '\nAny name with a ranking of 0 means that it was ranked lower than 1000th.')
        # check if the user enters 'quit' or not
        do_quit_program = quit_program(a)
        if do_quit_program:
            break

        # print out info_2
        b = wn.textinput('Press any key to continue',        # tell them the decade + name
                         'Your name' + ', ' + user_name + ',' + 'is the most popular during ' + year)
        # check if the user enters 'quit' or not
        do_quit_program = quit_program(b)
        if do_quit_program:
            break


wn.mainloop()