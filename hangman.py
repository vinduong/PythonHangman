import random

def play_again():
    answer = input('Would you like to play again? y/n').lower()
    if answer == 'y':
        play_game()
    else:
        pass

def get_word():
    words = ['cat', 'dog', 'goldfish', 'hamster', 'lizard']
    return random.choice(words)

def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hangman = ['''
          +---+
          |   |
              |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''']
    word = get_word()
    letters_guessed = []
    tries = 6
    guessed = False
    
    print('The word contains', len(word), 'letters.')
    print(len(word) * '*')
    while guessed == False and tries > 0:
        if tries < 6:
            print(hangman[6 - tries])
        print('You have ' + str(tries) + ' tries left')
        guess = input('Please enter one letter or the full word.').lower()
        
        #Single letter guess
        if len(guess) == 1:
            if guess not in alphabet:
                print('You have not entered a valid letter.')
            elif guess in letters_guessed:
                print('You have guessed that letter before.')
            elif guess not in word:
                print('Sorry, that letter is not in the word.')
                letters_guessed.append(guess)
                tries -= 1
            elif guess in word:
                print('Correct, that letter is in the word!')
                letters_guessed.append(guess)
            else:
                print('Something went wrong.')
                
        #Full word guess
        elif len(guess) == len(word):
            if guess == word:
                print('Good job, you guessed the word!')
                guessed = True
            else:
                print('Sorry, that is not the right word.')
                tries -= 1
                
        #Different word lengths
        else:
            print('Sorry, that is not the right word.')
            tries -= 1
            
        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == word:
            print('Good job, you guessed the word!')
            guessed = True
        elif tries == 0:
            print(hangman[6])
            print('Sorry, you are out of guesses. The correct answer is ' + word + '.')

    play_again()
   
play_game()
