"""
This module is responsible for actual generation of valid and invalid logins and passwords.
Module creates character sets to be used during generation, calculates set sizes and creates
valid/invalid logins and passwords that are put into list of lists.
"""

import random
import string


def generate_logins_and_passwords(args):
    """
    This function generates valid and invalid logins and passwords
    and puts them into a list of lists.

    :param login_params: a dictionary with login settings.
    :param passwd_params: a dictionary with password settings.
    :return: a list of lists with valid and invalid sets.
    """
    data = []

    login_params = args[0]
    passwd_params = args[1]

    params = calculate_sets_size(login_params, passwd_params, warnings=True)
    login_characters = generate_character_set(login_params['characters'])
    passwd_characters = generate_character_set(passwd_params['characters'])

    for _ in range(params['positive_sets']):
        data.append([
            generate_record(login_characters, login_params['min_length'], login_params['max_length']),
            True,
            generate_record(passwd_characters, passwd_params['min_length'], passwd_params['max_length']),
            True,
        ])

    valid_logins = []
    invalid_logins = []
    valid_passwds = []
    invalid_passwds = []

    val_log_inv_pass = round(params['negative_sets'] / 3)
    inval_log_val_pass = val_log_inv_pass
    inval_log_inval_pass = params['negative_sets'] - val_log_inv_pass - inval_log_val_pass

    len_valid_logins = val_log_inv_pass
    len_valid_passwords = len_valid_logins
    len_invalid_logins = inval_log_inval_pass + len_valid_passwords
    len_invalid_passwords = inval_log_inval_pass + len_valid_logins

    for i in range(len_valid_logins):
        valid_logins.append(
            generate_record(login_characters, login_params['min_length'], login_params['max_length']))
    for i in range(len_valid_passwords):
        valid_passwds.append(
            generate_record(passwd_characters, passwd_params['min_length'], passwd_params['max_length']))
    for i in range(len_invalid_logins):
        invalid_logins.append(
            generate_invalid_record(login_characters, login_params['min_length'], login_params['max_length']))
    for i in range(len_invalid_passwords):
        invalid_passwds.append(
            generate_invalid_record(passwd_characters, passwd_params['min_length'], passwd_params['max_length']))

    for i in range(val_log_inv_pass):
        data.append([valid_logins.pop(), True, invalid_passwds.pop(), False])
    for i in range(inval_log_val_pass):
        data.append([invalid_logins.pop(), False, valid_passwds.pop(), True])
    for i in range(inval_log_inval_pass):
        data.append([invalid_logins.pop(), False, invalid_passwds.pop(), False])
    return data


def generate_invalid_record(characters, min_length, max_length):
    """
    This function calculates new, incorrect length of login/password and uses it
    to generate a record with invalid length.

    :param characters: the dictionary of characters from which login or password is being generated.
    :param min_length: minimum length of a single login or password.
    :param max_length: maximum length of a single login or password.
    :return: a single invalid login/password.
    """
    bigger = random.randint(max_length + 1, max_length + 20)

    if min_length < 2:
        final = bigger
    else:
        smaller = random.randint(1, min_length - 1)
        final = random.choice([smaller, bigger])
    return generate_record(characters, final, final)


def generate_record(characters, min_len, max_len):
    """
    This function takes care of generating valid and invalid login or password
    of a size within range of min_len and max_len.

    :param characters: the dictionary of characters from which login or password is being generated.
    :param min_len: minimum length of a single login or password.
    :param max_len: maximum length of a single login or password.
    :return: returns single login or password.
    """
    return ''.join(random.choice(characters) for _ in range(random.randint(min_len, max_len)))


def generate_character_set(chars):
    """
    This function generates a "dictionary" of unique characters from which random logins
    and passwords are being generated. The dictionary consists of user's input,
    ascii letters and digits.

    :param chars: a set of characters declared by the user.
    :return: a list of characters to be used during data generation.
    """
    result = ''.join([chars, string.ascii_letters, '0123456789'])
    return list(set(result))


def calculate_sets_size(login_params, passwd_params, warnings=False):
    """
    This function takes care of proper calculation of a number of positive and
    negative sets to be generated, according to user's choice. If the number of sets or the percentage
    of positive data to be generated differs between 'login' and 'password' settings,
    the warnings can be seen on the screen. If the values differ, the program calculates the output
    using the number of sets and the percentage from the 'login' settings.

    :param login_params: a dictionary with login parameters.
    :param passwd_params: a dictionary with password parameters.
    :param warnings: optional parameter to see warnings during execution.
    :return: a dictionary of values to be used during output generation.
    """
    args = (login_params, passwd_params)
    percentage = 0
    positive_sets = 0
    negative_sets = 0
    list_length = 0
    for arg in args:
        if arg['login_or_password'] == 'login':
            positive_sets = round(arg['list_length'] * arg['positive_percentage'] / 100)
            negative_sets = arg['list_length'] - positive_sets
            percentage = arg['positive_percentage']
            list_length = arg['list_length']
        if warnings and arg['login_or_password'] == 'password' and arg['positive_percentage'] != percentage:
            print('Percentage for login and password differ. '
                  'The percentage ({}%) from the login setting will be used to generate positive values'.format(percentage))
        if warnings and arg['login_or_password'] == 'password' and arg['list_length'] != list_length:
            print('The number of sets for login and password differ. '
                  'The number of sets ({}) from the login setting will be used to generate data'.format(list_length))
    return {'percentage': percentage, 'positive_sets': positive_sets, 'negative_sets': negative_sets,
            'list_length': list_length}
