"""
Module responsible for gathering user's input, validating if correct input type
is provided and saving user's input to 2 dictionaries, for login and password respectively.
"""

f_types = ('txt', 'csv')
login_or_pass = ''
dictionary = {}


def login_password(dictionary):
    """
    Check if user want to provide constraints for login or password.

    :param dictionary: empty dictionary
    :return: type str, ("login", "password")
    """
    global login_or_pass
    while True:
        l_p = input('Would you like to provide constraints for login or password?: ')
        login_or_pass = l_p.lower()
        if login_or_pass not in ('login', 'password'):
            print('Invalid input')
        else:
            dictionary['login_or_password'] = login_or_pass
            return login_or_pass


def login_min_len(dictionary):
    """
    Check if login length has an integer type within range 1-1000

    :param dictionary: empty dictionary
    :return: dictionary with key "min_length", value type int
    """
    cont = True
    while cont:
        answer = input('Please provide minimum length: ')
        dictionary['min_length'] = answer
        if type(dictionary['min_length']) != int:
            try:
                dictionary['min_length'] = int(dictionary['min_length'])
                if dictionary['min_length'] < 1 or dictionary['min_length'] > 1000:
                    print('Invalid number')
                else:
                    cont = False
                    return dictionary['min_length']
            except ValueError:
                print('Invalid data type, please provide integer')


def login_max_len(dictionary):
    """
    Check if login length has an integer type within range 1-1000

    :param dictionary: dictionary with key "min_length", value type int
    :return: dictionary updated with key "max_length", value type int
    """
    cont = True
    while cont:
        answer = input('Please provide maximum length: ')
        dictionary['max_length'] = answer
        if type(dictionary['max_length']) != int:
            try:
                dictionary['max_length'] = int(dictionary['max_length'])
                if dictionary['max_length'] < dictionary['min_length'] or dictionary['max_length'] > 1000:
                    print('Invalid number')
                else:
                    cont = False
                    return dictionary['max_length']
            except ValueError:
                print('Invalid data type, please provide integer')


def is_ascii(dictionary):
    """
    Check if provided characters are from ASCII table, if not, characters are excluded

    :param dictionary: dictionary with key "min_length", value type int; key "max_length", value type int;
    :return: updated dictionary with key "characters" value type str;
    """
    answer = input('Provide special characters from list [none all ` ~! @ # $ % ^ & * ( ) _ + - = [ ] { } | \ ; \' : \" , < . > / ?] eg.: #$%: ')
    dictionary['characters'] = answer
    lista = '` ~! @ # $ % ^ & * ( ) _ + - = [ ] { } | \ ; \' : \" , < . > / ?'
    new_characters = ''
    if answer == 'none':
        dictionary['characters'] = ''
    elif dictionary['characters'] == 'all':
        dictionary['characters'] = '` ~! @ # $ % ^ & * ( ) _ + - = [ ] { } | \ ; \' : \" , < . > / ?]'.replace(' ', '')
    else:
        for char in dictionary['characters']:
            if char.isalpha() or char.isdigit():
                new_characters += ''
            elif char in lista:
                new_characters += char
        dictionary['characters'] = new_characters.replace(' ', '')
    return dictionary['characters']


def number_of_records(dictionary):
    """Check if number of records has valid data type

    :param dictionary: dictionary with key "min_length", value type int; key "max_length", value type int;
           key "characters" value type str;
    :return: updated dictionary with key "list_length" value type int;
    """
    cont = True
    while cont:
        answer = input('Provide number of records to generate: ')
        dictionary['list_length'] = answer
        if type(dictionary['list_length']) != int:
            try:
                dictionary['list_length'] = int(dictionary['list_length'])
                if dictionary['list_length'] < 1:
                    print('Invalid number')
                else:
                    cont = False
                    return dictionary['list_length']
            except ValueError:
                print('Invalid data type, please provide integer')


def ratio(dictionary):
    """
    Check if ratio of positive and negative data is valid

    :param dictionary: dictionary with key "min_length", value type int; key "max_length", value type int;
           key "characters" value type str; key "list_length" value type int;
    :return: updated dictionary with key "positive_percentage" value type int;
    """
    cont = True
    while cont:
        answer = input('Provide ratio of positive data in %: ')
        dictionary['positive_percentage'] = answer
        if type(dictionary['positive_percentage']) != int:
            try:
                dictionary['positive_percentage'] = int(dictionary['positive_percentage'])
                if dictionary['positive_percentage'] < 0 or dictionary['positive_percentage'] > 100:
                    print('Invalid ratio')
                else:
                    cont = False
                    return dictionary['positive_percentage']
            except ValueError:
                print('Invalid data type')


