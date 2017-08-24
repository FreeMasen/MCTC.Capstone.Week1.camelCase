

def parse(text):
    broken = text.split(' ')
    broken[0] = lower(broken[0])
    broken[1:] = map(camel, broken[1:])
    return ''.join(broken)

def lower(word):
    return word.lower()

def camel(word):
    lowered = word.lower()
    
    return word[0].upper() + lowered[1:]

def main():
    print(parse(raw_input('Enter the text you would like turned into camelCase notation\n')))

main()