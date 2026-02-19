# Prompt for and then open that book file
my_book = input('What book would you like to read? ')
my_open_book = open('txts/' + my_book.strip())

# Print every line in the book
while True:
    the_line = my_open_book.readline()
    print(the_line, end='')

    # Check for EOF
    if the_line == '':
        break

    my_open_book.close()

print("The End.")
