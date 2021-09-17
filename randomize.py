#Python project ideas: Beginner level
#create a "code" generator that takes text as input and replaces each letter with another letter, and outputs the "encoded" message
# need to get each letter and randomize it
import  random
userIn = input().strip().replace(" ", "")
code = userIn.replace(random.choice(userIn), random.choice(userIn))
print(code)
