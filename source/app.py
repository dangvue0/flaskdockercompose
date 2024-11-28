from flask import Flask, jsonify, g
import pandas as pd
import os



app = Flask(__name__)

data = {'Name': ['John', 'Mary', 'Peter'], 'Age': [20, 25, 30]}
df = pd.DataFrame(data)

    
# df.to_csv('csv_files/data1.csv', index=False)
# print(df)

data = {'Name': ['DDDD', 'AAAA', 'BBBB'], 'Age': [22, 33, 44]}
df_next = pd.DataFrame(data)
# df_next.to_csv('csv_files/data2.csv', index=False)
# print(df_next)


@app.route('/', methods=['GET'])
def index():
    
    return jsonify(f"This is App.")

@app.route('/df', methods=['GET'])
def show_df():
    global df
    return jsonify(df.to_dict(orient='records'))

@app.route('/df/get_update', methods=['GET'])
def updat_df():
    global df
    df = df_next.copy()
    return jsonify(df.to_dict(orient='records'))
   
   
if __name__ == '__main__':
    app.run()