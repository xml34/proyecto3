import pykafka
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import twitter_config
import sys

#Configuracion de las keys del api de twitter
consumer_key = twitter_config.consumer_key
consumer_secret = twitter_config.consumer_secret
access_token = twitter_config.access_token
access_secret = twitter_config.access_secret


#Autorizacion por medio del las key del api
aut = OAuthHandler(consumer_key, consumer_secret)
aut.set_access_token(access_token, access_secret)

api = tweepy.API(aut)

#Stream Listener de tweets
class KafkaPushListener(StreamListener):          
	def __init__(self):
		#localhost:9092 = puesto de acceso de zookeeper (por defecto)
		self.client = pykafka.KafkaClient("localhost:9092")
		
		#optiende al producer que tiene como nombre twitter (Topic)
		self.producer = self.client.topics[bytes("twitter", "ascii")].get_producer()
  
	def on_data(self, data):
		#Producer produce data para consumer
		#Data viene de Tweter
		self.producer.produce(bytes(data, "ascii"))
		return True
                                                                                                                                           
	def on_error(self, status):
		print(status)
		return True

#configuracion Twitter Stream 
twitter_stream = Stream(aut, KafkaPushListener())

#Data que tiene el hastag de word
word='#'+str(sys.argv[1])
twitter_stream.filter(track=[word])
