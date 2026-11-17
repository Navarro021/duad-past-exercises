
def count_letters(text):
    upper_count = 0
    lower_count = 0

    for letter in text:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1

    print(f"There's {upper_count} upper cases and {lower_count} lower cases")


count_letters("I love Nación Sushi")
