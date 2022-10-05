# じゃんけんします
import random

def get_players_hand():
    first_message = "Enter 'rock', 'sissors' or 'paper': "
    your_input = input(first_message)

    if your_input == "rock":
        your_hand = 1
    elif your_input == "sissors":
        your_hand = 2
    elif your_input == "paper":
        your_hand = 3
    else:
        print("An error occuered")
        get_players_hand()
    return your_hand



def get_opponent_hand():
    opp_hand = random.randint(1,3)
    return opp_hand



def judge(hand_a, hand_b):
    culc = hand_a - hand_b

    if culc == -1 or culc == 2:
        did_win = True
        return did_win
    elif culc == -2 or culc == 1:
        did_win = False
        return did_win
    elif culc == 0:
        print("AIKO DE!")
        janken()




def show_result(win):
    if win:
        print("YOU WIN")
    elif win == False:
        print("YOU LOSE")


def janken():
    players_hand = get_players_hand()
    opponent_hand = get_opponent_hand()
    show_result(judge(hand_a=players_hand, hand_b=opponent_hand))
    

janken()




# Classの復習
# print("Hello world")
# class Agent:
#     def __init__(self, name, role, ultimate):
#         self.name = name
#         self.role = role
#         self.ultimate = ultimate

#     def info(self):
#         print(f"{self.name}, you are the {self.role}. Your ultimate ability is named {self.ultimate}")

# raze = Agent(name = "Raze", role = "Duelist", ultimate = "Showstopper")
# sage = Agent(name="Sage", role="Sentinel", ultimate="Rescurection")

# raze.info()







# 0 から 100 までの整数がランダムに格納されたリストを返す関数 randlist を作成してください。引数でリストのサイズを指定します。randlist の実行例を以下に示します。

# >>> randlist(10)
# [31, 98, 49, 2, 90, 27, 12, 0, 11, 54]
# >>> randlist(5)
# [85, 29, 92, 40, 18]
# >>> randlist(3)
# [43, 2, 89]

# import random

# # print(random.randint(1,19))

# def randlist(num):
    
#     list = []
    
#     for i in range(num):
#         i = random.randint(0, 100)
#         list.append(i)
    
#     print(list)

# randlist(4)






# 「ランダムなリスト」で作成した randlist で、リストに格納される整数の範囲をキーワード引数から指定できるようにして下さい。

# randlist の実行例を以下に示します。

# >>> randlist(10)                           #  0 から 100 まで
# [31, 52, 81, 9, 85, 11, 13, 82, 25, 51]
# >>> randlist(5, lower=20)                  # 20 から 100 まで
# [95, 20, 31, 51, 83]
# >>> randlist(3, upper=50)                  #  0 から  50 まで
# [12, 31, 23]
# >>> randlist(6, lower=20, upper=50)        # 20 から  50 まで
# [24, 38, 38, 40, 44, 47]

# def randlist2(num, lower=0, upper=100):
#     list = []

#     for i in range(num):
#         i = random.randint(lower, upper)
#         list.append(i)
    
#     print(list)

# randlist2(4)