def has_headers(dictionary):
    """
    Check if data has to have headers - if 'yes/no'

    :param dictionary: dictionary with key "min_length", value type int; key "max_length", value type int;
           key "characters" value type str; key "list_length" value type int;
           key "positive_percentage" value type int;
    :return: updated dictionary with key "headers" value type boolean;
    """
    while True:
        answer = input('Would you like to have headers yes/no: ').lower()
        if answer not in {'yes', 'no'}:
            print('Invalid input. Please type yes/no')
        else:
            if answer == 'yes':
                dictionary['headers'] = True
            elif answer == 'no':
                dictionary['headers'] = False
            return dictionary['headers']


def file_type(dictionary):
    """
    Check if file type is valid

    :param dictionary: dictionary with key "min_length", value type int; key "max_length", value type int;
           key "characters" value type str; key "list_length" value type int;
           key "positive_percentage" value type int; key "headers" value type str;
    :return: updated dictionary with key "file_format" value type str;
    """

    while True:
        answer = input('Provide file type txt/csv: ')
        dictionary['file_format'] = answer
        if dictionary['file_format'].lower() not in f_types:
            print('Invalid file type')
        else:
            return dictionary['file_format']


def copy_constraints(dictionary):
    """
    Check if copy constraints value is equal to 'yes/no'

    :param dictionary: dictionary with key "min_length", value type int; key "max_length", value type int;
           key "characters" value type str; key "list_length" value type int;
           key "positive_percentage" value type int; key "headers" value type str;
           key "file_format" value type str;
    :return: updated dictionary with key "copy_constraints" value type str;
    """

    while True:
        answer = input('Would you like to copy constraints for second feature yes/no: ')
        dictionary['copy_constraints'] = answer
        if dictionary['copy_constraints'].lower() not in ('yes', 'no'):
            print('Invalid input. Please type yes/no')
        else:
            return dictionary['copy_constraints']


def creating_dict(dictionary):
    """
    Creates dictionary for both login and password based on original dictionary, if
    option to copy is chosen, then two same dictionaries are created.

    :param dictionary: dictionary with key "min_length", value type int; key "max_length", value type int;
           key "characters" value type str; key "list_length" value type int;
           key "positive_percentage" value type int; key "headers" value type str;
           key "file_format" value type str; key "copy_constraints" value type str;
    :return: tuple of two dictionaries
    """
    dict_password, dict_login = {}, {}
    if dictionary['copy_constraints'].lower() == 'yes':
        dict_password = dictionary
        dict_login = dictionary
        dict_password['login_or_password'] = 'password'
        dict_login['login_or_password'] = 'login'
    elif login_or_pass == 'login' and dictionary['copy_constraints'].lower() == 'no':
        dict_login = dictionary
        dict_login['login_or_password'] = 'login'
        login_min_len(dict_password)
        login_max_len(dict_password)
        is_ascii(dict_password)
        dict_password['list_length'] = dictionary['list_length']
        dict_password['positive_percentage'] = dictionary['positive_percentage']
        dict_password['headers'] = dictionary['headers']
        dict_password['file_format'] = dictionary['file_format']
        dict_password['copy_constraints'] = dictionary['copy_constraints']
        dict_password['login_or_password'] = 'password'
    else:
        dict_password = dictionary
        dict_password['login_or_password'] = 'password'
        login_min_len(dict_login)
        login_max_len(dict_login)
        is_ascii(dict_login)
        dict_login['list_length'] = dictionary['list_length']
        dict_login['headers'] = dictionary['headers']
        dict_login['file_format'] = dictionary['file_format']
        dict_login['positive_percentage'] = dictionary['positive_percentage']
        dict_login['copy_constraints'] = dictionary['copy_constraints']
        dict_login['login_or_password'] = 'login'
    return (dict_login, dict_password)


def execute_constraints_application():
    login_password(dictionary)
    login_min_len(dictionary)
    login_max_len(dictionary)
    is_ascii(dictionary)
    number_of_records(dictionary)
    ratio(dictionary)
    has_headers(dictionary)
    file_type(dictionary)
    copy_constraints(dictionary)
    return creating_dict(dictionary)
