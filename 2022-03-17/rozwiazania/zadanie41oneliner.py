print(sum(1 for x in open('napisy.txt').read() if x.isnumeric()))
