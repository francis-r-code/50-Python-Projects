# Dice Roller


A program written in Python to understand dictionaries and matplotlib.

To see how I coded the program, check out the [coding session's YouTube video!](https://youtu.be/AB9ie8aKYu4)

## 🎯 Objective
Create a program that will allow users to roll a virtual dice by specifying:
* How many sides the dice should have
* How many times they want to roll the dice

Additionally, display a graph that visually demonstrates how many times each side was rolled on the dice.

## 🔧 Challenges and Learnings
* **Dictionaries:** I chose to use a dictionary for this program instead of other types, such as lists, because dictionaries let you easily map values (dice rolls) to keys (dice sides) and increment them. On the other hand, using a list would result in it being be significantly long if I wanted a large amount of rolls, since each roll would be stored as an item in the list. For this project, I had to learn how to work with dictionaries, including keys and values, and how to get and modify its data.
* **Matplotlib:** This module allows me to have a visual representation of my data by displaying a grpah. In this project, I had to learn how to create a graph, give it my data, and change different aspects of the graph such as bar widths and graph labels. Because Matplotlib has a lot of customizable features, I encountered difficulties understanding what functions I should use for my graph to make it more visually appealing.

## 🎥 Demo

*This program requires the matplotlib module to run. To install it, open your terminal and enter the command:*
```
pip install matplotlib
```