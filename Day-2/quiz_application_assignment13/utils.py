from question import Question,questions
from exception import InvalidAnswerError

def display_question(
    question_data: Question,
    question_number: int
) -> None:
    """
    Display a quiz question and its options.

    Args:
        question_data: Dictionary containing the question,
            options, and correct answer.
        question_number: Position of the current question.

    Returns:
        None.
    """

    print("\n" + "=" * 50)

    print(
        f"Question {question_number}: "
        f"{question_data['question']}"
    )

    options: list[str] = question_data["options"]

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


def get_answer() -> int:
    """
    Get a valid answer from the user.

    The answer must be a number between 1 and 4.

    Returns:
        A valid answer as an integer.

    Raises:
        InvalidAnswerError: If the entered value is invalid.
    """

    try:
        answer: int = int(
            input("Enter your answer (1-4): ")
        )

        if answer < 1 or answer > 4:
            raise InvalidAnswerError(
                "Answer must be between 1 and 4."
            )

        return answer

    except ValueError:
        raise InvalidAnswerError(
            "Please enter a valid number."
        )


def check_answer(
    user_answer: int,
    correct_answer: int
) -> bool:
    """
    Check whether the user's answer is correct.

    Args:
        user_answer: Answer selected by the user.
        correct_answer: Correct answer number.

    Returns:
        True if the answer is correct, otherwise False.
    """

    return user_answer == correct_answer


def calculate_score(
    correct_answers: int,
    total_questions: int
) -> float:
    """
    Calculate the quiz score percentage.

    Args:
        correct_answers: Number of correct answers.
        total_questions: Total number of questions.

    Returns:
        Quiz score as a percentage.
    """

    if total_questions == 0:
        return 0.0

    return (
        correct_answers / total_questions
    ) * 100


def run_quiz() -> None:
    """
    Run the complete quiz application.

    Displays questions, accepts answers, checks answers,
    and shows the final quiz result.

    Returns:
        None.
    """

    correct_count: int = 0
    wrong_count: int = 0

    total_questions: int = len(questions)

    print("===== PYTHON QUIZ APPLICATION =====")

    for question_number, question_data in enumerate(
        questions,
        start=1
    ):

        display_question(
            question_data,
            question_number
        )

        while True:

            try:
                user_answer: int = get_answer()
                break

            except InvalidAnswerError as error:
                print(f"Invalid Answer: {error}")

        correct_answer: int = question_data["answer"]

        is_correct: bool = check_answer(
            user_answer,
            correct_answer
        )

        if is_correct:

            print("Correct!")

            correct_count += 1

        else:

            print("Wrong!")

            options: list[str] = (
                question_data["options"]
            )

            print(
                f"Correct answer: "
                f"{correct_answer}. "
                f"{options[correct_answer - 1]}"
            )

            wrong_count += 1

    score: float = calculate_score(
        correct_count,
        total_questions
    )

    print("\n" + "=" * 50)
    print("QUIZ RESULT")
    print("=" * 50)

    print(f"Total Questions: {total_questions}")
    print(f"Correct: {correct_count}")
    print(f"Wrong: {wrong_count}")
    print(f"Score: {score:.2f}%")

