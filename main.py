
def main():
    
    text = get_book_text("books/frankenstein.txt")
    count_words = get_count_words(text)
    count_char = get_count_char(text)
    char_report = sort_chars_dict(count_char)

    print("---begin report of books/frankenstein.txt--- ")
    print(f"{count_words} words found in document")
    print()
    for item in char_report:
         if item["char"].isalpha() == True:
              print(f"the {item["char"]} character was fround {item["num"]} times")
    
def get_count_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
     return d["num"]


def sort_chars_dict(char_dict):
     sorted = []
     for char in char_dict:
          sorted.append({"char": char, "num": char_dict[char]})
     sorted.sort(reverse=True, key=sort_on)
     return sorted          

def get_count_char(text):
    char_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_dict:
                char_dict[lowered_char] += 1
        else:
            char_dict[lowered_char] = 1
    return char_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()