# read in a tweet
# how many characters are in my tweet
# am I within the limit?
# how many hashtags are there?
# what are the hashtags
# how many @mentions are there
# what are the @mentions

import sys

def getTweetFromUser():

def checkLength(tweet):
  tweetLength = len(tweet)
  print("Tweet is " + str(tweetLength) + " characters long")

  maxTweetLength = 140
      if tweetLength > maxTweetLength:

          print("The number of characters in this tweet is too damn high!\nThe limit is 140.")

def checkHashtags():


def checkMentions():



# primary function tweetalize:
def tweetalize():
    print("Welcome to the awesometastic tweetalizer! Start analyzing your tweets now!")

    while True:  #if using python3, use input() instead of raw_input()
      tweet = input("What tweet would you like to analyze? To quit, just enter 'q'. ")

      if tweet == 'q' or tweet == 'Q':
          exit()

      checkLength(tweet)

      keyword = 0
      for hashtag in tweet.split(' '):
          if hashtag[0] == "#":
              print("Tweet contains the hashtag: " + hashtag)
              keyword += 1
      print("The tweet has " + str(keyword) + " total #hashtags")

      mention = 0
      for mentions in tweet.split(' '):
          if mentions[0] == "@":
              print("Tweet contains the mention: " + mentions)
              mention += 1
      print("The tweet has " + str(mention) + " total @mentions")


tweetalize()