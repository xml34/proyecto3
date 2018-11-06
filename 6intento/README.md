# Twitter y Spark Streaming con kafka

Este proyecto cuenta todos los tweets que tengan que ver con el hashtag
que se ingresa como parametro en el archivo listener.py en tiempo real.

## Esplicacion del Código

1. La autenticación se da a través de la libreria Tweepy y sus credenciales
2. El streaming linstener llamado Kafka_push_listener fué creado para el 
streming en twitter, este produce la data para que sea consumido por kafka.
3. Los datos son filtrados a traves del hastag seleccionado
4. la variable Sparkcontext es creada para conectar con el cluster(de spark)
5. se crea kafka cosumer con consume los datos de twitter
6. se calcular cuantos tweets se ha echo por persona hacerca del hastag
ingresado

