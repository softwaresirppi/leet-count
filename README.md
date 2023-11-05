# What?
A python script to fetch the number of problems solved from leetcode link(s)

# How to use?
## If you have a leetcode username, invoke it like this.
`python3 leet_count.py username`
This will print the number of problems solved by that user to the stdout.
## If you have a CSV file with leetcode links in it, invoke it like this.
`python3 leet_count_csv.py input.csv output.csv`
This will read into the `input.csv`, finds a leetcode link in each row (if there are many, last one will be picked) and populates a new column with the number of problems solved into the `output.csv`
