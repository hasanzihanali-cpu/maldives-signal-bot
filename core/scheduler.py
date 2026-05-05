import schedule
import time
from core.pipeline import run_pipeline

def start():
    schedule.every(3).minutes.do(run_pipeline)

    while True:
        schedule.run_pending()
        time.sleep(5)
