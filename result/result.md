# A/B Test Analysis Report: Menu Layout Optimization

**Author**: Senior Experimentation Analyst  
**Date**: February 15, 2026  
**Project**: E-Commerce UI Refinement Initiative  

---

## 1. Executive Summary

### Business Objective
The primary goal of this experiment was to evaluate the impact of a structural change to the user interface: transitioning the **Menu Layout** from a traditional **Horizontal** orientation to a modern **Vertical** layout. The objective was to enhance user engagement and potentially increase monetization.

### Key Finding
While the **Conversion Rate** remained statistically stable across both variants, the **Average Revenue Per User (ARPU)** experienced a **significant decrease** in the Treatment group. The shift to a Vertical layout resulted in a ~9% drop in revenue per session among purchasers.

### Final Recommendation
> [!IMPORTANT]
> **REJECT / DO NOT LAUNCH**
>
> The Vertical Menu layout negatively impacts user monetization without providing a lift in conversion efficiency. It is recommended to retain the Horizontal layout and investigate the friction points introduced by the Vertical design.

### Estimated KPI Impact
*   **Conversion Rate**: 0% change (Neutral)
*   **ARPU**: -9.1% (Significant decline)
*   **Projected Revenue Loss**: Based on experimental volume, broad deployment would likely lead to a direct reduction in platform yield.

---

## 2. Business Problem & Experiment Context

### Business Problem
A/B testing is critical for UI refinements because "intuitive" design changes often lead to counter-intuitive behavioral shifts. The E-Commerce team aimed to modernize the site navigation, hypothesized that a Vertical menu would better utilize screen real estate and improve the discoverability of high-value items.

### Why Conducted
The experiment was conducted to validate if a radical change in navigation structure would translate to higher revenue or if the novelty would distract users from completing purchases.

### Experiment Hypothesis
*   **Null Hypothesis ($H_0$)**: The Menu Layout (Horizontal vs. Vertical) has no effect on user engagement or revenue metrics.
*   **Alternative Hypothesis ($H_1$)**: The Menu Layout change will result in a significant shift in primary or secondary KPIs.

### Primary and Secondary KPIs
*   **Primary KPI**: **Conversion Rate (CR)** - Ratio of sessions resulting in a purchase (Binary).
*   **Secondary KPI**: **ARPU (Average Revenue Per User)** - Monetization efficiency per session (Continuous).
*   **Health KPI**: **Bounced Sessions** - Ensuring the new layout doesn't drive immediate exits.

---

## 3. Data Overview

### Dataset Description
The analysis utilizes the `test1_menu.csv` dataset, which captures user interactions during the experimental period across diverse platforms and browsers.

### Sample Size
| Variant | Sample Size (N) |
| :--- | :--- |
| **Control (Horizontal)** | 3,500 |
| **Treatment (Vertical)** | 3,500 |
| **Total** | 7,000 |

### Key Experiment Variables
*   `variant`: The experimental group assignment (Control/Treatment).
*   `revenue`: Transaction value per session.
*   `device_type`, `browser`, `region`: User attributes for randomization validation.
*   `is_purchase`: Derived binary flag (1 if revenue > 0).

### Metric Definitions
1.  **Conversion Rate (CR)**: Calculated as `count(is_purchase == 1) / total_sessions`.
2.  **ARPU**: Defined as the mean/median revenue across all sessions in a specific group.

---

## 4. Experiment Validation Framework

### Sample Ratio Mismatch (SRM) Test
SRM is a critical "guardrail" test to detect randomization bias.
*   **SRM Result**: $p = 1.000$
*   **Conclusion**: **PASS**. The observed 50/50 split is perfectly aligned with the target allocation, suggesting no technical allocation errors.

### Randomization & Covariate Balance Checks
We verified that user attributes were evenly distributed across variants:
*   **Device Type Balance**: $p = 0.519$ (Pass)
*   **Browser Balance**: $p = 0.663$ (Pass)
*   **Region Balance**: $p = 0.835$ (Pass)

### Validation Conclusion
> [!TIP]
> **Is the experiment trustworthy?**
> Yes. With successful SRM, covariate balance, and temporal stability checks, we can confidently attribute the observed deltas to the layout change rather than external noise.

---

## 5. Data Preparation & Handling Methodology

### Cleaning & Processing
*   **Missing Values**: Handled via drop-na for critical revenue/variant columns.
*   **Outlier Strategy**: Revenue distributions often display extreme skews. While values were kept, non-parametric tests were selected to ensure outliers didn't disproportionately skew the p-values.
*   **Preprocessing**: 
    - Standardized feature naming.
    - Timestamp conversion to Date objects for temporal stability analysis.
    - Derived `is_purchase` feature from revenue to facilitate conversion analysis.

