class Question:
    """
    Represents an individual multiple-choice question in a quiz.
    """

    def __init__(self, prompt: str, options: list[str], correct_answer: int) -> None:
        if not prompt or not prompt.strip():
            raise ValueError("Question prompt cannot be empty.")
        if not options or len(options) < 2:
            raise ValueError("Question must have at least 2 options.")
        if correct_answer < 1 or correct_answer > len(options):
            raise ValueError(f"Correct answer index must be between 1 and {len(options)}.")

        self.prompt: str = prompt.strip()
        self.options: list[str] = [opt.strip() for opt in options]
        self.correct_answer: int = correct_answer

    def is_correct(self, user_choice: int) -> bool:
        """Check if user choice matches correct option index."""
        return user_choice == self.correct_answer

    def display(self, question_number: int) -> None:
        """Print question prompt and numbered options list."""
        print("\n" + "=" * 50)
        print(f"Question {question_number}: {self.prompt}")
        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")


DEFAULT_QUESTIONS = [
    Question("What is Python?", ["Language", "Database", "OS", "Browser"], 1),
    Question("Which keyword is used to define a function?", ["func", "define", "def", "function"], 3),
    Question("Which data type is mutable?", ["Tuple", "String", "List", "Integer"], 3),
    Question("What is the output type of input()?", ["int", "str", "float", "bool"], 2),
    Question("Which symbol is used for comments?", ["//", "#", "/*", "--"], 2),
]
