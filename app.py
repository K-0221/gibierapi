from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Gibier API'

@app.route('/api/recipe')
def recipe():
    dish = request.args.get("dish")
    if not dish:
        return jsonify({'error': 'No dish provided'}), 400
    return jsonify({
        'dish': dish,
        'method': f'{dish}のおすすめ調理法はローストです！'
    })
  
if __name__=='__main__':
    app.run()