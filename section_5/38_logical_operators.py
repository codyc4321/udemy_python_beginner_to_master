def is_valid_grade():
    grade = float(input("What was your grade? "))
    valid = grade >= 0 and grade <= 100
    if valid:
        print(f"{grade} is a valid grade")
    else:
        print(f"{grade} is not a valid grade")


def male_or_female():
    response = input("Are you male or female? ")
    lowercase_input = response.lower()
    if lowercase_input in ["m","male", "man", "guy", "dude"]:
        print("You are male")
    elif lowercase_input in ["f", "female", "woman", "gal", "lady", "madam"]:
        print("You are female")
    else:
        print("Hmm not sure what your gender is, please try again.")
        male_or_female()


def is_valid_age_to_work():
    age = int(input("What is your age? "))
    if age >= 18 and age <= 60
        print(f"{age} is a valid age to work")
    else:
        print(f"{age} is not a valid age to work")


if __name__ == "__main__":
    is_valid_grade()
    male_or_female()
    is_valid_age_to_work()