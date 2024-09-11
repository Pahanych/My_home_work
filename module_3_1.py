calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    list = []
    list.append(len(string))
    list.append(string.upper())
    list.append(string.lower())
    a = tuple(list)
    print(a)

def is_contains(string, list_to_search):
    count_calls()
    a = string.lower()
    b = [i.lower() for i in list_to_search]
    found = a in b
    print(found)

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)