from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    # Assuming the user provides two numbers as query parameters
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    
    result = num1 + num2
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
