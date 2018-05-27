import re

class readFile(object):

    def read(self, file):
        """
        Reads txt files passed to the module as file path from the source directory
        :return: List of text broken at '\n' character.
        """
        try:
            with open(file, 'rU') as f:
                fList = f.readlines()
            self.tokenization(self, fList)
        except Exception as ex:
            print(ex)

    @staticmethod
    def tokenization(self, fileItems):
        """
        For debug to print the statements from the file.
        :return: Items from the read list.
        """
        cleanList = []
        for item in fileItems:
            cleanList.append(re.sub(r'[^a-zA-Z ]', '', str(item)).split())

        for item in cleanList:
            print(item)
            print(list(set(item)))


if __name__ == "__main__":
    readFile().read('sentiment-pos.txt')