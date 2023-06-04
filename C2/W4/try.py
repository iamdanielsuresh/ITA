def character_frequency(filename):
    """counts the freq of char in the given file"""
    #first try to open the file

    try:
        f = open(filename, 'r')
    except OSError:
        return None   

    #Now process the file

    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
        f.close()
        return characters
character_frequency('log messages.txt')