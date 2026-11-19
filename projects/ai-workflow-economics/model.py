"""Illustrate per-task economics with synthetic inputs."""

from decimal import Decimal

HOURLY_COST = Decimal("60")
MANUAL_MINUTES = Decimal("30")
AI_DRAFT_MINUTES = Decimal("10")
AI_TOOL_COST = Decimal("2")


def cost_per_task(minutes: Decimal) -> Decimal:
    return minutes * HOURLY_COST / Decimal("60")


def main() -> None:
    manual_cost = cost_per_task(MANUAL_MINUTES)
    break_even = (manual_cost - AI_TOOL_COST) * 60 / HOURLY_COST - AI_DRAFT_MINUTES
    print(f"Manual cost per task: ${manual_cost:.2f}")
    print(f"Break-even review and rework: {break_even:.0f} minutes")
    print("Review and rework (minutes) | AI cost | Savings vs. manual")
    for review_minutes in (5, 10, 18, 25):
        ai_cost = cost_per_task(AI_DRAFT_MINUTES + review_minutes) + AI_TOOL_COST
        print(f"{review_minutes:>27} | ${ai_cost:>6.2f} | ${manual_cost - ai_cost:>7.2f}")


if __name__ == "__main__":
    main()
