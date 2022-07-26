import pandas as pd

from flask import Flask
from mlxtend.frequent_patterns import apriori, association_rules

app = Flask(__name__)

df = pd.read_excel('app\dataset\GleanInvoice.xlsx')
df = df.groupby(['Invoice', 'ProductID'])['Quantity'].sum().unstack().fillna(0).applymap(lambda x: True if x > 0 else False)

freq_itemsets = apriori(df, min_support=0.01, use_colnames=True)
freq_itemsets.sort_values("support", ascending=False)

rules = association_rules(freq_itemsets, metric="support", min_threshold=0.01)
rules.sort_values("support", ascending=False)

sorted_rules = rules.sort_values("lift", ascending=False)


from app import endpoint