#!/usr/bin/env python
# src/financial_researcher/main.py
import os
from datetime import datetime
from financial_researcher.crew import ResearchCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    """
    # 動態取得目前月份與年份
    now = datetime.now()
    until_date = now.strftime("%B %Y")  # e.g. "June 2025"

    inputs = {
        'company': os.getenv("COMPANY", "Apple"),
        'until_date': until_date,
    }

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print(f"\n\nReport has been saved to output/{inputs['company']}_report.md")

if __name__ == "__main__":
    run()