import os, random

def clear_screen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

game_running = True

# Wordlists
determiners = ["the","a","an","this","that","these","those","my","your","their"]
adjectives = ["bright","cold","heavy","smooth","quick","lazy","sharp","quiet","bitter","deep"]
nouns = ["table","mountain","river","elephant","computer","book","city","cloud","idea","song"]

body_pieces = [
        " ",
        "(   )", # Head
        "|",     # Body
        "/",     # L-(arm/leg)
        "\\",    # R-(arm/leg)
        "(x x)"  # Dead Head
        ]
head = body_pieces[0]
body = body_pieces[0]
lArm = body_pieces[0]
rArm = body_pieces[0]
lLeg = body_pieces[0]
rLeg = body_pieces[0]
dead = False

def puzzle_generator(*args):
    word1 = args[0][random.randint(0,9)]
    word2 = args[1][random.randint(0,9)]
    word3 = args[2][random.randint(0,9)]
    return [word1, word2, word3]

def clean_puzzle(string, ignore):
    ignored_chars = [" "]

    for item in ignore:
        ignored_chars.append(item)

    clean_string = ""

    for char in string:
        if not char in ignored_chars:
            char = "_"
        clean_string = clean_string + char

    return clean_string

def format_guesses(incorrect):
    formatted = []

def hang_the_man(incorrect):
    global head, body, lArm, rArm, lLeg, rLeg

    match incorrect:
        case 1:
            head = body_pieces[1]
        case 2:
            body = body_pieces[2]
        case 3:
            lArm = body_pieces[3]
        case 4:
            rArm = body_pieces[4]
        case 5:
            lLeg = body_pieces[3]
        case 6:
            rLeg = body_pieces[4]

def check(puzzle, guess):
    return puzzle == guess

def draw(incorrect, clean):
    global head

    clear_screen()
    hang_the_man(len(incorrect))

    if dead:
        head = body_pieces[5]

    incorrect_string = ""
    for char in incorrect:
        incorrect_string = incorrect_string + char
    print(f'''
Trys:{len(incorrect)}    +----+
          |    |
         {"\b"*len(incorrect_string)+incorrect_string} |  {head}
          |   {lArm}{body}{rArm}
          |   {lLeg} {rLeg}
          |
    ------+-------
 {clean}\n''')

def main():
    global dead

    guesses = []
    incorrect = []
    puzzle = " ".join(puzzle_generator(determiners, adjectives, nouns))
    clean = clean_puzzle(puzzle, guesses)

    while(game_running):
        draw(incorrect, clean)

        guess = input("Guess> ")

        if len(guess) == 1:
            guesses.append(guess)

        if not guess in puzzle and not guess in incorrect:
            incorrect.append(guess)

        clean = clean_puzzle(puzzle, guesses)

        if not guess:
            break;
        
        if len(incorrect) >= 6:
            dead = True
            draw(incorrect, clean)
            print("Sorry, the man has hanged! \nBetter luck next time!")
            break;

        win = check(puzzle, clean)
        if win:
            draw(incorrect, clean)
            print("YOU WIN!")
            break;

    print("\nThanks for playing!")

main()
