import aiml
import time
k = aiml.Kernel()
k.learn("study.xml")
k.respond("load aiml b")

while True:
    print(k.respond(input("input >>")))