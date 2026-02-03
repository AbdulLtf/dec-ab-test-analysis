# A/B Test Analysis Project: From Raw Logs to Business Intelligence

## 🚀 Overview
Welcome to the A/B Test Analysis Project. Our mission was to transform noisy, multi-faceted datasets from five concurrent e-commerce experiments into clear, actionable business strategies. This project represents a journey through complex data cleaning, rigorous statistical verification, and robust automation.

## 📊 The Analytical Journey
Analyzing concurrent tests is inherently challenging. We went beyond simple "Control vs. Treatment" checks to ensure that every recommendation was backed by "purified" data. Our journey involved three critical stages:

### 1. The Purification Phase (Data Integrity)
Raw logs are often messy. We identified and resolved several critical errors that could have misled our decisions:
- **Deduplication**: We removed nearly **40% duplication** in some tests (like Test 4). Without this, our results would have looked artificially precise.
- **Outlier Control**: We used **Winsorization** to stop "Whale" customers (unusually large single orders) from skewing our averages and hiding genuine behavioral trends.
- **Missing Metric Restoration**: We implemented logic to automatically derive missing indicators (like `is_purchase` and `date`) directly from behavioral signals, restoring the ability to analyze tests that were previously considered "broken."

### 2. The Scalability Fix (Multi-Variant Analysis)
Standard analysis scripts often assume only two groups (Control & Treatment). However, our **"Test 3: Product"** experiment introduced a third variant. We redesigned our engine to:
- Dynamically detect any number of treatment variants.
- Perform individual statistical comparisons for each variant against the control.
- Consolidate all these findings into a unified, easy-to-read summary table.

### 3. The Stakeholder Transformation
Data is only useful if it's understood. We've provided two layers of reporting:
- **For Technical Teams**: The [ab_test_analysis.ipynb](ab_test_analysis.ipynb) contains full statistical rigor (Z-Tests, T-Tests, and visual distributions).
- **For Business Leadership**: The [executive_summary.md](executive_summary.md) speaks in plain English, focusing on "Launch" vs. "Reject" decisions.

## 📂 The Datasets
Located in the `raw dataset/` folder, these files represent the core of our platform optimization:

1. **Test 1: Menu Optimization** (`test1_menu.csv`): Testing a new horizontal menu layout.
2. **Test 2: Novelty Slider** (`test2_novelty_slider.csv`): Gauging the impact of differently highlighted new arrivals.
3. **Test 3: Product Sliders** (`test3_product_sliders.csv`): A complex, multi-variant test on geometric product arrangements.
4. **Test 4: User Reviews** (`test4_reviews.csv`): Exploring if more prominent reviews increase trust and conversion.
5. **Test 5: Search Algorithm** (`test5_search_engine.csv`): Tuning search efficiency to help users find products faster.

## 🛠️ Project Structure
- `ab_test_analysis.ipynb`: The main analytical workhorse.
- `executive_summary.md`: The non-technical findings.
- `plan.md`: Consolidated project history and task tracking.
- `helper/`: Contains `helper.py`, our specialized maintenance utility.

## 🔬 How to Run
1.  Verify that all 5 CSV files are in the `raw dataset/` folder.
2.  Open `ab_test_analysis.ipynb`.
3.  **Run All Cells**. The notebook will clean the data, derive missing metrics, and generate the final summary report automatically.

---
**Statistical Standards**: All tests use a **95% Confidence Interval** ($p < 0.05$).
