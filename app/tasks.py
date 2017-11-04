from app import celery, SocketIO
import time

@celery.task(soft_time_limit=2, time_limit=4)
def test():
    try:
        time.sleep(1)
        print("Celery Works!")
    except Exception as e:
        raise Exception("Failed because of: %s" % e)