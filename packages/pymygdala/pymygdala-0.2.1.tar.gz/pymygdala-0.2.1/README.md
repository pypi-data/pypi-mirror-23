# Pymygdala

A CAPO aware library and suite of CLIs for interacting with RabbitMQ. This work borrows heavily from python-logging-rabbit, which can be found here:

https://github.com/albertomr86/python-logging-rabbitmq/tree/master/python_logging_rabbitmq

## Requirements

This library depends on pycapo and Pika.

## Usage


### Logging API

This is the minimal use case, where Pymygdala gets connection details from CAPO and relies on the defaults where it can.

    log = logging.getLogger(__name__)
    log.setlevel(logging.DEBUG)
    handler = LogHandler(profile='test', application='test-app',
                         level=logging.INFO)
    log.addHandler(handler)
    log.error("there are eels in my hovercraft")

### Logging CLI

    pym-sendlog, 0.2.0: a command line tool for logging to RabbitMQ.

    optional arguments:
      -h, --help            show this help message and exit
      --profile PROFILE     CAPO profile name to use, e.g. test, production
      --exchange EXCHANGE   exchange name to use, e.g. archive.logs
      --type EXCHANGE_TYPE  exchange type to use, e.g. fanout
      --hostname HOSTNAME   server name of the RabbitMQ server
      --username USERNAME   username of the RabbitMQ server
      --password PASSWORD   password of the RabbitMQ server
      --port PORT           port number of the RabbitMQ server
      --key ROUTING_KEY     routing key, e.g. archive.logs

    required arguments:
      --level LEVEL         logging level, e.g. DEBUG, WARN
      --message MESSAGE     message to log
      --app APPLICATION     the application name to log as

### DumpLogs CLI

    pym-dumplogs, 0.2.0: connect to a RabbitMQ server and dump out logs.

    optional arguments:
      -h, --help            show this help message and exit
      --profile PROFILE     CAPO profile name to use, e.g. test, production
      --exchange EXCHANGE   exchange name to use, e.g. archive.logs
      --type EXCHANGE_TYPE  exchange type to use, e.g. fanout
      --hostname HOSTNAME   server name of the RabbitMQ server
      --username USERNAME   username of the RabbitMQ server
      --password PASSWORD   password of the RabbitMQ server
      --port PORT           port number of the RabbitMQ server
      --outfile OUTFILE     write output to file, - for STDOUT

    This is the pym-dumplogs epilog.

### Sending an event, API

    message = {'eventName': settings['metadata']['workflow'],
               'type': settings['metadata']['type'],
               'additionalPaths': [],
               'metadata': settings['metadata']}
    se = SendEvent(**settings)
    se.send(json.dumps(message))

### Sending an event, CLI

This is the pym-sendevent description, 0.2.0

    optional arguments:
      -h, --help            show this help message and exit
      --profile PROFILE     CAPO profile name to use, e.g. test, production
      --exchange EXCHANGE   exchange name to use, e.g. archive.logs
      --type EXCHANGE_TYPE  exchange type to use, e.g. fanout
      --hostname HOSTNAME   server name of the RabbitMQ server
      --username USERNAME   username of the RabbitMQ server
      --password PASSWORD   password of the RabbitMQ server
      --port PORT           port number of the RabbitMQ server
      --key ROUTING_KEY     routing key, e.g. archive.logs
      --metadata METADATA   provide a KEY=VALUE pair to be passed to RabbitMQ; can be used multiple times

    This is the pym-sendevent epilog.