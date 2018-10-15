from random import randint


def main():
    bible_books = load_bible_books()

    for _ in range(1):
        chosen_book = randint(0, len(bible_books)) - 1
        chosen_chapter = randint(0, bible_books[chosen_book][1]) + 1
        print "The random book and chapter for today is", bible_books[chosen_book][0] + ', chapter', chosen_chapter


def load_bible_books():
    ret_array = []
    with open('bible_books.txt', 'r') as read_file:
        for line in read_file.readlines():
            line_split = line.split()
            chapter_num = int(line_split[-1])
            if len(line_split) == 2:
                book = line_split[0]
            elif len(line_split) == 3:
                book = line_split[0] + ' ' + line_split[1]
            else:
                book = line_split[0] + ' ' + line_split[1] + ' ' + line_split[2]

            ret_array.append((book, chapter_num))
    return ret_array


if __name__ == '__main__':
    main()
