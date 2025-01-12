import pyttsx3 as pt
robo = pt.init()
print("Welcome to Tisha Robo:1.0")
print("Enter 'quit' to Exit")

while True:
    word = input("Type to Say Something :")
    goodbye = "Bye Bye Bye.. Hope to see you again!"
    if word == 'quit':
        robo.say(goodbye)
        robo.runAndWait()
        break
    robo.say(word)
    robo.runAndWait()
