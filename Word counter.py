def count_words(input_text):
    if not input_text:
        return 0
    words = input_text.split()
    return len(words)

//count how many word in the given text.
user_input = input("Enter a text:")
count = count_words(user_input)
print(f"Word count:{count}")



