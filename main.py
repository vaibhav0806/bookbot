def char_freq(str):
    dict = {}
    for char in str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def count_words(str):
    words = str.split()
    return len(words)

def sort_on(d):
    return d["num"]

def main():
    with open("./books/frankenstein.txt") as f:
        file_content = f.read()
        word_count = count_words(file_content)
        dict = char_freq(file_content.lower())
        sorted_list = []
        for ch in dict:
            sorted_list.append({"char": ch, "num": dict[ch]})
        sorted_list.sort(reverse=True, key=sort_on)
        print('--- Begin report of books/frankenstein.txt ---')

        print(f"{word_count} words found in the document\n\n")

        for item in sorted_list:
            if not item["char"].isalpha():
                continue
            print(f"The '{item['char']}' character was found {item['num']} times")
        
        print("--- End report ---")
            
main()