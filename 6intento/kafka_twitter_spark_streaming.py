from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

if __name__ == "__main__":

    #se crea un spark contex para conectarse con el cluster(de spark)
    sc = SparkContext(appName="PythonStreamingKafkaTweetCount")

    #streaming cada 10 segundos 
    ssc = StreamingContext(sc, 10)

    #crea un stream en kafka para consumir los datos que vienen de twitter(Topic)
    #localhost:2181 direccion de puerto por defecto de zookeeper como consumer 
    kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming', {'twitter':1})
    #kafkaStream.pprint()
    
    #transforma los datos como json
    parsed = kafkaStream.map(lambda v: json.loads(v[1]))

    #cuenta en numero de tweets por usuario
    user_counts = parsed.map(lambda tweet: (tweet['user']["screen_name"]["text"], 1)).reduceByKey(lambda x,y: x + y)

    #imprimer la cuenta
    user_counts.pprint()

    #inicia la ejecusion de Streams
    ssc.start()
    ssc.awaitTermination()


