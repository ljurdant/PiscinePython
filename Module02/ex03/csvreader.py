class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.lines = None

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
        except:
            print("No such file or directory: "+self.filename)
            return None
        self.lines = self.file.readlines()
        size = len(self.lines[0].split(self.sep))
        for line in self.lines:
            if len(line.split(self.sep)) != size:
                return None
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
            Return:
                nested list (list(list, list, ...)) representing the data.
        """
        if len(self.lines) < self.skip_top + self.skip_bottom:
            return []
        data = []
        for i in range(self.skip_top, len(self.lines) - self.skip_bottom):
            line = self.lines[i].split(self.sep)
            data.append(line)
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
            header = self.lines[0].split(self.sep)
            return header
