from sys import argv


def tes():
    # first argument filename
    filename = argv[1]
    if 'csv' in filename:
        spliter = ','
    else:
        spliter = ' '
    f = open(str(filename), "r")
    # second argument min or max
    if argv[2] == "min":
        print('Minimum constrains:')
        # third and forth argument value
        minimum(f, spliter, argv[3], argv[4])
    elif argv[2] == "max":
        # third and forth argument value
        maximum(f, spliter, argv[3], argv[4])
    else:
        print("Wrong answer.")
        return 0


def minimum(file, spl, len_log, len_pass):
    i = 0
    positive = 0
    for line in file:
        i = i + 1
        b = line.split(spl)
        if b[0] == 'Login' or b[2] == 'Password':
            i = 0
            continue
        if b[1] == 'P':
            if len(b[0]) < int(len_log):
                print('Line ' + str(i) + ' WRONG')
            else:
                print('Line ' + str(i) + ' OK')
        if b[3] == 'P\n':
            if len(b[2]) < int(len_pass):
                print('Line ' + str(i) + ' WRONG')
            else:
                print('Line ' + str(i) + ' OK')
        if b[1] == 'P' and b[3] == 'P\n':
            positive = positive + 1
    print('Number of data: ' + str(i))
    print('Number of positive data: ' + str(positive))
    print('Positive ratio: ' + str(positive/i * 100))


def maximum(file, spl, len_log, len_pass):
    i = 0
    positive = 0
    for line in file:
        i = i + 1
        b = line.split(spl)
        if b[0] == 'Login' or b[2] == 'Password':
            i = 0
            continue
        if b[1] == 'P':
            if len(b[0]) > int(len_log):
                print('Line ' + str(i) + ' WRONG')
            else:
                print('Line ' + str(i) + ' OK')
        if b[3] == 'P':
            if len(b[2]) > int(len_pass):
                print('Line ' + str(i) + ' WRONG')
            else:
                print('Line ' + str(i) + ' OK')
        if b[1] == 'P' and b[3] == 'P\n':
            positive = positive + 1
    print('Number of data: ' + str(i))
    print('Number of positive data: ' + str(positive))
    print('Positive ratio: ' + str(positive/i * 100))

tes()

#HOW to launch:
#python3 Auto.py FILENAME min/max numOfLettersinlogin numOfLettersinPass
