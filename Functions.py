import os


# Word Histogram extracting function from a specified text - returns a list od dict
def word_histogram(org_str):
    
    org_str = org_str.lower()
    irrelevant_word = ["\n", ".", ",", "? ", "! ", " the ", " a ", " for ", "by ", "and ", " to ", " in ",
                       " with ", " is ", " of ", " this ", " very ", " our ", " was ", " all ", " must ", " so ",
                       " no ", " his ", " at ", " on ", " was ", " were ", " his ", " her ", " him ", " its ",
                       " new ", " be ", " had ", " he ", " that ", " it ", " from ", " you ", " as ", " have ",
                       " been ", " would ", " who ", " about ", " has ", " then ", " an ", " i ", " my ", " just ",
                       " not ", " mr ", " up ", " better ", " us ", " she ", " they ", " are ", " could ", " also ",
                       " after", " not ", " will ", " than ", " -- ", " when ", " said ", " want ", " told ",
                       " but ", " - ", " more ", " if ", " which ", " there ", " we ", " or ", " can ", " – ",
                       " u ", " s ", " their ", " most ", " le ", " every ", " one ", " didn't ", " such ", " _ ",
                       " i’m ", " it's ", " 000 ", " what ", " 2016 ", " should ", " — ", " please "]
    for irr_word in irrelevant_word:
        org_str = org_str.replace(irr_word, " ")

    word_list = org_str.split(" ")

    word_hist = {}
    for word in word_list:
        if word not in word_hist.keys():
            word_hist[word] = 1
        else:
            word_hist[word] = word_hist[word] + 1

    word_hist.pop("")
    return word_hist


def read_folder_files():

    title = []
    data = []
    
    data_folder = os.path.join(os.getcwd(), 'articles')

    for root, folder, files in os.walk(data_folder):
        for file in files:
            path = os.path.join(root, file)
            with open(path, 'r', errors='ignore') as inf:
                title.append(inf.readline())
                data.append(inf.read())
                inf.close()

    return title, data


# Extracting n max elements in a dictionary - returns a dict
def max_elements(dict1, n):

    sorted_dict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    max_dict = dict(sorted_dict[0:n+1])

    return max_dict