#random is used to assign random words when one wouldnt be in the dictionary 
import random 
#we import log to calculate the surprisal 
from collections import defaultdict
# you need to install nltk
import nltk
from nltk import sent_tokenize, word_tokenize

#I decided to create two classes, one for the populating of the dictionary, and the second one for the Autocorrector. 

class Bigram_freq:

    def get_lines(path):
        with open (path,"r") as f:
            df = f.read()
        return df

    def get_bigrams(txt):
        dic = defaultdict(int)
        for sentence in txt:
            
            # we tokenize the text file  that we will pass

            words = word_tokenize(sentence.lower())
            for i in range(len(words)-1):
                
                # we define the bigrams

                bigram = (words[i],words[i+1])
                dic[bigram] += 1
        return dic
    

#the whole class will follow an autocorrector with distance 1, so only one change is allowed per sequence

class Autocorrector:

    def __init__(self, word_list, alpha):
        self.word_list = word_list
        self.alpha = alpha

# the first method is insertion: where we insert a character in every part of the word "ahouse"

    def insertion(self,word,alpha):
        lst = []
        for i in range(len(word)+1):
            for char in self.alpha:
                
                """
                we need to define the new word for each character in our file with the alphabet
                we construct it like: everything until the index i, we add a new character and then we get everything that follows.
                We reconstruct the word like: 
                i[1]
                
                0 1 2 3 4    the first part is h : then add a then : ouse == haouse
                h o u s e       this process is the same for the next mathods, but with different changes. 
                
                """

                clean = word[:i] + char + word[i:]
                lst.append(clean)
        return lst
    
# The second method is deletion, where we delete a character from the word 
    def deletion(self,word):
        lst =[]
        for i in range(len(word)):
            
            """
            we take everything until index, then we skip the index, and append from index onwards: 
            i[1] h (o) use = huse

            """

            clean = word[:i] + word[i+1:]
            lst.append(clean) 
        return lst

# The third method is substitution, here we change one character into another in the alphabet 
    def substitution(self,word,alpha):
        lst =[]
        for i in range(len(word)):
            for char in self.alpha:
                
                """
                We take everything until the index, we add a character that substitutes our i, then we add everything after the i:
                i[1] h (o) a use = hause
                
                """

                clean = word[:i] + char + word[i+1:]
                
                #to skip repeated elements
                
                if char != word[i]:
                    lst.append(clean)
        return lst

# The fourth method is swapping: we change the order of two character of the word 
    def swapping(self,word):
        lst =[]
        for i in range(len(word)-1):
            
            """
            we take everything until the index, then we pick the next one after index, and then the index, finally we take everything following
            i[1] h (o) (u) se = huose
            """

            clean = word[:i] + word[i+1] + word[i] + word[i+2:]
            lst.append(clean)
        return lst

#here we will make a set with all the results ( to skip those repeated) of each method so we have another lexicon for the corrections (although all the options here will not be corrected, and we will need to compare with the lexicon.)
    
    def suggestion(self,word):
        union = (self.insertion(word,self.alpha) +
                self.deletion(word) +
                self.substitution(word,self.alpha) +
                self.swapping(word)
                )
        return set(union)



