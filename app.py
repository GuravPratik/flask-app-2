from flask import Flask, jsonify, request
from flask_cors import CORS
from db import execute_query

PORT = 3000
app = Flask(__name__)
CORS(app)

@app.route("/query-question")
def query_question():
    question_id = int(request.headers['Question-Id'])
    result, columns = execute_query(question_id=question_id)

    if result is not None and columns is not None:
        response_data = {'data': result, 'columns': columns}
        return jsonify(response_data)
    else:
        return jsonify({'error': 'Failed to execute the query'}), 500

if __name__ == "__main__":
    app.run(port=PORT)