# CS515-Project1

# Text-Based Adventure Game

## Author Information
Kavitha Siratla
ksiratla@stevens.edu

## Repository
[Github Repository](https://github.com/kavitha-siratla/CS515-Project1/)

## How to run the program
1. Install python3
2. Clone the git repository or download the map file, adventure.py file to a folder
3. Navigate to the folder and run the command `python3 adventure.py [map filename]`


## About the program
Several verbs which can be used as commands in the game are:

1. **go**: The go verb tries to go in a given direction. You can use the command by typing `go [direction]` with direction as a valid exit.

2. **look**: The look shows once again the the room that a person is in. You can use the command by just typing `look`.

3. **get**: The get verb lets a player pick up items that are in the room. When a player says `get [ITEM]`, if that item is in the room, the player will pick it up, the item will no longer be in the room but rather it will be in the player’s inventory. 

4. **drop**: The get verb lets a player drop the items that are in his inventory to the room he is in. When a player says `drop [ITEM]`, if that item is in the inventory, the player will drop it, the item will no longer be in the inventory. 

5. **inventory**: The inventory verb shows the player the list of the items they are carrying.

6. **help**: The help verb gives the player the list of all the valid verbs.

7. **quit**: The 'quit' verb ends the game and exits the program.

## Time spent on the project
Estimated time spent: 9 hours

## How the code was tested
I have tested the code manually by running it against different test cases and with multiple map files. I have also tested it using the provided spec and using diff to compare the outputs.

## Bugs or issues
No bugs or issues

## Difficult issue or bug and its resolution
I had an issue with the arbitary spaces in the inputs and I have used regex to solve that issue.

## Extensions implemented
1. **Help Verb**: I have implemented a dynamic help verb that lists out all the valid verbs for the game. I have listed out all the methods in the player class by using dir(). The help ver can be accessed by just typing `help`.
In my example, the command `help` can be used anywhere to get the list of valid verbs.
2. **Winning and Losing Conditions**: I have a winning condition in the game that a player wins if the player uses the verb `win` when he is in the last room of the map. He loses the game in case he uses the command when he is in any other room. 
Example: Consider we have a map with 5 rooms. If the player is in the 5th room i.e. the last room and he gives the command `win`, he'd win whereas, if the player is in the 4th room and he gives the command `win`, he'd lose. 
In my example map, the Black room(the last is where the player can give a command `win` to win the game.
Step 1: go north
step 2: go south
step 3: win
3. **Drop Verb**: I have implemented a drop verb to allow the player to drop an item in a room. The item will be removed from the inventory and be placed in the room the player is. To use the verb, the player can type `drop [item]` with a valid item existing in the inventory.
In my example, the player can go to any room where there are any items to pick them up and then he can use the `drop` verb to drop any items he has in his inventory.

