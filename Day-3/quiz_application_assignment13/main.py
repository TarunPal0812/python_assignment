from question import DEFAULT_QUESTIONS
from quiz import QuizEngine

if __name__ == "__main__":
    quiz_engine = QuizEngine(DEFAULT_QUESTIONS)
    quiz_engine.run()
