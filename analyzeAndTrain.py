import main
import csv
import functools
import grabAttributes

numOfGames = len(main.list())
numOfAttrs = 15
givenwin = []
givenloss = []
list = []
prob_win = []

def p_x_y(attr):
    with open(main.teamname()+'data.csv', 'r') as csvfile:
        next(csvfile)
        read = csv.reader(csvfile, delimiter=' ', quotechar=',')
        given_win = 0
        given_loss = 0
        notxgivenwin = 0
        notxgivenloss = 0
        for row in read:
            # This grabs a certain column and reads how many times it happens
            for word in row:

                word = word.split(",")

                for i in range(len(row)): #

                    if '1' in word[attr] and '1' in word[-1]:
                        given_win += 1
                    if '1' in word[attr] and '0' in word[-1]:
                        given_loss += 1
                    if '0' in word[attr] and '1' in word[-1]:
                        notxgivenwin += 1
                    if '0' in word[attr] and '0' in word[-1]:
                        notxgivenloss += 1

        p_not_x_y = given_loss / numOfGames
        p_x_y = given_win / numOfGames
        not_p_x_y = notxgivenwin / numOfGames
        not_p_not_x_y = notxgivenloss / numOfGames

    return p_x_y, p_not_x_y

def prob_of_win():
    if main.teamname() == main.teamname1():

        with open(main.teamname1()+'data.csv', 'r') as csvfile:
            next(csvfile)
            read = csv.reader(csvfile, delimiter=' ', quotechar=',')
            wins = 0
            for row in read:

                for word in row:
                    #print(word)
                    word = word.split(",")
                    #print(word)
                    if '1' in word[-1]:
                        wins += 1
            chances = ((wins / numOfGames) + 0.5) / 2
            print(chances)
            prob_win.append(chances)
            return (chances)
    else:
        with open(main.teamname2()+'data.csv', 'r') as csvfile:
            next(csvfile)
            read = csv.reader(csvfile, delimiter=' ', quotechar=',')
            wins = 0
            for row in read:

                for word in row:
                    #print(word)
                    word = word.split(",")
                    #print(word)
                    if '1' in word[-1]:
                        wins += 1

            print(((wins / numOfGames) + 0.5) / 2)
            return (((wins / numOfGames) + 0.5) / 2)
def prob_of_lose():
    with open(main.teamname()+'data.csv', 'r') as csvfile:
        next(csvfile)
        read = csv.reader(csvfile, delimiter=' ', quotechar=',')
        wins = 0
        for row in read:



            #print(row)
            for word in row:
                #print(word)
                word = word.split(",")
                #print(word)
                if '0' in word[-1]:
                    wins += 1

        print(((wins/ numOfGames) + 0.5) / 2)
        return (((wins/ numOfGames) + 0.5) / 2)

def append_csv():
    prob_of_win()
    for i in range(numOfAttrs):
        givenwin.append(p_x_y(i)[0])
    givenwin.append(prob_of_win())
        #givenloss.append(p_x_y(i)[1])
    with open(main.teamname() + "data.csv", "a") as f:

        wr = csv.writer(f)
        wr.writerow(givenwin)
    #test.compareAttrs()
append_csv()
"""def train():
    answer = []

    for i in range(numOfAttrs):
        givenwin.append(p_x_y(i)[0])
        givenloss.append(p_x_y(i)[1])

    prob_win = functools.reduce(lambda x, y: x * y if y != 0 and x != 0 else 0.1, givenwin) * prob_of_win()
    prob_loss = functools.reduce(lambda x, y: x * y if y != 0 and x != 0 else 0.1, givenloss) * prob_of_lose()
    #print(prob_win)
    #print(prob_loss)
    answer.append(prob_win)
    answer.append(prob_loss)
    print(answer)
    #if max(answer) == answer[0]:
        #print("Probabily going to win")
    #else:
       # print("Probabily going to lose")

    with open(main.teamname() + "data.csv", "a") as f:
        wr = csv.writer(f)
        wr.writerow(answer)
    with open(main.teamname()+'data.csv', 'r') as csvfile:
        next(csvfile)
        read = csv.reader(csvfile, delimiter=' ', quotechar=',')
        for row in read:
            #print(row[-1])
            for word in row:

                word = word.split(",")
        print("Probability of lose: ", word[-1])
        print("Probability of win: ", word[-2])

train()"""

""" We want to grab all data for the season and then put it into a naive bayes testing set from there we analyze
the boosting algorithm. From there we can think about using that algorithm for e=stiment alalysis and see which 
answer is best. """

