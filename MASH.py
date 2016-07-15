from random import *

friendChoice = raw_input("Who do you want to be friends with?")
friends = ["Bill Gates", "Kendrick Lamar", "Bill Nye the Science Guy", "Bernie Sanders"]
friends.append(friendChoice)
x = choice(friends)
print("You will be friends with", x)

jobChoice = raw_input("What do you want your job to be?")
jobs = ["Bum", "Pro Wrestler", "Defense Attorney", "Obama's personal servant"]
jobs.append(jobChoice)
y = choice(jobs)
print("You will be", y)

wifeChoice = raw_input("Who do you want your wife to be?")
wives = ["Niki Minaj", "Negative Nancy", "Hilary Clinton", "Sarah Palin"]
wives.append(wifeChoice)
z = choice(wives)
print("Your wife will be", z)

home = ["White House", "Cave", "Shack", "Suburban House"]
a = choice(home)
print("Your home will be a", a)