import pandas
dem_data = pandas.read_csv("C:\Users\Devendra\Desktop\Software_carpentry_Feb_2017\Day 1\python\data\Dem_HealthData\TX.txt" , sep = '\t')
plt.scatter(dem_data['Population_Density'],dem_data['Poverty'])
plt.xlabel('Population Density')
plt.ylabel('Poverty')
plt.title('Relation between Population Density vs Poverty')
plt.show()