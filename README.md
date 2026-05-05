# Blade vs. Mallet: A Data Analysis of Putting Performance of Differing Putter Designs on the PGA Tour

## Contributors

- Jack Forman, University of Illinois Urbana-Champaign

---

## Summary

Putting is one of the most consequential and debated aspects of professional golf. In recent years, the PGA Tour has seen a marked shift toward mallet-style putters -- putters with large, geometrically shaped heads -- and away from the traditional blade design. Equipment manufacturers have marketed mallets as more forgiving, more stable, and better suited to modern green speeds and slopes. But the question of whether this design shift actually produces better putting results has not been systematically examined using player-level performance data.

This project investigates whether putter design -- specifically the blade vs. mallet distinction -- is associated with measurable differences in putting performance among PGA Tour professionals. The central metric used is Strokes Gained: Putting (SG:Putting), the official PGA Tour standard for evaluating putting performance. Unlike putts-per-hole, SG:Putting accounts for the distance of each putt and measures performance relative to the field average, making it a far more analytically appropriate metric for this type of comparison.

Two datasets were built and integrated for this analysis. The first covers the top 20 and bottom 20 PGA Tour players ranked by SG:Putting for the completed 2025 season, with putter type, brand, and model recorded for each. The second covers the 2026 Masters Tournament, which concluded on April 12, 2026, and includes finish position, round scores, and putter equipment for 44 players. The Masters was included as a case study because Augusta National's notoriously difficult greens create an analytically interesting context for examining equipment patterns under extreme putting conditions.

The data shows a consistent and striking pattern across both datasets. Among the 20 best putters on the 2025 PGA Tour, 85% used a mallet compared to 55% in the bottom 20. At the 2026 Masters, 90% of the top-10 finishers used mallets, and mallet users averaged -6.23 strokes to par for the tournament compared to -5.70 for blade users. However, within performance groups -- that is, comparing mallet and blade users only among the top 20, or only among the bottom 20 -- the mean SG:Putting values are nearly identical. The gap at the population level appears to be driven by composition: mallets are simply far more common among the best putters and far less common among the worst. Whether this reflects a causal relationship or a selection effect is a key open question.

The four research questions guiding this project are: (1) Do mallet users have higher SG:Putting values than blade users? (2) Among the top putters on Tour, what proportion use mallets? (3) Are there observable differences in average putting performance by putter type? (4) Can putter model information from equipment sources be reliably transformed into a usable categorical variable?

---

## Data Profile

### Dataset 1: 2025 PGA Tour SG:Putting (Top and Bottom 20)

**Location:** data/raw/pga_tour_sgputt_2025_raw.csv (raw), data/cleaned/pga_sgputt_2025_clean.csv (cleaned)

**Source:** PGA Tour official statistics for the 2025 FedExCup season, compiled via Eden Steak's analytical article (edensteak.com/?p=33), which cross-referenced the official PGA Tour stats page (pgatour.com/stats/putting) with equipment records for each player.

**Access method:** Manual structured extraction from publicly available web sources. The PGA Tour stats page is JavaScript-rendered and does not expose a public API, which ruled out automated scraping. The Eden Steak article presented the data in a structured format with equipment already cross-referenced, making it a more reliable and reproducible acquisition path than scraping the underlying PGA Tour page directly.

**Structure:** 40 rows, 10 columns (raw); 40 rows, 11 columns (cleaned, with derived putter_era column).

**Unit of observation:** One player for one season.

**Key variables:**

- rank: Integer. SG:Putting season rank (1 = best putter on Tour)
- player_name: String. Full player name
- sg_putting_avg: Float. Season SG:Putting average. Positive values indicate strokes gained relative to field; negative indicates strokes lost. Adjusted for putt distance.
- putter_type: String. Controlled vocabulary: blade or mallet
- putter_brand: String. Manufacturer (e.g., TaylorMade, Scotty Cameron, Odyssey)
- putter_model: String. Specific model name
- putter_release_year: Integer. Year the model was released
- group: String. top20 or bottom20
- season: Integer. 2025
- source: String. Per-row citation

**Coverage:** The dataset intentionally covers only the extremes of the SG:Putting distribution. Players ranked approximately 21st through 160th are not included. This is a known limitation discussed further in the Data Quality section.

**Ethical and legal constraints:** All data was derived from publicly available statistics and journalism sources. PGA Tour statistics are publicly accessible and carry no redistribution restrictions for non-commercial research use. Equipment data was sourced from published journalism (Golf Monthly, MyGolfSpy) written about publicly competing professional athletes. No personal or private information is included. The dataset is released under CC BY 4.0.

