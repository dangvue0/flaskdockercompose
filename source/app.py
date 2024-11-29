from flask import Flask, jsonify, g

from flask_caching import Cache
import pandas as pd
import numpy as np
from flask_apscheduler import APScheduler
import logging
 
logger = logging.getLogger(__name__)
logger.setLevel = logging.DEBUG

app = Flask(__name__)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# Configure caching
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

def clear_cache():
    cache.clear()

    
@scheduler.task('cron', id='do_job_1', hour=21, minute=43, misfire_grace_time=900)
def job1():
    logger.info("APSCHEDULER RUNNING")
    cache.clear()
    

@app.route('/', methods=['GET'])
def index():
    return jsonify(f"This is App.")



@cache.cached(timeout=86400)
def generate_random_df():
    df = pd.DataFrame(np.random.randint(0, 100, size=(500, 10)), columns=list('ABCDEFGHIJ'))
    return df

@app.route('/df', methods=['GET'])
def get_df():
    df = generate_random_df()
    return jsonify(df.to_dict(orient='records'))

@app.route('/df/reset', methods=['GET'])
def df_clear_cache():
    cache.clear()
    return jsonify(f"Clearing cache on thread.")
   
   
if __name__ == '__main__':
    app.run()