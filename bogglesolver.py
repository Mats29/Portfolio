#!/usr/bin/python3

import random

def load_words():
    '''
    Loads in words from the dictionary.
    '''
    valid_words = []
    with open('twl06.txt') as word_file:
        line = word_file.readline()
        while line:
            valid_words.append(line[:-1].upper())
            line = word_file.readline()
    return valid_words[2:]


def create_boggle_grid(seed=0):
    '''
    Creates a random Boggle grid based on the letter options for each die
    '''
    if seed!=0:
        random.seed(seed)
    grid=[]
    dice=["RIFOBX","IFEHEY","DENOWS","UTOKND","HMSRAO","LUPETS","ACITOA","YLGKUE","QBMJOA","EHISPN","VETIGN","BALIYT","EZAVND","RALESC","UWILRG","PACEMD"]
    for i in range(4):
        row=[]
        for j in range(4):
            d=random.randint(0,len(dice)-1)
            n=random.randint(0,5)
            row.append(dice.pop(d)[n])
        grid.append(row)
    return grid

def print_grid(grid):
    for i in range(4):
        for j in range(4):
            print(grid[i][j],end=" ")
        print("")

def check(word,i,valid_words):
    '''
    Returns the array index of the first word in english_words
    that is not before word in alphabetical order.
    '''
    while word > valid_words[i]:
        i += 1
    if word != valid_words[i][0:len(word)]:
        i = -1
    return i


def seek(grid,m,n,used,word,location,valid_words,wordlist):
    '''
    Recursively looks for words in the grid.
    Does not return a value.
    '''
    global score
    scorevect = [0, 0, 0, 1, 1, 2, 3, 5, 11, 11, 11, 11, 11, 11, 11, 11, 11]
    directionvect = [[1, 1], [1, 0], [0, 1], [1, -1], [-1, 1], [-1, -1], [0, -1], [-1, 0]]
    new_word = word + grid[m][n]
    if grid[m][n] == 'Q':
        new_word += 'U'
    location=check(new_word,location,valid_words)
    if location != -1:
        if new_word == valid_words[location]:
            if new_word not in wordlist:
                wordlist.append(new_word)
                score += scorevect[len(new_word)]
        for i in directionvect:
            new_m = m + i[0]
            new_n = n + i[1]
            if 0 <= new_m and new_m <= 3 and 0 <= new_n and new_n <= 3 and [new_m, new_n] not in used:
                seek(grid,new_m,new_n,used+[[m,n]],new_word,location,valid_words,wordlist)
def solve_grid(grid,valid_words):
    '''
    Finds all words in the grid.
    Does not return a value.
    Prints the list of words, and the score before exiting.
    '''
    global score
    wordlist=[]
    for i in range(4):
        for j in range(4):
            seek(grid,i,j,[],"",0,valid_words,wordlist)
    wordlist.sort()
    print(wordlist)
    print("The score is ",score)

if __name__ == '__main__':
    score=0
    valid_words=load_words()
    grid=create_boggle_grid()
    print_grid(grid)
    solve_grid(grid,valid_words)
