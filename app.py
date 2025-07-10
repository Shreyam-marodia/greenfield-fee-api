from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

students = [
    {
        "admission_number": "1001",
        "name": "Aarav Sharma",
        "class": "Grade 10",
        "pending_amount": 1500,
        "term": "Term 2",
        "last_payment_date": "2024-07-01"
    },
    {
        "admission_number": "1002",
        "name": "Diya Mehra",
        "class": "Grade 9",
        "pending_amount": 0,
        "term": "Term 2",
        "last_payment_date": "2024-05-22"
    },
    {
        "admission_number": "1003",
        "name": "Rohan Patel",
        "class": "Grade 8",
        "pending_amount": 500,
        "term": "Term 1",
        "last_payment_date": "2024-06-10"
    },
    {
        "admission_number": "1004",
        "name": "Mehak Bansal",
        "class": "Grade 10",
        "pending_amount": 0,
        "term": "Term 2",
        "last_payment_date": "2024-05-20"
    },
    {
        "admission_number": "1005",
        "name": "Kabir Arora",
        "class": "Grade 7",
        "pending_amount": 800,
        "term": "Term 2",
        "last_payment_date": "2024-06-30"
    },
    {
        "admission_number": "1006",
        "name": "Simran Kaur",
        "class": "Grade 9",
        "pending_amount": 2000,
        "term": "Term 3",
        "last_payment_date": "2024-06-28"
    },
    {
        "admission_number": "1007",
        "name": "Ishaan Verma",
        "class": "Grade 6",
        "pending_amount": 0,
        "term": "Term 1",
        "last_payment_date": "2024-05-10"
    },
    {
        "admission_number": "1008",
        "name": "Ananya Gupta",
        "class": "Grade 8",
        "pending_amount": 1300,
        "term": "Term 2",
        "last_payment_date": "2024-07-02"
    },
    {
        "admission_number": "1009",
        "name": "Yuvraj Chauhan",
        "class": "Grade 10",
        "pending_amount": 0,
        "term": "Term 2",
        "last_payment_date": "2024-06-15"
    },
    {
        "admission_number": "1010",
        "name": "Kriti Joshi",
        "class": "Grade 7",
        "pending_amount": 600,
        "term": "Term 1",
        "last_payment_date": "2024-06-17"
    },
    {
        "admission_number": "1011",
        "name": "Veer Singh",
        "class": "Grade 9",
        "pending_amount": 900,
        "term": "Term 2",
        "last_payment_date": "2024-07-03"
    },
    {
        "admission_number": "1012",
        "name": "Aanya Bhatt",
        "class": "Grade 8",
        "pending_amount": 0,
        "term": "Term 3",
        "last_payment_date": "2024-07-01"
    },
    {
        "admission_number": "1013",
        "name": "Aryan Malhotra",
        "class": "Grade 6",
        "pending_amount": 500,
        "term": "Term 2",
        "last_payment_date": "2024-06-29"
    },
    {
        "admission_number": "1014",
        "name": "Tanya Reddy",
        "class": "Grade 10",
        "pending_amount": 0,
        "term": "Term 1",
        "last_payment_date": "2024-05-25"
    },
    {
        "admission_number": "1015",
        "name": "Dev Mehra",
        "class": "Grade 9",
        "pending_amount": 1100,
        "term": "Term 3",
        "last_payment_date": "2024-07-05"
    },
    {
        "admission_number": "1016",
        "name": "Riya Singh",
        "class": "Grade 7",
        "pending_amount": 0,
        "term": "Term 2",
        "last_payment_date": "2024-06-10"
    },
    {
        "admission_number": "1017",
        "name": "Harsh Desai",
        "class": "Grade 8",
        "pending_amount": 1200,
        "term": "Term 2",
        "last_payment_date": "2024-06-27"
    },
    {
        "admission_number": "1018",
        "name": "Sneha Kapoor",
        "class": "Grade 6",
        "pending_amount": 0,
        "term": "Term 3",
        "last_payment_date": "2024-07-02"
    },
    {
        "admission_number": "1019",
        "name": "Manav Ghosh",
        "class": "Grade 9",
        "pending_amount": 700,
        "term": "Term 2",
        "last_payment_date": "2024-06-21"
    },
    {
        "admission_number": "1020",
        "name": "Priya Iyer",
        "class": "Grade 10",
        "pending_amount": 0,
        "term": "Term 3",
        "last_payment_date": "2024-06-18"
    }
]

@app.route("/")
def home():
    return "Greenfield Public School Fee API is live."

@app.route("/api/fees/status", methods=["GET"])
def get_fee_status():
    admission_number = request.args.get("admission_number")
    
    if not admission_number:
        return jsonify({"error": "Admission number is required."}), 400
    
    for student in students:
        if student["admission_number"] == admission_number:
            return jsonify(student)
    
    return jsonify({"message": "No record found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
