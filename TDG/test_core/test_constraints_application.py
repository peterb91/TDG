import pytest
from TDG.core.constraints_application import login_password, login_min_len,\
    is_ascii, number_of_records, ratio, has_headers, file_type, copy_constraints,\
    login_max_len, creating_dict


def test_login_password(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'login')
    assert login_password({}) == 'login'

def test_login_password2(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'password')
    assert login_password({}) == 'password'

def test_login_password3(monkeypatch):
    def x(a):
        raise ValueError('Invalid input')
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'abc')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        login_password({})
    assert str(error_text.value) == 'Invalid input'


def test_login_min_len(monkeypatch):
    def x(a):
        raise ValueError('Invalid data type, please provide integer')
    monkeypatch.setitem(__builtins__,'input', lambda x: 'aaa')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        login_min_len({})
    assert str(error_text.value) == 'Invalid data type, please provide integer'

def test_login_min_len2(monkeypatch):
    def x(a):
        raise ValueError('Invalid number')
    monkeypatch.setitem(__builtins__,'input', lambda x: '0')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        login_min_len({})
    assert str(error_text.value) == 'Invalid number'

def test_login_min_len3(monkeypatch):
    def x(a):
        raise ValueError('Invalid number')
    monkeypatch.setitem(__builtins__,'input', lambda x: '20000')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        login_min_len({})
    assert str(error_text.value) == 'Invalid number'

def test_login_min_len4(monkeypatch):
    monkeypatch.setitem(__builtins__,'input', lambda x: '50')
    assert login_min_len({}) == 50

def test_login_max_len(monkeypatch):
    def x(a):
        raise ValueError('Invalid data type, please provide integer')
    monkeypatch.setitem(__builtins__,'input', lambda x: 'xxc')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        login_max_len({})
    assert str(error_text.value) == 'Invalid data type, please provide integer'

def test_login_max_len2(monkeypatch):
    def x(a):
        raise ValueError('Invalid number')
    monkeypatch.setitem(__builtins__,'input', lambda x: '22')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        login_max_len({'min_length':23})
    assert str(error_text.value) == 'Invalid number'

def test_login_max_len3(monkeypatch):
    def x(a):
        raise ValueError('Invalid number')
    monkeypatch.setitem(__builtins__,'input', lambda x: '20000')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        login_max_len({'min_length':23})
    assert str(error_text.value) == 'Invalid number'

def test_login_max_len4(monkeypatch):
    monkeypatch.setitem(__builtins__,'input', lambda x: '50')
    assert login_min_len({}) == 50
def test_is_ascii(monkeypatch):
    monkeypatch.setitem(__builtins__,'input', lambda x: '$%')
    assert is_ascii({}) == '$%'

def test_is_ascii2(monkeypatch):
    monkeypatch.setitem(__builtins__,'input', lambda x: '$%ą')
    assert is_ascii({}) == '$%'

def test_number_of_records(monkeypatch):
    def x(a):
        raise ValueError('Invalid data type, please provide integer')
    monkeypatch.setitem(__builtins__,'input', lambda x: 'qq')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        number_of_records({})
    assert str(error_text.value) == 'Invalid data type, please provide integer'

def test_number_of_records2(monkeypatch):
    def x(a):
        raise ValueError('Invalid number')
    monkeypatch.setitem(__builtins__,'input', lambda x: '0')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        number_of_records({})
    assert str(error_text.value) == 'Invalid number'

def test_number_of_records3(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: '50')
    assert number_of_records({}) == 50

def test_ratio(monkeypatch):
    def x(a):
        raise ValueError('Invalid data type')
    monkeypatch.setitem(__builtins__,'input', lambda x: 'aaa')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        ratio({})
    assert str(error_text.value) == 'Invalid data type'

def test_ratio2(monkeypatch):
    def x(a):
        raise ValueError('Invalid ratio')
    monkeypatch.setitem(__builtins__,'input', lambda x: '-1')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        ratio({})
    assert str(error_text.value) == 'Invalid ratio'

def test_ratio3(monkeypatch):
    def x(a):
        raise ValueError('Invalid ratio')
    monkeypatch.setitem(__builtins__,'input', lambda x: '20000')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        ratio({})
    assert str(error_text.value) == 'Invalid ratio'

def test_ratio4(monkeypatch):
    monkeypatch.setitem(__builtins__,'input', lambda x: '50')
    assert ratio({}) == 50

def test_has_headers(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'yes')
    assert has_headers({}) == True

def test_has_headers2(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'no')
    assert has_headers({}) == False

def test_has_headers3(monkeypatch):
    def x(a):
        raise ValueError('Invalid input. Please type yes/no')
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'abc')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        has_headers({})
    assert str(error_text.value) == 'Invalid input. Please type yes/no'

def test_file_type(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'txt')
    assert file_type({}) == 'txt'

def test_file_type2(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'csv')
    assert file_type({}) == 'csv'

def test_file_type3(monkeypatch):
    def x(a):
        raise ValueError('Invalid file type')
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'abc')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        file_type({})
    assert str(error_text.value) == 'Invalid file type'

def test_copy_constraints(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'yes')
    assert copy_constraints({}) == 'yes'

def test_copy_constraints2(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'no')
    assert copy_constraints({}) == 'no'

def test_copy_constraints3(monkeypatch):
    def x(a):
        raise ValueError('Invalid input. Please type yes/no')
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'abc')
    monkeypatch.setitem(__builtins__, 'print', x)
    with pytest.raises(ValueError) as error_text:
        copy_constraints({})
    assert str(error_text.value) == 'Invalid input. Please type yes/no'
