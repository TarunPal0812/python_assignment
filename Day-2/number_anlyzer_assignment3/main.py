# 3. Number Analyzer 
# Create functions: 
# is_prime() 
# is_even() 
# is_odd() 
# get_factors() 
# get_prime_factors() 
# Given a number: 
# Enter number: 84 
# Output: 
# Even: Yes 
# Prime: No 
# Factors: [1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84] 
# Prime Factors: [2, 3, 7] 
# Handle 
# ● Negative numbers 
# ● Zero 
# ● One 
# ● Invalid input 

from utils import is_even,get_factors,get_prime_factors,is_prime


def main() -> None:
    """
    Read a number and display its analysis.
    """

    try:
        number = int(input("Enter number: "))

     
        if number < 0:
            number = abs(number)
            print("Negative number converted to:", number)

  
        if number == 0:
            print("Even: Yes")
            print("Prime: No")
            print("Factors: Not defined")
            print("Prime Factors: Not defined")

  
        elif number == 1:
            print("Even: No")
            print("Prime: No")
            print("Factors: [1]")
            print("Prime Factors: []")

        else:
            print("Even:", "Yes" if is_even(number) else "No")
            print("Prime:", "Yes" if is_prime(number) else "No")
            print("Factors:", get_factors(number))
            print("Prime Factors:", get_prime_factors(number))

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