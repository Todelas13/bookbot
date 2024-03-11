def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    letters = {}
    for w in words:
        for c in w:
            c_lower = c.lower()
            if c_lower in letters:
                letters[c_lower] += 1
            else:
                letters[c_lower] = 1
    
    list_dict = []
    for key,value in letters.items():
        if key.isalpha():
            new_dict= {"char": key, "num": value}
            list_dict.append(new_dict)
    
    list_dict.sort(reverse=True, key=sort_on)
    for item in list_dict:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    

def sort_on(dict):
    return dict["num"]

main()

