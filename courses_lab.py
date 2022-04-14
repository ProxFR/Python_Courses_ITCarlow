from random import randrange


######################## 2.6.1.11 ########################
def operators_and_expressions():

    hour = int(input("Starting time (hours): "))
    mins = int(input("Starting time (minutes): "))
    dura = int(input("Event duration (minutes): "))

    mins += dura%60
    hour = (hour + dura//60 + mins//60)%24
    mins = mins%60

    print(hour, ":", mins)


######################## 3.2.1.14 ########################
def essentials_of_the_while_loop():

    blocks = int(input("Enter the number of blocks: "))

    height = 0
    i = 1
    while i <= blocks:
        height += 1
        blocks -= i
        i += 1

    print("The height of the pyramid:", height)


######################## 3.2.1.15 ########################
def collatz_hypothesis():

    c0 = int(input("Enter a number : "))

    i = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        elif c0 % 2 == 1: 
            c0 = (3*c0) + 1
        i += 1
        print(int(c0))

    print ("steps = ", i)


######################## 3.4.1.13 ########################
def the_basics_of_lists():
    # step 1
    beatles = []
    print("Step 1:", beatles)

    # step 2
    beatles.append("John Lennon")
    beatles.append("Paul McCartney")
    beatles.append("George Harrison")
    print("Step 2:", beatles)

    for i in range(2):
        name = str(input("Enter a name : "))
        beatles.append(name)
    print("Step 3:", beatles)

    del beatles[3]
    del beatles[3]
    print("Step 4:", beatles)

    beatles.insert(0,"Ringo Starr")
    print("Step 5:", beatles)


    # testing list legth
    print("The Fab", len(beatles))


######################## 3.6.1.9 ########################
def operating_with_lists():
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

    temp_list = []
    i = 0

    for element in my_list:
        if element not in temp_list:
            temp_list.append(element)
    my_list = temp_list[:]


    print("The list with unique elements only:")
    print(my_list)


######################## 4.3.1.6 ########################
def function_leap_year():
    def is_year_leap(year):
        if ((year % 400 == 0) and (year % 100 == 0) or (year % 4 ==0) and (year % 100 != 0)):
            return True
        else:
            return False

    test_data = [1900, 2000, 2016, 1987]
    test_results = [False, True, True, False]
    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr,"->",end="")
        result = is_year_leap(yr)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")

######################## 4.3.1.7 ########################
def how_many_days():
    def is_year_leap(year):
        if ((year % 400 == 0) and (year % 100 == 0) or (year % 4 ==0) and (year % 100 != 0)):
            return True
        else:
            return False

    def days_in_month(year, month):
        if year < 1582 or month < 1 or month > 12:
            return None
        month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        result  = month_length[month - 1]
        if month == 2 and is_year_leap(year):
            result = 29
        return result


    test_years = [1900, 2000, 2016, 1987]
    test_months = [2, 2, 1, 11]
    test_results = [28, 29, 31, 30]
    for i in range(len(test_years)):
        yr = test_years[i]
        mo = test_months[i]
        print(yr, mo, "->", end="")
        result = days_in_month(yr, mo)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")

######################## 4.3.1.8 ########################
def day_of_the_year():
    def is_year_leap(year):
        if ((year % 400 == 0) and (year % 100 == 0) or (year % 4 ==0) and (year % 100 != 0)):
            return True
        else:
            return False

    def days_in_month(year, month):
        if year < 1582 or month < 1 or month > 12:
            return None
        month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        result  = month_length[month - 1]
        if month == 2 and is_year_leap(year):
            result = 29
        return result

    def day_of_year(year, month, day):
        total = 0
        for i in range(month - 1):
            total += days_in_month(year, i + 1)
        total += day
        return total

    print(day_of_year(2000, 12, 31))


######################## 4.3.1.9 ########################
def prime_numbers():
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
                    break
            return True


    for i in range(1, 20):
        if is_prime(i + 1):
                print(i + 1, end=" ")
    print()


######################## 4.3.1.10 ########################
def converting_fuel_consumption():
    def liters_100km_to_miles_gallon(liters):
        gallon = liters / 3.785411784
        miles = 100 * 1000 / 1609.344
        return(miles / gallon)

    def miles_gallon_to_liters_100km(miles):
        km100 = miles * 1609.344 / 1000 / 100
        liters = 3.785411784
        return liters / km100

    print(liters_100km_to_miles_gallon(3.9))
    print(liters_100km_to_miles_gallon(7.5))
    print(liters_100km_to_miles_gallon(10.))
    print(miles_gallon_to_liters_100km(60.3))
    print(miles_gallon_to_liters_100km(31.4))
    print(miles_gallon_to_liters_100km(23.5))


