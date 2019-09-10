import io
import pytest
from TDG.core.generate_output_file import _file_writer, generate_output_file, _generate_output_name, _replace_boolean
from freezegun import freeze_time


@freeze_time('2017-06-09 21:37:00')
def test_generate_output_name():
    assert _generate_output_name('testextension') == 'TDG_2017-06-09_21-37-00.testextension'


@pytest.mark.parametrize("test_list, expected_list", [
    ([['login', True, 'pwd', False], ['login2', False, 'pwd2', False]], [['login', 'P', 'pwd', 'N'], ['login2', 'N', 'pwd2', 'N']]),
    ([[True, True], [False, False]], [['P', 'P'], ['N', 'N']])
])
def test_replace_boolean(test_list, expected_list):
    assert _replace_boolean(test_list) == expected_list


def test_file_writer_csv_no_headers():
    test_data = [['First column first row', 'Second column first row'], ['first column second row', 'second column second row']]
    mock_file = io.StringIO()
    _file_writer(mock_file, 'csv', test_data, False)
    mock_file.seek(0)
    assert mock_file.readlines() == ['First column first row,Second column first row\r\n', 'first column second row,second column second row\r\n']


def test_file_writer_csv_with_headers():
    test_data = [['First column first row', 'Second column first row'], ['first column second row', 'second column second row']]
    mock_file = io.StringIO()
    _file_writer(mock_file, 'csv', test_data, True)
    mock_file.seek(0)
    assert mock_file.readlines() == ['Login,P/N,Password,P/N\r\n', 'First column first row,Second column first row\r\n', 'first column second row,second column second row\r\n']


def test_file_writer_txt_no_headers():
    test_data = [['first_element_first_row', 'second_element_first_row'], ['first_element_second_row', 'second_element_second_row']]
    mock_file = io.StringIO()
    _file_writer(mock_file, 'txt', test_data, False)
    mock_file.seek(0)
    assert mock_file.readlines() == ['first_element_first_row second_element_first_row\r\n', 'first_element_second_row second_element_second_row\r\n']


def test_file_writer_txt_with_headers():
    test_data = [['first_element_first_row', 'second_element_first_row'], ['first_element_second_row', 'second_element_second_row']]
    mock_file = io.StringIO()
    _file_writer(mock_file, 'txt', test_data, True)
    mock_file.seek(0)
    assert mock_file.readlines() == ['Login P/N Password P/N\r\n', 'first_element_first_row second_element_first_row\r\n', 'first_element_second_row second_element_second_row\r\n']


@freeze_time('2017-01-02 12:30:11')
def test_generate_output_file(mocker, monkeypatch):
    mocked_open = mocker.patch('builtins.open')
    generate_output_file([['test'], ['data']], 'testext', True)
    mocked_open.assert_called_once_with('TDG_2017-01-02_12-30-11.testext', 'a', newline='')
