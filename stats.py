def get_num_words(content):
    
    words = content.split()
    num_words = len(words)
    
    return num_words

def get_character_count(content):
    character_count = {}
    for character in content.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return sorted(character_count.items())


   