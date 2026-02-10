# A/B Test Analysis Project: From Data Verification to Business Strategy

## 🚀 Overview
This project is a professional-grade A/B testing suite designed to analyze behavioral data from five concurrent e-commerce experiments. It automates the transition from raw csv logs to a final business verdict, ensuring that every decision is backed by rigorous statistical validation.

---

## 🏗️ Project Structure
The repository is organized to maintain a clear separation between raw data, experimental logic, and business reporting:
- `ab_test_analysis_v2.ipynb`: **The Analytical Engine**. A documentation-rich Jupyter Notebook that performs data loading, verification, and statistical testing.
- `executive_summary.md`: **Stakeholder Brief**. A concise summary of winning/losing variants and recommended business actions.
- `experiment_summary.xlsx`: **Automated Data Export**. The final results table, including conversion lifts and p-values, formatted for reporting.
- `helper/`: Internal utility folder containing methodology definitions like `validation.py`.
- `raw dataset/`: Source folder containing the 5 CSV files for the Menu, Novelty, Product, Reviews, and Search experiments.

---

## 🛠️ Tech Stack & Libraries
The analysis is built on a robust Python data science stack:
- **Python 3.13+**: The core language for processing.
- **Pandas**: Used for high-performance data manipulation and cleaning.
- **NumPy**: Powers the underlying mathematical and vector operations.
- **SciPy (stats)**: The statistical engine used for T-Tests (Revenue) and Chi-Square tests (SRM).
- **Statsmodels**: Handles Z-Tests for proportions and Multiple Testing Correction (Holm-Bonferroni).
- **Matplotlib & Seaborn**: Generates professional-grade statistical visualizations.
- **Openpyxl**: Manages the export to Excel workbooks.

---

## 🔬 How the Analysis Works (Simple View)
Think of this pipeline as a digital "Scientific Lab":
1.  **Incoming Data**: We load raw user behavior from various tests into the system.
2.  **Health Check (Validation)**: Before trusting any result, we check if the test was "fair" (e.g., did 50% of people really go to the control group? Is the traffic steady?).
3.  **The Comparison**: We compare the **Control** (Original version) against the **Treatment** (New version).
4.  **Statistical Guardrails**: We look at "P-values". In simple terms, this tells us: *"Is this win real, or just a lucky coincidence?"*. We only declare a winner if the win is likely real.
5.  **Final Report**: The system automatically types up a summary in Excel and identifies which experiments are **Winners**, which are **Losers**, and which need more time (**Inconclusive**).

---

## 🏁 How to Use
1.  Ensure all experiment data is saved in the `raw dataset/` folder.
2.  Install required libraries: `pip install pandas numpy scipy statsmodels matplotlib seaborn openpyxl`.
3.  Open `ab_test_analysis_v2.ipynb` in your favorite environment (Jupyter, VS Code) and select **Run All**.
4.  Check `experiment_summary.xlsx` for the final verdict on all 5 tests.

---
**Author**: Muhammad Abdul Lathief  
**Version**: 4.0 (Enhanced Clarity & Stakeholder Documentation)
