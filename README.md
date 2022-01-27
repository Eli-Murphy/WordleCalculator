# Wordle Calculator 1.0

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [How To Use](#how-to-use)

## General Info

The Wordle Calculator is a python script that assists in finding adequite words for [Wordle](https://www.powerlanguage.co.uk/wordle/). My collecting the letters with a known position (green colored letters), the letters with an unknown location (Yellow), and letters that are not in the word (grey).

## Technologies

This was created using:
* Python 3.9
* Microsoft Visual Studio Code
* [English Words Git Repository](https://github.com/dwyl/english-words)

## How To Use

### How to Use with given dictionary
1. Run wordlecalc.py
2. Play wordle for a good amount of time until you have a good amount of data to input
3. Follow prompts 
4. Use best option as a guess on Wordle!
  * If there are too many uses, keep playing regularly until you have more letters to input

### How to Use with New Dictionary
1. Open dictfrom.txt and paste your dictionary into the file (Must be split my a newline)
2. Save dictfrom.txt
3. Run dirnarrow.py to isolate 5 letter words and words that comtain exclusivly english alphabetical characters
4. Follow [How to Use with given dictionary](#how-to-use-with-given-dictionary)


## Bug Notes

I am relativly new to coding, so there are some bugs I am currently working on. Below are the known bugs.

Bug 27 January 2022: If there are letters that are in the unknown location section, it will still give it the possibility of being in the known incorrect spot.  

* Example Scenario:
    1. Wordle Word: Chase
    2. Known position letters: -ha-- <br />
    3. Known letters unknown position: c (Yellow in first position, meaning cant start with C)  <br />
    4. Return possibilities: ['chace', 'chafe', 'chaff', 'chain', 'chair', 'chalk', 'champ', 'chant', 'chaos', 'chaps', 'chard', 'charm', 'chars', 'chart', 'chary', 'chase',    'chasm', 'chats', 'shack', 'whack']<br />
    5. It is returning wirds that begin with C when the user knows it cannot.<br />
    6. Status: Work In Progress

## To-Be-Added Features
* Try/Except on user inputs
* More appealing UI

## Contact

Any questions please DM me on github or discord ILikeBrunch#0826
