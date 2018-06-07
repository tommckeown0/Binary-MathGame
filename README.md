# Binary-MathGame
Learning to Code With Python Project

In this game the user will enter a user name to start with. If the user name exists in the userScores.txt file it will read the score and display it to you. If no user exists with the name entered it will create it with a score of 0.

Next the user chooses between the math or binary game by enter 1 or 2, any other input throws up an error and prompts the user to re-enter.

The user will choose how many questions they want from 1 to 10, any number lower or higher than this limit will default to 1 or 10 respectively and any input other than an integer will prompt for re-enter again.

In the math game 5 digits from 1-9 are randomly genereted along with 4 operators ('+', '-', '*'[*] and '**')[**] The exponent operator has been set to not appear consecutively as this causes difficulty in parsing the question without parentheses emphasising which exponent to evaluate first. ONly a number is accepted, anything will require re-entering.

The binary game offers a number from 1-100 in base 10 that the user must convert to base 2. Only a base 2 number will be accepted as an answer, anything else will require the user to re-enter.

In both games if the correct answer is given it will be displayed and the score will be added to the users total score. If an incorrect answer is given (in the right format) the answer is displayed and the game moves to the next question.

Once complete the score is updated in the userScores.txt file and the user can press Enter to exit the application!
