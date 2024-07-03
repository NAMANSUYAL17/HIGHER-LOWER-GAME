import random
import os
import logovs
import game_database
import logohigher
print(logohigher.logo)
score=0
def display_account_info(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return (f"{name},a {description} from {country}")
def check_answer(guess,follower_1,follower_2):
    if follower_1<follower_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
Continue_flag=True
account_2=random.choice(game_database.data)
while Continue_flag:
    account_1=account_2
    account_2=random.choice(game_database.data)
    while account_1==account_2:
        account_2=random.choice(game_database.data)
    print(f"Compare 1: {display_account_info(account_1)}")
    print(logovs.logo)
    print(f"Compare 2: {display_account_info(account_2)}")
    guess=int(input("Who has more no. of followers?Type 1 or 2:"))
    followerscount_1=account_1['follower_count']
    followerscount_2=account_2['follower_count']
    is_correct=check_answer(guess,followerscount_1,followerscount_2)
    os.system('cls')
    print(logohigher.logo)
    if is_correct:
        score+=1
        print(f"You are right,your score is {score}")
    else:
        print(f"you are wrong,your score is {score}")
        Continue_flag=False





