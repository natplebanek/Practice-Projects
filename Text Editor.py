#Natalie Plebanek       Project 3       CSC 6003

import os

#       -- Functions --

def check_file():
    while True:
        file = input('Name of file you would like to edit: ') + '.txt'
        if os.path.exists(file):
            return file
        else:
            print('That file does not exist. Please enter a valid file path.')

def AllWordCount(frname):
#count the frequency of each word in the
#file and output the top 5 most common words that appear.
    counts = dict()
    for line in frname:
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    remove_punc = ['.', ',', '?', '!', '...']
    for keys in remove_punc:
        del counts[keys]
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1]))
    print(f'''
The top five words that show up the most frequently in your file are:
1) {list(sorted_counts)[-1]}
2) {list(sorted_counts)[-2]}
3) {list(sorted_counts)[-3]}
4) {list(sorted_counts)[-4]}
5) {list(sorted_counts)[-5]}
''')
    return

def SingleWordCount(frname, search_word):
#ask the user for a word as input (check to make
#sure is a single word, you might want to create
#a function to handle input is a single word) and
#output the number of times that word appears
    counts = dict()
    for line in frname:
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    remove_punc = ['.', ',', '?', '!', '...']
    for keys in remove_punc:
        del counts[keys]
    if search_word in counts:
        print(f'The frequency that {search_word} shows up in the text is {counts[search_word]} time(s).')
    else:
        print(f'The word, {search_word}, does not show up in the text.')

    return

def ReplaceWord(frname):
#take a word as input and take another input as a
#replacement. It will replace the word and output
#the number of words changed.
    text = frname.read()

    counts = dict()
    words_in_file = text.split()
    for word in words_in_file:
        word_upper = word.upper()
        if word_upper not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    while True:
        try:
            user_input = input('What word would you like to replace? ').upper()
            if user_input in counts:
                break
            else:
                print('That word is not in the text file. Please enter a different word to replace.')
        except ValueError:
            print('That word is not in the text file. Please enter a different word to replace.')

    replacement = input(f'What word would you like to replace {user_input} with? ').upper()

    updated_text = ''
    for word in words_in_file:
        if word.upper() == user_input:
            updated_text += replacement + ' '
        else:
            updated_text += word + ' '
     
    updated_text = updated_text.strip()

    print(f'{counts[user_input]} word(s) were replaced with {replacement}.')
    print('Text replaced successfully.')
    return updated_text

def AddText(frname):
#add text to the existing text in the file
    text = frname.read()
    text2add = input('Input text would you like to append to the bottom of the text file: ').upper()
    updated_text = text + ' ' + text2add
    print('Your text input has been appended to the text within the file.')
    return updated_text

def DeleteText(frname):
#take as input text and delete the first instance
#of that text from the file. For ex: ' a ' 
    text = frname.read()
    counts = dict()
    words_in_file = text.split()
    for word in words_in_file:
        word_upper = word.upper()
        if word_upper not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    while True:
        try:
            user_input = input('What word would you like to delete? ').upper()
            if user_input in counts:
                break
            else:
                print('That word is already not in the text file. Please enter a different word to delete.')
        except ValueError:
            print('That word is already not in the text file. Please enter a different word to delete.')

    updated_text = ''
    counter = 0
    for word in words_in_file:
        if (word.upper() == user_input) and (counter == 0):
            updated_text += ' '
            counter += 1
        else:
            updated_text += word + ' '
     
    updated_text = updated_text.strip()
    print(f'The first instance of {user_input} was deleted from the text file successfully.')
    return updated_text

def HighLight(frname):
#take an input word and then output the text with
#all instances of that word surrounded by symbols
#to make it easier to see.
    text = frname.read()
    counts = dict()
    words_in_file = text.split()
    for word in words_in_file:
        word_upper = word.upper()
        if word_upper not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    while True:
        try:
            user_input = input('What word would you like to highlight? ').upper()
            if user_input in counts:
                break
            else:
                print('That word is not in the text file. Please enter a different word to highlight.')
        except ValueError:
            print('That word is not in the text file. Please enter a different word to highlight.')

    updated_text = ''
    for word in words_in_file:
        if word.upper() == user_input:
            updated_text += ' **' + word + '** '
        else:
            updated_text += word + ' '
     
    updated_text = updated_text.strip()

    print(f'{user_input} was highlighted successfully.')
    return updated_text


