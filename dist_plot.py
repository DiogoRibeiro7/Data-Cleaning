# quantity distribition plot
plt.subplots(figsize=(10,8))
sns.distplot(df.quantity[df.quantity < 100], label='Quantity').legend()

plt.xlabel('Quantity')
plt.ylabel('Normalized Distribution')
plt.title('Quantity Distribution')
plt.show()