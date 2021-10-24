# Mastermind
It's codebreaker versus codebreaker. Pit yourself against your friends 
and find out who the real <i>Mastermind</i> is! The rules are simple. 
Players take turns trying to crack their secret code using logic and visual 
hints. The first person to prove they're a mastermind wins!

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. 
Open a terminal and browse to the project's root folder. Start the program by 
running the following command.
```
python3 mastermind 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- mastermind          (source code for game)
  +-- game              (specific game classes)
    +-- __init__.py     (python package file)
    +-- director.py     (Controller)
    +-- console.py      (Interfacer)
    +-- player.py       (Information Holder)
    +-- roster.py       (Structurer)
    +-- safe.py         (Information Holder)
    +-- turn.py         (Information Holder)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

### Classes
---
| **Class** | **Description**                           | **Stereotypes**    | **Public Methods**                                      | **Dependencies**             |
| --------- | ----------------------------------------- | ------------------ | ------------------------------------------------------- | ---------------------------- |
| Director  | Controls the sequence of play             | Controller         | start\_game                                             | Console, Roster, Safe, Guess |
| Console   | Gets inputs and outputs to<br>the players | Interfacer         | get\_name<br>get\_combo<br>print\_turn<br>print\_string |                              |
| Player    | Holds player information                  | Information Holder | get\_name<br>get\_guess                                 | Guess                        |
| Roster    | Holds both players                        | Structurer         | get\_player\_turn<br>next\_turn<br>add\_player          | Player                       |
| Safe      | Holds the number to be guessed            | Information Holder | generate\_code<br>create\_hint                        |                              |
| Guess     | Gets player’s guess                       | Information Holder | guess<br>get\_previous\_guess                           |                              |

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Bryndi Hellewell - brynlol12@gmail.com
* Chase Odermott - ode16003@byui.edu 
* Carson Bush - hyperdriveguy@byui.edu