**Relation to research questions:** This dataset directly addresses research questions 1, 2, and 3 by providing SG:Putting averages for players whose putter type is known. It addresses question 4 by documenting the process of transforming model names into the blade/mallet classification.

---

### Dataset 2: 2026 Masters Tournament Leaderboard and Equipment

**Location:** data/raw/masters_2026_leaderboard_raw.csv (raw), data/cleaned/masters_2026_clean.csv (cleaned)

**Source:** Multiple corroborating journalism sources collected April 13-14, 2026, immediately after the tournament concluded. Sources include: Golf Monthly WITB articles, EssentiallySports player profiles, Sky Sports final leaderboard, MyGolfSpy equipment reviews, and Wikipedia's 2026 Masters Tournament article.

**Access method:** Manual structured extraction from multiple public web sources. No public API or structured data feed exists for Masters equipment or leaderboard data -- Augusta National does not release Shotlink data publicly. Equipment data was triangulated across dedicated WITB articles (high confidence for top finishers) and pre-tournament equipment coverage (medium confidence for lower finishers).

**Structure:** 44 rows, 12 columns (raw); 44 rows, 13 columns (cleaned, with derived finish_num column).

**Unit of observation:** One player in one tournament.

**Key variables:**

- finish: String. Final finish position (e.g., 1, T3, MC for missed cut)
- player_name: String. Full player name
- score_to_par: Integer. 72-hole score relative to par. Null for MC players.
- r1, r2, r3, r4: Integer. Round scores (gross). r3 and r4 are null for MC players.
- putter_type: String. Controlled vocabulary: blade or mallet
- putter_notes: String. Free-text field recording confidence level, equipment switches, or classification rationale
- source: String. Per-row citation

**Coverage:** 40 players who made the cut, plus 4 players who missed the cut included for context. Full field size was 91 players. Players who withdrew or were not captured in equipment sources were excluded.

**Ethical and legal constraints:** All data was derived from publicly available tournament results and equipment journalism. The leaderboard is public information. Equipment data is derived from published third-party journalism about public sporting events. Released under CC BY 4.0 for the curated dataset; original source articles retain their own copyrights.

**Relation to research questions:** This dataset provides a tournament-level case study for research questions 1, 2, and 3. It also offers a different context (major championship at a uniquely difficult putting venue) from the regular-season PGA Tour data, enabling cross-context comparison.

---

### Integrated Dataset

**Location:** data/integrated/integrated_putter_analysis.csv

**Structure:** 75 rows, 16 columns

**Description:** Full outer join of the two cleaned datasets on player_name. Records from players who appear in only one dataset contain null values for the columns from the other. Five players appear in both datasets: Cameron Young, Jake Knapp, Rory McIlroy, Sam Burns, and Tommy Fleetwood.

**Key derived columns:**

- putter_consistency: Flags whether putter type is consistent across datasets, or only appears in one.
- putter_type_unified: Single unified putter type, preferring Masters classification (more recent) and falling back to 2025 season classification.

---

## Data Quality

A formal quality assessment was conducted using scripts/quality_assessment.ipynb. Results are written to logs/quality_report.txt. Five quality dimensions were assessed.

**Completeness:** The PGA 2025 dataset has no missing values across any column -- all 40 records are fully populated. In the Masters 2026 dataset, r3 and r4 are null for the four players who missed the cut. This is expected and structurally correct, not a quality error. The integrated dataset has nulls wherever a player appears in only one source, which is by design.

**Validity:** All putter_type values in both datasets fall within the defined controlled vocabulary (blade, mallet, unknown). No invalid values were found. SG:Putting averages in the PGA dataset range from -0.970 to +0.983, which is consistent with the expected distribution for season averages among Tour professionals (the typical range for season leaders and worst performers is approximately -1.5 to +1.5). Masters scores to par range from -13 to +5, which is consistent with typical Augusta scoring distributions.

**Consistency:** All five players appearing in both datasets show consistent putter type classifications across both sources. There are no contradictions between the PGA 2025 data and the Masters 2026 data for shared players.

**Uniqueness:** No duplicate player records exist in either dataset. This was verified using pandas duplicate detection on the player_name field (and player_name plus season for the PGA dataset).

**Timeliness:** The PGA 2025 dataset reflects the completed 2025 FedExCup season (October 2025). The Masters 2026 dataset was collected within 48 hours of the tournament's conclusion (April 12, 2026), which is the most current available data.

**Known limitations and concerns:**

The most significant quality concern is coverage. The PGA 2025 dataset covers only the top and bottom 20 players by SG:Putting, representing approximately 22% of the full ranked player pool. The 140-odd players in the middle of the distribution are not captured. This means the analysis reflects extremes and cannot characterize the full population-level relationship between putter type and performance. This limitation is acknowledged throughout the project and is the primary gap identified for future work.

