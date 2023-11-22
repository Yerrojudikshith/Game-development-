def scene1():
    import time
    print("""WELCOME TO THE ADVENTURE GAME!
        Let's start the action! ?-????-?
 
        swathi wakes up in her bedroom in the middle of the night. She heard a loud BAN outside the house.
        Now she has two choices she can either stay in the room or check what the sound might be about.
 
        Type your choice: Stay or Evaluate?
    """)
 
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="STAY"):
            print("\nswathi decides to stay in the room and ends up staying inside forever as noone seems to come to help her.")
            ans = 'correct'
        elif(c1.upper()=="EVALUATE"):
            print("swathi exits the room silently and reaches the main hall.")
            ans='correct'
            scene2()
        else:
            print("ENTER THE CORRECT CHOICE! Stay or Evaluate?")
            c1 = input()
def scene2():
    import time
    print("""
            In the main hall, she finds a strange but cute teddy bear on the floor. 
            She wanted to pick the teddy up. 
            But should she? It doesn't belong to her. (•??•?)
 
            Type your choice: Pick or Ignore?
 
            """)
    time.sleep(2)
    c1 = input()
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="PICK"):
            print("""\nThe moment swathi picked up the the teddy bear. The Teddy bear starts TALKING!The bear tells Lily that she is in grave danger as there is a monster in the house.And the monster has captured her PARENTS as well!But he hugged her and told her not to get scared as he knows how to beat the moster!""")
            time.sleep(2)
            print("""\nThe bear handed swathi a magical potion which can weaken the moster and make him run away!He handed her the potion and then DISAPPEARED!Lily moved forward.""")
            ans = 'correct'
            pick="True"
        elif(c1.upper()=='IGNORE'):
            print("""\nswathi decided not to pick up the bear and walked forward.""")
            ans='correct'
            pick="False"
        else:
            print("Wrong Input! Enter pick or ignore?")
            c1=input()
    time.sleep(2)
scene1()
print("\n\n")
print("=================================END OF CHAPTER 1=================================")
