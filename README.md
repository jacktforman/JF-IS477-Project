# Blade vs. Mallet: A Data Analysis of Putting Performance of Differing Putter Designs on the PGA Tour

## Contributors

- Jack Forman, University of Illinois Urbana-Champaign

---

## Summary

Putting is one of the most debated parts of professional golf, and over the past several years there has been a pretty obvious shift on the PGA Tour toward mallet putters. Equipment companies have pushed mallets hard (more forgiving, better alignment aids, higher MOI) and a lot of top players have made the switch. But whether that shift actually shows up in the performance data is a different question, and one I wanted to look at more carefully.

This project looks at whether putter design, specifically the blade vs. mallet distinction, is associated with differences in putting performance among PGA Tour professionals. The main metric I used is Strokes Gained: Putting (SG:Putting), which is the standard the PGA Tour uses to measure putting. It accounts for the distance of each putt and compares performance against the field average, which makes it a much better measure than putts-per-hole. A player who hits it close all day will have fewer putts regardless of how well they are actually putting, and SG:Putting corrects for that.

I built two datasets for this project. The first covers the top 20 and bottom 20 PGA Tour players by SG:Putting for the completed 2025 season, with putter type, brand, and model recorded for each player. The second covers the 2026 Masters Tournament, which finished on April 12, and includes finish position, round scores, and putter equipment for 44 players. I added the Masters because it finished three days before my status report was due and it was directly relevant. Nine of the top ten finishers used mallets. Augusta also has notoriously difficult greens, which makes it an interesting context for asking whether the blade/mallet pattern holds under more extreme putting conditions.

The data tells a pretty consistent story across both sources. Among the 20 best putters on the 2025 PGA Tour, 85% used mallets. Among the 20 worst, that drops to 55%, a 30-point gap. At the Masters, 90% of the top-10 finishers used mallets, and mallet users averaged -6.23 to par compared to -5.70 for blade users. So on the surface it looks like mallets are associated with better results.

The more interesting finding is what happens when you look within each group. Among the top 20, mallet users averaged +0.585 SG:Putting and blade users averaged +0.578. Among the bottom 20, mallets averaged -0.553 and blades averaged -0.577. Those gaps are essentially nothing, less than 0.025 strokes per round. So within each performance tier, putter type does not seem to matter much. The large overall gap between all mallet users (+0.138) and all blade users (-0.288) is driven by composition: mallets are just much more common among the best putters. Whether that means mallets help performance or that good putters tend to choose mallets is something this data cannot answer.

The four research questions guiding this project are: (1) Do mallet users have higher SG:Putting values than blade users? (2) Among the top putters on Tour, what proportion use mallets? (3) Are there observable differences in average putting performance by putter type? (4) Can putter model information from equipment sources be reliably turned into a usable categorical variable?

---

## Data Profile

### Dataset 1: 2025 PGA Tour SG:Putting (Top and Bottom 20)

**Location:** data/raw/pga_tour_sgputt_2025_raw.csv (raw), data/cleaned/pga_sgputt_2025_clean.csv (cleaned)

**Source:** PGA Tour official statistics for the 2025 FedExCup season, compiled via an analytical article from edensteak.com that cross-referenced the official PGA Tour stats page with equipment records for each player.

**Access method:** Manual structured extraction from publicly available web sources. The PGA Tour stats page is JavaScript-rendered and does not expose a public API, so automated scraping was not practical. The Eden Steak article had already cross-referenced equipment with the stats in a structured format, which made it a cleaner and more reproducible source than trying to scrape the underlying page directly.

**Structure:** 40 rows, 10 columns (raw); 40 rows, 11 columns (cleaned, with a derived putter_era column added during cleaning).

**Unit of observation:** One player for one season.

**Key variables:**

