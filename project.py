# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:54:31 2018

@author: tommc
"""

import gametasks
import gameclasses

try:
    mathInstructions = '\nIn this game, you will be given a simple arithmetic question.\nEach correct answer gives you one mark.\nNo mark s deducted for wrong answers.\n'
    binaryInstructions = '\nIn this game, you will be given a number in base 10.\nYour task is to convert this number to base 2.\nEach correct answer gives you one mark.\nNo mark is deducted for wrong answers.\n'
    bg = gameclasses.BinaryGame()
    mg = gameclasses.MathGame()    
    userName = input('Please enter your name: ')
    score = gametasks.getUserScore(userName)
    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False
    print('Welcome {}, you have a score of {}.'.format(userName, score))
    userChoice = 0
    while userChoice != '-1':
        game = 0          
        while game == 0:
            try:
                game = int(input('Math Game (1) or Binary Game (2)?: '))
                if game != 1 and game != 2:
                    game = 0
                    print('Please enter 1 or 2')
            except ValueError:
                print('Please enter 1 or 2')
        numPrompt = input('How many questions do you want per game (1 to 10): ')
        while True:
            try:
                num = int(numPrompt)
                break
            except:
                numPrompt = input('Please enter a number: ')
        if game == 1:
            mg.noOfQuestions = num
            print(mathInstructions)
            score += mg.generateQuestions()
        elif game == 2:
            bg.noOfQuestions = num
            print(binaryInstructions)
            score += bg.generateQuestions()
        userChoice = '-1'
    gametasks.updateUserScore(userName, score, newUser)
    newScore = gametasks.getUserScore(userName)
    print('You answered {} questions correct and your new score is {}!'.format(score, newScore))
    input('Press Enter to exit: ')
except:
    print('Error')