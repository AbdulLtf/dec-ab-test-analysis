# A/B Test Analysis Project: From Raw Logs to Business Intelligence

## 🚀 Overview
This project provides a professional-grade A/B testing analysis pipeline, transforming raw behavioral logs from five concurrent e-commerce experiments into actionable business strategies. The pipeline handles data purification, statistical validation, and automated reporting.

## 📊 Methodology & Experiment Pipeline

The analysis follows a rigorous four-stage pipeline to ensure statistical validity and business relevance:

### 1. Data Integrity & Purification
Before analysis, data is subjected to a strict audit:
- **Deduplication**: Removes redundant session logs (often up to 40% in raw logs) to prevent artificial precision.
- **Outlier Control (Winsorization)**: Mitigates the impact of extreme revenue values ("whales") that can skew mean-based metrics.
- **Metric Restoration**: Automatically derives key indicators like `is_purchase` from behavioral signals (`added_to_cart` or `revenue > 0`) when missing.

### 2. Analytical Validation
Each experiment is validated against core experimental assumptions:
- **Sample Ratio Mismatch (SRM)**: Uses a Chi-square test to ensure the assignment between groups followed the intended distribution.
- **Covariate Balance**: Verifies that non-experimental factors (device, browser) are balanced across variants.
- **Temporal Stability**: Checks if conversion rates are stable over the experiment duration.

### 3. Statistical Framework
Significant findings are determined using the following tests at a **95% Confidence Level** ($\alpha = 0.05$):
- **Conversion Rate (CR)**: Two-proportion Z-test.
- **Average Revenue Per User (ARPU)**: Welch’s t-test (handles unequal variances).
- **Multiple Comparisons**: (Planned Improvement) Integration of Bonferroni correction for multi-variant tests.

### 4. Automated Reporting
The pipeline generates an `experiment_summary.xlsx` file containing:
- Statistical results (Uplift, P-values).
- Automatic winner detection (Control vs. Treatment vs. Inconclusive).
- A complete data dictionary for stakeholders.

## 📂 Project Structure
- `ab_test_analysis.ipynb`: The core analytical workhorse implementing the pipeline.
- `executive_summary.md`: Non-technical findings and strategic recommendations for stakeholders.
- `experiment_summary.xlsx`: Automated data export with detailed metrics.
- `raw dataset/`: Source CSV logs for all 5 experiments.

## 🔬 Interpretation Guide

### Understanding the Results
- **Winner = Treatment**: The variant showed a statistically significant positive uplift in Conversion Rate.
- **Winner = Control**: The variant performed significantly worse than the baseline.
- **Winner = Inconclusive**: No statistically significant difference was detected (often due to insufficient sample size or neutral impact).

### How to Run
1. Ensure all CSV files are in the `raw dataset/` directory.
2. Open `ab_test_analysis.ipynb` in a Jupyter environment.
3. **Run All Cells**. The notebook will execute the full purification and analysis pipeline, outputting visual trends and saving the Excel summary.

---
**Author**: Muhammad Abdul Lathief
**Version**: 2.0 (Industry Ready Audit)
