from analyzer import NumberAnalyzer


def main() -> None:
    try:
        raw_input = input("Enter number: ")
        val = int(raw_input)
        analyzer = NumberAnalyzer(val)
        analyzer.display_analysis()
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()

# Output
# Enter number: 10
# Even: Yes
# Prime: No
# Factors: [1, 2, 5, 10]
# Prime Factors: [2, 5]
