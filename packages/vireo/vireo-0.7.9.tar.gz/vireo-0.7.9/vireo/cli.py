import json
import logging
import pprint

from gallium.interface import ICommand

from .core             import Core
from .drivers.rabbitmq import Driver, NoConnectionError
from .observer         import Observer, SYNC_START
from .helper           import prepare_logger


class Server(ICommand):
    """ Run the sample observer. """
    def identifier(self):
        return 'sample.observe'

    def define(self, parser):
        parser.add_argument(
            '--debug',
            '-d',
            action = 'store_true'
        )

        parser.add_argument(
            '--bind-url',
            '-b',
            default='amqp://guest:guest@172.17.0.1:5672/%2F'
        )

    def execute(self, args):
        logger = prepare_logger(logging.DEBUG if args.debug else logging.INFO)

        driver = Driver(
            args.bind_url,
            unlimited_retries = True,
            on_connect        = lambda c = None: logger.info('--><-- CONNECTED to {} ({})'.format(c.route, c.queue_name))                if c else None,
            on_disconnect     = lambda c = None: logger.error('-x--x- DISCONNECTED from {} ({})'.format(c.route, c.queue_name))          if c else None,
            on_error          = lambda c = None, e = None: logger.error('-->-x- ERROR on {} ({}) → {}'.format(c.route, c.queue_name, e)) if c else None,
        )

        service = Observer(driver)

        # In this example, delegation is disabled.
        # vireo.open('vireo.sample.primary', delegation_ttl = 5000)
        # vireo.on('vireo.sample.primary.delegated', lambda x: print('vireo.sample.primary.delegated: {}'.format(x)))

        def wrapper(label, data):
            print('{}:'.format(label))
            pprint.pprint(data, indent = 2)

        service.on('vireo.sample.direct',           lambda x: wrapper('vireo.sample.direct',    x))
        service.on('vireo.sample.secondary',        lambda x: wrapper('vireo.sample.secondary', x))
        service.on('vireo.sample.direct.resumable', lambda x: wrapper('vireo.sample.direct',    x), resumable = True)

        service.on(
            'vireo.sample.error',
            lambda x: wrapper('vireo.sample.error', x),
        )


        service.on_broadcast('vireo.sample.broadcast.one', lambda x: wrapper('vireo.sample.broadcast.one', x))
        service.on_broadcast('vireo.sample.broadcast.two', lambda x: wrapper('vireo.sample.broadcast.two', x))

        service.join(SYNC_START)


class EventEmitter(ICommand):
    """ Emit an event """
    def identifier(self):
        return 'event.emit'

    def define(self, parser):
        parser.add_argument(
            '--debug',
            '-d',
            action = 'store_true'
        )

        parser.add_argument(
            'event_name',
            help = 'The name of the event (e.g., "sample.primary")'
        )

        parser.add_argument(
            'event_data',
            help  = 'The JSON-compatible string data of the event',
            nargs = '?'
        )

        parser.add_argument(
            '--bind-url',
            '-b',
            default='amqp://guest:guest@172.17.0.1:5672/%2F'
        )

    def execute(self, args):
        prepare_logger(logging.DEBUG if args.debug else logging.INFO)

        driver  = Driver(args.bind_url)
        service = Core(driver)

        service.emit(args.event_name, json.loads(args.event_data) if args.event_data else None)

class EventBroadcaster(ICommand):
    """ Broadcast an event """
    def identifier(self):
        return 'event.broadcast'

    def define(self, parser):
        parser.add_argument(
            '--debug',
            '-d',
            action = 'store_true'
        )

        parser.add_argument(
            'event_name',
            help = 'The name of the event (e.g., "sample.primary")'
        )

        parser.add_argument(
            'event_data',
            help  = 'The JSON-compatible string data of the event',
            nargs = '?'
        )

        parser.add_argument(
            '--bind-url',
            '-b',
            default='amqp://guest:guest@172.17.0.1:5672/%2F'
        )

    def execute(self, args):
        prepare_logger(logging.DEBUG if args.debug else logging.INFO)

        driver  = Driver(args.bind_url)
        service = Core(driver)

        service.broadcast(args.event_name, json.loads(args.event_data) if args.event_data else None)
