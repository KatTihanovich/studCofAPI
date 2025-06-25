from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Загружаем данные
df = pd.read_csv("prepared_drinks.csv")

@app.route("/drink", methods=["GET"])
def get_drink():
    query = request.args.get("name", "").lower()
    if not query:
        return jsonify({"error": "Missing name parameter"}), 400

    result = df[df["name"].str.lower().str.contains(query)]

    if result.empty:
        return jsonify({"error": "Drink not found"}), 404

    return jsonify(result.to_dict(orient="records"))  # <== список

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
