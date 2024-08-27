#Счётчик вызовов
calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()


print(string_info('Musk'))
print(string_info('Katerina'))


def is_contrains(string, list_to_search):
    count_calls()
    string = string.lower()
    for element in list_to_search:
        if element.lower() == string:
            return True
    return False


print(is_contrains('katerina', ['love', 'kiss', 'katERina']))
print(is_contrains('Raccoon', ['liVE', 'klass', 'listiNg']))
print(calls)
