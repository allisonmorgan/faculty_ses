# faculty_ses

Replication code for "Socioeconomic Roots of Academic Faculty". Due to the substantial risk of re-identification, the personally identifiable information it contains, and the terms of the consent agreement by participants, we cannot make the underlying data set publicly available. However, we are happy to share the data under an IRB-approved data sharing agreement that carries through appropriate protections for limiting the risk of re-identification.

Notebooks are ordered in the way they were executed. Outside of this repository, we have a notebook that merges the raw survey responses from all disciplines with USWNR / NRC institutional rankings into CSV files for the frame and respondents. Next `2_zipcode_information.ipynb` merges responses to benchmarks available from the U.S. Census, IRS, and NSF SED. The data produced here is used for all subsequent analyses. 

We have several notebooks for studying differences in income (`3_income_analysis.ipynb`), education (`4_education_analysis.ipynb` & `5_education_regression.ipynb`), and urban / rural upbringing (`6_geospatial_differences.ipynb`) relative to national benchmarks. The last two notebooks use our survey responses and national data to build the probabilistic model of becoming faculty given parents' education (`7_forecasting.ipynb`), and consider how representative our survey sample is given the survey frame (`8_post_stratification.ipynb`).

Analysis relies on matplotlib (3.3.3), numpy (1.19.5), pandas (1.2.0), scipy (1.6.0), seaborn (0.11.1), statsmodels (0.12.1), and geopandas (0.8.2).
