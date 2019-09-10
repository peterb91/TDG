"""
Forms to validate pages with the same and different constraints.
"""

from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField, validators, IntegerField
from wtforms.validators import Required


NUMBER_TO_GENERATE_DESCR = 'Number of records to generate'
RATIO_DESCR = 'Ratio of positive data'
HEADERS_DESCR = 'Would you like to have headers in the output file?'
MIN_LEN_DESCR = 'Minimum length'
MAX_LEN_DESCR = 'Maximum length'
SPECIAL_DESCR = 'Select special characters: ` ~! @ # $ % ^ & * ( ) _ + - = [ ] { } | \ ; \' : " , < . > / ?'
CUSTOM_DESCR = 'Enter custom characters here:'


class RequiredIf(Required):
    """
    This class creates a validator which makes a field required
    if another field is set and has a truthy value.
    """

    def __init__(self, other_field_name, *args, **kwargs):
        self.other_field_name = other_field_name
        super(RequiredIf, self).__init__(*args, **kwargs)

    def __call__(self, form, field):
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "%s" in form' % self.other_field_name)
        if bool(other_field.data):
            super(RequiredIf, self).__call__(form, field)


class SameForm(FlaskForm):
    """
    This class provides form for the data generation with the same constraints.
    """

    records_no = IntegerField(NUMBER_TO_GENERATE_DESCR,
                              [validators.required(),
                               validators.NumberRange(min=1, max=1000),
                               ])

    ratio = IntegerField(RATIO_DESCR,
                         [validators.required(),
                          validators.NumberRange(min=1, max=100),
                          ])

    headers = RadioField(HEADERS_DESCR,
                         [validators.required()],
                         choices=[('y_headers', 'Yes'), ('n_headers', 'No')])

    login_min_length = IntegerField(MIN_LEN_DESCR,
                                    [validators.NumberRange(min=1, max=50),
                                     validators.required()])

    login_max_length = IntegerField(MAX_LEN_DESCR,
                                    [validators.NumberRange(min=1, max=50),
                                     validators.required()])

    login_special_char = RadioField(SPECIAL_DESCR,
                                    [validators.required()],
                                    choices=[('login_all_special', 'All'),
                                             ('login_none_special', 'None'),
                                             ('login_custom_special', 'Custom')])

    login_textarea_custom = TextAreaField(CUSTOM_DESCR,
                                          validators=[RequiredIf('login_special_char')],
                                          )


class DifferentForm(SameForm):
    """
    This class provides form for the data generation with different constraints.
    """
    pass_min_length = IntegerField(MIN_LEN_DESCR,
                                   [validators.NumberRange(min=1, max=50),
                                    validators.required()])

    pass_max_length = IntegerField(MAX_LEN_DESCR,
                                   [validators.NumberRange(min=1, max=50),
                                    validators.required()])

    pass_special_char = RadioField(SPECIAL_DESCR,
                                   [validators.required()],
                                   choices=[('pass_all_special', 'All'),
                                            ('pass_none_special', 'None'),
                                            ('pass_custom_special', 'Custom')])

    pass_textarea_custom = TextAreaField(CUSTOM_DESCR,
                                         validators=[RequiredIf('pass_special_char')],
                                         )