def Word2Ascii(frname):
#convert a word from the text to ascii values
    text = frname.read()
    counts = dict()
    words_in_file = text.split()
    for word in words_in_file:
        word_upper = word.upper()
        if word_upper not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    while True:
        try:
            user_input = input('What word from the text would you like to get the ASCII value of? All words are converted to be uppercase. ').upper()
            if user_input in counts:
                break
            else:
                print('That word is not in the text file. Please enter a different word to convert to ASCII.')
        except ValueError:
            print('That word is not in the text file. Please enter a different word to convert to ASCII.')

    word2ascii = [ord(letter) for letter in user_input]

    print(f'The word, {user_input}, as ASCII values is {word2ascii}. Very cool.')
    return

def readTextFile(fname):
#reads the file and stores it for use in the program
    frname = open(fname, 'r')
    return frname

def saveTextFile(file, updated_text):
#save all changes made to the text and should be
#called after all changes to the text.
    with open(file, 'w') as fwname:
        fwname.write(updated_text)
    print('Updated text saved successfully.')
    return


#       -- Main Function & Let's Run the Program --

def main():
    print('Welcome to Notepad Text Editor!')
    print('''
Instructions: based on the menu that will be printed below,
1) Enter the name of the .txt file you would like to edit. It must be in the same
folder as this python file. The .txt will be appended to the end of the name you enter.
Example:
    The user inputs Seuss
    The input the code will see will automatically be Seuss.txt
2) Select from the menu what edits you would like to make to your notepad .txt file.
3) You will be asked to make your selection by inputting what number from the
table of contents you would like to be executed unto your .txt file.You may
be prompted for another input based on your selection.
4) The program will ask you if you're finished making edits. If you are not, you
will start back at step 1.
5) When you are finished with text editor, the changes will be saved to the file.
    ''')
    txtfile = check_file()
    user_continue = 'yes'
    while user_continue == 'yes':
        print('''
===Edit Menu===
1: Top 5 Most Common Words
2: Single Word Frequency
3: Replace a word
4: Add Text
5: Delete Text
6: Highlight Text
7: Convert word in text to ASCII values
===============
        ''')
        while True:
            try:
                menu_input = int(input('Select a menu option to edit text (input a number corresponding to a menu choice 1-7): '))
                if 1 <= menu_input <= 7:
                    break
                else:
                    print('Invalid input. Please enter a number between 1 and 7.')
            except ValueError:
                print('Invalid input. Please enter an integer between 1 and 7.')
        if menu_input == 1:
            frname = readTextFile(txtfile)
            AllWordCount(frname)
            frname.close()
        elif menu_input == 2:
            search_word = input('What word would you like to see the frequency of? ').upper()
            frname = readTextFile(txtfile)
            SingleWordCount(frname, search_word)
            frname.close()
        elif menu_input == 3:
            frname = readTextFile(txtfile)
            updated_text = ReplaceWord(frname)
            saveTextFile(txtfile, updated_text)
            frname.close()
        elif menu_input == 4:
            frname = readTextFile(txtfile)
            added_text = AddText(frname)
            saveTextFile(txtfile, added_text)
            frname.close()
        elif menu_input == 5:
            frname = readTextFile(txtfile)
            text2del = DeleteText(frname)
            saveTextFile(txtfile, text2del)
            frname.close()
        elif menu_input == 6: 
            frname = readTextFile(txtfile)
            text2highlight = HighLight(frname)
            saveTextFile(txtfile, text2highlight)
            frname.close()
        else:
            frname = readTextFile(txtfile)
            Word2Ascii(frname)
            frname.close()
        print()
        while True:
            try:
                user_continue = input('Would you like to make any more edits (Yes or No)? ').lower()
                if user_continue in {'yes', 'no'}:
                    break
                else:
                    print('Invalid input. Please enter yes or no.')
            except ValueError:
                print('Invalid input. Please enter yes or no.')
    print()
    print('All edits are completed and saved to your text file. Thank you for using my text editor.')
    
    return

main()











    
