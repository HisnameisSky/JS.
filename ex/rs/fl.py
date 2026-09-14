from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/convert", methods=["POST"])
def convert():
    # JSから送られてきたJSONデータを受け取る
    data = request.get_json()
    
    # Python側で計算ロジックを実行
    quantity = data["quantity"]
    converted = quantity * 240  # cup -> gram 換算
    
    # 計算結果をJSON形式でJSへ送り返す
    return jsonify({
        "ingredient": data["ingredient"],
        "convertedQuantity": converted
    })