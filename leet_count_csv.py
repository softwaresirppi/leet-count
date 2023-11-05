from leet_count import *
from csv import *
from re import match
from sys import argv

leetcode_url_pattern = r'https:\/\/leetcode\.com\/(\w+)/?'

output = writer(open(argv[2], 'w'))
with open(argv[1], 'r') as input:
    for row in reader(input):
        username = None
        for cell in row:
            found = match(leetcode_url_pattern, cell)
            if found:
                username = found.group(1)
        print(f'FETCHING {username}')
        row.append(str(solved(username)))
        output.writerow(row)
print('LEET COUNT FINISHED')
