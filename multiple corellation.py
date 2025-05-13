import pandas
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pandas.DataFrame([["A", 4, 0, 1, 27], 
                         ["B", 7, 1, 1, 29], 
                         ["C", 6, 1, 0, 23], 
                         ["D", 2, 0, 0, 20], 
                         ["etc.", 3, 0, 1, 21]], 
                         columns=["ID", "score", "male", "age20", "BMI"])
print (data.corr())

model = ols("BMI ~ score + male + age20", data=data).fit()
print (model.params)
print (model.summary())