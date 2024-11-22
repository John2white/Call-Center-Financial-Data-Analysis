import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from Excel
file_path = "National Call Center.xlsx"  # Ensure this matches the uploaded file name
df = pd.read_excel(file_path)

# Task (a): Bar Charts for Mean and Median Current Account Balance by Caller Gender
mean_balance_caller = df.groupby('Caller Gender')['Current Amount Due'].mean()
median_balance_caller = df.groupby('Caller Gender')['Current Amount Due'].median()

plt.figure(figsize=(8, 5))
mean_balance_caller.plot(kind='bar', color='green', alpha=0.7, label='Mean')
median_balance_caller.plot(kind='bar', color='blue', alpha=0.7, label='Median', width=0.4, position=1)
plt.title("Mean and Median Current Account Balance by Caller Gender", fontsize=14)
plt.xlabel("Caller Gender", fontsize=12)
plt.ylabel("Current Account Balance", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()

# Task (b): Bar Charts for Mean and Median Current Account Balance by Account Holder Gender
mean_balance_holder = df.groupby('Account Holder Gender')['Current Amount Due'].mean()
median_balance_holder = df.groupby('Account Holder Gender')['Current Amount Due'].median()

plt.figure(figsize=(8, 5))
mean_balance_holder.plot(kind='bar', color='green', alpha=0.7, label='Mean')
median_balance_holder.plot(kind='bar', color='blue', alpha=0.7, label='Median', width=0.4, position=1)
plt.title("Mean and Median Current Account Balance by Account Holder Gender", fontsize=14)
plt.xlabel("Account Holder Gender", fontsize=12)
plt.ylabel("Current Account Balance", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()

# Task (c): Scatter Diagram of Current Balance vs Past Due Amount
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Current Amount Due', y='Past Due Amount', hue='Caller Gender')
plt.title("Scatter Plot of Current Balance vs Past Due Amount", fontsize=14)
plt.xlabel("Current Amount Due", fontsize=12)
plt.ylabel("Past Due Amount", fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Task (d): Descriptive Statistics for Current Account Balance
descriptive_stats_balance = df.groupby(['Caller Gender', 'Account Holder Gender', 'Was this a Billing Question?'])['Current Amount Due'].describe()
print("\nDescriptive Statistics for Current Account Balance:")
print(descriptive_stats_balance)

# Task (e): Descriptive Statistics for Past Due Balances
descriptive_stats_past_due = df.groupby(['Caller Gender', 'Account Holder Gender', 'Was this a Billing Question?'])['Past Due Amount'].describe()
print("\nDescriptive Statistics for Past Due Amount:")
print(descriptive_stats_past_due)
