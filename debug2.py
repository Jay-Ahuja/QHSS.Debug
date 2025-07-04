# debug2.py

# This script should extract and print the third word from a sentence provided by the user.
# If the sentence has fewer than three words, it should display an error message.

# Extract the third word from a given sentence.
def get_third_word(sentence)
    words = sentence.split(" ")
    if words < 3:
        return Error: Sentence has less than 3 words.
    return words[3]

# Main function to get input and display output.
def main()
    print("This tool extracts the third word from your sentence.")
    sentence = input("Enter a sentence: ")
    word = getThirdWord(sentence)
    print("Third word is:", word)

main()