######################## 4.7.2.1 ########################
def tic_tac_toe():
    def display_board(board):
        print("+-------+-------+-------+")
        for row in range(3):
            print("|       |       |       |")
            for col in range(3):
                print("|   " + str(board[row][col]) + "   ",end="")
            print("|")
            print("|       |       |       |")
            print("+-------+-------+-------+")
            

    def enter_move(board):
        valid = False
        while not valid:
            user_move = int(input("Enter the number of the box you want to put an 'O' in : "))
            valid = user_move in range(1,11)
            if not valid:
                print("The number entered is not between 1 and 10...")
                continue
            user_move -= 1
            sign = board[user_move // 3][user_move % 3]
            valid = sign not in ['O','X'] 
            if not valid:
                print("The field is already occupied...5")
                continue
        board[user_move // 3][user_move % 3] = 'O'


    def make_list_of_free_fields(board):
        free = []
        for row in range(3):
            for col in range(3):
                if board[row][col] not in ['O','X']:
                    free.append((row,col))
        return free 


    def victory_for(board, sign):
        if sign == "X":
            winner = "computer1"
        elif sign == "O":
            winner = "human"
        else:
            winner = None
        cross1 = cross2 = True
        for xy in range(3):
            if board[xy][0] == sign and board[xy][1] == sign and board[xy][2] == sign:
                return winner
            if board[0][xy] == sign and board[1][xy] == sign and board[2][xy] == sign:
                return winner
            if board[xy][xy] != sign:
                cross1 = False
            if board[2 - xy][2 - xy] != sign:
                cross2 = False
        if cross1 or cross2:
            return winner
        return None


    def draw_move(board):
        free = make_list_of_free_fields(board)
        size = len(free)
        if size > 0:
            this = randrange(size)
            row, col = free[this]
            board[row][col] = 'X'        

    ############### MAIN ###############

    board = [["1", "2", "3"],
            ["4", "X", "6"],
            ["7", "8", "9"]]
            
    humanTurn = True # which turn is it now?
    while len(make_list_of_free_fields(board)) > 0:
        display_board(board)
        if humanTurn:
            enter_move(board)
            victory = victory_for(board,'O')
        else:	
            draw_move(board)
            victory = victory_for(board,'X')
        if victory != None:
            break
        humanTurn = not humanTurn		
        free = make_list_of_free_fields(board)

    display_board(board)

    if victory == "human":
        print("You won!")
    elif victory == "computer":
        print("Computer won!")
    else:
        print("Tie!")

######################## 2.3.1.18 ########################
def your_own_split():
    def mysplit(strng):
        result = []
        word = ''
        for c in strng:
            if c != ' ':
                word += c
            else:
                if word:
                    result.append(word)
                word = ''
        if word:
            result.append(word)
        return result


    print(mysplit("To be or not to be, that is the question"))
    print(mysplit("To be or not to be,that is the question"))
    print(mysplit("   "))
    print(mysplit(" abc "))
    print(mysplit(""))


######################## 2.4.1.6 ########################
def a_led_display():
    digit_list = ["#### ## ## ####",
                "  #  #  #  #  #",
                "###  #####  ###",
                "###  ####  ####",
                "# ## ####  #  #",
                "####  ###  ####",
                "####  #### ####",
                "###  #  #  #  #",
                "#### ##### ####",
                "#### ####  ####"]

    def print_digit(value):
        i = 0
        value_list = [char for char in str(value)]
        for n in range(5):
            for num in value_list:
                for position in range(n*3,n*3+3):
                    for c in digit_list[int(num)]:
                        if i in range(n*3,n*3+3):
                            print(c, end="")
                        i += 1                    
                print(" ", end="")
                i = 0
            print()
    
    try:
        num = int(input("Please enter the number to print : "))
    except ValueError:
        print("The value as to be a positive integer")
    print_digit(num)


######################## 2.5.1.6 ########################
def lab_improving_the_caesar_cipher():
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value between 1 and 25 : "))
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        code = ord(char)
        if char.isupper():
            if code + shift > ord('Z'):
                cipher += chr((code + shift) - 26)
            else:
                cipher += chr(code + shift)
        else:
            if code + shift > ord('z'):
                cipher += chr((code + shift) - 26)
            else:
                cipher += chr(code + shift)        

    print(cipher)


######################## 2.5.1.7 ########################
def lab_palindromes():
    text = str(input("Enter some text : "))
    string = ''
    i = 1
    for char in text:
        if char.isalpha():
            string += char.lower()
    while i <= len(string) // 2:
        if string[i - 1] != string[-i]:
            print("It's not a palindrome !")
            break
        if i == len(string) // 2:
            print("It's a palindrome !")
        i += 1


######################## 2.5.1.8 ########################
def lab_anagrams():
    def to_lower(text):
        string = ''
        for char in text:
            if char.isalpha():
                string += char.lower()
        return string

    text1 = list(to_lower(str(input("Enter some text : "))))
    text2 = list(to_lower(str(input("Enter some text : "))))
    text1.sort()
    text2.sort()
    if text1 == text2:
        print("Anagrams")
    else :
        print("Not anagrams")


######################## 2.5.1.9 ########################
def lab_the_digit_of_life():
    dob = list(str(input("Enter your DOB in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY : ")))
    total, total2 = 0
    for val in dob:
        total += int(val)
    final = list(str(total))
    while len(final) > 1:
        for v in final:
            total2 += int(v)
        final = str(total2)
    else :
        print(final[0])


######################## 2.5.1.10 ########################
def lab_find_a_word():
    str1 = list(str(input("Enter the first string : ")))
    str2 = list(str(input("Enter the second string : ")))
    result = True
    i = -1
    for c1 in str1 : 
        for c2 in str2 :
            i += 1
            if c1 == c2 :
                str2.pop(i)
                i = -1
                break
            if i + 1 == len(str2):
                result = False
    print("Result : ", result)


######################## 2.5.1.11 ########################
def lab_sudoku():
    def verify(line):
        if len(line) == len(set(line)): 
            return True
        else:
            return False

    result = True
    table = []
    temp_table = []

    # Ask for data
    for data in range(9):
        table.append(list(str(input("Enter a row : "))))

    # Test horizontally
    for row in table:
        if not verify(row):
            result = False
            break

    # Test vertically
    if result:
        for i in range(9):
            for col in table:
                temp_table.append(col[i])
            if not verify(temp_table):
                result = False
                break
            temp_table = []

    # Test blocs
    temp_table = []
    i = 0
    j = 0
    if result:
        for bloc in range(9):
            for lines in range(3):
                for num in range(3):
                    temp_table.append(table[lines + 3 * j][num + 3 * i])
            if i >= 2 :
                i = 0
                j += 1
            else:
                i += 1
            if not verify(temp_table):
                result = False
                break
            temp_table = []

    if result == False : print("No")
    else : print("Yes")


######################## 2.8.1.4 ########################
def reading_ints_safely():
    def read_int(prompt, min, max):
        ok = False
        while not ok:
            try:    
                value = int(input(prompt))
                ok = True
            except ValueError:
                print("Error: Wrong Input")
            if ok:
                ok = value >= min and value <= max
            if not ok:
                print("Error: The value is not within range(" + str(min) + ".." + str(max) + ")")
        return value

    v = read_int("Enter a number from -10 to 10: ", -10, 10)

    print("The number is:", v)


######################## MENU ########################
menu = """
-----------------------------------------------------------------

1. operators_and_expressions (2.6.1.11)
2. essentials_of_the_while_loop (3.2.1.14)
3. collatz_hypothesis (3.2.1.15)
4. the_basics_of_lists (3.4.1.13)
5. operating_with_lists (3.6.1.9)
6. function_leap_year (4.3.1.6)
7. how_many_days (4.3.1.7)
8. day_of_the_year (4.3.1.8)
9. prime_numbers (4.3.1.9)
10. converting_fuel_consumption (4.3.1.10)
11. tic_tac_toe (4.7.2.1)
12. your_own_split (2.3.1.18)
13. a_led_display (2.4.1.6)
14. lab_improving_the_caesar_cipher (2.5.1.6)
15. lab_palindromes (2.5.1.7)
16. lab_anagrams (2.5.1.8)
17. lab_the_digit_of_life (2.5.1.9)
18. lab_find_a_word (2.5.1.10)
19. lab_sudoku (2.5.1.11)
20. reading_ints_safely (2.8.1.4)
99. EXIT

-----------------------------------------------------------------
"""

ans = True
while ans:
    print(menu)
    try:
        ans = int(input("Please enter the number of the program you want to execute : "))
    except:
        print("\nWrong input. Please enter a number...")

    if ans == 1:
        operators_and_expressions()
    elif ans == 2:
        essentials_of_the_while_loop()
    elif ans == 3:
        collatz_hypothesis()
    elif ans == 4:
        the_basics_of_lists()
    elif ans == 5:
        operating_with_lists()
    elif ans == 6:
        function_leap_year()
    elif ans == 7:
        how_many_days()
    elif ans == 8:
        day_of_the_year()
    elif ans == 9:
        prime_numbers()
    elif ans == 10:
        converting_fuel_consumption()
    elif ans == 11:
        tic_tac_toe()
    elif ans == 12:
        your_own_split()
    elif ans == 13:
        a_led_display()
    elif ans == 14:
        lab_improving_the_caesar_cipher()
    elif ans == 15:
        lab_palindromes()
    elif ans == 16:
        lab_anagrams()
    elif ans == 17:
        lab_the_digit_of_life()
    elif ans == 18:
        lab_find_a_word()
    elif ans == 19:
        lab_sudoku()
    elif ans == 20:
        reading_ints_safely()
    elif ans == 99:
        print("\nGoodbye") 
        ans = None
    else:
       print("\nPlease enter a value present in the list...")