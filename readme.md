# Eurovision Randomizer
## EURsorandom.py

A simple randomizer that matches a list of names with the Eurovision countries. Put together quickly to randomly assign party-goers to fancy dress.

## Usage

Run with:

``python EURsorandom.py``

Asks for 2 pieces of user input [defaults: just hit enter]:
 - Countries filename (any list of countries separated by newlines) [default: eurovision2019.participants]
 - Names filename (any list of names separated by newlines) [default: names.txt]

Outputs:
 - output.txt (a formatted file of results)

Notes:
 - Does support having less countries than people and will report total number of times a duplicate was used.
 - eurovision2019.finalists will be updated once this is fully known on 16th May 2019.
 - Can be used to match any two arbitrary newline separated lists
