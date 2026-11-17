# third party modules are not inbuilt in python 
# third party modules are installable
# third party modules are in form of packages and bundles
# how to install third party modules 
# examples : python pip install modulename 
# examples : python -m pip install pandas numpy seaborn openpyxl
# how to check third party modules are installed or not 
# examples : python -m pip show pandas  
# Name: pandas
# Version: 3.0.5
# Summary: Powerful data structures for data analysis, time series, and statistics
# Home-page: https://pandas.pydata.org
# Author:
# Author-email: The Pandas Development Team <pandas-dev@python.org>
# License: BSD 3-Clause License

import pandas as pd
emp={
    "name":["om","smith","jay","rishikesh","brijesh"],
    "age":[21,22,23,24,35]
}

# pandas create a tabular layout or in dataframes 
df=pd.DataFrame(emp)
print(df)