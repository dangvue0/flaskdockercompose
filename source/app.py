from flask import Flask, jsonify, g
import pandas as pd
import os
from flask_caching import Cache
import numpy as np


app = Flask(__name__)

# Configure caching
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

# data = {'Name': ['John', 'Mary', 'Peter'], 'Age': [20, 25, 30]}
# df = pd.DataFrame(data)
# directory = 'csv_files'
# if not os.path.exists(directory):
#     os.makedirs(directory)
    
# df.to_csv('csv_files/data1.csv', index=False)
# print(df)

# data = {'Name': ['DDDD', 'AAAA', 'BBBB'], 'Age': [22, 33, 44]}
# df_next = pd.DataFrame(data)
# df_next.to_csv('csv_files/data2.csv', index=False)
# print(df_next)


@app.route('/', methods=['GET'])
def index():
    return jsonify(f"This is App.")




@cache.cached(timeout=5)
def generate_random_df():
    df = pd.DataFrame(np.random.randint(0, 100, size=(500, 10)), columns=list('ABCDEFGHIJ'))
    return df

@app.route('/df', methods=['GET'])
def get_df():
    df = generate_random_df()
    
    return jsonify(df.to_dict(orient='records'))
   
   
if __name__ == '__main__':
    app.run()