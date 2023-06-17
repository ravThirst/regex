from phonebook import Phonebook


if __name__ == '__main__':
    phone_book = Phonebook('phonebook_input.csv')
    phone_book.normalize_phones()
    phone_book.normalize_names()
    phone_book.merge_duplicates()
    phone_book.save("phonebook_output.csv")
