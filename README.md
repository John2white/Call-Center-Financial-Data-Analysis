# National Call Center Data Analysis

This project analyzes data from the National Call Center using Python in Google Colab. The analysis involves creating visualizations and computing descriptive statistics to understand variables such as **Current Amount Due**, **Past Due Amount**, **Caller Gender**, and **Account Holder Gender**.

---

## Features
1. **Bar Charts**: Visualize mean and median account balances by gender.
2. **Scatter Plot**: Analyze the relationship between current account balance and past due amount.
3. **Descriptive Statistics**: Compute key metrics (mean, median, standard deviation, etc.) for account balances and past due amounts based on grouping variables.

---

## Setup and Requirements

1. Open the provided Google Colab notebook.
2. Upload the dataset (`National Call Center.xlsx`) to Colab each time the notebook is run.
3. Required libraries are installed automatically in Colab. If missing, install them with:
   ```python
   !pip install pandas matplotlib seaborn
File Structure
plaintext
Copy code
.
├── National Call Center.xlsx  # Input dataset (uploaded to Colab)
├── analysis_notebook.ipynb    # Colab notebook containing the analysis
└── README.md                  # Documentation file
Usage Instructions
Open Google Colab:

Upload the analysis_notebook.ipynb to Colab or create a new notebook and copy the provided code.
Upload Dataset:

Use the Colab file upload functionality to upload National Call Center.xlsx at runtime.
Execute the Notebook:

Run each cell in sequence to perform the analysis.
View Outputs:

Visualizations will display inline within the notebook.
Descriptive statistics are printed in tabular form in the output cells.
Analysis Tasks
Task (a): Generate bar charts for the mean and median current account balances by caller gender.
Task (b): Generate bar charts for the mean and median current account balances by account holder gender.
Task (c): Create a scatter plot to show the relationship between the current account balance and the past due amount.
Task (d): Compute descriptive statistics for the Current Account Balance, grouped by:
Caller Gender
Account Holder Gender
Whether the call was a billing question.
Task (e): Compute descriptive statistics for the Past Due Amount with the same grouping as above.
Customization
Replace National Call Center.xlsx with your dataset.
Adjust the grouping variables or plot parameters as needed in the code.
Output
Visualizations:
Bar Charts: Mean and median account balances.
Scatter Plot: Relationship between current account balance and past due amount.
Descriptive Statistics:
For Current Amount Due and Past Due Amount:

Includes key metrics such as mean, median, standard deviation, minimum, and maximum values.
Libraries Used
pandas: For data manipulation and aggregation.
matplotlib: For creating bar charts and scatter plots.
seaborn: For enhanced statistical plotting.
