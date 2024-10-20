import random

name = input("What is your name? ")

question = input("So " + name + " what is your question? ")

answer = ["Yes - definitely" , "It is decidedly so" , 
"Without a doubt" , "Reply hazy, try again" , "Ask again later" ,
"Better not tell you now" , "My sources say no" , 
"Outlook not so good" , "Very doubtful"]

random_number = random.randint(0,8)

if not name:
  print("Question:",question)
else:
  print(name, "asks:", question)

if not question:
  print("No question?")
else:
  print("Magic 8-Ball’s answer:", answer[random_number])