A secondary concern is source confidence for the Masters dataset. Top-10 finishers have strong sourcing from dedicated equipment articles. Players finishing T25 and below were classified using pre-tournament equipment surveys, which may not reflect same-week setup changes. Known cases of uncertainty are flagged in the putter_notes column.

A third concern is mid-season equipment switches. Several players changed putter types during the 2025 season. Ben Griffin is the most notable example. He is classified as a blade user based on dominant-season usage, but his late-season switch to a mallet introduces classification uncertainty. Similar cases are flagged in the source column.

---

## Data Cleaning

All cleaning is implemented in clean_and_integrate.ipynb, which reads from data/raw/ and writes to data/cleaned/ and data/integrated/.

**Player name standardization.** Player names across both sources contained inconsistent whitespace and mixed capitalization. All names were stripped of leading/trailing whitespace and converted to title case using pandas str.strip().str.title(). This was necessary to ensure the player_name join key worked correctly when merging the two datasets.

**Controlled vocabulary enforcement for putter_type.** The raw data used lowercase values (blade, mallet) sourced from manual classification. The cleaning step verified that all putter_type values fall within the set {blade, mallet, unknown} and flagged any invalid values. No violations were found in either dataset, but this check provides a documented safeguard and is reproducible.

**Duplicate detection.** Both datasets were checked for duplicate records using pandas drop_duplicates on the player_name field (and player_name plus season for the PGA dataset). No duplicates were found.

**Range validation.** SG:Putting values were validated to fall within [-1.5, +1.5]. All 40 values passed. This check protects against data entry errors that would be obvious outliers.

**Derived column: putter_era.** A categorical column classifying each putter by release year was added to the PGA cleaned dataset. Values are classic (pre-2016), mid-era (2016-2020), and modern (2021+). This was derived from the putter_release_year column and enables a secondary analysis of whether putter recency correlates with performance.

**Derived column: finish_num.** A numeric version of the Masters finish column was added to the Masters cleaned dataset, parsing T-prefix ties and assigning MC records a value of 999 for sorting purposes. This enables numeric sorting and tier-based grouping for analysis.

**Integration.** The two cleaned datasets were joined using a pandas full outer join on player_name. This preserves all records from both sources. A putter_consistency column was derived by comparing putter_type_2025 and putter_type_masters for players appearing in both datasets. A putter_type_unified column was created preferring the Masters classification (more recent) and falling back to the 2025 season classification.

---

## Findings

These results are descriptive. The dataset size and sampling strategy (extremes only) do not support causal inference or formal statistical testing at this stage.

**Mallet dominance among the best putters.** Among the 20 best putters on the PGA Tour in 2025 by SG:Putting, 17 used mallet putters (85%) and 3 used blades (15%). Among the 20 worst putters, 11 used mallets (55%) and 9 used blades (45%). That is a 30-percentage-point gap in mallet prevalence between the two groups. Figure 1 shows this distribution.

**Within-group performance is similar across putter types.** This is the most analytically interesting finding. Among the top 20, mallet users averaged +0.585 SG:Putting and blade users averaged +0.578. Among the bottom 20, mallet users averaged -0.553 and blade users averaged -0.577. In both groups, the difference between putter types is less than 0.025 strokes per round -- essentially negligible. Figure 2 shows this clearly. The large overall mean gap between all mallet users (+0.138) and all blade users (-0.288) is therefore driven by composition: there are more mallets in the high-performing group and more blades in the low-performing group. Whether this is because mallets help performance, or because already-skilled putters have migrated to mallets, cannot be determined from this data.

**Masters results are consistent with the season data.** At the 2026 Masters, 9 of the top 10 finishers used mallets (90%). The only blade user in the top 10 was Collin Morikawa, widely recognized as one of the Tour's elite ball-strikers whose finishes typically reflect approach play more than putting. Among all 40 players who made the cut, 30 used mallets (75%) and 10 used blades (25%). Mallet users averaged -6.23 strokes to par for the tournament; blade users averaged -5.70, a gap of 0.53 strokes. Figure 4 shows putter type breakdown by finish tier.

**Equipment brands.** Among the top 20 PGA Tour putters in 2025, Scotty Cameron and TaylorMade Spider models account for the majority of mallet usage. Odyssey Ai-One models are also well represented. The three blade users in the top 20 (Harry Hall, Zach Johnson, Ben Griffin) use Odyssey, SeeMore, and Scotty Cameron models respectively.

See results/ for all four figures.

---

## Future Work

