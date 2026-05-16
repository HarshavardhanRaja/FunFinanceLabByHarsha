#!/usr/bin/env python3
"""
Episode Generator Script for DHANANDHAR Series

This script creates episode folders and template files for all remaining seasons.
Run this once to set up the complete directory structure.
"""

import os
from pathlib import Path

# Define the base path
BASE_PATH = Path("/Users/harshavardhanraja/Desktop/work/git_repos/FunFinanceLabByHarsha/DHANANDHAR/seasons")

# Season data with episodes
SEASONS_DATA = {
    "season_02_safety_net": [
        "ep_01_protection_before_investment",
        "ep_02_emergency_fund_oxygen",
        "ep_03_emergency_fund_amount",
        "ep_04_health_insurance_basics",
        "ep_05_health_insurance_mistake",
        "ep_06_term_insurance_30sec",
        "ep_07_insurance_vs_investment",
        "ep_08_hospital_bill_disaster",
        "ep_09_no_safety_net",
        "ep_10_financial_foundation"
    ],
    "season_03_earn_high": [
        "ep_01_income_problem_not_investment",
        "ep_02_salary_vs_inflation",
        "ep_03_increase_salary_fast",
        "ep_04_skills_that_pay_2026",
        "ep_05_side_income_myths",
        "ep_06_freelancing_vs_job",
        "ep_07_multiple_income_streams",
        "ep_08_one_income_trap",
        "ep_09_time_leverage",
        "ep_10_high_income_not_rich"
    ],
    "season_04_spend_less": [
        "ep_01_lifestyle_inflation",
        "ep_02_needs_vs_wants",
        "ep_03_rich_people_no_showoff",
        "ep_04_emi_slavery",
        "ep_05_small_expenses_kill",
        "ep_06_budgeting_no_restriction",
        "ep_07_psychology_spending",
        "ep_08_social_media_vs_reality",
        "ep_09_control_impulse_buying",
        "ep_10_smart_spending"
    ],
    "season_05_invest_rest": [
        "ep_01_investing_nonnegotiable",
        "ep_02_first_10k",
        "ep_03_mutual_funds_simple",
        "ep_04_sip_chai_analogy",
        "ep_05_stocks_vs_mutual_funds",
        "ep_06_risk_vs_return",
        "ep_07_compounding_intro",
        "ep_08_long_term_mindset",
        "ep_09_when_not_to_invest",
        "ep_10_first_investment_checklist"
    ],
    "season_06_wealth_engine": [
        "ep_01_compounding_power",
        "ep_02_5k_sip_future_value",
        "ep_03_asset_allocation",
        "ep_04_diversification",
        "ep_05_equity_debt_gold",
        "ep_06_rich_people_allocation",
        "ep_07_rebalancing",
        "ep_08_patience_wealth_skill",
        "ep_09_time_in_market",
        "ep_10_wealth_engine"
    ],
    "season_07_mistakes_traps": [
        "ep_01_biggest_mistakes",
        "ep_02_lose_money_market",
        "ep_03_fomo_investing",
        "ep_04_finance_scams_india",
        "ep_05_credit_card_trap",
        "ep_06_loan_psychology",
        "ep_07_overtrading",
        "ep_08_listening_tips",
        "ep_09_ignoring_risk",
        "ep_10_avoid_mistakes"
    ],
    "season_08_money_mindset": [
        "ep_01_mindset_matters",
        "ep_02_scarcity_vs_abundance",
        "ep_03_delayed_gratification",
        "ep_04_discipline_vs_motivation",
        "ep_05_emotional_spending",
        "ep_06_fear_investing",
        "ep_07_comparison_trap",
        "ep_08_long_term_thinking",
        "ep_09_financially_strong_habits",
        "ep_10_identity_with_money"
    ],
    "season_09_freedom_mode": [
        "ep_01_financial_freedom_means",
        "ep_02_how_much_you_need",
        "ep_03_fire_types",
        "ep_04_retire_early_india",
        "ep_05_passive_income_truth",
        "ep_06_choice_vs_compulsion",
        "ep_07_design_ideal_life",
        "ep_08_freedom_vs_luxury",
        "ep_09_financial_independence_roadmap",
        "ep_10_closer_than_you_think"
    ],
    "season_10_endgame": [
        "ep_01_journey_to_1cr",
        "ep_02_money_stopped_controlling",
        "ep_03_if_started_from_zero",
        "ep_04_biggest_lessons",
        "ep_05_matters_beyond_money",
        "ep_06_money_cant_fix",
        "ep_07_freedom_not_what_think",
        "ep_08_youre_ahead",
        "ep_09_next_10_year_plan",
        "ep_10_final_banger",
        "ep_11_bonus_behind_scenes"
    ]
}

