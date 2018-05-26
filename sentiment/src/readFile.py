class readFile(object):

    def read(self, file):

        """
        Reads txt files passed to the module as file path from the source directory
        :return: List of text broken at '\n' character.
        """

        try:
            with open(file, 'rU') as f:
                fList = f.readlines()
        except Exception as ex:
            print(ex)

        self.debug(fList)

    def debug(self, fileItems):
        """
        For debug to print the statements from the file.
        :return: Items from the read list.
        """
        for item in fileItems:
            print(item)




if __name__ == "__main__":
    readFile().read('sentiment-neg.txt')