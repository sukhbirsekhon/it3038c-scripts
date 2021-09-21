import time
start_time = time.time()

print('What is your name?')

myName = input()

print('Hello, ' + myName + '. That is a good name. How old are you?')

myAge = int(input())

# determine message based on age
if myAge < 13:
    print("Learning young, that's good!")
elif myAge == 13:
    print("You're teenager now...")
elif myAge > 13 and myAge < 30:
    print("Still young, still learning...")
elif myAge >= 30 and myAge < 65:
    print("Now you're adulting")
else: 
    print("... you've lived a long time!")

time.sleep(2)
programAge = int(time.time() - start_time)

print("%s? That's funny, I am only %s seconds old." % (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2))

time.sleep(1)
print("I'm tired. I go to sleep now.")

