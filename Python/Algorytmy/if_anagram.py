def if_anagram(string,string2):
    if sorted(string) == sorted(string2):
        return True
    return False

string = "anagram"
string2 = "nagaram"

print(if_anagram(string,string2))
