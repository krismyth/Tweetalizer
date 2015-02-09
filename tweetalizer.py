# read in a tweet
# how many characters are in my tweet
# am I within the limit?
# how many hashtags are there?
# what are the hashtags
# how many @mentions are there
# what are the @mentions

import sys

# primary function tweetalize:
def tweetalize():
  print("Welcome to the awesometastic tweetalizer! Start analyzing your tweets now!")
  while True:
    tweet = getTweetFromUser()
    checkLength(tweet)
    checkContent(tweet)

def getTweetFromUser():  #if using python3, use input() instead of raw_input()
  userInput = input("What tweet would you like to analyze? To quit, just enter 'q'. ")
  if userInput == 'q' or userInput == 'Q':
    exit()

  return userInput

def checkLength(tweet):
  tweetLength = len(tweet)
  print("Tweet is %d characters long" % tweetLength)

  maxTweetLength = 140
  if tweetLength > maxTweetLength:
    print("The number of characters in this tweet is too damn high!\nThe limit is 140.")

def checkContent(tweet):
  hashCount = 0
  mentionCount = 0

  tweetContent = tweet.split(' ')
  for word in tweetContent:
    if len(word) > 0:
      if isHashtag(word):
        hashCount += 1
      elif isMention(word):
        mentionCount += 1

  print("The tweet has %d total #hashtags" % hashCount)
  print("The tweet has %d total @mentions" % mentionCount)


def isHashtag(word):
  firstCharacter = word[0]
  if firstCharacter == "#":
    print("Tweet contains the hashtag: %s" % word)
    return True
  return False

def isMention(word):
  firstCharacter = word[0]
  if firstCharacter == "@":
    print("Tweet contains the mention: %s" % word)
    return True
  return False

tweetalize()
