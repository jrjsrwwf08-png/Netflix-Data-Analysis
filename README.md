# Netflix-Data-Analysis
Analyzing and visualizing the Netflix library using Python through six tasks presented by Auspify Technologies

## Tasks Progress
- [x] Task 1 : Netflix Data Cleaning & Preparation
- [x] Task 2 : Content Type Analysis
- [ ] Task 3 : Country-Wise Content Analysis
- [ ] Task 4 : Content Rating & Genre Analysis
- [ ] Task 5 : Trend Analysis by Release Year
- [ ] Task 6 : Netflix Business Insights Report

## Task 1

This task focuses on cleaning and preparing the raw Netflix catalog dataset for analytical workflows and reporting 
Raw datasets often suffer from missing values, inconsistent string casing, unparsed dates, and mixed metric units—all of which were resolved in this phase

### 📊 Before vs. After Summary

| Metric / Field | Raw Dataset | Cleaned Dataset | Transformation Logic |
| :--- | :--- | :--- | :--- |
| **Total Records** | 8,790 | 8,790 (or cleaned count) | Verified uniqueness & handled nulls |
| **Missing `director`** | ~2,634 missing | 0 nulls | Replaced with `'Unknown'` |
| **Missing `country`** | ~831 missing | 0 nulls | Mode imputation / `'Unknown'` |
| **`date_added` Format** | String (e.g., "September 25, 2021") | Datetime (`YYYY-MM-DD`) | Parsed using `pd.to_datetime` |
| **`duration` Structure** | Mixed String ("90 min", "2 Seasons") | Numeric + Unit separated | Regex / String splits |

---

### 📁 Task Artifacts
* `Dataset.csv`: Raw, unedited dataset.
* `02_data_cleaning.ipynb`: Jupyter notebook containing the full cleaning script and validation checks.
* `cleaned_netflix.csv`: Processed, production-ready dataset.

## Task 2
Analyzing the baseline distribution and proportions of Movies and TV Shows available on Netflix

### Key points :
* Total Titles Analyzed : 8790
* Movies Count : 6126 (69.7%)
* TV Shows Count : 2664 (30.3%)

### Visualization
![Netflix Content Type Analysis](Content-Type-Analysis-Dashboard/img1.png)
![Netflix Content Type Analysis](Content-Type-Analysis-Dashboard/img2.png)

### Business Insights And Recommendations
* **Most Preferred Content :** Movies make up approximately **70%** of the total library driven by rapid production and release cycles
* **Engagement vs. Volume :** While movies account for the majority of the content TV series are the primary driver of long term user retention and subscription growth
* **Strategic Move :** Netflix should balance its content portfolio by increasing investment in TV series to reduce churn rates
