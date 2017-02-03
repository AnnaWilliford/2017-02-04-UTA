import sys
import pandas
import matplotlib.pyplot

file_name=sys.argv[1]
col1=sys.argv[2]
col2=sys.argv[3]

print col1
print col2
print file_name


dem_data = pandas.read_csv(file_name , sep = '\t')
matplotlib.pyplot.scatter(dem_data[col1],dem_data[col2])
matplotlib.pyplot.xlabel(col1)
matplotlib.pyplot.ylabel(col2)
matplotlib.pyplot.show()