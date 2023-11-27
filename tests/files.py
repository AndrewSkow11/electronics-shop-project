import os

relative_path = "items_for_test.csv"
absolute_path = os.path.abspath(relative_path)

print(absolute_path)