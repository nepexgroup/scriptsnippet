# importing libraries
import pandas as pd
from pandas import ExcelWriter
import os


# function to get the data.
def get_data():
    # file location may vary according to installation of lynis.
    warnings = open('/usr/bin/warnings.txt', 'r')
    suggestions = open('/usr/bin/suggestions.txt', 'r')
    packages = open('/usr/bin/packages.txt', 'r')
    shells = open('/usr/bin/shells.txt', 'r')

    # create Note for system check

    warn_data = warnings.readlines()
    sugg_data = suggestions.readlines()
    pack_data = packages.read()
    shell_data = shells.readlines()

    return warn_data, sugg_data, pack_data, shell_data


def clean_data():
    warn, sugg, pack, shell = get_data()

    warn_clean = []
    for line in warn:
        warn_clean.append(line.split('|'))

    for i in range(len(warn_clean)):
        warn_clean[i] = warn_clean[i][:2]
    # print(warn_clean[i])

    sugg_clean = []
    for line in sugg:
        sugg_clean.append(line.split('|'))

    for i in range(len(sugg_clean)):
        sugg_clean[i] = sugg_clean[i][:2]
    # print(sugg_clean[i])

    pack_clean = []
    pack = pack.split('|')
    pack_clean = pack
    del pack_clean[0]

    shell_clean = []

    for i in range(len(shell)):
        shell_clean.append(shell[i].rstrip('\n'))
    # print(shell_clean[i])

    return warn_clean, sugg_clean, pack_clean, shell_clean


def convert_to_excel():
    warnings, suggestions, packages, shells = clean_data()

    try:
        os.mkdir('system_check')
    except(Exception):
        pass

    os.chdir('system_check')

    note = open("note.txt", "w+")
    note.write("This collection of system check file are solely based "
               "on lynis project and xlsx files are just the collection "
               "of categorized information.")
    note.close()

    warn_packages = []
    warn_text = []
    for i in range(len(warnings)):
        warn_packages.append(warnings[i][0])

    for i in range(len(warnings)):
        warn_text.append(warnings[i][1])

    print(warn_packages, warn_text)

    warn = pd.DataFrame()

    warn['Packages'] = warn_packages
    warn['warnings'] = warn_text

    # warn.to_excel('warnings.xlsx', index = False)

    writer = ExcelWriter('warnings.xlsx')

    warn.to_excel(writer, 'report1', index=False)

    workbook = writer.book
    worksheet = writer.sheets['report1']

    # Account info columns
    worksheet.set_column('A:A', 15)
    # State column
    worksheet.set_column('B:B', 45)
    # Post code
    # worksheet.set_column('F:F', 10)

    writer.save()

    sugg_packages = []
    sugg_text = []
    for i in range(len(suggestions)):
        sugg_packages.append(suggestions[i][0])

    for i in range(len(suggestions)):
        sugg_text.append(suggestions[i][1])

    # print(sugg_packages, sugg_text)

    sugg = pd.DataFrame()

    sugg['Packages'] = sugg_packages
    sugg['suggestions'] = sugg_text

    writer1 = ExcelWriter('suggestions.xlsx')

    sugg.to_excel(writer1, 'report2', index=False)

    workbook = writer1.book
    worksheet = writer1.sheets['report2']

    # Account info columns
    worksheet.set_column('A:A', 25)
    # State column
    worksheet.set_column('B:B', 120)
    # Post code
    # worksheet.set_column('F:F', 10)
    writer1.save()

    pack_data = pd.DataFrame()
    pack_data['Packages'] = packages
    writer1 = ExcelWriter('packages.xlsx')

    pack_data.to_excel(writer1, 'report3', index=False)

    workbook = writer1.book
    worksheet = writer1.sheets['report3']

    # Account info columns
    worksheet.set_column('A:A', 75)
    # State column
    # Post code
    # worksheet.set_column('F:F', 10)
    writer1.save()

    os.chdir('..')


if __name__ == '__main__':
    os.system("run.sh") # set up run.sh if not
    warnings, suggestions, packages, shells = clean_data()
    convert_to_excel()
