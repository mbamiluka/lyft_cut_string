'''
This program goes over a string from index 0, getting the
letter that's three steps ahead. And then it concatenates, 
these letters and returns it as a string.

For example: 'Beautiful'
              **a**i**l
              return 'ail'              

__author__: Mbami Luka

'''
from flask import Flask, jsonify, abort, request
import json

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def parse_json():
    try:
        string_to_cut = request.json['string_to_cut']
    except:
        print('POST request key not recognized')
        abort(400)
    result_string = cutString(string_to_cut)
    return_json = {
        "return_string": result_string,
    }
    return json.dumps(return_json)


def cutString ( string_to_cut:str) -> str :
  cut_string_result = ""

  if len(string_to_cut) < 3:
    return "Length of string_to_cut is less than 3"

  for i in range( 2, len ( string_to_cut), 3):
    cut_string_result += string_to_cut[i]

  return cut_string_result

app.run ( host='0.0.0.0', port=5000, debug=True)