- rank: Integer. SG:Putting season rank (1 = best putter on Tour)
- player_name: String. Full player name
- sg_putting_avg: Float. Season SG:Putting average. Positive values mean strokes gained relative to the field; negative means strokes lost. Adjusted for putt distance.
- putter_type: String. Controlled vocabulary: blade or mallet
- putter_brand: String. Manufacturer (e.g., TaylorMade, Scotty Cameron, Odyssey)
- putter_model: String. Specific model name
- putter_release_year: Integer. Year the model was first released
- group: String. top20 or bottom20
- season: Integer. 2025
- source: String. Per-row citation for both the performance data and the equipment classification

**Coverage:** This dataset only covers the top and bottom 20 players, roughly 22% of the full ranked player pool. Players ranked 21st through about 160th are not included. This is a known limitation discussed in the Data Quality section.

**Ethical and legal constraints:** All data comes from publicly available statistics and journalism. PGA Tour statistics are publicly accessible and have no redistribution restrictions for non-commercial research use. Equipment data comes from published journalism about publicly competing professional athletes. No personal or private information is included. Released under CC BY 4.0.

**Relation to research questions:** This dataset directly addresses questions 1, 2, and 3 by providing SG:Putting averages alongside putter type classifications. It also addresses question 4 by documenting the process of turning model names into a blade/mallet variable.

---

### Dataset 2: 2026 Masters Tournament Leaderboard and Equipment

**Location:** data/raw/masters_2026_leaderboard_raw.csv (raw), data/cleaned/masters_2026_clean.csv (cleaned)

**Source:** Multiple journalism sources collected April 13-14, 2026, right after the tournament ended. Sources include Golf Monthly WITB articles, EssentiallySports player profiles, Sky Sports final leaderboard, MyGolfSpy equipment reviews, and Wikipedia's 2026 Masters article.

**Access method:** Manual extraction from multiple public sources. Augusta National does not release Shotlink data publicly, and there is no structured database for Masters equipment. For the top finishers, I was able to use dedicated WITB articles to confirm equipment. For players further down the leaderboard I had to use pre-tournament coverage, which is less reliable.

**Structure:** 44 rows, 12 columns (raw); 44 rows, 13 columns (cleaned, with a derived finish_num column).

**Unit of observation:** One player in one tournament.

**Key variables:**

- finish: String. Final finish position (e.g., 1, T3, MC for missed cut)
- player_name: String. Full player name
- score_to_par: Integer. 72-hole score relative to par. Null for MC players.
- r1, r2, r3, r4: Integer. Round scores (gross). r3 and r4 are null for MC players.
- putter_type: String. Controlled vocabulary: blade or mallet
- putter_notes: String. Free-text field noting confidence level, equipment switches, or classification rationale
- source: String. Per-row citation

**Coverage:** 40 players who made the cut, plus 4 missed-cut players included for context. The full field was 91 players.

**Ethical and legal constraints:** All data comes from publicly available tournament results and equipment journalism. The leaderboard is public information. Released under CC BY 4.0 for the curated dataset; the original source articles retain their own copyrights.

**Relation to research questions:** This dataset provides a tournament-level case study for questions 1, 2, and 3. Augusta's unusual green conditions also make it a useful comparison point against the regular-season PGA data.

---

### Integrated Dataset

**Location:** data/integrated/integrated_putter_analysis.csv

**Structure:** 75 rows, 16 columns

**Description:** Full outer join of the two cleaned datasets on player_name. Players who appear in only one dataset have null values for the columns from the other. Five players appear in both: Cameron Young, Jake Knapp, Rory McIlroy, Sam Burns, and Tommy Fleetwood.

**Key derived columns:**

- putter_consistency: Flags whether putter type is consistent across both datasets, or whether the player only appears in one.
- putter_type_unified: A single unified putter type column, preferring the Masters classification (more recent) and falling back to the 2025 season classification.

---

## Data Quality

A formal quality assessment was run using quality_assesment.ipynb. Results are written to logs/quality_report.txt. Five dimensions were assessed.

