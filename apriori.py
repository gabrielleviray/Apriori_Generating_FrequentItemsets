# Apriori algorithm: Generating frequent itemsets
# Gabrielle Viray
# 9/16/2020
# CMPE : 255 Data Mining

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

dataset = [['Milk', 'Onion', 'Bread', 'Cheese', 'Cereals', 'Yogurt'],
           ['Oil', 'Onion', 'Bread', 'Cheese', 'Cereals', 'Yogurt'],
           ['Milk', 'Orange', 'Cheese', 'Cereals'],
           ['Milk', 'Eggs', 'Corn', 'Cheese', 'Yogurt'],
           ['Corn', 'Onion', 'Cheese', 'Ice cream', 'Cereals']]
           
# TransactionEncoder transforms the data into the correct format. Pandas helps us to create the dataframe:
# transforms dataset into a boolean array

print("\nBoolean Array:")
te = TransactionEncoder()  
te_ary = te.fit(dataset).transform(dataset) 
df = pd.DataFrame(te_ary, columns=te.columns_)
pd.set_option('display.max_columns',None)
pd.set_option('display.width', None)
print(df)

# Let us return the items and itemsets with at least 50% support: By default, apriori returns the column indices of the items, which is helpful for association rule mining.
# Set use_colnames=True to convert these integer values into the respective item names:

from mlxtend.frequent_patterns import apriori

frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
print("\nItems and Itemsets with at least 50% support:")
print(frequent_itemsets)

# The association_rules() function allows to (1) specify your metric of interest (2) the according threshold. In this notebook, the implemented measures are confidence and lift.
# Let's say you are interested in rules derived from the frequent itemsets only if the level of confidence is above the 60 % threshold (min_threshold=0.6):

from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
print("\nFrequent Itemsets with confidence level above 60% threshold:")
print(rules)

# Q1. Display associations rules for metric = 'lift' and min_threshold = 1.2
rules = association_rules(frequent_itemsets, metric="lift", min_threshold = 1.2)
print("\nFrequent Itemsets that have 'lift' score with a minimum of 1.2:")
print(rules)

# Q2. Display associations rules for metric = 'support' and min_threshold = 0.6
print("\nFrequent Itemsets that have 'support' score with a 60% threshold:")
rules = association_rules(frequent_itemsets, metric="support", min_threshold = 0.6)
print(rules)

# Let us add a new feature to the dataframe showing the length of antecedents. Following code does this feature creation:
print("\nDataframe which includes the length of antecedents:")
rules["antecedent_len"] = rules["antecedents"].apply(lambda x: len(x))
print(rules["antecedent_len"])

# Q3. At least 2 antecedents and confidence greater than or equal to 0.75
print("\nAt least 2 antecedents and confidence greater than or equal to 0.75:")
print(rules[  (rules["antecedent_len"] >= 2) & 
		(rules["confidence"] >= 0.75) ])

# Q4. support atleast 0.8 and lift atleast 1.00
print("\nSupport at least 0.8 and lift at least 1.00:")
print(rules[ (rules["support"] >= 0.8) &
	   (rules["lift"] >= 1.00) ])

# Q5. sort the rules in descending order first by length of antecedents and then by lift
