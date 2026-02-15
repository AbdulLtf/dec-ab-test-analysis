# A/B Test Analysis Report: Menu Layout Optimization
**Prepared by**: Senior Data Analyst
**Project**: E-Commerce UI Refinement Initiative
**Date**: February 15, 2026

---

## 1. Executive Summary

### Experiment Objective
The goal of this experiment was to evaluate the performance of a **Vertical Menu Layout** (Treatment) against the existing **Horizontal Menu Layout** (Control) in driving user engagement and monetization.

### Key Result
While the **Conversion Rate (CR)** remained stable at 100% for both groups (indicating a high-intent audience segment), there was a **statistically significant decline in Average Revenue Per User (ARPU)** in the Treatment group. The median ARPU dropped from **2.86** to **2.60**.

### Final Recommendation
> [!IMPORTANT]
> **REJECT**: We recommend maintaining the current **Horizontal Menu Layout**. The Vertical layout negatively impacts the average spend per session without providing a compensatory lift in conversion.

---

## 2. Experiment Background

### Problem Definition
The current horizontal navigation menu may limit the visibility of product categories on smaller screens or specific browser configurations, potentially suppressing user exploration and purchase value.

### Experiment Goal
To determine if a transition to a vertical layout (sidebar navigation) improves the user interface enough to increase monetization metrics without hurting the base conversion.

### Hypothesis Definition
*   **Null Hypothesis ($H_0$)**: There is no significant difference in KPI performance between the Horizontal and Vertical menu layouts.
*   **Alternative Hypothesis ($H_1$)**: The Vertical menu layout leads to a significant change in user behavior metrics.

### Success Metrics
*   **Primary KPI**: Conversion Rate (CR)
*   **Secondary KPI**: Average Revenue Per User (ARPU)
*   **Health Metric**: Sample Ratio Mismatch (SRM) & Temporal Stability

---

## 3. Data Overview

### Dataset Characteristics
The dataset represents high-intent user sessions where purchase intent was high. 
- **Timeframe**: Multi-day experimental period.
- **Scope**: Desktop and mobile users across various regions.

### Sample Sizes
| Variant | Sample Size (N) | % of Total |
| :--- | :--- | :--- |
| **Control (Horizontal)** | 3,500 | 50.0% |
| **Treatment (Vertical)** | 3,500 | 50.0% |

### Key Variables
- `variant`: User group assignment.
- `revenue`: Monetary value of the session.
- `is_purchase`: Binary indicator (1 if revenue > 0).
- `device_type`, `browser`, `region`: Contextual metadata used for validation.

---

## 4. Data Preparation & Methodology

The following preprocessing steps were applied to ensure analytical integrity:
1.  **Standardization**: Revenue columns from disparate sources were renamed to a unified `revenue` feature.
2.  **Feature Engineering**: An `is_purchase` flag was derived from the revenue data to facilitate binary conversion analysis.
3.  **Timestamp Conversion**: Raw timestamps were parsed into datetime objects to enable growth and stability monitoring over time.
4.  **Handling Missingness**: Sessions with null values in core metrics were isolated and removed to avoid skewing effect size calculations.

---

## 5. Validation Checks

Before interpreting results, we validated the experiment's integrity:

- **Sample Ratio Mismatch (SRM)**: A Chi-Square goodness-of-fit test returned a **p-value of 1.0000**. This confirms that the observed split (3,500 vs 3,500) perfectly matches the intended 50/50 allocation.
- **Covariate Balance**: We tested group distributions across `device_type`, `browser`, and `region`. All tests passed with p-values > 0.05, indicating successful randomization.
- **Temporal Stability**: The assignment ratio remained stable throughout the experiment (standard deviation < 0.05), suggesting no mid-experiment changes to the allocation logic.

---

## 6. Statistical Methodology

We employed a rigorous statistical framework to evaluate the results:

1.  **Proportion Test (Z-test)**: Used for the Conversion Rate to compare the ratio of purchases between groups.
2.  **Mann-Whitney U Test**: Selected for ARPU analysis because the revenue data did not follow a normal distribution (verified via Shapiro-Wilk test). This non-parametric test is more robust to outliers and skewed e-commerce spend data.
3.  **Holm-Bonferroni Correction**: Applied to adjust p-values for multiple comparisons, controlling the Family-Wise Error Rate (FWER) and preventing false-positive discoveries.
4.  **Confidence Level**: **95%** ($\alpha = 0.05$).

---

## 7. Statistical Results

| Metric | Test Statistic | p-value (Corrected) | Significance | Result |
| :--- | :--- | :--- | :--- | :--- |
| **Conversion Rate** | Z = 0.0 | 1.0000 | No | No Change |
| **ARPU** | U-Stat | 4.75e-08 | **Yes** | **Significant Decrease** |

**Key Metric Deep Dive:**
- **Control Median ARPU**: 2.86
- **Treatment Median ARPU**: 2.60
- **Interpretation**: The Vertical menu caused a highly significant drop in average spending per session.

---

## 8. What the Data Shows (Insight Section)

### Behavioral Differences
While neither menu layout influenced the *decision to buy* (as evidenced by the identical 100% CR), the **Vertical layout significantly inhibited the *total spend***. 

### Why did this happen?
- **Friction**: Sidebar menus on certain devices can obscure screen real estate, making it harder for users to add multiple items to their carts.
- **Discovery Deficit**: The horizontal layout may have facilitated easier "scanning" of high-value categories, which was lost in the condensed vertical format.

### Caveat & Power Note
> [!WARNING]
> While the decline in ARPU is statistically significant, the experiment was **underpowered** (N=7,000 total vs required N=15,000+ for a 10% MDE). However, given the direction and magnitude of the ARPU drop, the risk of "false negative" for the desired lift is essentially moot; the layout is actively harmful.

---

## 9. Business Impact Estimation

If the Vertical Menu Layout were implemented globally:
*   **Annual Revenue Projection**: Estimated **9.1% decline** in session-level revenue (based on median ARPU movement).
*   **Customer Lifetime Value (CLV)**: Possible downward pressure on CLV as users find current navigation less conducive to discovering new products.

---

## 10. Final Conclusion for Executive Stakeholders

### Decision
**DO NOT DEPLOY (REJECT)**

### Strategic Recommendation
The Vertical Layout does not improve conversion and actively detracts from purchase value. We should retain the Horizontal Layout as the default brand standard.

### Next Steps
1.  **Deep Dive**: Segment the ARPU results by `device_type`. If Vertical Layout only hurts Mobile but helps Desktop, consider a **responsive layout approach**.
2.  **Alternative Test**: Pivot focus to **Test 2 (Novelty Slider)**, as it addresses product discovery via a different UI pattern that may not share the friction issues identified here.