**Completeness:** The PGA 2025 dataset has no missing values. All 40 records are fully populated. In the Masters 2026 dataset, r3 and r4 are null for the four players who missed the cut, which is expected and structurally correct. The integrated dataset has nulls wherever a player appears in only one source, which is by design.

**Validity:** All putter_type values in both datasets fall within the defined vocabulary (blade, mallet, unknown). No invalid values were found. SG:Putting averages range from -0.970 to +0.983, which is consistent with where you would expect season extremes to fall for Tour professionals. Masters scores to par range from -13 to +5, which is normal for Augusta.

**Consistency:** All five players appearing in both datasets have consistent putter type classifications across both sources. No contradictions were found.

**Uniqueness:** No duplicate player records exist in either dataset, confirmed using pandas duplicate detection.

**Timeliness:** The PGA 2025 dataset reflects the completed FedExCup season (October 2025). The Masters 2026 dataset was collected within 48 hours of the tournament ending.

**Known limitations:**

The biggest quality concern is coverage. The PGA 2025 dataset only covers the top and bottom 20 players, about 22% of the full ranked pool. The roughly 140 players in the middle of the distribution are not included, so the analysis can only describe the extremes. This is the main thing I would address first in future work.

For the Masters dataset, source confidence varies. Top-10 finishers have strong sourcing from dedicated WITB articles. Players finishing T25 and below were classified using pre-tournament coverage, which may not reflect changes made during tournament week. Known uncertainty cases are flagged in the putter_notes column.

There is also the mid-season switcher problem. Several players in the PGA 2025 dataset changed putter types during the season. Ben Griffin is the clearest example. He used a blade for most of the year and switched to a mallet in the fall. He is classified as blade based on majority-season usage, which is the most defensible approach but still introduces some measurement noise for a handful of players.

---

## Data Cleaning

All cleaning is implemented in clean_and_integrate.ipynb, which reads from data/raw/ and writes to data/cleaned/ and data/integrated/.

**Player name standardization.** Player names across both sources had inconsistent whitespace and capitalization. All names were stripped and converted to title case using pandas str.strip().str.title(). This was necessary so the player_name join key would match correctly when merging the two datasets.

**Controlled vocabulary enforcement for putter_type.** The cleaning step verified that all putter_type values fall within the set {blade, mallet, unknown} and flagged any invalid values. No violations were found in either dataset, but the check is documented and reproducible.

**Duplicate detection.** Both datasets were checked for duplicates using pandas drop_duplicates on player_name (and player_name plus season for the PGA dataset). No duplicates were found.

**Range validation.** SG:Putting values were validated to fall within [-1.5, +1.5]. All 40 values passed. This is a safeguard against obvious data entry errors.

**Derived column: putter_era.** A column classifying each putter by release year was added to the PGA cleaned dataset: classic (pre-2016), mid-era (2016-2020), or modern (2021+). This comes from the putter_release_year column and could support secondary analysis of whether putter age correlates with performance.

**Derived column: finish_num.** A numeric version of the Masters finish column was added, parsing T-prefix ties and assigning MC records a value of 999. This enables sorting and tier-based grouping in the analysis.

**Integration.** The two cleaned datasets were joined on player_name using a full outer join, which keeps all records from both sources. A putter_consistency column compares putter_type_2025 and putter_type_masters for shared players. A putter_type_unified column was created preferring the Masters classification and falling back to the 2025 season value.

---

## Findings

These are descriptive results. The dataset size and sampling approach do not support causal conclusions or formal statistical testing.

**Mallet prevalence among the best putters.** Among the 20 best putters on Tour in 2025, 17 used mallets (85%) and 3 used blades. Among the 20 worst, 11 used mallets (55%) and 9 used blades. That is a 30-point gap in mallet prevalence between the two groups. Figure 1 shows this.

