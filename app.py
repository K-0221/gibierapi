from flask_cors import CORS
from flask import Flask, request, jsonify, render_template, Response
import os
import json
app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/api/recipe'methods=['GET'])
def recipe():
    dish = request.args.get("dish")
    if not dish:
        return  Response(
    json.dumps({'error': 'No dish provided'},ensure_ascii=False),
    content_type='application/json; charset=utf-8',
    status=400
        )
    return Response(
    json.dumps({
            'dish': dish,
            'method': f'{dish}のおすすめ調理法はローストです！'
        },ensure_ascii=False),
        content_type='application/json; charset=utf-8',
        status=200
    )
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)