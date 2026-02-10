# A/B Test Analysis Project: From Data Science to Business Strategy

## 🚀 Project Mission (Goals)
The primary objective of this project is to provide a comprehensive, scientifically rigorous analysis of five concurrent A/B tests. We aim to:
1.  **Validate Integrity**: Ensure that experimental data is healthy and unbiased.
2.  **Quantify Impact**: Measure the exact uplift in engagement and revenue caused by UI/UX changes.
3.  **Guide Strategy**: Provide clear, data-driven recommendations for product deployment.

---

## 🏆 The Executive Verdict: Results & Insights
This section summarizes the final decisions for stakeholders based on the verified evidence from all five test datasets.

| Experiment | Revenue Impact | **Final Verdict** | **Strategic Reason (Plain English)** |
| :--- | :--- | :--- | :--- |
| **1. Menu Layout** | **-10.5% (Loss)** | ❌ **REJECT** | The dropdown menu frustrated users, causing them to spend less. Stick to original. |
| **2. Novelty Slider** | **+5.8% (Gain)** | ✅ **LAUNCH** | Personalized algorithm-based sorting outperformed manual curation. |
| **3. Product Sliders**| **+21.0% (Big Gain)**| ✅ **LAUNCH** | This is our **star performer**. Placing "Similar Products" at the top drove massive ROI. |
| **4. User Reviews** | **None** | ⚖️ **HOLD** | Prominent reviews didn't change behavior significantly. Needs more data/iteration. |
| **5. Search Results** | **+1.26% (Gain)** | ✅ **LAUNCH** | Small but reliable efficiency gain from the Algolia search algorithm. |

> [!IMPORTANT]
> **Total Revenue Opportunity**: By rolling out the winning variants for Tests 2, 3, and 5, we estimate a cumulative revenue growth of **~28%**.

---

## 📚 Key Definitions (Terms for Everyone)
To ensure transparency, here are the core concepts used in our analysis:
- **Baseline (Control)**: The original experience users get (Status Quo).
- **Variant (Treatment)**: The new experiment we are testing.
- **Uplift**: The percentage improvement (or loss) the new version caused.
- **P-Value (The "Luck" Check)**: A number that tells us if a win is real. If **P < 0.05**, the result is officially "Significant" and not just a lucky fluke.
- **SRM (Health Check)**: "Sample Ratio Mismatch". This tells us if the platform distributed traffic fairly (e.g., exactly 50/50).

---

## 🧪 The Scientific Engine (Methodology)
We use a high-fidelity statistical stack to ensure our conclusions are accurate:
1.  **Validation Suite**: 
    - **SRM Check**: Using Chi-Square to detect assignment bias.
    - **Covariate Balance**: Using **SMD (Standardized Mean Difference)** to ensure user groups (mobile vs. desktop) are identical before the test.
2.  **Conversion Analysis**: Calculated via a **Two-Proportion Z-Test**.
3.  **Revenue Analysis**: Calculated via **Welch's T-Test** (ideal for skewed financial data with unequal variances).
4.  **Integrity Guard**: **Holm-Bonferroni Correction** is applied to prevent "False Winners" when analyzing multiple tests at once.

---

## 🏗️ The Journey: Steps Taken & Obstacles Overcome
Developing this pipeline involved several technical hurdles and refinements:

### Phase 1: Clean Up & Audit
- **Obstacle**: Raw logs contained redundant sessions and extreme "Whale" users (outliers) that skewed the average revenue.
- **Solution**: Implemented rigorous data purification and Winsorization to stabilize the metrics.

### Phase 2: Logic Synchronization
- **Obstacle**: The initial notebook used basic math that missed subtle biases.
- **Solution**: Synchronized the notebook with advanced production scripts (`validation.py`), introducing SRM and SMD checks.

### Phase 3: Debugging the Pipeline
- **Obstacle**: We encountered a `NameError` during Excel export due to incorrect cell ordering and a "Visibility" bug in the Excel engine.
- **Solution**: Relocated export logic to the end of the pipeline and optimized the `ExcelWriter` configuration.

---

## 📂 Project Organization
- `ab_test_analysis_v2.ipynb`: **The Workhorse**. Contains all code, documentation, and charts.
- `README.md`: This document (The central source of truth).
- `experiment_summary.xlsx`: Automated results export for reporting.
- `raw dataset/`: The "Vault" containing the original 5 behavioral logs in CSV format.

---

## 🏁 Setup & Execution
- **Environment**: Python 3.13.9 (or newer).
- **Libraries**: `pip install pandas numpy scipy statsmodels matplotlib seaborn openpyxl`.
- **How to Run**: Open the notebook and select **"Run All"**. The system will automatically process all 5 datasets and output the results to Excel.

---
**Lead Author**: Muhammad Abdul Lathief  
**Version**: 5.0 (The Comprehensive Unified Edition)
