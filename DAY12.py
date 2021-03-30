import random



# GUESS NUMBER
print("""
  ______                                                ________  __                        __    __                          __                                 
 /      \                                              /        |/  |                      /  \  /  |                        /  |                                
/$$$$$$  | __    __   ______    _______  _______       $$$$$$$$/ $$ |____    ______        $$  \ $$ | __    __  _____  ____  $$ |____    ______    ______        
$$ | _$$/ /  |  /  | /      \  /       |/       |         $$ |   $$      \  /      \       $$$  \$$ |/  |  /  |/     \/    \ $$      \  /      \  /      \       
$$ |/    |$$ |  $$ |/$$$$$$  |/$$$$$$$//$$$$$$$/          $$ |   $$$$$$$  |/$$$$$$  |      $$$$  $$ |$$ |  $$ |$$$$$$ $$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |      
$$ |$$$$ |$$ |  $$ |$$    $$ |$$      \$$      \          $$ |   $$ |  $$ |$$    $$ |      $$ $$ $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/       
$$ \__$$ |$$ \__$$ |$$$$$$$$/  $$$$$$  |$$$$$$  |         $$ |   $$ |  $$ |$$$$$$$$/       $$ |$$$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |            
$$    $$/ $$    $$/ $$       |/     $$//     $$/          $$ |   $$ |  $$ |$$       |      $$ | $$$ |$$    $$/ $$ | $$ | $$ |$$    $$/ $$       |$$ |            
 $$$$$$/   $$$$$$/   $$$$$$$/ $$$$$$$/ $$$$$$$/           $$/    $$/   $$/  $$$$$$$/       $$/   $$/  $$$$$$/  $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/             
""")
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def Play(attempts, comp_num):
    user_num = 0
    while comp_num != user_num and attempts != 0:
        user_num = int(input("Make a guess: "))
        if user_num < comp_num:
            print("Too low")
            attempts -= 1
            print(f"You left with {attempts} attempts")
        elif user_num > comp_num:
            print("Too high")
            attempts -= 1
            print(f"You left with {attempts} attempts")
        elif user_num == comp_num:
            print(f"You got it with {attempts - 1} left attempts. The answer was {comp_num}.")
        if attempts == 0:
            print("You lose!!(")


def set_difficulty(level):
    if level == 'easy':
        Play(EASY_LEVEL_TURNS, comp_num)
    elif level == 'hard':
        Play(HARD_LEVEL_TURNS, comp_num)


comp_num = random.randint(0, 101)
print("I'm thinking of a number between 1 and 100 \n")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

set_difficulty(level)


