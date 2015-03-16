from collections import defaultdict
import csv

class NameDenormalizer(object):
    def __init__(self, filename=None):
        filename = filename or 'names1.2.csv'
        print self.filename
        lookup = collections.defaultdict(list)
        with open(filename) as f:
            try:
                reader = csv.reader(f)
                for line in reader:
                    matches = set(line)
                    for match in matches:
                        lookup[match].append(matches)
                        print match
                        print lookup[match]
                self.lookup = lookup
            except ex:
                print ("Error ", ex)

    def __getitem__(self, name):
        name = name.lower()
        if name not in self.lookup:
            raise KeyError(name)
        names = reduce(operator.or_, self.lookup[name])
        if name in names:
            names.remove(name)
        return names

    def get(self, name, default=None):
        try:
            return self[name]
        except KeyError:
            return default
