import time
import random
import sys
# flake8:noqa
class SnakesandLadder:

    lad = {}
    sna = {}
    SIX=True
    winners=[]
    players={}
    CHECK=True
    STOP=True
    SLEEP_BETWEEN_ACTIONS = 1
    MAX_VAL = 20
    DICE_FACE = 6
    player_turn_text = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
    ]

    snake_bite = [
        "boohoo",
        "bummer",
        "snake bite",
        "oh no",
        "dang"
    ]

    ladder_jump = [
        "woohoo",
        "woww",
        "nailed it",
        "oh my God...",
        "yaayyy"
    ]
    
    def message(self):

        msg = """
        Welcome to Snake and Ladder Game.
        Developed by: Samardhh Reddy

        Rules:
        1. Initally players are at starting position i.e. 0. 
            Take it in turns to roll the dice. 
            Move forward the number of spaces shown on the dice.
        2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
        3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
        4. The first player to get to the FINAL position is the winner.
        5. Hit enter to roll the dice.
        6.Make sure that head value should always less than tail in ladder
        7.Make sure that head value should always greater than tail in snake
        8.Make sure that no two head and tail values should be same
        9.Make sure that head and tail of snakes should not collapse head and tail of ladder

        """
        print(msg)
        self.getplayers()
        # self.startgame()
        self.inputsnakeandladder()
    
    def getplayers(self):

        playf = open("player.txt","w")

        playerlist=[]

        plays=(input("please enter no of players "))

        playf.write(plays+"\n")

        print()
        print("Please enter name of players ")
        print()

        for i in range(int(plays)):

            txt = input()

            playerlist.append(txt)

        for line in playerlist:

            txt = ' '

            playf.write(txt.join(line)+"\n")

        playf.close()

        file4 = open("player.txt", "r+")

        temp = file4.readlines()

        playslist = []

        for i in temp:

            # li = list(i.strip().split(" "))

            playslist.append(i.strip())


        for k in playslist:

            if not k.isnumeric():

                self.players[k] = 0

        print(self.players)


    def inputsnakeandladder(self):

        outF = open("snake.txt", "w")

        textList = []

        Snakes = (input("Please enter no of snakes "))

        outF.write(Snakes+"\n")

        print()
        print("Please enter head and tail of the snakes")
        print()
        for i in range(int(Snakes)):

            txt = input()

            textList.append(txt.split())

        for line in textList:

            txt = ' '

            outF.write(txt.join(line)+"\n")

        outF.close()

        file1 = open("snake.txt", "r+")

        temp = file1.readlines()

        snakeslist = []

        for i in temp:

            li = list(i.strip().split(" "))

            snakeslist.append(li)

        for k in snakeslist:

            if len(k) > 1:

                self.sna[int(k[0])] = int(k[1])

        print(self.sna)

        inF = open("ladder.txt", "w")

        ladderlist = []

        ladders = (input("Please enter no of ladders "))

        inF.write(ladders+"\n")

        print()
        print("Please enter head and tail of the ladders")
        print()

        for i in range(int(ladders)):

            txt = input()

            ladderlist.append(txt.split())

        for line in ladderlist:

            txt = ' '

            inF.write(txt.join(line)+"\n")

        inF.close()

        file2 = open("ladder.txt", "r+")

        temp = file2.readlines()

        llist = []

        for i in temp:

            li = list(i.strip().split(" "))

            llist.append(li)

        for k in llist:

            if len(k) > 1:

                self.lad[int(k[0])] = int(k[1])

        print(self.lad)

        self.checksnakeandladder(self.sna, self.lad)

    def deletedetails(self):

        f = open("snake.txt", "r+")  
        f.seek(0)  
        f.truncate()
        self.sna={}
        f1 = open("ladder.txt", "r+")  
        f1.seek(0)  
        f1.truncate()
        self.lad={}  
        self.inputsnakeandladder()

    def checksnakeandladder(self, snake, ladder):

        snakekeys = list(snake.keys())
        snakevalues = list(snake.values())
        ladderkeys = list(ladder.keys())
        laddervalues = list(ladder.values())
        for i in range(len(snakekeys)):
            if snakekeys[i]<snakevalues[i]:
                cond1=False
                print()
                print("Head value of snake is less than its tail value")
                print()
                print("Please enter correct values")
                print()
                self.deletedetails()
                break
            elif snakekeys[i]==snakevalues[i]:
                cond1=False
                print()
                print("Head and tails must not be equal")
                print()
                print("Please enter correct values")
                print()
                self.deletedetails()
                break
            else:
                cond1=True
        if cond1:
            for i in range(len(ladderkeys)):
                if ladderkeys[i]>laddervalues[i]:
                    cond2=False
                    print()
                    print("Head value of ladder is greater than its tail value")
                    print()
                    print("Please enter correct value")
                    print()
                    self.deletedetails()
                    break
                elif ladderkeys[i]==laddervalues[i]:
                    cond2=False
                    print()
                    print("Head and tails must not be equal")
                    print()
                    print("Please enter correct value")
                    print()
                    self.deletedetails()  
                    break
                else:
                    cond2=True
        if cond2:
            for i in snakekeys:
                if i in snakevalues:
                    cond3=False
                    print()
                    print("Head of snake should not be equal to tail of any snake")
                    print()
                    print("Please enter correct value")
                    print()
                    self.deletedetails()
                    break
                elif i in ladderkeys:
                    cond3=False
                    print()
                    print("Head of snake should not be equal to head of ladder")
                    print()
                    print("Please enter correct value")
                    print()
                    self.deletedetails()
                    break
                elif i in laddervalues:
                    cond3=False
                    print()
                    print("Head of snake should not be equal to tail of any ladder")
                    print()
                    print("Please enter correct value")
                    print()
                    self.deletedetails()
                    break
                else:
                    cond3=True
        if cond3:
            for i in ladderkeys:
                if i in laddervalues:
                    cond4=False
                    print()
                    print("Head of ladder should not be equal to tail of any ladder")
                    print()
                    print("Please enter correct value")
                    print()
                    self.deletedetails()
                    break
                elif i in snakevalues:
                    cond4=False
                    print()
                    print("Head of ladder should not be equal to tail of any snake")
                    print()
                    print("Please enter correct value")
                    print()
                    self.deletedetails()
                    break
                else:
                    cond4=True
        if cond1 and cond2 and cond3 and cond4:
            self.startgame()

    def get_dice_value(self):
        time.sleep(self.SLEEP_BETWEEN_ACTIONS)
        dice_value = random.randint(1, self.DICE_FACE)
        print("Its a " + str(dice_value))
        return dice_value

    def got_snake_bite(self,old_value, current_value, player_name):
        print("\n" + random.choice(self.snake_bite).upper() + " ~~~~~~~~>")
        print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


    def got_ladder_jump(self,old_value, current_value, player_name):
        print("\n" + random.choice(self.ladder_jump).upper() + " ########")
        print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))

    def snake_ladder(self,player_name, current_value, dice_value):

        time.sleep(self.SLEEP_BETWEEN_ACTIONS)
        old_value = current_value
        current_value = current_value + dice_value

        if current_value > self.MAX_VAL:
            print("You need " + str(self.MAX_VAL - old_value) + " to win this game. Keep trying.")
            return old_value

        print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
        if current_value in self.sna:
            final_value = self.sna.get(current_value)
            self.got_snake_bite(current_value, final_value, player_name)

        elif current_value in self.lad:
            final_value = self.lad.get(current_value)
            self.got_ladder_jump(current_value, final_value, player_name)

        else:
            final_value = current_value

        return final_value

    def check_win(self,player_name, position):
        time.sleep(self.SLEEP_BETWEEN_ACTIONS)
        if self.MAX_VAL == position:
            print("\n\n\nThats it.\n\n" + player_name + " won the game.")
            print("Congratulations " + player_name)
            self.winners.append(player_name)
        if len(self.winners)==len(self.players)-1:
            self.CHECK=False
            self.STOP=False
            a=1
            for i in self.winners:
                print()
                print(i,"wins",a,"position")
                a+=1

    def startgame(self):
        while self.CHECK:
            for x in self.players:
                if self.STOP:
                    if x not in self.winners:
                        time.sleep(self.SLEEP_BETWEEN_ACTIONS)
                        input_1 = input("\n" + x + ": " + random.choice(self.player_turn_text) + " Hit the enter to roll dice: ")
                        print("\nRolling dice...")
                        dice_value = self.get_dice_value()
                        time.sleep(self.SLEEP_BETWEEN_ACTIONS)
                        if dice_value==6:
                            input_1 = input("\n" + x + ": " + random.choice(self.player_turn_text) + " Hit the enter to roll dice: ")
                            print("\nRolling dice...")
                            dice_value1=self.get_dice_value()
                            if dice_value1==6:
                                input_1 = input("\n" + x + ": " + random.choice(self.player_turn_text) + " Hit the enter to roll dice: ")
                                print("\nRolling dice...")
                                dice_value2=self.get_dice_value()
                                if dice_value2==6:
                                    dice_value=0
                                else:
                                    dice_value=dice_value+dice_value1+dice_value2
                            else:
                                dice_value=dice_value+dice_value1
                        print(x + " moving....")
                        self.players[x] = self.snake_ladder(x, self.players[x], dice_value)
                        self.check_win(x,self.players[x])

            

            

                    
                   




la = SnakesandLadder()

la.message()
