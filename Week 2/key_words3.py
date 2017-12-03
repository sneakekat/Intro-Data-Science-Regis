import json
import sys
import pandas as pd
import matplotlib.pyplot as plt
import pylab


def readTwitterData(twitterDataFile):    #functino to read twitter json file below
        tweets = []
        with open(twitterDataFile, encoding="utf-8") as infile:
                for line in infile:
                        tweets.append(json.loads(json.loads(line)))
        print(type(tweets[0]))
        return tweets

def key_words(row):
        words = []
        if row['text']:
                text = row["text"].lower()
                if "rock" in text or "climbing" in text:
                        words.append("climbing")
                if "mountains" in text or "colorado" in text:
                        words.append("colorado")
                if "snow" in text or "snow" in text:
                        words.append("snow")
                if "love" in text or "happy" in text:
                        words.append("happy")
        return ",".join(words)


if __name__ == '__main__':
        tweets_data_path = './req_output.json'
        tweets_data = []

        tweets_data = readTwitterData(tweets_data_path)
        tweets = pd.DataFrame()
        texts = []
        tweets['text'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))

        tweets["words"] = tweets.apply(key_words, axis=1)
        counts = tweets["words"].value_counts()
        print(counts)

        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Key Words', fontsize=15)
        ax.set_ylabel('Number of Tweets', fontsize=15)
        ax.set_title('Key Words', fontsize=15, fontweight='bold')
        counts[1:5].plot(ax=ax, kind='bar', color='purple')

        pylab.show()
