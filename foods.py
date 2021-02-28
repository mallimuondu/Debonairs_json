import json
import datetime as time
now = time.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Have a nice night.')

    
items =input( ''' This are the categiry we have
a.Food
b.iscreem
c.Drinks
which do you want: 
''')
if items == 'a' or items == 'A' or items == 'Food'or items == 'food':
    with open('foods.json','r') as i:
        food = json.load(i)
        for nyumy in food["Foods"]:
            print(nyumy['Food'],nyumy['price'])
elif items == 'b' or items == 'B' or items == 'iscreem' or items== 'Iscreem':
    with open('foods.json','r') as a:
        iscreems = json.load(a)
        for b in iscreems["isceream"]:
            print(b['icescreems'],b['price'])
elif items == 'c' or items == 'C' or items == 'Drinks' or items == 'drinks':
    with open('foods.json','r') as c:
        Drinks = json.load(c)
        for d in Drinks["Drink"]:
            print(d['drinks'],d['price'])