from flask import Flask, request, jsonify

app = Flask(__name__)

# Basit bir GET isteği için route
@app.route('/get', methods=['GET'])
def get_data():
    return jsonify({"message": "GET isteği başarılı", "data": [1, 2, 3, 4]})

# Basit bir POST isteği için route
@app.route('/post', methods=['POST'])
def post_data():
    data = request.json  # Gönderilen JSON verisini al
    if not data:
        return jsonify({"error": "Herhangi bir veri bulunamadı"}), 400
    
    return jsonify({"message": "POST isteği başarılı", "received_data": data})

if __name__ == '__main__':
    app.run(debug=True)
