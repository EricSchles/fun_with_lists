import random


#problem definition:
""" I'm given a data set of 1000 lists of up to 50 strings. 
My job is to make a list of each pair of strings that are mentioned 
together in at least 50 lists."""

def list_gen():
    list_of_lists = []

    words = []
    with open("word_list.txt","r") as f:
        for i in f:
            i = i.replace("\n","")
            words.append(i)

    words = words[:100]
    for i in xrange(1000):
        tmp = []
        length = random.randint(0,50)
        for j in xrange(length):
            tmp.append(words[random.randint(0,len(words)-1)])
        list_of_lists.append(tmp)
    
    return list_of_lists 
                   
