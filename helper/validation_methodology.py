"""
Validation Methodology for A/B Testing
Handles SRM tests, covariate balance checks, and temporal stability validation.
"""

import pandas as pd
import numpy as np
from scipy import stats
from typing import List, Dict, Optional

class ExperimentValidator:
    """
    Validates the integrity of an A/B test experiment.
    Checks for Sample Ratio Mismatch (SRM), covariate balance, and temporal stability.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        variant_col: str = "variant",
        session_col: str = "session_id",
        time_col: str = "timestamp",
        covariates: Optional[List[str]] = None,
        alpha: float = 0.05
    ):
        self.df = df.copy()
        self.variant_col = variant_col
        self.session_col = session_col
        self.time_col = time_col
        self.covariates = covariates or []
        self.alpha = alpha

        self.results = {
            "SRM": True,
            "Covariate Balance": True,
            "Temporal Stability": True
        }
        self.p_values = {}

    def check_srm(self) -> bool:
        """
        Performs a Chi-Square goodness-of-fit test to detect Sample Ratio Mismatch.
        """
        counts = self.df[self.variant_col].value_counts().sort_index()
        observed = counts.values
        # Assuming equal allocation (50/50 for 2 groups)
        expected = np.ones(len(observed)) / len(observed) * observed.sum()

        _, p = stats.chisquare(observed, expected)
        self.p_values["SRM"] = p

        passed = p >= self.alpha
        self.results["SRM"] = passed

        print(f"SRM Check: p-value = {p:.4f} -> {'PASS' if passed else 'FAIL'}")
        if not passed:
            print("WARNING: Sample Ratio Mismatch detected. Groups are not balanced as expected.")
        
        return passed

    def check_covariate_balance(self) -> bool:
        """
        Checks if the randomization was successful by comparing distribution of covariates across groups.
        """
        if not self.covariates:
            print("Covariate Balance Check: No covariates provided -> skipped")
            return True

        overall_passed = True
        for col in self.covariates:
            if col not in self.df.columns:
                print(f"  - {col}: Skipped (not found in dataframe)")
                continue

            # Drop NaNs for validation
            groups = [g[col].dropna() for _, g in self.df.groupby(self.variant_col)]
            
            # Remove empty groups
            groups = [g for g in groups if len(g) > 0]
            if len(groups) < 2:
                print(f"  - {col}: Skipped (not enough variant groups with data)")
                continue

            if pd.api.types.is_numeric_dtype(self.df[col]):
                # ANOVA for numeric covariates
                _, p = stats.f_oneway(*groups)
            else:
                # Chi-Square for categorical covariates
                contingency_table = pd.crosstab(self.df[col], self.df[self.variant_col])
                _, p, _, _ = stats.chi2_contingency(contingency_table)

            self.p_values[f"Covariate_{col}"] = p
            if p < self.alpha:
                overall_passed = False
                print(f"  - {col}: p={p:.4f} -> FAIL")
            else:
                print(f"  - {col}: p={p:.4f} -> PASS")

        self.results["Covariate Balance"] = overall_passed
        print(f"Covariate Balance: {'PASS' if overall_passed else 'FAIL'}")
        return overall_passed

    def check_temporal_stability(self, freq: str = "D") -> bool:
        """
        Checks if the ratio of variant assignments remains stable over time.
        """
        if self.time_col not in self.df.columns:
            print("Temporal Stability Check: No timestamp column -> skipped")
            return True

        df_temp = self.df.copy()
        df_temp[self.time_col] = pd.to_datetime(df_temp[self.time_col])

        # Group by time and variant
        daily_counts = (
            df_temp.groupby([pd.Grouper(key=self.time_col, freq=freq), self.variant_col])
            .size()
            .unstack(fill_value=0)
        )

        if daily_counts.empty:
            print("Temporal Stability Check: No data after grouping -> skipped")
            return True

        # Calculate ratios
        ratios = daily_counts.div(daily_counts.sum(axis=1), axis=0)
        
        # Check standard deviation of ratios across time units
        # If std is high, it indicates instability in assignment
        max_std = ratios.std().max()
        self.p_values["Temporal_Std"] = max_std

        passed = max_std < 0.05 # Threshold for stability
        self.results["Temporal Stability"] = passed

        print(f"Temporal Stability: std={max_std:.4f} -> {'PASS' if passed else 'FAIL'}")
        return passed

    def run_all(self) -> bool:
        """
        Executes all validation checks and returns a final pass/fail status.
        """
        print("\n--- EXPERIMENT VALIDATION SUITE ---")
        srm_pass = self.check_srm()
        cov_pass = self.check_covariate_balance()
        temp_pass = self.check_temporal_stability()
        
        final_pass = all([srm_pass, cov_pass, temp_pass])
        
        status = "✅ VALIDATION SUCCESS" if final_pass else "❌ VALIDATION FAILURE"
        print(f"\n{status}")
        
        if not final_pass:
            print("Recommendation: Investigate potential assignment bias or data collection issues.")
            
        return final_pass
