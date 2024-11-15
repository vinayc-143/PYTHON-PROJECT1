import pandas as pd
df = pd.read_csv('Dataset .csv')
cuisine_count = df['Cuisines'].value_counts()
top_cuisine=cuisine_count.head(3)
total_restaurant=df.shape[0]
total_restaurant_percentage=(top_cuisine/total_restaurant)*100
print("Top 3 Cuisines")
print(top_cuisine)
print("\n Percentage of restaurant serving top cuisine")
print(total_restaurant_percentage)