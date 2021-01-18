#wyszukiwanie wzorca w tekście

def is_pattern(pattern,word):
    return pattern in word

pattern = "motyw"
word = "lokomotywa"

print(is_pattern(pattern,word))

#implementacje iteracyjną zrobię kiedy indziej 
