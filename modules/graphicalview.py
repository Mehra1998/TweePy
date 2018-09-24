import tweepy , codecs
import pandas
import json
import datetime, time
import shutil
import os
from aylienapiclient import textapi
import csv , io

width = os.get_terminal_size().columns

import win_unicode_console , colorama
# Windows deserves coloring too :D
G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\33[97m'  # white

def Visualization():
    import matplotlib.pyplot as plt
    import pandas as pd
    from collections import Counter
    import csv, io

    with io.open(csv1 + "/%s.csv" % (q), 'r', encoding='utf-8') as csvfile:
        df = pd.read_csv(csvfile)
        sent = df['Sentiment']

        ## use Counter to count how many times each sentiment appears
        ## and save each as a variable
        counter = Counter(sent)
        positive = counter['positive']
        negetive = counter['negative']
        neutral = counter['neutral']

    ## declare the variables for the pie chart, using the Counter variables for “sizes”
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [positive, negetive, neutral]
    colors = ['green', 'red', 'blue']
    piechart_name = "%s" % (q)

    def make_autopct(sizes):
        def my_autopct(pct):
            total = sum(sizes)
            val = int(round(pct * total / 100.0))
            return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

        return my_autopct

    ## use matplotlib to plot the chart
    plt.pie(sizes, labels=labels, colors=colors, startangle=90,
            autopct=lambda p: '{:.2f}%  ({:,.0f})'.format(p, p * sum(sizes) / 100))
    plt.title("Sentiments of 200 Tweets About " + piechart_name)
    plt.savefig(graph + '/%s.png' % (q))
    plt.show()


try:
    q = input("\n%s[+] Enter You Want To Search : "%(W))

    ################### Directory Path #######################
    date = datetime.date.today()
    path = os.getcwd() + "/history"
    day = path + "/%s/" % (date)
    dir = day + "%s" % (q)
    txt = day + "%s/txt" % (q)
    csv1 = day + "%s/csv" % (q)
    graph = day + "%s/graph" % (q)

    ################### Creating Directory ###################
    def create():
        try:
            if os.path.isdir(day):
                os.mkdir(dir)
                os.mkdir(txt)
                os.mkdir(csv1)
                os.mkdir(graph)
            else:
                os.mkdir(day)
                os.mkdir(dir)
                os.mkdir(txt)
                os.mkdir(csv1)
                os.mkdir(graph)
        except Exception as err:
            d= err



    ############ Main for Searching the Tweets.###############
    try:
        if os.path.isdir('history'):
            print("%sCreating directory..."%(W))
            create()

        else:
            os.mkdir("history")
            print("%sCreating directory..."%(W))
            create()
    except Exception as err:
        d = err
        print('')

    ################### api_Key ##############################
    Customer_Key = "MnoVeh70jFgzijVdcjbHiO2Tb"
    Customer_Secret = "GlXJ0y6EelLMzcfcXOUEUZ9Rz0LAjgbdjI68wtND2wJJ9Ge24z"

    Access_Token = "910353892277460993-Yw6nO4A5oz5rdKMlwO4n9pttHHtejPo"
    Access_Token_Secret = "q1OjER4j6FZtcMfolwpr0KZRnDrE5PjFdCTKEnWv2WNK0"

    ############# Connecting to Twiter's Api #################
    auth = tweepy.OAuthHandler(Customer_Key , Customer_Secret)
    auth.set_access_token(Access_Token , Access_Token_Secret)
    api = tweepy.API(auth)

    ############### Searching the Tweets #####################
    results = api.search(q = q , lang = "en" , result_type = "recent" , count = 1000)

    ############# Save into into 'txt' file ##################
    file = codecs.open(txt + "/%s.txt"%(q), "w" , "utf-8")
    for result in results:
        file.write(result.text)
        file.write("\n\n")
    file.close()



    ###############################

    try:
        client = textapi.Client("b7284df6" , "b0f78c8d866645edf88c81d2e7b60407")


        with io.open(csv1 + "/%s.csv"%(q), 'w+', encoding='utf-8', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Tweets" , "Sentiment"])
            with io.open(txt + "/%s.txt"%(q), 'r+', encoding='utf-8') as f:
                print('\n')
                print('%s*'%(Y) * width)
                for tweet in f.readlines():
                    ## Remove extra spaces or newlines around the text
                    tweet = tweet.strip()

                    ## Reject tweets which are empty so you don’t waste your API credits
                    if len(tweet) == 0:
                        continue

                    print('%s--> %s' % (W, G) + tweet)

                    ## Make call to AYLIEN Text API
                    sentiment = client.Sentiment({'text' : tweet})

                    ## Write the sentiment result into csv file
                    csv_writer.writerow([sentiment['text'], sentiment['polarity']])

                print('%s*'%(Y) * width)
                Visualization()
                time.sleep(2)

    except Exception as err:
            d = err
            Visualization()
            print('%s*' % (Y) * width)
except KeyboardInterrupt:
    print('\n', "You Didn't Enter any Query.")