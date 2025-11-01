df = pd.read_csv("products.csv")
dd = pd.read_csv("orders.csv")

print(df.head())
print(df.tail(10))

print(dd.head())
print(dd.tail(10))

merge=pd.merge(df,dd,on="ProductID")
merge.insert(7,"Total Revenue",merge["Price"] * merge["Quantity"])
TotalRev=merge["Total Revenue"].sum()
print("Total rev is: ",TotalRev)

sales=merge.groupby("ProductName")["Quantity"].sum()
top=sales.sort_values(ascending=False).head()
bottom=sales.sort_values(ascending=True).head()
print("Top 5 best sellers are: ",top)
print("Top 5 worst sellers are: ",bottom)

avgprice=merge.groupby("Category")["Price"].mean()
print("Avg price per Category:",avgprice)

merge["OrderDate"]=pd.to_datetime(merge["OrderDate"],format="%m-%d-%Y")
merge["day"]=merge["OrderDate"].dt.day
merge["month"]=merge["OrderDate"].dt.month
merge["year"]=merge["OrderDate"].dt.year

day_rev=merge.groupby('day')["Total Revenue"].sum().idxmax()
month_rev=merge.groupby('month')["Total Revenue"].sum().idxmax()
year_rev=merge.groupby('year')["Total Revenue"].sum().idxmax()

print("day with max revenue: ",day_rev)
print("month with max revenue: ",month_rev)
print("year with max revenue: ",year_rev)

monthlyRev=merge.groupby("month")["Total Revenue"].sum()
print("Total Revenue by each month: ",monthlyRev)

print(merge.isnull().sum())

print("no null value")
