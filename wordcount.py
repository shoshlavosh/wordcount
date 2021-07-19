def word_count(file):
    """ Creates a dictionary that keeps track of the count of each word 
    """

    #open the file
    words_file = open(file)

    #create a new dictionary
    word_count_dict = {}
    
    for line in words_file: 
        #loops over each line in the file
        line = line.rstrip(" ") 
        #removes blank spaces in lines, saves to variable "line"
        line = line.rstrip("?") 
        line = line.rstrip(",")
        line = line.rstrip(".")


        words = line.split(" ")
        #adds a " " between each word and saves to variable "words"

        # print(words)

        #loop over all words in lists and add to dictionary
        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

        for key, value in word_count_dict.items():
            print(f"key = {key}, value = {value}")

    print(word_count_dict)

    #close the file
    words_file.close()

word_count("test.txt")
# word_count("twain.txt")
