# file_counts = { "jpg" : 15, "txt" : 12, "mp4": 5, "png" : 11}
# for extentions in file_counts:
#     print(extentions)
# for ext, amount in file_counts.items():
#     print("There are {} files with the .{}".format(amount, ext))

# print(file_counts.keys())
# print(file_counts.values())

#create a function which counts the number of words in a text

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("fuck you tommy "))



