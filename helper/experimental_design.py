"""
Experimental Design Methodology
Handles sample size calculation, hypothesis definition, and KPI selection.
"""

import numpy as np
from scipy import stats
from typing import Dict, Tuple, Optional

def calculate_sample_size(
    baseline_rate: float,
    mde: float,
    alpha: float = 0.05,
    power: float = 0.80,
    two_tailed: bool = True
) -> int:
    """
    Calculates the required sample size per variant.
    
    Args:
        baseline_rate: The current conversion rate (0-1).
        mde: Minimum Detectable Effect as a relative lift (e.g., 0.1 for 10% lift).
        alpha: Significance level (Type I error).
        power: Statistical power (1 - Type II error).
        two_tailed: Whether to use a two-tailed test.
        
    Returns:
        The required sample size per variant.
    """
    if two_tailed:
        z_alpha = stats.norm.ppf(1 - alpha/2)
    else:
        z_alpha = stats.norm.ppf(1 - alpha)
    
    z_beta = stats.norm.ppf(power)
    
    # Effect size
    p1 = baseline_rate
    p2 = baseline_rate * (1 + mde)
    
    # Selection of probability
    p2 = min(p2, 0.999)
    p2 = max(p2, 0.001)
    
    # Pooled variance
    # Standard formula for proportion sample size
    numerator = (z_alpha + z_beta)**2 * (p1 * (1 - p1) + p2 * (1 - p2))
    denominator = (p2 - p1)**2
    
    n = numerator / denominator
    
    return int(np.ceil(n))

def define_hypotheses(metric_name: str) -> Dict[str, str]:
    """
    Returns the null and alternative hypotheses for a given metric.
    """
    return {
        "null": f"H0: μ_control = μ_treatment (There is no significant difference in {metric_name})",
        "alternative": f"H1: μ_control ≠ μ_treatment (There is a significant difference in {metric_name})"
    }

def get_kpi_definitions() -> Dict[str, str]:
    """
    Returns standard definitions for primary and secondary KPIs.
    """
    return {
        "Conversion Rate (CR)": "Total Purchases / Total Sessions",
        "Average Revenue Per User (ARPU)": "Total Revenue / Total Sessions",
        "Bounce Rate": "Sessions with 1 page viewed / Total Sessions",
        "Pages per Session": "Total Pages Viewed / Total Sessions"
    }
