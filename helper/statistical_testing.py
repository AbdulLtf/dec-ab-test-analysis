"""
Statistical Testing Framework for A/B Testing
Includes t-tests, proportion tests, chi-square, mann-whitney U, and multiple testing correction.
"""

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency
from statsmodels.stats.multitest import multipletests
from typing import Dict, List, Tuple, Optional, Any
import warnings

class ABTestAnalyzer:
    """
    Core analyzer for performing statistical tests on A/B test data.
    """

    def __init__(self, alpha: float = 0.05):
        self.alpha = alpha

    def two_sample_ttest(
        self,
        control: np.ndarray,
        treatment: np.ndarray,
        metric_name: str,
        equal_var: bool = False
    ) -> Dict[str, Any]:
        """Performs Welch's t-test for continuous metrics."""
        control = control[~np.isnan(control)]
        treatment = treatment[~np.isnan(treatment)]
        
        statistic, pvalue = stats.ttest_ind(treatment, control, equal_var=equal_var)
        
        control_mean, treatment_mean = control.mean(), treatment.mean()
        control_std, treatment_std = control.std(ddof=1), treatment.std(ddof=1)
        n_control, n_treatment = len(control), len(treatment)
        
        # Cohen's d
        pooled_std = np.sqrt((control_std**2 + treatment_std**2) / 2)
        cohens_d = (treatment_mean - control_mean) / pooled_std if pooled_std > 0 else 0
        
        # Confidence Interval
        se_diff = np.sqrt(control_std**2/n_control + treatment_std**2/n_treatment)
        if not equal_var:
            num = (control_std**2/n_control + treatment_std**2/n_treatment)**2
            denom = ((control_std**2/n_control)**2/(n_control-1) + (treatment_std**2/n_treatment)**2/(n_treatment-1))
            df = num / denom if denom > 0 else n_control + n_treatment - 2
        else:
            df = n_control + n_treatment - 2
            
        t_crit = stats.t.ppf(1 - self.alpha/2, df)
        diff = treatment_mean - control_mean
        ci_lower, ci_upper = diff - t_crit * se_diff, diff + t_crit * se_diff
        
        relative_lift = (diff / control_mean * 100) if control_mean != 0 else 0
        
        return {
            'metric': metric_name,
            'test_type': 't-test',
            'pvalue': pvalue,
            'significant': pvalue < self.alpha,
            'control_mean': control_mean,
            'treatment_mean': treatment_mean,
            'relative_lift_pct': relative_lift,
            'cohens_d': cohens_d,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'test_selection': 'parametric'
        }

    def proportion_test(
        self,
        control_successes: int,
        control_total: int,
        treatment_successes: int,
        treatment_total: int,
        metric_name: str
    ) -> Dict[str, Any]:
        """Performs Z-test for proportions (binary metrics)."""
        p_control = control_successes / control_total
        p_treatment = treatment_successes / treatment_total
        p_pooled = (control_successes + treatment_successes) / (control_total + treatment_total)
        
        se = np.sqrt(p_pooled * (1 - p_pooled) * (1/control_total + 1/treatment_total))
        z_stat = (p_treatment - p_control) / se if se > 0 else 0
        pvalue = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        
        diff = p_treatment - p_control
        z_crit = stats.norm.ppf(1 - self.alpha/2)
        se_diff = np.sqrt(p_control*(1-p_control)/control_total + p_treatment*(1-p_treatment)/treatment_total)
        ci_lower, ci_upper = diff - z_crit * se_diff, diff + z_crit * se_diff
        
        relative_lift = (diff / p_control * 100) if p_control > 0 else 0
        
        return {
            'metric': metric_name,
            'test_type': 'proportion_test',
            'pvalue': pvalue,
            'significant': pvalue < self.alpha,
            'control_rate': p_control,
            'treatment_rate': p_treatment,
            'relative_lift_pct': relative_lift,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'test_selection': 'binary'
        }

    def mann_whitney_u_test(
        self,
        control: np.ndarray,
        treatment: np.ndarray,
        metric_name: str
    ) -> Dict[str, Any]:
        """Performs Mann-Whitney U test (non-parametric)."""
        control = control[~np.isnan(control)]
        treatment = treatment[~np.isnan(treatment)]
        
        statistic, pvalue = stats.mannwhitneyu(treatment, control, alternative='two-sided')
        
        rank_biserial = 1 - (2*statistic) / (len(control) * len(treatment))
        
        return {
            'metric': metric_name,
            'test_type': 'mann_whitney',
            'pvalue': pvalue,
            'significant': pvalue < self.alpha,
            'control_median': np.median(control),
            'treatment_median': np.median(treatment),
            'rank_biserial': rank_biserial,
            'test_selection': 'non-parametric'
        }

    def chi_square_test(
        self,
        control: np.ndarray,
        treatment: np.ndarray,
        metric_name: str
    ) -> Dict[str, Any]:
        """Performs Chi-Square test for categorical data."""
        combined = np.concatenate([control, treatment])
        labels = np.concatenate([np.zeros(len(control)), np.ones(len(treatment))])
        contingency_table = pd.crosstab(combined, labels)
        
        chi2, pvalue, _, _ = chi2_contingency(contingency_table)
        
        n = len(combined)
        min_dim = min(contingency_table.shape) - 1
        cramers_v = np.sqrt(chi2 / (n * min_dim)) if min_dim > 0 else 0
        
        return {
            'metric': metric_name,
            'test_type': 'chi_square',
            'pvalue': pvalue,
            'significant': pvalue < self.alpha,
            'cramers_v': cramers_v,
            'test_selection': 'categorical'
        }

    def bootstrap_ci(
        self,
        control: np.ndarray,
        treatment: np.ndarray,
        metric_name: str,
        n_bootstrap: int = 5000
    ) -> Dict[str, Any]:
        """Calculates bootstrap confidence interval for the difference in means."""
        control = control[~np.isnan(control)]
        treatment = treatment[~np.isnan(treatment)]
        
        boot_diffs = []
        for _ in range(n_bootstrap):
            c_boot = np.random.choice(control, size=len(control), replace=True)
            t_boot = np.random.choice(treatment, size=len(treatment), replace=True)
            boot_diffs.append(t_boot.mean() - c_boot.mean())
            
        ci_lower, ci_upper = np.percentile(boot_diffs, [2.5, 97.5])
        observed_diff = treatment.mean() - control.mean()
        
        return {
            'metric': metric_name,
            'test_type': 'bootstrap',
            'observed_diff': observed_diff,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'significant': not (ci_lower <= 0 <= ci_upper)
        }

    def apply_multiple_testing_correction(
        self,
        results: List[Dict[str, Any]],
        method: str = 'holm'
    ) -> List[Dict[str, Any]]:
        """Applies multiple testing correction to a list of results."""
        p_values = [r['pvalue'] for r in results if 'pvalue' in r]
        if len(p_values) <= 1:
            return results
            
        reject, pvals_corrected, _, _ = multipletests(p_values, alpha=self.alpha, method=method)
        
        for i, result in enumerate(results):
            if 'pvalue' in result:
                result['pvalue_corrected'] = pvals_corrected[i]
                result['significant_corrected'] = reject[i]
                result['correction_method'] = method
                
        return results

    def check_normality(self, data: np.ndarray) -> bool:
        """Helper to check normality (Shapiro-Wilk)."""
        data_clean = data[~np.isnan(data)]
        if len(data_clean) > 5000:
            sample = np.random.choice(data_clean, 5000, replace=False)
        else:
            sample = data_clean
        _, p = stats.shapiro(sample)
        return p >= self.alpha
