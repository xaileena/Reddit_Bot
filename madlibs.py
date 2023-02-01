#Name : Aileena Xie
#Student ID : 261050876

import random
import pickle

def capitalize_sentences(sequenced_str):
    '''(str) -> str
    Returns sequenced_str with the first letter of each sentence capitalized
    A sentence ends with a period, exclamation point or question mark, each followed by a space
    
    >>> capitalize_sentences("hello. hello! hello???? HI!")
    'Hello. Hello! Hello???? HI!'
    
    >>> capitalize_sentences(".hey! hru? LOL,")
    '.hey! Hru? LOL,'
    
    >>> capitalize_sentences("hahaha! ! !")
    'Hahaha! ! !'
    
    >>> capitalize_sentences("? ? what's wrong? ?")
    '? ? What's wrong? ?'
    
    '''
    
    punctuation = ['.', '?', '!']
    cap_str = sequenced_str[0].upper()  #If the first character is a letter, it needs to be capitalized
    
    
    for index in range(1, len(sequenced_str)):
        
        if sequenced_str[index-1] == ' ' and sequenced_str[index-2] in punctuation:
            cap_str += sequenced_str[index].upper()
        
        else:
            cap_str += sequenced_str[index]
    
    return cap_str




def capitalize_sentence_grid(grid):
    '''(list) -> list
    Returns nested_list with the first letter of the first word of
    each new sentence capitalized
    
    >>> grid = [["you", "might", "think"], ["these", "are", "separate", "sentences"], ["but", "they", "are", "not!", "ok,", "this"], ["one", "is."]]
    >>> capitalize_sentence_grid(grid)
    [['You', 'might', 'think'], ['these', 'are', 'separate', 'sentences'], ['but', 'they', 'are', 'not!', 'Ok,', 'this'], ['one', 'is.']]
    
    
    >>> grid = [["this", "roadtrip", "is"], ["boring!", "when", "will", "we"], ["arrive?!"], ["please", "tell", "me."]]
    >>> capitalize_sentence_grid(grid)
    [["This", "roadtrip", "is"], ["boring!", "When", "will", "we"], ["arrive?!"], ["Please", "tell", "me."]]
    
    >>> grid = [["ugh."], ["spiders", "really", "give"], ["me", "the", "creeps!", "i"], ["wish", "we", "lived", "somewhere", "else."]]
    >>> capitalize_sentence_grid(grid)
    [["Ugh."], ["Spiders", "really", "give"], ["me", "the", "creeps!", "I"], ["wish", "we", "lived", "somewhere", "else."]]
    
    '''
        
    copy_grid = grid[:]  
    
    temp_list = []      #I will merge all sublists together to get one list
    
    for sublist in copy_grid:
        for i in range(len(sublist)):
            
            if i <= len(sublist) - 2:  
                temp_list.append(sublist[i])
            
            else:
                temp_list.append(sublist[i])
                temp_list.append(1)     #Appending 1 as an indicator for where the sublist is supposed to end
                                        # if the index, i <= len(sublist)-2 we will not append 1 because we are not
                                        # at the end of the last sublist
        
    
    cap_string = temp_list[0][0].upper() + temp_list[0][1:]    #We want to capitalize the first letter of the first sublist
    temp_list[0] = cap_string
    
    for j in range(len(temp_list)):
        
        if type(temp_list[j]) == int:  #we will skip our indicator 
            continue
        
        if '?' in temp_list[j] or '!' in temp_list[j] or '.' in temp_list[j]:
            
            if j < len(temp_list) - 2:   #If the punctuation is at the last element of the last sublist, we do not need to capitalize
                
                if type(temp_list[j+1]) == int:
                    cap_string =  temp_list[j+2][0].upper() + temp_list[j+2][1:]    #This covers the case in the second example in the docstring
                    temp_list[j+2] = cap_string                                     #["arrive?!"] contains only one element in the sublist
                                                                                    #when we merge and add the indicator, we will have 1, "arrive?!', 1
                                                                                    #we need to append the index after "arrive?!" and 1
                else:
                    cap_string =  temp_list[j+1][0].upper() + temp_list[j+1][1:]
                    temp_list[j+1] = cap_string
    
    
    copy_grid = []   #Now we empty the copy_grid to fill it with the original sublists now capitalized
    mark = 0         #our mark to know where the indicator is (and to not include it in copy_grid)

    for l in range(len(temp_list)):
        if type(temp_list[l]) == int:
            copy_grid.append(temp_list[mark:l])
            mark = l + 1 #+1 to skip the int
           
    
    return copy_grid




