# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:54:23 2018

@author: tommc
"""

import random

class Game:
    
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions
   
    @property
    def noOfQuestions(self):
        return self._noOfQuestions
    
    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print('\nMinimum number of Questions = 1')
            print('Hence, number of questions will be set to 1')
        elif value > 10:
            self._noOfQuestions = 10
            print('\nMaximum number of questions = 10')
            print('Hence, number of questions will be set to 10')
        else:
            self._noOfQuestions = value
            
            
class BinaryGame(Game):    
  
    def generateQuestions(self):
        score = 0
        question = 1
        for i in range(self.noOfQuestions):
            base10 = random.randint(1, 100)
            userResult = input('Question {}\nConvert {} to binary: '.format(question, base10))
            while True:
                try:
                    answer = int(userResult, base = 2)
                    if answer == base10:
                        score += 1
                        question += 1
                        print('\nCorrect! Your score is now {}'.format(score))
                        break
                    else:
                        question += 1
                        print('\nIncorrect, the answer was {:b}.'.format(base10))
                        break
                except:                    
                    userResult = input("You need to enter a number in base 2!\nConvert {} to binary: ".format(base10))
        return score
                    
'''                  
test = BinaryGame()
test.noOfQuestions = 3
test.generateQuestions()
'''

class MathGame(Game):
    
    def generateQuestions(self):
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {0:'+', 1:'-', 2:'*', 3:'**'}
        random.randint(0,3)
        question = 1
        for i in range(self.noOfQuestions):
            for i2 in range(len(numberList)):
                numberList[i2] = random.randint(1, 9)
            for i3 in range(len(symbolList)):
                if symbolList[i3-1] == '**':
                    symbolList[i3] = operatorDict[random.randint(0, 2)]
                else:
                    symbolList[i3] = operatorDict[random.randint(0, 3)]
            questionString = ('')
            for i4 in range(len(numberList)):
                questionString += str(numberList[i4])
                if i4 == 4:
                    break
                questionString += str(' ' + symbolList[i4] + ' ')
            result = eval(questionString)
            questionString = questionString.replace('**', '^')
            while True:
                userResult = int(input('Question {}\n{} = '.format(question, questionString)))
                try:
                    if userResult == result:
                        score += 1
                        question += 1
                        print('\nCorrect! Your score is now {}'.format(score))
                        break
                    else:
                        question += 1
                        print('\nIncorrect, the answer was {}.'.format(result))
                        break
                except:
                    userResult = input('You need to enter a number!\n{}'.format(questionString))
        return score
            
'''            
test = MathGame()
test.noOfQuestions = 3
test.generateQuestions()
'''