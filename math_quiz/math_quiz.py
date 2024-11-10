import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Randomly choose one of the mathematical operators: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def calculate_expression(n1, n2, operator):
    """
    Calculate the result of applying the operator to the two numbers.
    """
    expression = f"{n1} {operator} {n2}"

    # Perform calculation based on operator
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    else:
        result = None  # In case of an invalid operator

    return expression, result

def math_quiz():
    score = 0
    total_questions = 5  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.\n")

    for _ in range(total_questions):
        # Generate two random integers and an operator for the math problem
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        # Generate the problem and its correct answer
        problem, correct_answer = calculate_expression(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        
        try:
            # Get user input and check for validity
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue  # Skip this question and move to the next

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()