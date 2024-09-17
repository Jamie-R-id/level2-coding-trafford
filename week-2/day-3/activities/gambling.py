import random
import time
import os

def look_cool(icon1,icon2,icon3):
    # print(display[icon1] , display[icon2] , display[icon3])
    for x in range(0,5):
        #uh oh spaghetti code
        icon1 = display[icon1]
        icon2 = display[icon2]
        icon3 = display[icon3]
        icon1+=1
        icon2+=1
        icon3+=1
        print(icon1, icon2, icon3)
        #print(f"| {display[icon1]} | {display[icon2]} | {display[icon3]} |")

        time.sleep(0.1)
        
        
money = 50
winnings = {
    "🍒": 5,
    "🍋": 25,
    "🍀": 50,
    "💎": 500
}

display = {
    "🍒": 1,
    "🍋": 2,
    "🍀": 3,
    "💎": 4
}

roll=["🍒","🍀","💎"]
print("Write leave to exit at any time")
while True:
    
    if input(f"You have £{money}").lower() == "leave":
        break
    time.sleep(0.3)
    if money == 0:
        print("No more gambling :(")
        break
    os.system('cls')
    look_cool(roll[0],roll[1],roll[2])
    money -= 1
    for x in range(0,3):
        tmp = (random.randrange(1,100))
        if tmp in range(0,34):
            roll[x]="🍒"
        elif tmp in range(35,68):
            roll[x]="🍋"
        elif tmp in range(69,89):
            roll[x]="🍀"
        else:
            roll[x]="💎"

    print(f"| {roll[0]} | {roll[1]} | {roll[2]} |")
    if roll[0] == roll[1] and roll[1] == roll[2]:
        print(f"Congratulations you won £{winnings[roll[0]]}")
        money += winnings[roll[0]]
    


if money > 50:
    print("You win")
else:
    print("You lose")