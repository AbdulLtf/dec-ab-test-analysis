# A/B Test Analysis Project: From Raw Logs to Business Intelligence

## 🚀 Overview
This project provides a professional-grade A/B testing analysis pipeline, transforming raw behavioral logs from five concurrent e-commerce experiments into actionable business strategies. The pipeline handles data purification, statistical validation, and automated reporting.

---

## 📊 The Unified Analysis Pipeline: Core Logic
Modern e-commerce requires scaling experimentation. This codebase is designed to handle **five concurrent A/B tests** through a single, standardized function (`analyze_experiment`), ensuring consistency across:
1.  **Menu Layout**: Horizontal vs. Vertical optimization.
2.  **Novelty Slider**: Evaluating algorithmic vs. manual curation.
3.  **Product Sliders**: Testing geometric vs. list layouts.
4.  **Reviews**: Prominence of user feedback.
5.  **Search Engine**: Tuning discovery algorithms.

### Educational Data Flow
The pipeline follows a strict sequence to ensure reliability:
1.  **Data Purification**: 
    - **Deduplication**: Removes redundant session logs (preventing artificial precision).
    - **Outlier Control**: Uses Winsorization to mitigate "whales" that skew results.
2.  **Validation Guardrails**: Confirms experimental integrity before testing.
3.  **Statistical Inference**: Calculates p-values and confidence intervals.
4.  **Automated Reporting**: Exports results to `experiment_summary.xlsx`.

---

## 🔬 Statistical Methodology & Theory

The project employs two primary statistical engines to evaluate performance at a **95% Confidence Level** ($\alpha = 0.05$).

### 1. Conversion Rate (CR): Two-Proportion Z-Test
**Theory**: The Conversion Rate is a **Bernoulli Trial** (purchase vs. no-purchase). For large sample sizes, the difference between two proportions follows a **Normal Distribution** based on the **Central Limit Theorem**.
-   **Why it's used**: It provides a robust framework to determine if a change in UI (like a new menu) significantly shifts user behavior.
-   **Formula Basis**: 
    $$ Z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})(\frac{1}{n_1} + \frac{1}{n_2})}} $$

### 2. Average Revenue (ARPU): Welch's T-Test
**Theory**: Standard Student’s T-Tests assume equal variances between groups (Homoscedasticity). However, e-commerce revenue is typically skewed and volatile. 
-   **Why it's used**: **Welch's T-Test** (unpaired t-test with unequal variance) is used because it does not assume equal variances or equal sample sizes. This makes it significantly more accurate for financial data.
-   **Formula Basis**: 
    $$ t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} $$

---

## 🛡️ Validation Framework: The Guardrail Suite

Results are only valid if the underlying experiment is healthy. We use three specific "Guardrail" checks:

### A. Sample Ratio Mismatch (SRM)
-   **Test**: Pearson's Chi-Square Test.
-   **Rationale**: Detects **assignment bias**. If we expect a 50/50 split but get 45/55, SRM indicates that the randomization engine failed or certain users (e.g., bots or power users) were systemically excluded from one group.

### B. Covariate Balance
-   **Test**: Chi-Square (Categorical) / ANOVA (Continuous).
-   **Rationale**: Ensures that groups are **statistically identical** at baseline. It verifies that factors like Device Type, Browser, and Region are distributed equally so that any lift is caused solely by the experiment.

### C. Temporal Stability
-   **Rationale**: Monitors the experiment's ratio day-by-day. It flags technical glitches (logging drops) or "Novelty Effects" where a short-term spike in interest fades quickly.

---

## 📂 Project Structure
- `ab_test_analysis.ipynb`: The core analytical workhorse implementing the pipeline.
- `executive_summary.md`: Strategic recommendations for stakeholders.
- `experiment_summary.xlsx`: Automated data export with detailed metrics.
- `raw dataset/`: Source CSV logs for all 5 experiments.

## 🏁 Interpretation & Usage

### Decision Matrix
- **Winner = Treatment**: Statistically significant positive uplift (p < 0.05, Uplift > 0).
- **Winner = Control**: Treatment performed significantly worse than baseline.
- **Winner = Inconclusive**: No significant difference detected (Underpowered or Neutral).

### How to Run
1. Place CSV files in `raw dataset/`.
2. Open `ab_test_analysis.ipynb` and **Run All Cells**.
3. Inspect `experiment_summary.xlsx` for the final verdict.

---
**Author**: Muhammad Abdul Lathief
**Version**: 3.0 (Comprehensive Educational Merge)
