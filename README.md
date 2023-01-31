# library-eda

*Project Description*
Our team conducted an exploratory data analysis to answer the question: How has COVID-19 impacted US library services and patronage?

*Contributors*
- Vanessa Walden
- Olivia Montesano
- Mary Marcontell
- Gabriela Lopez
- Nicole Campos

*Who will this inform?*
This analysis may assist library directors, policymakers, activists, and educators in making informed decisions about the strategic management and support of libraries.

*Key Questions*
- After the COVID-19 pandemic began:
- How did per capita expenditures change?
- How did library patronage change?
- Is there a correlation between expenditures and library usage?

*Approach*
Our team used annual US survey data from the Institute of Museum and Library Services, which  examines when, where, and how library services are changing to meet the needs of the public. These data are supplied annually by 17,000 public library systems across the United States and its territories. 

*Manipulations Conducted*
- Cleaned the data to include only the columns we needed
- Input needed columns (179 columns) into data frames for each year
- Merged the data frames into a single dataframe
- Calculated per capita: expenditures, library visits, and registered users
- Collapsed regions based on US Census Five Regions

*Software / Libraries*
Jupyter Notebooks, Pandas, Numpy, Matplotlib, Scipy.stats

*Limitations and Challenges*
Notably, several limitations arose in reviewing survey data (meaning, results should be interpreted directionally):
- Survey field dates are not the same for every library, meaning the variability we see in the data may be due in part to different survey fielding periods
- Similarly, budget data is recorded during different time periods for each library
- The survey uses self-reported data, which is subjective and imprecise
- Library visit count may be inaccurate (e.g., people exiting the facility and returning later would count as two separate visitors)
- Web visits were not tracked until 2018
- 2021-2022 library data unavailable to compare and further illustrate COVID-19’s impact

*Conclusions*
- The Southwest sees the highest number of users and expenses per capita; US libraries generally experienced declines in usership in 2020.
- Correlations show that expenditures have little to do with program attendance and circulation.
- Expenditures fell for print collections and rose for digital.
- Library patronage decreased after the pandemic began.
