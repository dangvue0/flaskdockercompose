from flask import Flask, jsonify, g
import pandas as pd
import os



app = Flask(__name__)

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
   
   
if __name__ == '__main__':
    app.run()