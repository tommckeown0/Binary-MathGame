# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:50:02 2018

@author: tommc
"""

import os

def printInstructions():
    print('Welcome to my game. INSTRUCTIONS')
    
def getUserScore(userName):
    try:        
        f = open('userScores.txt', 'r')
        counter = 0
        for line in f:
            name, score = line.split(', ')
            if userName == name:
                print('Score for {} is {}'.format(name, score))
                counter += 1
                score1 = int(score.replace('\n', ''))
                return score1
        if counter == 0:
            return -1                        
        f.close()
    except FileNotFoundError:
        f = open('userScores.txt', 'w')
        f.close()
        return -1
    except ValueError:
        return -1
    
def updateUserScore(userName, score, newUser = True):
    try:
        f = open('userScores.txt', 'r')
        for line in f:
            name, currentScore = line.split(', ')
            if userName == name:
                newUser = False
        f.close()
    except ValueError:
        newUser = True
    if newUser == True:
        f = open('userScores.txt', 'a')
        f.write('{}, {}\n'.format(userName, score))
        f.close()
    else:
        ftemp = open('userScores.tmp', 'w')
        f = open('userScores.txt' ,'r')
        for line in f:
            name, currentScore = line.split(', ')            
            if userName == name:
                ftemp.write('{}, {}\n'.format(name, score))
            elif userName != name:
                ftemp.write('{}, {}'.format(name, currentScore))
        ftemp.close()
        f.close()              
        os.remove('userScores.txt')
        os.rename('userScores.tmp', 'userScores.txt')