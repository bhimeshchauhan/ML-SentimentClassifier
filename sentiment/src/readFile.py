import nltk

class readFile(object):

    def read(self, file):

        """
        Reads txt files passed to the module as file path from the source directory
        :return: List of text broken at '\n' character.
        """

        try:
            with open(file, 'rU') as f:
                fList = f.readlines()
            self.debug(fList)
        except Exception as ex:
            print(ex)



    def debug(self, fileItems):
        """
        For debug to print the statements from the file.
        :return: Items from the read list.
        """
        nltk.download('words')
        english_vocab = set(w.lower() for w in nltk.corpus.words.words())
        for item in fileItems:
            sList = item.strip().split()
            print("old slist ", sList)
            for words in sList:
                if words not in english_vocab:
                    sList.remove(words)
            print(sList)
        print(',' in english_vocab)




if __name__ == "__main__":
    readFile().read('sentiment-neg.txt')