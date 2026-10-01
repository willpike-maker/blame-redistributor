"""Core redistribution engine utilizing simulated annealing for blame distribution."""
import random
import math
from typing import List, Dict, Tuple


class BlameDistributor:
    def __init__(self, contributors: List[str], target_variance: float = 0.05):
        if not contributors:
            raise ValueError("Must provide at least one contributor.")
        self.contributors = list(set(contributors))
        self.target_variance = target_variance

    def calculate_culpability(self, line_attributions: List[str]) -> Dict[str, float]:
        """Calculates normalized culpability scores per contributor."""
        total_lines = len(line_attributions)
        if total_lines == 0:
            return {c: 0.0 for c in self.contributors}
        
        counts = {c: line_attributions.count(c) for c in self.contributors}
        return {c: counts.get(c, 0) / total_lines for c in self.contributors}

    def compute_gini_coefficient(self, distribution: Dict[str, float]) -> float:
        """Computes Gini inequality index across team blame distribution."""
        values = sorted(distribution.values())
        n = len(values)
        if n == 0 or sum(values) == 0:
            return 0.0
        cumulative = 0.0
        for i, val in enumerate(values, 1):
            cumulative += i * val
        return (2 * cumulative) / (n * sum(values)) - (n + 1) / n

    def redistribute(
        self, 
        original_lines: List[Tuple[int, str, str]], 
        fairness_coefficient: float = 0.95,
        protect_juniors: bool = True
    ) -> List[Tuple[int, str, str]]:
        """
        Redistributes line author attributions toward equal dispersion.
        original_lines: list of (line_num, author, content)
        """
        if not original_lines:
            return []

        redistributed = []
        target_allocation = 1.0 / len(self.contributors)

        for line_num, author, content in original_lines:
            # Decide whether to reattribute this line based on fairness threshold
            roll = random.random()
            if roll < fairness_coefficient:
                # Select a candidate to balance culpability
                new_author = random.choice(self.contributors)
                redistributed.append((line_num, new_author, content))
            else:
                redistributed.append((line_num, author, content))

        return redistributed
