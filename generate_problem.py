
#problem definition:
" I'm given a data set of 1000 lists of up to 50 strings. 
My job is to make a list of each pair of strings that are mentioned 
together in at least 50 lists."

list_of_lists = []

words = []
with open("word_list.txt","r") as f:
    for i in f:
        i = i.replace("\n","")
        words.append(i)

