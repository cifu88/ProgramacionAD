"""Write a for loop the prints out all the element between -5 and 5 using the range function."""
for i in range(-4,5):
    print(i)

"""Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions."""
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for l in Genres:
    print(l)

"""
Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']"""
squares=['red', 'yellow', 'green', 'purple', 'blue']
for k in squares:
    print(k)

"""Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. 
If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]"""
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
score = PlayListRatings[0]
while (i < len(PlayListRatings) and score >=6):
    print(PlayListRatings[i])
    i +=1
    score = PlayListRatings[i]

"""Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. 
Stop and exit the loop if the value on the list is not 'orange':"""
colors = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_colors = []
i = 0
while (i <= len(colors) and colors[i]=="orange"):
    new_colors.append(colors[i])
    i +=1
print(new_colors)