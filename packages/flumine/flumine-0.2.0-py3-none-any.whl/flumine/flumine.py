import os
import logging
import threading
from betfairlightweight import (
    APIClient,
    BetfairError,
)

from .listener import FlumineListener
from .exceptions import RunError

logger = logging.getLogger(__name__)


class Flumine:

    def __init__(self, recorder, settings=None, unique_id=1e3):
        self.trading = self._create_client(settings)
        self.recorder = recorder
        self.unique_id = unique_id

        self._running = False
        self._socket = None
        self.listener = FlumineListener(recorder)  # output queue hack

    def start(self, heartbeat_ms=None, conflate_ms=None, segmentation_enabled=None, async=True):
        """Checks trading is logged in, creates socket,
        subscribes to markets, sets running to True and
        starts handler/run threads.
        """
        logger.info('Starting stream: %s' % self.unique_id)
        if self._running:
            raise RunError('Flumine is already running, call .stop() first')
        self._check_login()
        self._create_socket()
        self.unique_id = self._socket.subscribe_to_markets(
                market_filter=self.recorder.market_filter,
                market_data_filter=self.recorder.market_data_filter,
                conflate_ms=conflate_ms,
                heartbeat_ms=heartbeat_ms,
                segmentation_enabled=segmentation_enabled,
        )
        self._running = True
        if async:
            threading.Thread(target=self._run, daemon=True).start()
        else:
            self._run()

    def stop(self):
        """Stops socket, sets running to false
        and socket to None
        """
        logger.info('Stopping stream: %s' % self.unique_id)
        if not self._running:
            raise RunError('Flumine is not running')
        if self._socket:
            self._socket.stop()
        self._running = False
        self._socket = None

    def stream_status(self):
        """Checks sockets status
        """
        return str(self._socket) if self._socket else 'Socket not created'

    @staticmethod
    def _create_client(settings):
        """Returns APIClient based on settings
        or looks for username in os.environ
        """
        if settings:
            return APIClient(
                **settings.get('betfairlightweight')
            )
        else:
            username = os.environ.get('username')
            return APIClient(
                username=username
            )

    def _run(self):
        """ Runs socket and catches any errors
        """
        try:
            self._socket.start(async=False)
        except BetfairError as e:
            logger.error('Betfair error: %s' % e)
            self.stop()
        except Exception as e:
            logger.error('Unknown error: %s' % e)
            self.stop()

    def _check_login(self):
        """Login if session expired
        """
        if self.trading.session_expired:
            self.trading.login()

    def _create_socket(self):
        """Creates stream
        """
        self._socket = self.trading.streaming.create_stream(
            unique_id=self.unique_id,
            description='Flumine Socket',
            listener=self.listener
        )

    @property
    def running(self):
        return True if self._running else False

    @property
    def status(self):
        return 'running' if self._running else 'not running'

    def __repr__(self):
        return '<Flumine>'

    def __str__(self):
        return '<Flumine [%s]>' % self.status
