from numpy import product
from app import sorted_rules
from functools import wraps

def get_recommendations(target_prod):
    recommendations = set()
    for i, products in enumerate(sorted_rules['antecedents']):
        for product in list(products):
            if product == target_prod:
                recommended = list(sorted_rules.iloc[i]['consequents'])[0]
                recommendations.add(recommended)

    return {"response":tuple(recommendations)}

