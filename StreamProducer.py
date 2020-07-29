from kafka import KafkaProducer
import kafka
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

KAFKA_VERSION = (0,10,2,0);

# TWITTER API CONFIGURATIONS



# Twitter Stream Listener
class KafkaPushListener(StreamListener):
    def __init__(self):
        # localhost:9092 = Default Zookeeper Producer Host and Port Adresses
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=KAFKA_VERSION)

    # Get Producer that has topic name is Twitter
    # self.producer = self.client.topics[bytes("twitter")].get_producer()

    def on_data(self, data):
        # Producer produces data for consumer
        # Data comes from Twitter
        self.producer.send("twitter", data.encode('utf-8'))
#        print(data)
        return True

    def on_error(self, status):
#        print(status)
        return True





def main(hashtag):
    
    consumer_key = "slMY9a0u7ECiy90cmQm6gudOI"
    consumer_secret = "OGKntBZ5unXOBiEFsnPqjI73MMglyI0emnUaZt5XA2cC1dXXZE"
    access_token = "2436900156-plKfSeKZopgq0p1rBzN7BUlamQuUPqWIqRoRdzw"
    access_secret = "fBLvM1JZqPkJOcOpqPKXc3AoNlkSkeVRjrVjf39KCUZfk"
    
    # TWITTER API AUTH
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    api = tweepy.API(auth)
    
    
    # Twitter Stream Config
    twitter_stream = Stream(auth, KafkaPushListener())
    
    # Produce Data that has trump hashtag (Tweets)
    twitter_stream.filter(track=hashtag)

    




