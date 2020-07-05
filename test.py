import json
from difflib import SequenceMatcher


data = json.load(open("data.json")) #data is loaded from JSON file

#Following function finds similarity check, note we can use get_close_matches() instead.
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


#This function is used to translate word to their respective meaning. :-)
def translate(value):
    value = value.lower()
    value2 = "empty"
    if value in data:
        print(data[value]) #it gives values of the keys
    else :
        for i in data.keys():
            if similar(i,value)>0.8:
                print("did you mean '{}' ? (y/n) ".format(i))
                ask = input();
                if ask == 'y' or ask == "Y":
                    value2 = i
                    print("okay, the meaning for {} is :".format(i))
                    print(data[i])
                    break;
                elif ask == 'n' or ask == 'N':
                    value2 = "anything"
                    print("okay, program is closing because the word doesn't exist.")
                    break;
        if value2 != "empty":
            pass
        else:
            print("The word doesn't exist.")



word = input("Enter word : ")
translate(word)
















# def translate(value):
#     value = value.lower()
#     if value in data:
#         return data[value] #it gives values of the keys :-)
#     else:
#         return "The word doesn't exist."
