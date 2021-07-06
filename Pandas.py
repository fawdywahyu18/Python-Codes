import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')

def convert_price_string_to_float(txt):
    return float(txt[1:])

df['item_price'] = df['item_price'].apply(convert_price_string_to_float)

# Show the first 10 rows
print(df.head(10))

# Show random 10 rows of dataframe
print(df.sample(n=10))

# Rows where order_id is 21
print(df[df['order_id'] == 21])

# Rows where quantity is larger than 4
print(df[df['quantity'] > 4])

# Creating new column called customer price
tax_rate = 0.06
df['VAT'] = df['item_price'] * tax_rate
df['customer_price'] = df['item_price'] + df['VAT']
print(df['customer_price'].head(10))

# Find the total VAT (Value added tax)
total_VAT = df['VAT'].sum()
print(total_VAT)

# Grouping by item_names and sum
quant_by_item = df.groupby('item_name')['quantity'].sum()
print(quant_by_item)

# Top 10 barang yang dijual
quant_by_item_sorted = quant_by_item.sort_values(ascending=False)
q_by_item_top10 = quant_by_item_sorted.head(n=10)
print(q_by_item_top10)

# Creating bar graph
import matplotlib.pyplot as plt
_ = q_by_item_top10.plot.bar(figsize=(10,10))

# Challenge!!

# Top 10 item by revenues
df['revenues'] = df['quantity'] * df['item_price']
rev_by_item = df.groupby('item_name')['revenues'].sum()
rev_top10 = rev_by_item.sort_values(ascending=False).head(10)
graph_rev = rev_top10.plot.bar(figsize=(10,10))

# Creating new column with multiple conditions
def test_group(test):
    if ('Chicken' in test['item_name'])==True:
        return 'Chicken'
    elif ('Beef' in test['item_name'])==True or ('Steak' in test['item_name'])==True:
        return 'Beef'
    elif ('Carnitas' in test['item_name'])==True:
        return 'Pork'
    else:
        return 'Not Meat'
    
# Aggregating based on the group_meat column
df['group_meat'] = df.apply(test_group, axis=1)
rev_by_group1 = df.groupby('group_meat')['revenues'].sum()
rev_group1_top10 = rev_by_group1.sort_values(ascending=False).head(10)
graph_group = rev_group1_top10.plot.bar(figsize=(10,10))