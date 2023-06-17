import csv
import regex_tools
import codecs


class Phonebook:
    def __init__(self, file_name: str):
        with codecs.open(file_name, 'r', 'utf-8') as f:
            rows = csv.reader(f, delimiter=',')
            data = list(rows)
            self.headers = data[0]
            self.book = data[1:]

    def normalize_phones(self):
        for i, row in enumerate(self.book):
            phone_number = row[5]
            formatted_number = regex_tools.format_phone_number(phone_number)
            row[5] = formatted_number

    def normalize_names(self):
        for raw in self.book:
            other_fields = raw[3:]
            names = ' '.join(raw[:3]).split()
            while len(names) != 3:
                names.append('')
            for i, item in enumerate(names):
                raw[i] = item

    def merge_duplicates(self):
        merged_book = {}
        for raw in self.book:
            full_name = f'{raw[0]} {raw[1]}'
            if merged_book.get(full_name):
                for i, item in enumerate(raw):
                    if item == '':
                        continue
                    merged_book[full_name][i] = item
            else:
                merged_book[full_name] = raw
        self.book = [item for item in merged_book.values()]

    def save(self, name):
        with codecs.open(name, "w", "utf-8") as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerow(self.headers)
            datawriter.writerows(self.book)
