
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 👈 Enables CORS for all routes



fee_records = [
    {"student_name": "Riya Sharma", "class": "Grade 5", "pending_amount": 6200, "term": "Term 2", "last_payment_date": "2025-06-10"},
    {"student_name": "Kabir Singh", "class": "Grade 6", "pending_amount": 0, "term": "Term 2", "last_payment_date": "2025-05-28"},
    {"student_name": "Anaya Gupta", "class": "Grade 4", "pending_amount": 1500, "term": "Term 1", "last_payment_date": "2025-04-10"},
    {"student_name": "Devansh Mehta", "class": "Grade 7", "pending_amount": 3000, "term": "Term 1", "last_payment_date": "2025-04-22"},
    {"student_name": "Saanvi Patel", "class": "Grade 3", "pending_amount": 0, "term": "Term 2", "last_payment_date": "2025-06-02"},
    {"student_name": "Arjun Nair", "class": "Grade 8", "pending_amount": 4800, "term": "Term 2", "last_payment_date": "2025-06-05"},
    {"student_name": "Mehak Bhatia", "class": "Grade 9", "pending_amount": 0, "term": "Term 1", "last_payment_date": "2025-04-30"},
    {"student_name": "Yuvraj Chauhan", "class": "Grade 10", "pending_amount": 2000, "term": "Term 2", "last_payment_date": "2025-06-07"},
    {"student_name": "Ishita Verma", "class": "Grade 2", "pending_amount": 1000, "term": "Term 1", "last_payment_date": "2025-03-18"},
    {"student_name": "Veer Kulkarni", "class": "Grade 1", "pending_amount": 500, "term": "Term 1", "last_payment_date": "2025-03-12"}
]

@app.route('/')
def home():
    return "Greenfield Fee Status API is running!"

@app.route('/api/fees/status', methods=['GET'])
def check_fee_status():
    student_name = request.args.get('student_name')
    student_class = request.args.get('class')

    if not student_name or not student_class:
        return jsonify({"error": "Missing student_name or class"}), 400

    for record in fee_records:
        if (
            record["student_name"].lower() == student_name.lower()
            and record["class"].lower() == student_class.lower()
        ):
            return jsonify(record)

    return jsonify({"message": "No record found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
