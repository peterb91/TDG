"""
This the main module of Data Generator Application - it imports three functions from three different modules,
allowing to generate login and password data based on constrains given by the user in the console.


Copyright(c) 2017 by ATA4.0
"""
if __name__ == '__main__':
    from core.constraints_application import execute_constraints_application
    from core.data_generation import generate_logins_and_passwords
    from core.generate_output_file import generate_output_file

    data = execute_constraints_application()
    output = generate_logins_and_passwords(data)
    generate_output_file(output, data[0]['file_format'], data[0]['headers'])
