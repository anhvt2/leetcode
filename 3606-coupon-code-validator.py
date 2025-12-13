
from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        """
        Return the codes of all valid coupons, sorted by:
        1) businessLine order: electronics, grocery, pharmacy, restaurant
        2) lexicographical order of code within each category
        """

        # Allowed business lines in required priority order
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        # Regex to validate coupon codes
        code_pattern = re.compile(r"^[A-Za-z0-9_]+$")

        valid = []

        # Step 1: filter valid coupons
        for c, b, active in zip(code, businessLine, isActive):
            if (
                active and                      # must be active
                c and                           # non-empty
                code_pattern.fullmatch(c) and   # valid characters
                b in priority                   # valid business line
            ):
                valid.append((priority[b], c))

        # Step 2: sort by businessLine priority, then by code
        valid.sort()

        # Step 3: extract only the coupon codes
        return [c for _, c in valid]
