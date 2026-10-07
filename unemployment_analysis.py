import pandas as pd
import matplotlib.pyplot as plt

# Load the India unemployment dataset
df = pd.read_csv("Unemployment in India.csv")

# Clean column names and dates
df.columns = [column.strip() for column in df.columns]
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")

# Convert numeric columns
numeric_columns = [
    "Estimated Unemployment Rate (%)",
    "Estimated Employed",
    "Estimated Labour Participation Rate (%)"
]
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Monthly average unemployment rate
monthly = (
    df.groupby("Date", as_index=False)["Estimated Unemployment Rate (%)"]
      .mean()
)

# Plot overall trend
plt.figure(figsize=(10, 5))
plt.plot(
    monthly["Date"],
    monthly["Estimated Unemployment Rate (%)"],
    marker="o"
)
plt.axvline(pd.Timestamp("2020-03-01"), linestyle="--")
plt.xlabel("Date")
plt.ylabel("Average unemployment rate (%)")
plt.title("India Average Unemployment Rate, 2019–2020")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# COVID-19 comparison
before_covid = df[df["Date"] < "2020-03-01"]["Estimated Unemployment Rate (%)"].mean()
march_2020 = df[df["Date"].dt.to_period("M") == "2020-03"]["Estimated Unemployment Rate (%)"].mean()
april_may = df[df["Date"].between("2020-04-01", "2020-05-31")]["Estimated Unemployment Rate (%)"].mean()
june_2020 = df[df["Date"].dt.to_period("M") == "2020-06"]["Estimated Unemployment Rate (%)"].mean()

print(f"Before COVID (May 2019–Feb 2020): {before_covid:.2f}%")
print(f"March 2020: {march_2020:.2f}%")
print(f"April–May 2020: {april_may:.2f}%")
print(f"June 2020: {june_2020:.2f}%")

# Regional comparison
regional = (
    df.groupby("Region")["Estimated Unemployment Rate (%)"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(9, 5))
plt.barh(regional.index[::-1], regional.values[::-1])
plt.xlabel("Average unemployment rate (%)")
plt.title("10 Regions with Higher Average Unemployment Rates")
plt.tight_layout()
plt.show()
