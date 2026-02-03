# A/B Test Analysis: Executive Summary

## Overview
We conducted five simultaneous A/B tests to optimize our e-commerce platform's user experience and financial performance. This report analyzes the impact of these changes on **Customer Conversion (Purchases)** and **Revenue**.

## The Experiments
We tested changes across the following areas:
1.  **Menu Layout**: Does a new horizontal menu help users find products faster?
2.  **Novelty Slider**: Does highlighting "New Items" differently drive more sales?
3.  **Product Display**: Do new geometric slider arrangements appeal more to users?
4.  **User Reviews**: Does making reviews more prominent increase trust and sales?
5.  **Search Engine**: Does tuning our search algorithm help users find what they want?

## Key Findings

| Experiment | Status | Result | Key Metric Uplift | Decision |
| :--- | :--- | :--- | :--- | :--- |
| **Test 1: Menu** | 🔴 Negative | **Control Won** | Rev: -10.51% | **Do Not Release** |
| **Test 2: Novelty** | 🟢 Positive | **Treatment Won** | Rev: +5.81% | **Role Out** |
| **Test 4: Reviews** | 🟡 Neutral | Inconclusive | CR: +0.80% | Iterate |
| **Test 5: Search** | 🟡 Neutral | Inconclusive | CR: +4.93% | Collect More Data |

> **Note**: Test 3 was excluded due to data quality issues.

For detailed analysis, see [executive_summary.md](executive_summary.md) and the analysis notebook.

---

## Technical Details
For the data science team and stakeholders requiring deep dives:

### Methodology
- **Statistical Significance**: We used Z-Tests for conversion rates (Proportions) and T-Tests for revenue (Means).
- **Confidence Level**: All tests are evaluated at a 95% confidence interval ($p < 0.05$).

### How to Run the Analysis
1.  Ensure you have the `raw dataset/` folder containing the 5 CSV files.
2.  Open `ab_test_analysis.ipynb` in Jupyter Notebook or VS Code.
3.  Run all cells. The notebook will:
    - Load and clean data from all 5 experiments.
    - Handle inconsistencies in data logging (e.g., missing revenue tracking in Reviews test).
    - Generate comparative charts and a summary table.
