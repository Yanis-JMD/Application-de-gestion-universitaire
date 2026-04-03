from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    dbname="student_db",
    user="postgres",
    password="YanisBrice2008",
    host="localhost",
    port="5432"
)

# Route test
@app.route('/')
def home():
    return "API is running nicely Yanis!"

# Ajouter matière
@app.route('/subjects', methods=['POST'])
def add_subject():
    try:
        data = request.json
        print("DATA SUBJECT:", data)

        name = data['name']
        coef = data['coef']

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO subjects (name, coef) VALUES (%s, %s)",
            (name, coef)
        )
        conn.commit()
        cur.close()

        return jsonify({"message": "Subject added"})

    except Exception as e:
        print("ERREUR SUBJECT:", e)
        return jsonify({"error": str(e)}), 500

# Ajouter note
@app.route('/grades', methods=['POST'])
def add_grade():
    try:
        data = request.json
        print("DATA GRADE:", data)

        subject_id = data['subject_id']
        grade = data['grade']

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO grades (subject_id, grade) VALUES (%s, %s)",
            (subject_id, grade)
        )
        conn.commit()
        cur.close()

        return jsonify({"message": "Grade added"})

    except Exception as e:
        print("ERREUR GRADE:", e)
        return jsonify({"error": str(e)}), 500

# Calcul moyenne
@app.route('/average', methods=['GET'])
def average():
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT SUM(g.grade * s.coef) / SUM(s.coef)
            FROM grades g
            JOIN subjects s ON g.subject_id = s.id
        """)
        result = cur.fetchone()[0]
        cur.close()

        return jsonify({"average": result})

    except Exception as e:
        print("ERREUR AVERAGE:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
