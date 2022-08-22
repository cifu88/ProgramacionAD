"""Write an if statement to determine if an album had a rating greater than 8. 
Test it using the rating for the album “Back in Black” that had a rating of 8.5. If the statement is true print "This album is Amazing!"""
RatingBiB = 8.5

if RatingBiB > 8:
    print("This album is Amazing!")

"""Write an if-else statement that performs the following. 
If the rating is larger then eight print “this album is amazing”. If the rating is less than or equal to 8 print “this album is ok”."""

if RatingBiB > 8:
    print("This album is Amazing!")
else:
    print("This album is ok")

"""Write an if statement to determine if an album came out before 1980 or in the years: 1991 or 1993. 
If the condition is true print out the year the album came out."""

AlbumYear = 1990

if AlbumYear < 1980 or AlbumYear == 1991 or AlbumYear == 1993:
    print(AlbumYear)