def main():
    
    # here we pass through our first class the text file, so the program can read the text that we will base our program in 
    corpus = Bigram_freq.get_lines("english.corpus.txt") 
    
    #here we pass our lexicon (the dictionary to check the autocorrected words, so we can have real words)
    lexicon = set(open("lexicon_en.txt").read().split())
    
    #the file alpha.txt passes the alphabet in the 3rd position of our argument in the terminal 
    alphabet = open("alpha.txt").read().split()
    
    #we tokenize our text
    cleaned_lines = sent_tokenize(corpus)
    
    #we get the bigrams on base frequency, which is not the most optimal way.
    bigrams = Bigram_freq.get_bigrams(cleaned_lines)
    
    #to get the list in reversed order and have the dictionary with bigrams and frequency
    sorted_list = sorted(bigrams.items(),key=lambda x: x[1],reverse=True)


    """
    Here is where the interface of our program starts
    """
    
    #we create an empty text, that will contain the sentence that we costruct
    message = []        
    
    #the statement to break the program: we will add the break patter everywhere in the code.  
    print("If you want to end the program, type q")
    
    #we start with a while loop as we need the program to continiously run, until the user wants it to stop
    while True:
        
        #to have a first case, for the first word
        if not message:
            
            # here we introduce the first word

            word = input("Enter a word:")
            
            #the command line to stop the generating of sentences
            
            if word.lower() == "q":
                break
        
        else:
            
            #To get the whole sentence each step
            
            print(f"Your entire message was:"," ".join(message))
            
            # Here we get the suggestion based on the bigrams, to know what is the next word given the previous(the first 0 js needed so we dont get the frequency

            new_word = []
            for bigram in sorted_list:
                if bigram[0][0] == word:
                    option = bigram[0][1]
		
		# we get rid of punctuation and symbols
                    if option.isalpha() and len(option)>1:
                        new_word.append(option)            
           

 # we will check if there are not suggestion available for a word we typed.

            if len(new_word) == 0:
                print(f"There are not suggested words for this option.")
                print(f"Here there are 3 random options.")
                
                # we are generating random options, for all the instances that the words would not have any possible bigram 
                
                no_word = random.sample(list(lexicon), 3)
                for i, w in enumerate(no_word):
                    print(f"{i}: {w}")
                print("or type something else:")
                suggest = input()

                if suggest.lower() == "q":
                    break

                #Here we get in the message depending of the input 

                if suggest.isdigit():
                    word = no_word[int(suggest)]
                    message.append(word)
                    continue
                elif suggest in lexicon:
                    message.append(suggest)
                    word = suggest
                    continue

                # We use the class autocorrector to check for the real words that are inputed 
                
                checker = Autocorrector(lexicon, alphabet).suggestion(suggest)
                corrector = []
                for w in checker:
                    if w in lexicon:
                        corrector.append(w)
                
                # if we only have one suggestion

                if len(corrector) == 1:
                    print(f"Did you mean '{corrector[0]}'? y/n")
                    if input().lower() == "y":
                        word = corrector[0]
                        message.append(word)
                        continue
                    else:
                        continue
                
                # If we have more options we allow the user to chose

                elif len(corrector) > 1:
                    print("Did you mean any of the following?:")
                    for i, w in enumerate(corrector[:3]):
                        print(f"{i}: {w}")
                    print("or type something else:")
                    choice = input().strip()

                    
                    if choice.lower() == "q":
                        break

                    if choice.isdigit():
                        word = corrector[int(choice)]
                        message.append(word)
                        continue
                    elif choice in lexicon:
                        word = choice
                        message.append(word)
                        continue
                    else:
                        continue
                #this is allowing us the code to continue, restarting the code
                continue
                
            # Here we suggest 3 words based on raw frequency of the dictionary 

            print("Either select a word:")

            for i, words in enumerate(new_word[:3]):
                print(f"{i}: {words}")
                
            print(f"or type something else:")
            
            #we store it in this variable 
            answer = input()
            
            if answer.lower() == "q":
                break

            # to get the word for each word based on their i. 
            if answer.isdigit():
                word = new_word[int(answer)]
            
            # to get in case the user wrote a new word
            else:
                word = answer

            if word.lower() == "q": 
                break
        
        # Checking the spelling
        if word not in lexicon:

            # we get the Damerau Levenshtein 1 distance 

            checker =  Autocorrector(lexicon,alphabet).suggestion(word)
            fixer = []
            for w in checker:
                if w in lexicon:
                    fixer.append(w)

            # Here we check if we only have on option for the fixer, to suggest the word that the user may had misspelled
            if len(fixer) == 1:
                print(f"Did you mean '{fixer[0]}'? y/n")
                polar_quest = input().lower()
                if polar_quest == "y":
                    message.append(fixer[0])
                    word = fixer[0]
                    continue
                
                # I decided to leave the user the possibility to save the word they wrote if they want it in the sentence, for flexibility 

                elif polar_quest == "n":
                    print(f"Do you want to keep your word? y/n")
                    second_polar = input().lower()
                    if second_polar == "y":
                        message.append(word)
                        word = word
                        continue
                    else: 
                        pass

                # multiple corrections up to 3
            elif len(fixer) > 1:
                print("Did you mean any of the following?:")
            
                for i, w in enumerate(fixer[:3]):  # Show first three corrections
                    print(f"{i}: {w}")
                print("or type something else:")
                choice = input()

                if choice.isdigit():
                
                    # We choose one out of the 3 options, selecting the number (we need to select the number)
                
                    word = fixer[int(choice)]
                    message.append(word)
                    continue

                elif choice in lexicon:
                    # User typed a valid lexicon word instead
                    word = choice
                    message.append(word)
                    continue

                # fallback option, we take the random options 
        
            print(f"That word is not in the lexicon,")
            print(f"Here are some random suggestions:")
            no_word = random.sample(list(lexicon), 3)
            
            # we present again 3 random options with an index for the user to select, to continue the sentence formation 

            for i, words in enumerate(no_word[:3]):
                print(f"{i}: {words}")
            print(f"or type something else:")
            suggest = input()

            if suggest.lower() == "q":
                break

            if suggest.isdigit():
                message.append(no_word[int(suggest)])
                word = no_word[int(suggest)]
                continue
            elif suggest in lexicon:
                message.append(suggest)
                word = suggest
                continue
            else:
                continue

        if word.lower() != "q":
            message.append(word)

    # we give the entire sentence when we quit the program 

    print(f"Your final sentence is:", " ".join(message))

if __name__ == "__main__":
    main()

