"""
Module responsible for creating output file in desired formatting with name containing timestamp,
and saving this file to disc.
"""

from copy import deepcopy
import csv
from datetime import datetime


def _replace_boolean(data):
    """
    Returns new list with booleans replaced with 'P' or 'N'.

    :param data: List of lists containing rows of data
    :return: List of lists containing rows of data with string instead of booleans
    """
    output_data = deepcopy(data)
    for row in output_data:
        for i, element in enumerate(row):
            if element is True:
                element = 'P'
            elif element is False:
                element = 'N'
            row[i] = element
    return output_data


def _generate_output_name(extension):
    """
    Generates name, containing timestamp, for file.

    :param extension: String containing file extension
    :return: String containing name.
    """
    output_name = 'TDG_{:%Y-%m-%d_%H-%M-%S}.{}'.format(datetime.now(), extension)
    return output_name


def _file_writer(file, extension, output_data, headers):
    """
    Writes data into file in desired format, depending on extension.

    :param file: File-like object
    :param extension: String containing file extension
    :output_data: Iterable containing data
    :headers: Boolean informing whether to add header to begining of file
    """
    if extension == 'csv':
        separator = ','
    else:
        separator = ' '
    writer = csv.writer(file, delimiter=separator, quotechar='|')
    if headers is True:
        writer.writerow(['Login', 'P/N', 'Password', 'P/N'])
    writer.writerows(output_data)


def generate_output_file(data, extension, headers):
    """
    Creates output file, based on desired file extension(format).
    If file with generated name already exists, generated data will be appended to existing file.

    :param extension: String containing file extension
    :param data: List of lists containing rows of data
    :headers: Boolean informing whether to add header to begining of file
    :return: None
    """
    output_data = _replace_boolean(data)
    output_name = _generate_output_name(extension)
    with open(output_name, 'a', newline='') as file:
        _file_writer(file, extension, output_data, headers)
