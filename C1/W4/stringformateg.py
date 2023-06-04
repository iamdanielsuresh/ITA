# #ounce convertor

# def convert_weight(ounces):
#     pounds = ounces /16
#     result = "{} ounces equak {:.2f} pounds".format(ounces,pounds)
#     return result
# print(convert_weight(12))

# #username creator

# def username(last_name,birth_year):
#     return("{}{}".format(last_name[0:3],birth_year))
# print(username("Ivanov", "1985"))

#

def replace_date(schedule, old_date, new_date):
    if schedule.endswith(old_date):
        p = len(old_date)
        new_schedule = schedule[:-p] + schedule[:-p].replace(old_date,new_date)
        return new_schedule
    return schedule
print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June")) 
# Should display "The convention is scheduled for June"
    
def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
