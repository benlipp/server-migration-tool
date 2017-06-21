import os
from os import listdir


class Parser(object):
    """Parser"""

    def __init__(self, directory):
        super().__init__()
        self._files = []
        self.records = []
        self.directory = os.path.realpath(directory)

    def parse(self):
        self._get_files()
        self._get_records()
        return self.records
        pass

    def _get_files(self):
        self.files = listdir(self.directory)
        pass

    def _get_records(self):
        for filename in self.files:
            filename = os.path.join(self.directory, filename)
            with open(filename, 'r') as file:
                content = file.readlines()
                content = [x.strip() for x in content]
                for line in content:
                    record = self._parse_record(line)
                    if record: self.records.append(record)
                    del record

        pass

    def _parse_record(self):
        #implemented in subclasses
        pass


