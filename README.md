## Description

Simulates the movie/book series The Hunger Games in a text-based format, but with a twist. Instead of generic teenagers include your own friends, family or favourite celebrities. Simply add your tributes to the text file and have a new entertaining scenario every time.

## Features

Currently Present:

- Names input
- Consistant pronoun usage (male, female or they/them)
- Weapons can be collected which increases kill chance
- Weapons can break
- Weapons can be stolen from dead players
- Players can die from natural causes or other players
- Kills are tracked for each player and displayed at the end
- Day/night cycle
- Tributes can receive sponsorships
- Variable probabilites that can be edited by the user

To be added:

- Arena events
- Feasts
- Teammates tracked over time

## Usage

To use, add names and genders to the players.txt file in the format:

- John, M, Jane, F, James, M, Joe, T etc.
  Doing this incorrectly will cause the program to crash

You can edit the event_pools.py file to change the probabilities of different events happening throughout the game. They must total to 1.

When this is configured simply run main.py and read the story created for you
