# read in a tweet
# how many characters are in my tweet
# am I within the limit?
# how many hashtags are there?
# what are the hashtags
# how many @mentions are there
# what are the @mentions

import sys

def tweetalize():
    print("Welcome to the awesometastic tweetalizer! Start analyzing your tweets now!")

    while True:
      tw = input("What tweet would you like to analyze? To quit, just enter 'q'. ") #if using python 3, use input function

      if tw == 'q' or tw == 'Q':
          exit()

      print("Tweet is " + str(len(tw)) + " characters long")
      if len(tw) > 140:
          print("The number of characters in this tweet is too damn high!\nThe limit is 140.")

      keyword = 0
      for hashtag in tw.split(' '):
          if hashtag[0] == "#":
              print("Tweet contains the hashtag: " + hashtag)
              keyword += 1
      print("The tweet has " + str(keyword) + " total #hashtags")

      mention = 0
      for mentions in tw.split(' '):
          if mentions[0] == "@":
              print("Tweet contains the mention: " + mentions)
              mention += 1
      print("The tweet has " + str(mention) + " total @mentions")


tweetalize()