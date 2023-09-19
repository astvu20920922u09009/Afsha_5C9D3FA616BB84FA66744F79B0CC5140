"""Implement a class called Player that represents the cricket player. The Player class should have a method called play() which prints "The player is playing cricket". Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call play() method for each object."""

#Define the base class player
class Player:
  def play(self):
    print("The player is playing cricket")

#Define the derived class batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting")

#Define the derived class bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling")

#Create objects of batsman and bowler
batsman=Batsman()
bowler=Bowler()

#Call the play() method
batsman.play()
bowler.play()





