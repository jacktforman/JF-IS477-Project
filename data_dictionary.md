# Data Dictionary

**Project:** Blade vs. Mallet -- A Data Analysis of Putting Performance of Differing Putter Designs on the PGA Tour  
**Author:** Jack Forman | IS477 SP26  
**Last updated:** May 2026

This document describes all variables in each dataset used in this project. It covers the two raw datasets, two cleaned datasets, and the integrated analytical dataset.

---

## 1. pga_tour_sgputt_2025_raw.csv / pga_sgputt_2025_clean.csv

**Location:** data/raw/ and data/cleaned/  
**Description:** 2025 PGA Tour season-level putting statistics for the top 20 and bottom 20 players ranked by Strokes Gained: Putting. Sourced from PGA Tour official statistics via Eden Steak analysis (edensteak.com).  
**Rows:** 40  
**Unit of observation:** One player for one season

| Variable | Type | Description | Example |
|---|---|---|---|
| rank | integer | Player's final SG:Putting rank for the 2025 season (1 = best) | 1 |
| player_name | string | Full player name, title-cased and whitespace-stripped | Sam Burns |
| sg_putting_avg | float | Strokes Gained: Putting season average. Positive = strokes gained vs. field; negative = strokes lost. Adjusted for putt distance. | 0.983 |
| putter_type | string | Controlled vocabulary: blade, mallet, or unknown | mallet |
| putter_brand | string | Equipment manufacturer | Odyssey |
| putter_model | string | Specific model name as reported in equipment sources | Ai-ONE 7S |
| putter_release_year | integer | Year the putter model was first released | 2023 |
| group | string | Which extreme the player falls in: top20 or bottom20 | top20 |
| season | integer | PGA Tour season year | 2025 |
| source | string | Citation for both the performance data and the equipment classification | PGA Tour Stats / Eden Steak analysis |
| putter_era | string | Derived field (cleaned dataset only). Classifies putter by release year: classic (pre-2016), mid-era (2016-2020), modern (2021+) | modern |

**Notes:**
- SG:Putting is calculated relative to the field average using a distance-weighted model. A value of +1.0 means the player gained approximately one stroke per round on the greens compared to the average Tour player.
- The dataset covers only the extremes of the distribution (top and bottom 20). The approximately 140 players ranked between 21st and 160th are not included.
- Ben Griffin (rank 19) switched from a blade to a mallet mid-season. He is classified as blade (dominant-season designation). This is noted in his source column.

---

## 2. masters_2026_leaderboard_raw.csv / masters_2026_clean.csv

**Location:** data/raw/ and data/cleaned/  
**Description:** 2026 Masters Tournament final leaderboard for all players who made the cut, plus four missed-cut players. Includes putter equipment data for each player. Sourced from Golf Monthly, EssentiallySports, Sky Sports, MyGolfSpy, and Wikipedia.  
**Rows:** 44  
**Unit of observation:** One player in one tournament

| Variable | Type | Description | Example |
|---|---|---|---|
| finish | string | Final finish position. Ties use T prefix. Missed cut recorded as MC | T3 |
| player_name | string | Full player name, title-cased | Rory Mcilroy |
| score_to_par | integer | 72-hole score relative to par. Negative = under par. Null for MC players. | -13 |
| r1 | integer | Round 1 score (gross) | 67 |
| r2 | integer | Round 2 score (gross) | 65 |
| r3 | integer | Round 3 score (gross). Null for MC players. | 73 |
| r4 | integer | Round 4 score (gross). Null for MC players. | 71 |
| putter_type | string | Controlled vocabulary: blade, mallet, or unknown | mallet |
| putter_brand | string | Equipment manufacturer | TaylorMade |
| putter_model | string | Specific model name | Spider Tour X |
| putter_notes | string | Free text. Records confidence level, equipment switches, or classification rationale | Switched at 2024 Tour Championship |
| source | string | Specific source(s) used to determine putter type for this player | Golf Monthly WITB 2026 / MyGolfSpy |
| finish_num | integer | Derived field (cleaned dataset only). Numeric finish for sorting. Ties get the same number. MC = 999. | 1 |

**Notes:**
- r3 and r4 are intentionally null for the four MC players (they did not play the weekend rounds). This is expected and not a data quality error.
- Source confidence is tiered. Top-10 finishers have dedicated WITB articles and are high-confidence. Players finishing T25 and below were sourced from pre-tournament equipment surveys and are medium-to-lower confidence. Confidence level is noted in putter_notes where relevant.
- Augusta National does not release Shotlink data publicly. Tournament-level SG:Putting is therefore not available for Masters players in this dataset.

---

## 3. integrated_putter_analysis.csv

**Location:** data/integrated/  
**Description:** Full outer join of the two cleaned datasets on player_name. Contains 75 unique player records. Players who appear in only one dataset will have null values for columns from the other.  
**Rows:** 75  
**Unit of observation:** One player (covering their 2025 season stats and/or 2026 Masters result)

| Variable | Type | Description |
|---|---|---|
| player_name | string | Full player name (join key) |
| pga_2025_rank | float | Player's SG:Putting rank in 2025. Null if not in PGA dataset. |
| pga_2025_sg_putt | float | SG:Putting season average from the PGA 2025 dataset. Null if not in PGA dataset. |
| putter_type_2025 | string | Putter type from the PGA 2025 dataset. Null if not in PGA dataset. |
| putter_brand_2025 | string | Putter brand from the PGA 2025 dataset |
| putter_model_2025 | string | Putter model from the PGA 2025 dataset |
| pga_2025_group | string | top20 or bottom20 from the PGA 2025 dataset |
| season | float | Season year (2025) |
| masters_2026_finish | string | Finish position from the Masters dataset. Null if not in Masters dataset. |
| masters_2026_finish_num | float | Numeric finish from Masters dataset |
| masters_2026_score | float | Score to par from Masters dataset |
| putter_type_masters | string | Putter type from the Masters dataset. Null if not in Masters dataset. |
| putter_brand_masters | string | Putter brand from the Masters dataset |
| putter_model_masters | string | Putter model from the Masters dataset |
| putter_consistency | string | Derived. Describes whether putter type is consistent across datasets. Values: consistent, changed: blade->mallet (or vice versa), only_in_one_dataset. |
| putter_type_unified | string | Derived. Single unified putter type. Prefers Masters classification (more recent); falls back to PGA 2025. |

---

## Putter Type Classification

The following describes how putter type was assigned. This classification was applied consistently across both datasets.

**Mallet:** A putter with a larger, typically semi-circular or geometric head shape behind the face. Generally associated with higher moment of inertia (MOI), better forgiveness on off-center strikes, and built-in alignment aids. Examples: TaylorMade Spider Tour X, Scotty Cameron Phantom series, Odyssey Ai-One series.

**Blade:** A putter with a thin, blade-like head, historically the traditional shape. Associated with better feel feedback, lower MOI, and a more traditional aesthetic. Examples: Scotty Cameron Newport series, Odyssey Toulon Design, Ping Anser.

**Unknown:** Assigned when putter type could not be confidently determined from available sources. No records currently have this value in either dataset.

Classification was based on manufacturer specifications, Golf Monthly WITB articles, EssentiallySports WITB profiles, MyGolfSpy equipment reviews, and GolfWRX equipment coverage. Where sources disagreed, the most recently published dedicated WITB article took precedence.
