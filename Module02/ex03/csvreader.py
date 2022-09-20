class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        # self.

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
        except:
            print("No such file or directory: "+self.filename)
        lines = self.file.readlines()
        size = len(lines[self.skip_top].split(self.sep))
        for i in range(self.skip_top, len(lines) - self.skip_bottom):
            line = lines[i].split(self.sep)
            if len(line) != size:
                return None
        self.file.close()
        self.file = open(self.filename, 'r')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
            Return:
                nested list (list(list, list, ...)) representing the data.
        """
        lines = self.file.readlines()
        if len(lines) < self.skip_top + self.skip_bottom:
            return []
        size = len(lines[self.skip_top].split(self.sep))
        data = []
        for i in range(self.skip_top, len(lines) - self.skip_bottom):
            line = lines[i].split(self.sep)
            if len(line) != size:
                return None
            else:
                data.append(line)
        self.file.close()
        self.file = open(self.filename)
        return data

    def getheader(self):
        """ Retrieves the header from csv file.
            Returns:
                list: representing the data (when self.header is True).
                None: (when self.header is False).
        """
        if not self.header:
            return None
        else:
            header = self.file.readline().split(self.sep)
            self.file.close()
            self.file = open(self.filename)
            return header
