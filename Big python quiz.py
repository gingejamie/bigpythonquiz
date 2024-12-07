import time
import asyncio

async def main():
    score = 0
    print("welcome to the python quiz")
    time.sleep(1)
    print()
    print("Are you ready to rumbleeeee!!!")
    time.sleep(0.5)
    print()
    print("A: Yes")
    time.sleep(0.5)
    print()
    print("B: No")
    time.sleep(0.5)
    print()
    yon = input("Answer Here:")
    start = False

    if yon == "A" or "a":
        start = True

    elif yon == "B" or "b":
        time.sleep(1)
        print()
        print("OH I rlly thought you were gonna say yes")
        time.sleep(0.5)
        print("Uhm")
        time.sleep(0.5)
        print("I guess ill wait for like 10 seconds")
        time.sleep(10)
        print("Are you ready to rumb... nah I aint doin that again do you wanna do it or not")
        time.sleep(0.5)
        print()
        print("A: Yes")
        time.sleep(0.5)
        print()
        print("B: No")
        time.sleep(0.5)
        print()
        yon1 = input("Answer Here:")

        if yon1 == "A" or "a":
            start = True
        if yon1 == "B" or "b":
            print("tough luck")
            start = True


    if start == True:
        print("your first big question is what is a variable")
        time.sleep(0.5)
        print()
        print("A: A true or false statement")
        time.sleep(0.5)
        print()
        print("B: A storage location that can change")
        time.sleep(0.5)
        print()
        print("C: A type of sandwich from subway")
        time.sleep(0.5)
        print()
        print("D: A programming language")
        answer = input("answer here:")

        if answer == "B":
            print("Correct")
            score = score+1

        else:
            print("Incorrect")

        print("Number 2 is who is the creator of python")
        time.sleep(0.5)
        print()
        print("A: guillermo del toro")
        time.sleep(0.5)
        print()
        print("B: jack hondstone")
        time.sleep(0.5)
        print()
        print("C: Mr python")
        time.sleep(0.5)
        print()
        print("D: guido van rossum")
        answer1 = input("answer here:")

        if answer1 == "D":
            print("Correct")
            score = score+1

        else:
            print("Incorrect")

        print("numero tres is what company uses python a lot")
        time.sleep(0.5)
        print()
        print("A: Universal studios")
        time.sleep(0.5)
        print()
        print("B: N.A.S.A")
        time.sleep(0.5)
        print()
        print("C: TikTok")
        time.sleep(0.5)
        print()
        print("D: Unreal Engine")
        answer2 = input("answer here:")

        if answer2 == "B":
            print("Correct")
            score = score+1

        else:
            print("Incorrect")

        print("Number 4 is what is the file type of every python file")
        time.sleep(0.5)
        print()
        print("A: .pythonfiles")
        time.sleep(0.5)
        print()
        print("B: .png")
        time.sleep(0.5)
        print()
        print("C: .py")
        time.sleep(0.5)
        print()
        print("D: .txt")
        answer3 = input("answer here:")

        if answer3 == "C":
            print("Correct")
            score = score+1

        else:
            print("Incorrect")

        print("your final question is can you make games in python")
        time.sleep(0.5)
        print()
        print("A: Yes")
        time.sleep(0.5)
        print()
        print("B: No")
        answer4 = input("answer here:") 

        if answer4 == "A":
            print("Correct")
            score = score+1

        else:
            print("Incorrect")
    grade = 0
    print("your score was", score)
    if score == 5:
        print("your grade was an A")

    if score == 4:
        print("your grade was a B")

    if score == 3:
        print("your grade was a C")

    if score == 2:
        print("your grade was a D")

    if score == 1 or 0:
        print("your grade was a F")
    await asyncio.sleep(0)
asyncio.run(main())