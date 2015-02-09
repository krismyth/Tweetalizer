# read in a tweet
# how many characters are in my tweet
# am I within the limit?
# how many hashtags are there?
# what are the hashtags
# how many @mentions are there
# what are the @mentions

import sys

def checkLength(tweet):
  # checkLength function code goes here
  tweetLength = len(tweet)
      maxLength = 140

      print("Tweet is " + str(tweetLength) + " characters long")
      if tweetLength > maxLength:
    # if let(tw) > 140:
          print("The number of characters in this tweet is too damn high!\nThe limit is 140.")


# primary function tweetalize:
def tweetalize():
    print("Welcome to the awesometastic tweetalizer! Start analyzing your tweets now!")

    while True:
      tweet = input("What tweet would you like to analyze? To quit, just enter 'q'. ") #if using python 3, use input function

      if tweet == 'q' or tweet == 'Q':
          exit()

      checkLength(tweet)

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