#Счётчик вызовов
calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    print([len(string), string.lower(), string.upper()])
    count_calls()


string_info('Musk')
string_info('Katerina')


def is_contrains(string, list_to_search):
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            print(True)
        else:
            print(False)
    count_calls()


is_contrains('katerina', ['love', 'kiss', 'katERina'])
is_contrains('Raccoon', ['liVE', 'klass', 'listiNg'])


print(calls)
