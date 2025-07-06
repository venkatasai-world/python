import art
import game_data as gd
import random as rd

print(art.logo)
times = int(input("Enter How Many Times You Will Play:"))
while times > 0:
    value1 = gd.data[rd.randint(0, 49)]
    name1 = value1['name']
    occu1 = value1['description']
    cou1 = value1['country']
    print(f"Compare A: {name1}, a {occu1} and, from {cou1}!")
    print(art.vs)
    value2 = gd.data[rd.randint(0, 49)]
    while value1 == value2:
        value2 = gd.data[rd.randint(0, 49)]
    name2 = value2['name']
    occu2 = value2['description']
    cou2 = value2['country']
    print(f"Against B: {name2}, a {occu2} and, from {cou2}!")
    user = input("Who has More Followers? Type 'A' or 'B': ").lower()
    if value1['follower_count'] > value2['follower_count']:
        if user == 'a':
            print("Hurray! You Won It")
        else:
            print("Better Luck Next Time!")
    elif value1['follower_count'] < value2['follower_count']:
        if user == 'b':
            print("Hurray! You Won It")
        else:
            print("Better Luck Next Time!")
    else:
        print("Enter valid option")
    times = times - 1








