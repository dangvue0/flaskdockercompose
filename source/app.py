from flask import Flask, jsonify, g

from flask_caching import Cache
import pandas as pd
import numpy as np
from flask_apscheduler import APScheduler
import logging

# Configure logging before creating the Flask app
logging.basicConfig(
    filename='app.log',  # Optional: Log to a file
    level=logging.DEBUG,  # Set the desired logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Optional: Customize the log format
)

class Config:
    """App configuration."""

    SCHEDULER_API_ENABLED = True
    
scheduler = APScheduler()

@scheduler.task("interval", id="do_job_1", seconds=30, misfire_grace_time=900)
def job1():
    """Sample job 1."""
    print("Job 1 executed")
    

app = Flask(__name__)
app.config.from_object(Config())

# Configure the logger

# logging.basicConfig(filename='app.log', level=logging.DEBUG)
# logger.info("Flask starting...")



    
scheduler.init_app(app)
scheduler.start()

# Configure caching
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

def clear_cache():
    cache.clear()
    
def hello():
    print('TEST')


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