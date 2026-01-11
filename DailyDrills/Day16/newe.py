from numpy.ma.core import left_shift
from prettytable import PrettyTable
table = PrettyTable()


table.add_column("Name", ["Abenezer", "Samuel", "Arsema"])
table.add_column("age", [20,6,0])

table.align = "c"
print(table)