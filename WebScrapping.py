from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

web_url = "https://www.tofler.in/companylist/hyderabad"
page = requests.get(web_url)
soup = BeautifulSoup(page.content, "html.parser")

find = soup.find_all('table',class_="responsive-table")
tableheading = soup.find_all('th')

names = [titles.text.strip() for titles in tableheading]

import pandas as pd

df = pd.DataFrame(columns = names)

for rows in find:
    rows = rows.find_all('tr')
    for row in rows[1:]:
        data = row.find_all('td')
        rowdata = [row.text.strip() for row in data]
        print(rowdata)

        length = len(df)
        df.loc[length] = rowdata

# Assuming 'df' is your DataFrame
# Convert 'Incorp. Year' to numeric, handling potential errors
df['Incorp. Year'] = pd.to_numeric(df['Incorp. Year'], errors='coerce')

# Group by 'Incorp. Year' and count the number of companies
year_counts = df.groupby('Incorp. Year').size().reset_index(name='Company Count')

# Create the bar plot
plt.figure(figsize=(12, 6))  # Adjust figure size as needed
plt.bar(year_counts['Incorp. Year'], year_counts['Company Count'], color='skyblue')
plt.xlabel('Incorporation Year')
plt.ylabel('Number of Companies')
plt.title('Number of Companies Incorporated Each Year')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()
df.to_csv(r'C:\Users\TEJESWARSAI\Documents\webscrapper.csv')
df