# sample(main)
import paho.mqtt.client as paho


def on_message(mosq, obj, msg):
    print("Executando Comando {!s}".format(msg.topic, msg.qos, msg.payload))
    mosq.publish('pong', 'ack', 0)

def on_publish(mosq, obj, mid):
    pass


# sample(main)
if __name__ == '__main__':
    client = paho.Client()
    client.on_message = on_message
    client.on_publish = on_publish

    #sclient.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    client.connect("broker.hivemq.com", 1883, 60)
    client.subscribe("campainha", 0)

    while client.loop() == 0:
        pass
# end-sample
