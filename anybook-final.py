# Prompt for and then open that book file
my_book = input('What book would you like to read? ')

# Print every line in the book
with open('txts/' + my_book.strip()) as my_open_book:
    while True:
        the_line = my_open_book.readline()
        print(the_line, end='')

        # Check for EOF
        if the_line == '':
            break

print("The End.")
