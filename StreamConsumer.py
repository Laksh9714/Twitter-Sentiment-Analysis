from kafka import KafkaConsumer
import json
import string
from elasticsearch import Elasticsearch
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sentiment_mod as s

es = Elasticsearch()


#generating a sentiment score for each tweet obtained
#def sentiment_analyze(sentiment_text):
#    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
#    return score
#    
    
# sentiment_analyze("Today is a great day for an awakening of war and death")
    

def main():
    '''
    main function initiates a kafka consumer, initialize the tweetdata database.
    Consumer consumes tweets from producer extracts features, cleanses the tweet text,
    calculates sentiments and loads the data into postgres database
    '''
    # set-up a Kafka consumer
    consumer = KafkaConsumer("twitter")
    for msg in consumer:
        try:
            dict_data = json.loads(msg.value)
            tweet = dict_data["extended_tweet"]["full_text"]
            tweet = tweet.lower()
            clean_tweet = tweet.translate(str.maketrans('','',string.punctuation))
        
            
            sentiment,conf=s.sentiment(clean_tweet)
            print(tweet)
            print("\n")
            print(sentiment,conf) 
            
#            if(sentiment_score["compound"] >= 0.05):
#                sentiment = "positive"
#                print(sentiment)
#            elif(sentiment_score["compound"] <= -0.05):
#                sentiment = "negative"
#                print(sentiment)
#            else:
#                sentiment = "neutral"
#                print(sentiment)            
#            
            # add text and sentiment info to elasticsearch
            es.index(index="tweets_laksh",
                      doc_type="test-type",
                      body={"author": dict_data["user"]["screen_name"],
                            "date": dict_data["created_at"],
                            "message": dict_data["text"],
                            "sentiment":sentiment})
            print('\n')

            
        except:
            continue
        
if __name__ == "__main__":
    main()