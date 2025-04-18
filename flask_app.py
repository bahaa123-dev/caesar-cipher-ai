from flask import Flask, request, jsonify
from caesar_ai import ai_caesar_crack

app = Flask(__name__)


@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()
    encrypted_text = data.get("text", "")
    if not encrypted_text:
        return jsonify({"error": "No text provided"}), 400

    plaintext, shift, score = ai_caesar_crack(encrypted_text)

    return jsonify({
        "decrypted_text": plaintext,
        "detected_shift": shift,
        "score": score
    })


if __name__ == "__main__":
    app.run(debug=True)