# Episode template
EPISODE_README = """# Episode {ep_num}: {title}

## Episode Details

- **Season:** {season_num} - {season_title}
- **Episode Number:** {ep_num}
- **Title:** {title}
- **Status:** Draft / In Progress / Ready / Published
- **Publish Date:** 
- **Platform Links:**
  - YouTube: 
  - Instagram Reels: 
  - YouTube Shorts: 

---

## Content Files

- [Idea](idea.md) - Core concept and angle
- [Raw Script](script.md) - Full dialogue and breakdown
- [Video Assets](video/) - Raw videos and media files

---

## Metrics (Post-publish)

- Views:
- Likes:
- Comments:
- Saves:
- Click-through Rate:

---

## Notes

- Add episode-specific notes here
- Modifications, feedback, learnings
"""

IDEA_TEMPLATE = """# Idea: {title}

## Angle / Hook

[Add the main hook that grabs attention in 3 seconds]

## Core Concept

[Describe the central idea and why it matters]

## Key Points to Cover

- Point 1:
- Point 2:
- Point 3:
- Point 4:

## Visual Concepts

[Describe key visuals or graphics needed]

## Call-to-Action

[What do you want viewers to do after watching]

## References / Research

[Links, data, or sources to back up claims]
"""

SCRIPT_TEMPLATE = """# Raw Script: {title}

## Timing: [X seconds]

---

## Hook (0:00 - 0:05)

[Opening statement to grab attention]

---

## Body (0:05 - 0:25)

[Main content, points, story]

---

## Punchline (0:25 - 0:30)

[Final message, call-to-action]

---

## Visuals / On-Screen Text

- [Visual 1]
- [Text overlay 1]
- [Visual 2]

---

## Notes for Creator

- [Production notes]
- [Music/SFX cues]
- [Any special instructions]
"""

def slugify(text):
    """Convert text to folder-friendly slug"""
    return text.lower().replace(" ", "_").replace("-", "_")

def create_episode_files(episode_folder, episode_num, title, season_num, season_title):
    """Create README, idea, and script files for an episode"""
    
    episode_folder.mkdir(parents=True, exist_ok=True)
    
    # Create video folder
    (episode_folder / "video").mkdir(exist_ok=True)
    
    # Create README
    readme_path = episode_folder / "README.md"
    if not readme_path.exists():
        readme_path.write_text(EPISODE_README.format(
            ep_num=episode_num,
            title=title,
            season_num=season_num,
            season_title=season_title
        ))
    
    # Create idea.md
    idea_path = episode_folder / "idea.md"
    if not idea_path.exists():
        idea_path.write_text(IDEA_TEMPLATE.format(title=title))
    
    # Create script.md
    script_path = episode_folder / "script.md"
    if not script_path.exists():
        script_path.write_text(SCRIPT_TEMPLATE.format(title=title))

def main():
    """Generate all episode folders and files"""
    
    season_info = {
        "season_02_safety_net": (2, "The Safety Net 🛡️"),
        "season_03_earn_high": (3, "Earn High 💼"),
        "season_04_spend_less": (4, "Spend Less (Smartly) 💸"),
        "season_05_invest_rest": (5, "Invest Rest 📈"),
        "season_06_wealth_engine": (6, "Wealth Engine 📊"),
        "season_07_mistakes_traps": (7, "Mistakes & Traps ⚠️"),
        "season_08_money_mindset": (8, "Money Mindset 🧠"),
        "season_09_freedom_mode": (9, "Freedom Mode 🚀"),
        "season_10_endgame": (10, "The Endgame 👑"),
    }
    
    for season_dir, episodes in SEASONS_DATA.items():
        season_num, season_title = season_info[season_dir]
        season_path = BASE_PATH / season_dir
        
        for ep_folder in episodes:
            ep_num = ep_folder.split("_")[1]
            # Extract title from folder name
            title = ep_folder.replace(f"ep_{ep_num}_", "").replace("_", " ").title()
            
            episode_path = season_path / "episodes" / ep_folder
            create_episode_files(episode_path, ep_num, title, season_num, season_title)
        
        print(f"✅ Created episodes for {season_dir}")
    
    print("\n🎉 All episodes generated successfully!")
    print(f"📍 Location: {BASE_PATH}")

if __name__ == "__main__":
    main()
