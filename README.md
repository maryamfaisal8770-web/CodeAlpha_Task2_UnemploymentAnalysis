# Unemployment Analysis in India — CodeAlpha Task 2

## Project Overview
This project analyzes unemployment trends in India using the dataset supplied for the CodeAlpha Data Science Internship.

The analysis focuses on:
- Overall unemployment trends from 2019 to 2020
- The sharp change around the beginning of the COVID-19 period
- Monthly patterns in the available data
- Regional differences in average unemployment rates

## Dataset
The supplied `Unemployment in India.csv` contains regional unemployment observations from May 2019 to June 2020. The main variables include estimated unemployment rate, estimated employment, labour participation rate, region, date, frequency, and area.

## Analysis
The data was cleaned by removing extra spaces from column names, converting dates to a standard datetime format, and converting numeric measures to numeric values.

### COVID-19 period
The average unemployment rate before March 2020 was **9.51%**. It increased to **10.70%** in March 2020, then reached **23.64%** in April and **24.88%** in May.

The May 2020 monthly average was the highest point in the dataset at **24.88%**. By June 2020, the average had fallen to **11.90%**, showing a substantial short-term decline from the April–May peak.

These figures show a strong disruption around the early COVID-19 period. The dataset alone does not establish that COVID-19 was the sole cause of every change, but the timing coincides with the beginning of the pandemic period.

## Key Findings
1. Unemployment was relatively stable around 9–10% during most of the 2019 period.
2. The rate increased in early 2020, before a much larger spike in April and May.
3. May 2020 recorded the highest monthly average unemployment rate in the available data.
4. The rate declined considerably in June 2020, although it remained above most 2019 monthly averages.
5. Regional averages varied, showing that unemployment was not distributed equally across regions.

## Seasonal and Long-Term Patterns
The available period is only about 14 months, so it is too short to make a strong claim about recurring annual seasonality. The clearest pattern is a major short-term disruption in 2020 rather than a reliable multi-year seasonal cycle.

## Files
- `unemployment_analysis.ipynb` — complete analysis notebook
- `unemployment_analysis.py` — source code
- `Unemployment in India.csv` — supplied dataset
- `monthly_unemployment_summary.csv` — monthly summary used in the analysis
- PNG files — visualizations
- `README.md` — project documentation

## Tools
Python, Pandas, Matplotlib