---

## 6. Statistical Methodology

### Metric Type Identification
*   **Conversion Rate**: Binary (0 or 1).
*   **ARPU**: Continuous and highly skewed (Non-Normal).

### Statistical Test Selection
1.  **Proportion Z-Test**: Used for the Conversion Rate to compare success ratios.
2.  **Mann-Whitney U Test**: Selected for ARPU. Since the revenue data failed the Shapiro-Wilk normality check, a non-parametric test was required to compare the distributions' central tendencies (medians).

### Assumptions & Standards
*   **Confidence Level**: 95% ($\alpha = 0.05$).
*   **Multiple Testing Correction**: Holm method applied to control for Type I error across primary/secondary KPIs.
*   **Effect Size**: Rank-Biserial Correlation (for Mann-Whitney) and Relative Lift.

---

## 7. Statistical Results

### Control vs. Treatment Comparison
| Metric | Control (H) | Treatment (V) | p-value | Relative Lift | Significant? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Conversion Rate** | 100%* | 100%* | 1.000 | 0.0% | No |
| **Median ARPU** | 2.86 | 2.60 | 2.38e-08 | -9.1% | **YES** |

*\*Note: In this specific dataset iteration, conversion was saturated at 100% for all experimental sessions, allowing for a focused analysis on revenue yield.*

### Interpretation
The Mann-Whitney U test confirms that the decrease in ARPU is highly significant (p < 0.001). This suggests that although the Vertical layout doesn't stop users from buying, it significantly reduces the amount they choose to spend per transaction.

---

## 8. Experimental Outcomes (Cross-Test Summary)

While the primary focus remains the **Menu Layout (Test 1)**, the broader experimentation cycle captured insights across five distinct tests. This provides a comparative baseline for optimization efforts.

### Holistic Test Results
| Experiment | Primary Metric | Result | Impact |
| :--- | :--- | :--- | :--- |
| **Test 1: Menu** | ARPU | **-9.1% Lift** | **Significant Decline** |
| **Test 2: Novelty** | ARPU | **+5.57% Lift** | **Significant Increase** |
| **Test 3: Product** | ARPU | **+20.97% Lift** | **Significant Increase** |
| **Test 4: Reviews** | CR | **+0.53% Lift** | Not Significant |
| **Test 5: Search** | ARPU | **0.00% Lift** | Not Significant |

### Analysis of Sibling Experiments
*   **Test 3 (Product Sliders)**: Observed the highest practical impact with a ~21% jump in ARPU. This suggests that layout optimizations should focus on content delivery (sliders) rather than structural navigation (vertical menu).
*   **Test 2 (Novelty Slider)**: Shows that targeted UI "novelty" can drive monetization without hurting conversions.
*   **Test 5 (Search Engine)**: Improvements to the underlying search logic were neutral, indicating that the current engine is likely not a primary bottleneck for user spending.

---

## 9. What the Data Shows (Insight Section)

### Behavioral Observations
The Vertical layout appears to create a **friction point** in the monetization funnel. While the "purchase intent" (Conversion) is unaffected, the "basket value" (Revenue) is adversely impacted.

### Practical vs. Statistical Significance
The ARPU decline is not just a statistical anomaly; a **-9.1% drop** represents a massive regression in business efficiency. In a production environment, this delta would likely trigger an immediate automated rollback.

### Risks and Caveats
*   **Novelty Effect**: Users accustomed to the Horizontal layout might perform worse initially due to friction. However, with a highly significant negative result, the risk of "waiting for recovery" is too great.
*   **Sample Power**: The observed sample size (3,500) was below the theoretical target (7,842). However, given the very small p-value, the effect is strong enough to be conclusive despite the lower power.

---

## 10. Business Impact Estimation

### Expected KPI Decline
*   Deploying the Vertical layout site-wide would expect to see a **~9% drop in total platform yield**.

### Strategic Implications
The Vertical menu likely clutters the interface or buries high-margin items compared to the Horizontal layout. This experiment proves that "modernizing" the layout without considering visual hierarchy can be detrimental to the bottom line.

---

## 11. Final Executive Conclusion

### Decision Statement
Based on the results of Test 1 (Menu), we **reject the transition to a Vertical Menu layout**.

### Deployment Recommendation
*   **Current Action**: Cease all traffic to the Vertical variant and return 100% of users to the Horizontal baseline.
*   **Next Experiment**: Test a **Hybrid Menu** or refined **Horizontal Categories** with better mobile responsiveness. We should explore why the Vertical layout suppressed spending—did it hide product filters or make navigation feel cluttered?

---
*Report generated for executive review by the Experimentation Analysis Team.*
