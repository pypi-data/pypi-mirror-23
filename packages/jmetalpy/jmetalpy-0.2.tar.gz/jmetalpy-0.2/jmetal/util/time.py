import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_time_of_execution(fn):
    """ Decorator to get time of execution of any method inside a class. """

    def wrapped(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        logger.info("Computing time to " + fn.__name__ + " (in seconds): " + str(time.time() - start_time))

        return res

    return wrapped
