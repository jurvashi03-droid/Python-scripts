import pandas as pd

# Load the two CSV files
may_list = pd.read_csv("MMH Class of 2026 Personal Emails - May list.csv")
aug_list = pd.read_csv("MMH Class of 2026 Personal Emails 8.14- Aug list.csv")

# Extract email columns and normalize
may_emails = set(may_list["Email Address"].str.strip().str.lower())
aug_emails = set(aug_list["Email"].str.strip().str.lower())

# Find common emails
common_emails = may_emails & aug_emails

# Find emails in Aug list but not in May list
new_emails = aug_emails - may_emails

# Create DataFrames for output
common_df = pd.DataFrame({"Email": sorted(common_emails)})
new_df = pd.DataFrame({"Email": sorted(new_emails)})

# Display results
print("Emails in Both Lists:")
display(common_df)

print("\nNew Emails in Aug List Only:")
display(new_df)
