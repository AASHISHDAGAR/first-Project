
# coding: utf-8

# # Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output


def display_board(board):
    clear_output()
    print(f"   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print(f"___|___|___")
    print(f"   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print(f"___|___|___")
    print(f"   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print(f"   |   |   ")


# **TEST Step 1:** run your function on a test version of the board list,
# and make adjustments as necessary


# **Step 2: Write a function that can take in a player input and assign
# their marker as 'X' or 'O'. Think about using *while* loops to continually
# ask until you get a correct answer.**


def player_input():
    player1_marker = input("Player1: Want you want to be X or O: ")
    while player1_marker not in ["X", "O"]:
        player1_marker = input(
                              "Player1: Choose a valid Marker either X or O: ")
    if player1_marker =="X":
        player2_marker = "O"
    else:
        player2_marker ="X"
    print("player_input function working")
    return player1_marker , player2_marker


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[4]:


#player_input()


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[5]:


def place_marker(board, marker, position):
    
    board[position] =marker
    print("place_maker function working")
    


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[6]:


place_marker(test_board,'$',8)
display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[7]:


def win_check(board, mark):
    return ((board[7:9:1] ==[mark]*3) or (board[4:7:1] ==[mark]*3)
            or(board[1:4:1] ==[mark] *3) or (board[7:0:-3] ==[mark]*3) or
            (board[8:1:-3] == [mark]*3) or (board[9:2:-3] ==[mark]*3) or
            (board[7:2:-2] ==[mark]*3) or (board[9:0:-4] == [mark]*3))


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[8]:


win_check(test_board,'X')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[9]:


import random

def choose_first():
    player = ['player1','player2']
    num  =random.randint(0,1)
    print(f"{player[num]}  goes first")
    return player[num]


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[10]:


def space_check(board, position):
    return board[position].isspace()


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[11]:


def full_board_check(board):
    for num in board:
        if num.isspace():
            return False
    return True


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[12]:


board = [" "]*10


# In[13]:


def player_choice(board):
    while True:
        position = int(input("Enter your move integer btw 1-9: "))
        if space_check(board,position):
            while position not in range(1,10):
                position = int(input("Enter your next move btw 1-9: "))
            return position
        
        else:
            print("This position is already filled choose other position.")
            continue


# In[14]:


#player_choice(board)


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[ ]:


def replay():
    ask = input("Want to Play Again ? yes/no: ")
    while ask not in ["yes","no","Yes",'No']:
        ask = input("Enter a valid choice yes/no :")
    return ask[0].lower()=="y"


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[ ]:


print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    board = ["#"," "," "," "," "," "," "," "," "," "]
    #display_board(board)
    player1_marker ,player2_marker = player_input()
    turn = choose_first()
    game_on = True
    print("Game Starting")
    #display_board(board)
    

    while game_on:
        #Player 1 Turn
        
        print("Game Started")
        
        if turn =="player1":
            display_board(board)

            position = player_choice(board)
            place_marker(board,player1_marker,position)
            
            if win_check(board,player1_marker):
                display_board(board)
                print(f"{player1_marker} Wins!!")
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("Game Draw")
                game_on = False
            else:
                turn ="player2"
        
        
        # Player2's turn.
        if turn =="player2":
            display_board(board)
            
            position = player_choice(board)
            place_marker(board,player2_marker,position)
            
            
            
            if win_check(board,player2_marker):
                print(f"{player2_marker} Wins!!")
                game_on = False
            elif full_board_check(board):
                print("Game Draw")
                game_on = False
            else:
                turn ="player1"
            
            #pass

    if not replay():
        break


# ## Good Job!
