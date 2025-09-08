"""
Write a program that reads each line in a file, reverses its lines, and writes them to another file. Also, print the total character count and word count on the screen.  For example, if the file file.txt contains the lines (Marks 5)

Mary had a little lamb
Its fleece was white as snow
And everywhere that Mary went
The lamb was sure to go.

reverse_file.txt result.txt
then result.txt contains

lamb little a had Mary
snow as white was fleece Its
went Mary that everywhere And
.go to sure was lamb The

"""


import os
# Build the absolute path to poem.txt, relative to this script's folder
BASE_DIR = os.path.dirname(__file__)
MAIN_DOCUMENT = os.path.join(BASE_DIR, "reverse_file.txt")

OUTPUT_FILENAME = "result.txt"

# TODO: set the total characters and total words as global variables 


def main(): 
    read_file(MAIN_DOCUMENT, OUTPUT_FILENAME)


def read_file(input_filename, output_filename):
    """
    TODO: docstring explain function 
    """

    try:
        with open(input_filename, 'r') as infile:
            lines = [line.strip() for line in infile.readlines()]
            
        word_count = 0
        character_count = 0
        with open(output_filename, 'w') as outfile:
            for line in lines:
                character_count += len(line)
                word_count += len(line.split())
                reversed_words = " ".join(line.split()[::-1])
                print(reversed_words)
                outfile.write(reversed_words + "\n")
            print(f"The character count is: {character_count}")
            print(f"The word count is: {word_count}")
        
        print(f"Lines reversed and saved to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found")
    except Exception as e: 
        print(f"An error occured: {e}")


main()

