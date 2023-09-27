def check_text(number):
    shortest_word = ""
    longest_word = ""
    total_length = 0

    words = []
    longest_words = []
    shortest_words = []

    for i in range(1, number + 1):
        word = input(f"Word #{i} please > ")
        words.append(word)
        total_length += len(word)

        if not shortest_words or len(word) < len(shortest_words[0]):
            shortest_words = [word]
        elif len(word) == len(shortest_words[0]):
            shortest_words.append(word)

        if not longest_words or len(word) > len(longest_words[0]):
            longest_words = [word]
        elif len(word) == len(longest_words[0]):
            longest_words.append(word)

    
    return shortest_words[-1], longest_words[-1], total_length / len(words) 

while True:
    number = int(input("How many words will you enter? > "))

    if 3 <= number <= 6:
        analysis = check_text(number)
        print("Shortest: {}\n"
              "Longest: {}\n"
              "Average Length: {:.2f}".format(analysis[0], analysis[1], analysis[2]))
        break
    else:
        print("Invalid input. Please enter a number between 3 and 6")
        continue
