import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  
    
from stats import get_num_words, get_character_count

book_path = sys.argv[1]
with open(book_path, "r", encoding="utf-8") as f:
    content = f.read()
    
num_words = get_num_words(content)

character_count = get_character_count(content)

print("""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------""")

print(f"Found {num_words} total words")

print ("--------- Character Count -------")

for char, count in character_count:
    print(f"{char}: {count}")

