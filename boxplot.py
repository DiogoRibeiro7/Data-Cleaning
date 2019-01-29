plt.subplots(figsize=(10,8))
sns.boxplot(df.unit_price)

plt.xlabel('Unit Price')
plt.title('Boxplot for Unit Price')
plt.show()