The most important limitation of this project is coverage. The PGA 2025 dataset covers only the top and bottom 20 players by SG:Putting. Expanding this to all approximately 180 ranked players for the 2025 season would dramatically change the nature of the analysis. With a full-population dataset, it would be possible to run a proper regression of SG:Putting on putter type while controlling for relevant factors such as experience level, rounds played, and world ranking. The current dataset can only describe the extremes.

A related extension would be adding a temporal dimension. The PGA Tour dataset used here covers one season. Expanding to five or ten seasons would allow analysis of whether the mallet trend has grown over time and whether individual players who switch putter types show performance changes. Several high-profile switches occurred during this period -- Scottie Scheffler and Rory McIlroy both moved to mallets and won major championships shortly after -- but anecdotal examples are not evidence. A longitudinal dataset tracking individual players across seasons would allow before-and-after comparisons.

There is also a missing variable problem. Putter type alone is likely a weak predictor of performance compared to factors like green reading ability, stroke mechanics, and mental composure under pressure. A stronger model would incorporate additional variables such as green in regulation percentage (to control for approach proximity), years on Tour (as a proxy for experience), or world ranking. None of these are currently in the dataset.

The Masters case study is a starting point for tournament-level analysis, but a single tournament is not a sufficient sample. Extending the equipment dataset to cover multiple major championships -- ideally all four majors over multiple years -- would allow a more robust test of whether Augusta's specific conditions change the blade/mallet picture, or whether the pattern is consistent across contexts.

Finally, the putter_era variable (classifying each putter as classic, mid-era, or modern by release year) has not been analyzed yet. It is possible that performance differences are better explained by how recently a player adopted a new putter than by the putter type itself. A player who has used the same blade for fifteen years may putt differently than one who just switched, regardless of the shape of the head.

---

## Challenges

**JavaScript-rendered data sources.** The original plan called for scraping ESPN's PGA Tour stats page and GolfWRX's What's In The Bag forum. Both turned out to be impractical. ESPN's stats tables are rendered with JavaScript, meaning a standard HTTP request returns an empty page structure. GolfWRX is forum content with inconsistent formatting across posts. Working around these required switching to compiled secondary sources -- the Eden Steak article for PGA stats, and dedicated sports journalism for equipment data. This was a better outcome analytically (better metric, cleaner data) but required rethinking the acquisition approach midway through the project.

**No structured source for Masters equipment data.** Augusta National does not release Shotlink data publicly and no structured equipment database covers Masters fields. Building the Masters dataset required manually cross-referencing multiple journalism sources for each player, assigning confidence tiers, and documenting each classification individually. This is time-consuming and introduces variability in source quality across the dataset that would not exist in a structured API.

**Mid-season equipment switches.** At least three players in the PGA 2025 dataset switched putters during the season. Ben Griffin is the clearest case. This creates an assignment problem: his SG:Putting average reflects months of play with a blade and months with a mallet, but the putter_type column assigns him one value. The dominant-season approach used here is the most defensible choice with available information, but it introduces measurement error for affected players. This problem would be harder to ignore with a full-population dataset.

**Limited player overlap between datasets.** Only five players appear in both the PGA 2025 and Masters 2026 datasets. This significantly limits cross-dataset comparisons. The cause is the PGA dataset's extreme-only design -- expanding it to all ranked players would resolve most of this.

**Metric selection.** The original plan used putts-per-hole as the performance metric. Switching to SG:Putting was the right decision analytically, but it required identifying alternative data sources partway through the project. SG:Putting is not as straightforward to acquire as a simple table scrape, and the switch added time to the acquisition phase.

---

## Reproducing

The following steps will reproduce all outputs from raw data through final figures.

**Requirements:**
- Python 3.10 or higher
- pip (Python package manager)
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

This will execute the following steps in order:
1. scripts/acquire.py -- verifies SHA-256 checksums of raw data files
2. clean_and_integrate.ipynb -- cleans both datasets and produces the integrated CSV
3. quality_assesment.ipynb -- runs data quality checks and writes logs/quality_report.txt
4. scripts/analysis.py -- generates summary statistics and saves figures to results/

**Expected outputs after running:**
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

**Note on raw data:** The raw CSV files (data/raw/) are included in the repository and do not require re-downloading. They were manually curated from public sources documented in the source column of each file. The acquire.py script verifies their integrity against known SHA-256 checksums but does not re-fetch them from the web.

**Note on notebooks:** The cleaning and quality assessment steps use Jupyter notebooks (clean_and_integrate.ipynb, quality_assesment.ipynb). The run_all.py script executes them using nbconvert. If nbconvert is not available, the notebooks can also be run manually in Jupyter:

```
jupyter notebook
```

Then open and run each notebook in order: clean_and_integrate.ipynb, then quality_assesment.ipynb.

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
