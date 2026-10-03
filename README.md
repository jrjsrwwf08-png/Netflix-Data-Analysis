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
Cleaning and preparing the raw Netflix dataset (8,790 titles) for accurate business analytics and reporting.

---

### Task Workflow
* **Step 1: Data Import** — Loaded `Dataset.csv` using Pandas and inspected missing values and data types
* **Step 2: Missing Values** — Replace missing values ​​in `director` with `Unknown` and `country` with `Mode`
* **Step 3: Deduplication** — Removed duplicate rows and remove excess whitespace from the beginning and end of string fields
* **Step 4: Standardization** — Converted `date_added` to `datetime` (`YYYY-MM-DD`) 
* **Step 5: Dataset Export** — Exported the clean dataset to `Cleaned_Dataset.csv`.

---

### Summary of Cleaning Actions

| Column / Feature | Action Taken |
| :--- | :--- |
| **Missing Values** | Filled nulls in `director` and `country` with `'Unknown'` and `Mode` |
| **Text Casing & Spaces** | Remove whitespace and standardized casing across text columns |
| **`date_added`** | Parsed string dates into standard `YYYY-MM-DD` format |

---

### Task Artifacts
* `Dataset.csv` — Raw dataset
* `task1.ipynb` — Data cleaning script
* `Cleaned_Dataset.csv` — Final cleaned dataset

----

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
