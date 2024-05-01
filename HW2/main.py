# students = []
#
# def add_student(name, surname, age, grade):
#     student = {"Name": name, "Surname": surname, "Age": age, "Grade": grade}
#     students.append(student)
#
# def show_all():
#     for student in students:
#         print('Name:', student["Name"], ' Surname:', student["Surname"], ' Age:', student["Age"], ' Grades:', student["Grade"])
#
# def show_avg_grade():
#     for student in students:
#         avg = sum(student["Grade"]) / len(student["Grade"])
#         print (student["Name"], student["Surname"], avg)
#
# def delete_student(surname):
#     for student in students:
#         if student["Surname"] == surname:
#             students.remove(student)
#
#
# add_student("Smart","Fella",18,[5,5,5,5,5])
# add_student("Sorry","Smella",15,[1,3,2,1,3])
#
# show_all()
#
# show_avg_grade()
#
# def more_than_4():
#  return [student for student in students if sum(student["Grade"]) / len(student["Grade"]) > 4]

text = 'please generate a text with at least 100 words and assign to the variable and perform the following analysis: Count the occurrences of each word in the text. Create a set of unique words in the text. Create a list containing the lengths of each word in the text. Generate a list of words with a length greater than 5 characters. Calculate the average word length in the text. Display the results of the analysis. There was only 75 words, so I had to add something to accomplish a goal of getting at least one hundred. These are the last.'


def text_work():
    # I know about .split() method, but wasn`t sure if it is allowed
    words = []
    word = ''
    for x in text:
        if x != ' ' and x != '.' and x != ',' and x != ':' and x != ';' and x != '!' and x != '?':
            word += x
        else:
            words.append(word)
            word = ''

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    unique_words = [word for word, count in word_counts.items() if count == 1]

    word_lengths = [len(word) for word in words]

    long_words = [word for word in words if len(word) > 5]

    average_word_length = sum(word_lengths) / len(word_lengths)

    print("Word Counts:", word_counts)
    print("Unique Words:", unique_words)
    print("Word Lengths:", word_lengths)
    print("Long Words:", long_words)
    print("Average Word Length:", average_word_length)
    print("Total Words:", len(words))


text_work()
