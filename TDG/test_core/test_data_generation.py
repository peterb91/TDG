import random
import string
from TDG.core.data_generation import *
import pytest


def test_set_characters():
    mychars = generate_character_set('')
    for character in ''.join(['0123456789', string.ascii_letters]):
        assert character in mychars, 'No character {} characters in the set'.format(character)


def test_set_user_characters():
    user_data = '!@#$%^&*()'
    mychars = generate_character_set(user_data)
    for character in ''.join(['0123456789', string.ascii_letters, user_data]):
        assert character in mychars, 'No character {} characters in the set'.format(character)


def test_set_multiple_characters():
    user_data = '!!!!!!!!!!!!!'
    mychars = generate_character_set(user_data)
    assert len(mychars) == len(string.ascii_letters) + 10 + 1, 'Non-unique characters in the set'


def test_generating_data():
    x = random.choice(string.ascii_letters)
    l = random.randint(1, 50)
    result = generate_record(x, l, l)
    assert result == x * l, "Expected {!r}({}), got {!r}".format(x, l, result)

# some dummy data for next tests
test_data1 = {'max_length': 10,
              'login_or_password': 'login',
              'headers': 'y',
              'min_length': 8,
              'positive_percentage': 70,
              'characters': '&**$#@',
              'copy_constrains': 'y',
              'file_format': 'txt',
              'case_sensitive': 'y',
              'list_length': 12}

test_data2 = {'characters': '!@#$%^&*()',
              'min_length': 10,
              'positive_percentage': 30,
              'login_or_password': 'password',
              'max_length': 20,
              'copy_constrains': 'n',
              'case_sensitive': 'n',
              'list_length': 1000000000000000000,
              'file_format': 'csv'}

test_data3 = {'max_length': 55,
              'login_or_password': 'login',
              'headers': 'y',
              'min_length': 20,
              'positive_percentage': 50,
              'characters': '&**$#@',
              'copy_constrains': 'y',
              'file_format': 'txt',
              'case_sensitive': 'y',
              'list_length': 10}

test_data4 = {'characters': '!@#$%^&*()',
              'min_length': 1,
              'positive_percentage': 22,
              'login_or_password': 'password',
              'max_length': 3,
              'copy_constrains': 'n',
              'case_sensitive': 'n',
              'list_length': 1000000000000000000,
              'file_format': 'csv'}

expected12 = {'negative_sets': 4, 'list_length': 12, 'percentage': 70, 'positive_sets': 8}
expected34 = {'percentage': 50, 'list_length': 10, 'negative_sets': 5, 'positive_sets': 5}

characters = ['Y', 'u', 'o', '!', 'w', 'C', 'i', 'R', 'K', 'r', 'v', 'M', 'c', 'a', 'h', 'b', 'O', 'W', '5', 'x',
              'L', 'f', '0', 'Q', 'n', 'P', '6', 'j', 'e', 'l', 'A', '1', 't', 's', 'y', 'D', '#', 'd', 'p', '8',
              'F', '&', 'J', 'U', 'k', 'B', 'T', 'V', '%', 'z', 'G', 'S', '7', '$', '3', 'Z', 'H', 'g', 'm', '4',
              'q', '9', '*', 'E', 'I', 'N', '@', 'X', '^', '2']

data = generate_logins_and_passwords((test_data1, test_data2))


def test_if_number_of_gen_data_is_correct():
    assert len(data) == test_data1['list_length'], 'The number of generated sets does not match the number of login[\'list_length\']'


def test_check_invalid_records():
    data_to_be_checked = generate_invalid_record(characters, test_data1['min_length'], test_data1['max_length'])
    assert len(data_to_be_checked) not in range(test_data1['min_length'],test_data1['max_length']+1), 'Login or password that should be invalid seems to be valid'


def test_check_valid_records():
    data_to_be_checked = generate_record(characters, test_data1['min_length'],
                                                                 test_data1['max_length'])
    assert len(data_to_be_checked) in range(test_data1['min_length'], test_data1[
        'max_length']+1), 'Login or password that should be valid seems to be invalid'


params = calculate_sets_size(test_data1, test_data2, warnings=False)
@pytest.mark.parametrize("login_params,password_params,expected", [
    (test_data1, test_data2, expected12),
    (test_data3, test_data4, expected34),

])
def test_chceck_set_sizes(login_params, password_params, expected):
    assert calculate_sets_size(login_params, password_params) == expected
