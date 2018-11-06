# PROYECTO 3 - BigData <h1>
# Análisis de sentimientos <h2>

### Atributos de calidad seleccionados:
Este Proyecto consta de realizar una prueba de concepto (analisis de sentimientos)
sobre Data Streaming desde Twitter utilizando Kafka.

__Miembros del equipo y asignación de QA’s:__
* Daniel Morales Londoño

### 1. Análisis de tecnologías:

__Data Streaming: __
Es la transmision de datos a una alta y constante velocidad, la cual debe ser sufuciente 
para soportar las aplicaciones como la television de alta definición

__Apache Spark: __
Apache Spark es un framework open source para el procesamiento de datos masivos diseñado
con tres prioridades en mente: velocidad, facilidad de uso, y capacidades avanzadas de analítica.

__Tweepy: __
Es una herramienta útil para conocer, analizar y administrar los seguidores y seguidos
de una cuenta de Twitter.
este es quien nos permite a través de una keys acceder a los tweets que luegos serán
usados para el análisis de sentimientos

__Apache kafka: __
Apache Kafka es un proyecto de intermediación de mensajes,tiene como objetivo proporcionar
una plataforma unificada, de alto rendimiento y de baja latencia para la manipulación en
tiempo real de fuentes de datos.


### 1. Descrición del problema:
__Problema: __
se desea analisar cual es la reaccion del publico a ciertos hastags con el fin de analisar
cual es la respuesta del mercado a ciertos porductos y marcar expuestas a través de la 
red social Twitter

__Planeación de la solución del problema: __
A través de este proyecto se desea extraer y analisar información de la data de las redes
sociales en tiempo real, utlizando una de las soluciones de big data vistas en el curso 
de Top. en telemática: Apache Spark y python
se construirá una aplicación que lea tranmisiones en tiempo real de Twitter usado python,
y luego procesaremos los datos usando Spark Streamig para identificar los hashtags, y
aplicarles un analisis de sentimientos

### 2. Desarrollo del proyecto:
__Como correr el proyecto: __
para poder correr este proyecto se deben instalar primero ciertas herramientas como lo son:
Kafka (requiere Zookeeper), python3 (3.5.2 en este caso) y las siguientes librerias para
python desde pip o conda
	kafka-python
	oauthlib
	requests
	requests-oauthlib
	six
	tweepy
	configparser
	matplotlib

una vez instalado todo lo anterior se debe correr primero el zookeeper:
	sudo /opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties
luego se debe correr el kafka
	sudo /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties 

una vez esten corriento kafka y zookeeper se debe correr el archivo litener.py con python3
de la siguiente manera:
	PYSPARK_PYTHON=python3 /opt/spark/bin/spark-submit kafka_push_listener.py

y luego se corre el archivo spark streming.py de la siguiente manera
	PYSPARK_PYTHON=python3 /opt/spark/bin/spark-submit --packages org.apache.spark:spark-s
	treaming-kafka-0-8_2.11:2.2.0 kafka_twitter_spark_streaming.py


__Fuentes y Cybergrafia__