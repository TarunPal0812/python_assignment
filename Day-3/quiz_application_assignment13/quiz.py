from question import Question
from exceptions import InvalidAnswerError


class QuizEngine:
    """
    Manages quiz progression, input scoring, and final statistics.
    """

    def __init__(self, questions: list[Question]) -> None:
        self.questions: list[Question] = questions
        self.correct_count: int = 0
        self.wrong_count: int = 0

    @staticmethod
    def get_answer(options_count: int) -> int:
        """Prompt and parse option choice from user input."""
        try:
            answer = int(input(f"Enter your answer (1-{options_count}): "))
            if answer < 1 or answer > options_count:
                raise InvalidAnswerError(f"Answer must be between 1 and {options_count}.")
            return answer
        except ValueError:
            raise InvalidAnswerError("Please enter a valid number.")

    def calculate_score(self) -> float:
        """Calculate percentage score achieved."""
        total = len(self.questions)
        if total == 0:
            return 0.0
        return (self.correct_count / total) * 100.0

    def run(self) -> None:
        """Execute full interactive quiz session."""
        print("===== PYTHON QUIZ APPLICATION =====")

        for q_idx, question in enumerate(self.questions, start=1):
            question.display(q_idx)

            while True:
                try:
                    user_answer = self.get_answer(len(question.options))
                    break
                except InvalidAnswerError as error:
                    print(f"Invalid Answer: {error}")

            if question.is_correct(user_answer):
                print("Correct!")
                self.correct_count += 1
            else:
                print("Wrong!")
                correct_text = question.options[question.correct_answer - 1]
                print(f"Correct answer: {question.correct_answer}. {correct_text}")
                self.wrong_count += 1

        score = self.calculate_score()
        total_questions = len(self.questions)

        print("\n" + "=" * 50)
        print("QUIZ RESULT")
        print("=" * 50)
        print(f"Total Questions: {total_questions}")
        print(f"Correct: {self.correct_count}")
        print(f"Wrong: {self.wrong_count}")
        print(f"Score: {score:.2f}%")