def fill_in_madlib(madlib_str, words):
    '''(str) -> dict
    Returns filled in madlib_str from words in words (dictionary)
    Madlib string contains one or more annotated blank spaces
    
    >>> random.seed(9004)
    >>> d = {'COLOR': ['yellow', 'glowing green', 'red'], 'VEHICLE': ['hoverboard', 'sportscar', 'electric bike', 'starship']}
    >>> fill_in_madlib("Wow! Is that a [COLOR] [VEHICLE]?", d)
    'Wow! Is that a glowing green starship?'
    
    >>> random.seed(104)
    >>> d = {'VIDEO-GAME': ['stardew valley', 'elden Ring', 'league of legends'], 'PLAYER-ID': ['shark12', 'fobfan1', 'awesome_one', 'catperson323'], \
    'PLAYER-MODE': ['multiplayer', 'singleplayer']}
    >>> fill_in_madlib("Are you playing [VIDEO-GAME]? Is it a [PLAYER-MODE] game? Can you add me? [PLAYER-ID_1] is my player ID. \
    Is your player ID [PLAYER-ID_2]?", d)
    Are you playing stardew valley? Is it a multiplayer game? Can you add me? Fobfan1 is my player ID. Is your player ID catperson323?
    
    >>> random.seed(202)
    >>> d = {'COLOR': ['orange', 'white', 'black', 'purple', 'blue', 'yellow', 'brown', 'red']}
    >>> fill_in_madlib("whoa! you have a [COLOR_1] cat and a [COLOR_1] dog? I have a [COLOR_2] bird at home.", d)
    Whoa! You have a cat and a dog? I have a bird at home.
    
    >>> d =  >>> d = { COLOR: ['orange', 'white', 'black', 'purple', 12, 'yellow', 'brown', 'red']}
    >>> fill_in_madlib("whoa! you have a [COLOR_1] cat and a [COLOR_1] dog? I have a [COLOR_2] bird at home.")
    Traceback (most recent call last):
    AssertionError: Dictionary must contain valid words only.
    '''

    filled_str = ''
    dictionary = {}
    word_choice = ''
    my_list = madlib_str.split()
    
    for word in words:
        if type(word)!=str:
            raise AssertionError('Dictionary must contain valid words only.')
        
        for element in words[word]:
            if type(element)!=str:
                raise AssertionError('Dictionary must contain valid words only.')
    
    if len(words) == 0:
        raise AssertionError('Dictionary is empty.')
    
    if len(madlib_str) == 0:
        raise AssertionError('Madlib string is empty.')
    
    
    for word in my_list:
        
        brackets = word.find(']')
        if '[' in word:
            
            if '_' in word:
                
                underscore = word.find('_')
                annotation = word[1:underscore]     #instead of ['COLOR_1'] for example, annotation = 'COLOR'
                
                if annotation not in words:
                    raise AssertionError('Dictionary does not contain an option for this.')
                
                if word[-1]!=brackets: #Could be the case if we had something like ['COLOR_1']???
                    dictionary_key = word[0:brackets+1]
                
                else:
                    dictionary_key = word
                
            
            else:
                annotation = word[1:brackets]
                if annotation not in words:
                    raise AssertionError('Dictionary does not contain an option for this.')
                
                if word[-1]!=brackets: 
                    dictionary_key = word[0:brackets+1]
                
                else:
                    dictionary_key = word
                
                
            word_choice = random.choice(words.get(annotation))
                
            if dictionary_key not in dictionary:   #dictionary is used to keep track of the random options available
                
                for element in dictionary:   
                    if dictionary[element] == word_choice:
                        while dictionary[element] == word_choice:    #if value does exist, keep generating random word_choice
                            word_choice = random.choice(words.get(annotation))
          
                dictionary[dictionary_key] = word_choice    #append to the dictionary if we have a new entry
              
              
            else:
                word_choice = dictionary[dictionary_key]   #if the entry exists, refer to the value associated to the key in dictionary
            
            
            if word[-1]!=brackets:
                filled_str += word_choice + word[brackets+1:] + ' '
                          
            else:
                filled_str += word_choice + ' '
            
       
        else:
            filled_str += word + ' '
    

    
    return(capitalize_sentences(filled_str))




def load_and_process_madlib(madlib_filename):
    '''(str) -> None
    Returns nothing
    Reads the madlib string and the dictionary from word_dict.pkl
    and fills in madlib string and saves it back to a new file
    The new file's name would be malib_filename_filled
    
    >>> random.seed(900)
    >>> load_and_process_madlib('madlib1.txt')
    >>> f = open('madlib1_filled.txt', 'r')
    >>> s = f.read()
    >>> s
    'I want Alex Thonny to be our next President!! They are more nice than Boole Ian, and I think they will do a better job!'
    
    >>> random.seed(900)
    >>> load_and_process_madlib('madlib2.txt')
    >>> f = open('madlib2_filled.txt', 'r')
    >>> s = f.read()
    >>> s
    "Hopefully, Alex Thonny will be our next president. (That's not because I secretly have a crush on them
    or anything). Anyway, please vote for Alex Thonny! And Alex Thonny, if you see this, please reply to me."
    
    >>> random.seed(900)
    >>> load_and_process_madlib('madlib10.txt')
    >>> f = open('madlib10_filled.txt', 'r')
    >>> s = f.read()
    >>> s
    'I saw Alex Thonny using plastic water bottles. That means they supposed climate change!
    #Cancel Alex Thonny '
    
    '''
    
    f = open("word_dict.pkl", "rb")
    saved_obj = pickle.load(f)
    f.close()
    
    fobj = open(madlib_filename, "r")
    madlib_str = fobj.read()          
        
    fobj.close()
    
    new_filename = madlib_filename[0:-4] + '_filled' + '.txt'    #madlib_filename[0:-4] excludes the .txt
    fobj1 = open(new_filename, "w")
    fobj1.write(fill_in_madlib(madlib_str, saved_obj))
        
    fobj1.close()



def generate_comment():
    '''(NoneType) -> str
    Chooses a random number k between 1 and 10
    Reads the madlib string contained in the file at madlibk.txt
    Fills in the madlib string using the word dictionary from word_dict.pkl
    Returns string that was saved to file madlibk_filled.txt
    '''
    
    number = random.randint(1, 10)
    
    madlib_filename = 'madlib' + str(number) + '.txt'
    load_and_process_madlib(madlib_filename)
    
    filename = 'madlib' + str(number) + '_filled' + '.txt'
    fobj = open(filename, 'r')
    
    s = fobj.read()
    
    return s
    fobj.close()
    