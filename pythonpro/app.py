from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)

# Define Question model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255))
    option1 = db.Column(db.String(255))
    option2 = db.Column(db.String(255))
    option3 = db.Column(db.String(255))
    option4 = db.Column(db.String(255))
    correct_answer = db.Column(db.String(255))
    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'option1': self.option1,
            'option2': self.option2,
            'option3': self.option3,
            'option4': self.option4,
            'correct_answer': self.correct_answer
        }
    def __repr__(self):
        return f"<Question {self.id}>"

# Create the questions table within application context
with app.app_context():
    db.create_all()

    # Add a new question if it doesn't exist
    new_questions = [
        {
            "question": "Python'da yapay zeka geliştirmek için hangi kütüphaneleri kullanabilirsiniz? (5 puan)",
            "option1": "A. TensorFlow, PyTorch, scikit-learn",
            "option2": "B. NumPy, Pandas, Matplotlib",
            "option3": "C. OpenCV, Pillow, Pygame",
            "option4": "D. Her ikisi de A ve C",
            "correct_answer": "D"
        },
        {
            "question": "Görüntü sınıflandırma problemlerini çözmek için hangi algoritmaları kullanabilirsiniz? (5 puan)",
            "option1": "A. K-Nearest Neighbors (KNN)",
            "option2": "B. Destek Vektör Makineleri (SVM)",
            "option3": "C. Yapay Sinir Ağları (ANN)",
            "option4": "D. Hepsi A, B ve C",
            "correct_answer": "D"
        },
        {
            "question": "Metinlerde duygu analizi yapmak için hangi teknikleri kullanabilirsiniz? (5 puan)",
            "option1": "A. Kelime Gömme",
            "option2": "B. Bag-of-Words (BoW)",
            "option3": "C. N-gram",
            "option4": "D. Hepsi A, B ve C",
            "correct_answer": "D"
        },
        {
            "question": "Bir yapay zeka modelini bir Python uygulamasına nasıl entegre edersiniz? (5 puan)",
            "option1": "A. Modelin kütüphanesini yükleyin ve modeli oluşturun.",
            "option2": "B. Modeli eğitilmiş verilerle eğitin.",
            "option3": "C. Modeli yeni veriler üzerinde tahmin yapmak için kullanın.",
            "option4": "D. Hepsi A, B ve C",
            "correct_answer": "D"
        }
    ]

    for question_data in new_questions:
        new_question = Question.query.filter_by(question=question_data["question"]).first()
        if new_question is None:
            new_question = Question(
                question=question_data["question"],
                option1=question_data["option1"],
                option2=question_data["option2"],
                option3=question_data["option3"],
                option4=question_data["option4"],
                correct_answer=question_data["correct_answer"]
            )
            db.session.add(new_question)
            db.session.commit()

# Add a route to display questions
# Flask uygulamanızdaki index route'unun içinde
@app.route('/')
def index():
    questions = Question.query.all()
    questions_json = [question.to_dict() for question in questions]  # Question nesnelerini JSON uyumlu hale getir
    return render_template('index.html', questions=questions_json)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