**Within each group, putter type barely matters.** This is the most interesting result. In the top 20, mallet users averaged +0.585 SG:Putting and blade users averaged +0.578. In the bottom 20, mallets averaged -0.553 and blades averaged -0.577. Neither gap is more than 0.025 strokes per round, which is essentially nothing. Figure 2 shows this clearly. The larger overall gap between all mallet users (+0.138 mean) and all blade users (-0.288 mean) is a composition effect. There are just more mallets in the high-performing group. Whether that reflects a real performance advantage or is a product of selection (better putters gravitating toward mallets) is something this data cannot answer.

**The Masters is consistent with the season data.** Nine of the top 10 finishers at the 2026 Masters used mallets (90%). The one exception was Collin Morikawa, whose results at Augusta tend to be driven by his iron play more than his putting. Among all 40 players who made the cut, 30 used mallets (75%) and 10 used blades. Mallet users averaged -6.23 to par; blade users averaged -5.70, a gap of about half a stroke over 72 holes. Figure 4 shows the breakdown by finish tier.

**Brand breakdown.** Among the top 20 PGA Tour putters in 2025, Scotty Cameron Phantom and TaylorMade Spider models make up most of the mallet usage. Odyssey Ai-One is also well represented. The three blade users in the top 20 (Harry Hall, Zach Johnson, and Ben Griffin) use Odyssey, SeeMore, and Scotty Cameron models respectively.

All four figures are in the results/ folder.

---

## Future Work

The most obvious next step is expanding the PGA dataset to cover all ranked players rather than just the top and bottom 20. With a full population, it would be possible to run a regression of SG:Putting on putter type while controlling for other factors like world ranking, rounds played, or years on Tour. The current dataset can only describe the extremes, which is interesting but limited.

Adding a time dimension would also be valuable. The data here covers one season. Looking at five or ten seasons would let you track whether the mallet trend has grown over time and, more importantly, whether individual players who switch putter types show performance changes before and after the switch. Rory McIlroy and Scottie Scheffler both switched to mallets and then won major championships, but two examples is not a study. A longitudinal dataset would let you actually test that.

There is also a missing variable problem. Putter type is probably a weak predictor on its own compared to things like green reading, stroke mechanics, or how far a player typically hits approach shots. A better model would include variables like greens in regulation percentage (to account for approach proximity) or world ranking. None of those are in the current dataset.

The Masters is a useful starting point for tournament-level analysis, but one tournament is a small sample. Extending the equipment data to all four majors over multiple years would allow a more reliable test of whether Augusta's conditions change the blade/mallet pattern or whether it holds consistently across settings.

One thing I built into the dataset but have not analyzed yet is the putter_era column, which classifies putters by release year. It is possible that how recently a player switched putters matters more than the shape of the head. Someone who just changed to a new putter, whether blade or mallet, may putt differently than someone who has used the same club for a decade.

---

## Challenges

**JavaScript-rendered data sources.** The original plan was to scrape ESPN's stats page and GolfWRX's What's In The Bag forum. Neither worked well. ESPN's tables are rendered with JavaScript, so a normal HTTP request returns an empty page. GolfWRX is forum content with no consistent formatting across posts. I switched to the Eden Steak article for the PGA stats and dedicated journalism for the equipment data. The outcome was actually better in terms of data quality and metric choice, but it meant rethinking the acquisition approach partway through.

**No structured source for Masters equipment data.** Augusta National does not release Shotlink data publicly, and there is no equipment database for Masters fields. Building the Masters dataset meant going through multiple sources for each player individually, rating confidence by source type, and documenting everything. It was more labor intensive than a structured API would have been and introduces variability in source reliability across the dataset.

**Mid-season equipment switches.** At least three players in the PGA 2025 dataset changed putters during the season. The clearest case is Ben Griffin, whose SG:Putting average reflects months with a blade and months with a mallet, but who gets one classification in the dataset. The dominant-season approach is the best available option with the information I had, but it is an imperfect solution.

**Limited overlap between datasets.** Only five players appear in both datasets. This limits direct cross-dataset comparisons. The cause is straightforward: the PGA dataset only covers the extremes, so most Masters field members are not in it. Expanding PGA coverage would fix most of this.

**Metric selection.** The original plan used putts-per-hole, which turned out to be the wrong metric for this question. Switching to SG:Putting was the right call but required finding new data sources mid-project, which added time to the acquisition phase.

---

## Reproducing

**Requirements:**
- Python 3.10 or higher
- pip
- Git

**Step 1: Clone the repository**

```
git clone https://github.com/jacktforman/JF-IS477-Project.git
cd JF-IS477-Project
```

**Step 2: Install dependencies**

```
pip install -r requirements.txt
```

**Step 3: Run the full pipeline**

```
python run_all.py
```

This runs four steps in order:
1. scripts/acquire.py verifies SHA-256 checksums of the raw data files
2. clean_and_integrate.ipynb cleans both datasets and produces the integrated CSV
3. quality_assesment.ipynb runs quality checks and writes logs/quality_report.txt
4. scripts/analysis.py generates summary statistics and saves the four figures to results/

**Expected outputs:**
- data/cleaned/pga_sgputt_2025_clean.csv
- data/cleaned/masters_2026_clean.csv
- data/integrated/integrated_putter_analysis.csv
- logs/acquisition_log.txt
- logs/quality_report.txt
- logs/analysis_results.txt
- results/fig1_putter_distribution.png
- results/fig2_mean_sg_by_group.png
- results/fig3_scatter_sg_rank.png
- results/fig4_masters_tiers.png

**Note on raw data:** The raw CSV files are included in the repository and do not need to be re-downloaded. They were built from public sources documented in the source column of each file. The acquire.py script verifies their integrity via SHA-256 checksums but does not re-fetch anything from the web.

**Note on notebooks:** The pipeline runs the notebooks using nbconvert. If that fails for any reason, you can also run them manually by opening Jupyter and executing clean_and_integrate.ipynb first, then quality_assesment.ipynb.

```
jupyter notebook
```

---

## References

- PGA Tour official statistics, 2025 season. https://www.pgatour.com/stats/putting

- Eden Steak (March 31, 2026). Blade vs. Mallet: What the Best and Worst Putters on the 2025 PGA Tour Use. https://edensteak.com/?p=33

- Golf Monthly (2026). The Clubs Rory McIlroy Is Using At The 2026 Masters. https://www.golfmonthly.com/news/the-clubs-rory-mcilroy-is-using-at-the-2026-masters

- Golf Monthly (November 3, 2025). 5 Interesting Takeaways From The Gear Used By The PGA Tour's Top 50 Players. https://www.golfmonthly.com/features/the-equipment-debrief

- PGA Tour (November 25, 2025). Why pros are switching to mallet putters. https://www.pgatour.com/article/news/equipment-report/2025/11/25/why-pros-are-switching-to-mallet-putters

- EssentiallySports (April 2026). Sam Burns WITB April 2026. https://www.essentiallysports.com/golf-news-sam-burns-witb-april-2026

- Sky Sports Golf (April 12, 2026). The Masters 2026 leaderboard: Final golf scores. https://www.skysports.com/golf/news/12176/13529496

- Wikipedia (2026). 2026 Masters Tournament. https://en.wikipedia.org/wiki/2026_Masters_Tournament

- MyGolfSpy (June 20, 2025). Mallets Versus Blades: What The Best Putters On Tour Use. https://mygolfspy.com/news-opinion/tour/mallets-versus-blades-what-the-best-putters-on-tour-use/

- GolfDigest (2026). Masters 2026: Do you really have to putt well to win at Augusta National? https://www.golfdigest.com/story/masters-2026-do-you-really-have-to-putt-well-to-win-at-augusta-national

- McKinney, Wes (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference. [pandas library]

- Hunter, J.D. (2007). Matplotlib: A 2D graphics environment. Computing in Science and Engineering, 9(3), 90-95. [matplotlib library]
