# Interim Status Report: Blade vs. Mallet — A Data Analysis of Putting Performance of Differing Putter Designs on the PGA Tour


## 1. Overview

This project looks at whether putter design between blade and mallet is associated with differences in putting performance on the PGA Tour. There has been a noticeable shift toward mallet putters over the past several years, but it is not obvious whether that trend is actually supported by performance data or if it is more of a narrative.

Since submitting the original project plan, I made some changes to both the data sources and the main performance metric. I've updated my plan to be more realistic and suited to the question I want to answer.


## 2. Task Status

Data acquisition for both datasets is complete. I collected the 2025 PGA Tour SG:Putting data (top and bottom 20 players) and built a dataset for the 2026 Masters leaderboard with putter information.

The project folder structure is set up, including raw, cleaned, and integrated data directories, along with scripts and logs.

Data cleaning and standardization are complete and handled through a Python script. Dataset integration is also complete, and the merged dataset has been created.

A separate script for data quality assessment has been written and generates a log file summarizing the results.

At this point, I'm not fully complete with the analysis. I have summary statistics, but I still need to make visualizations.

I haven't created the final README yet. I will make it once I am done with everything prior.


## 3. Progress on Each Task

### Data Acquisition

For the 2025 PGA Tour dataset, my original plan was to scrape ESPN’s stats page and use putts-per-hole as the main metric. That approach did not work well for two reasons. First, the ESPN page is JavaScript-rendered, so a normal request does not return usable data. Scraping it would require either manual work or tools which I am not familiar with, so I decided to opt out.

The second issue is that putts-per-hole is not actually as a strong metric as I thought because it does not account for distance. Players who hit the ball closer to the hole will naturally appear to be better putters, even if that is not actually the case.

Because of that, I switched to Strokes Gained: Putting (SG:Putting), which is the standard metric used by the PGA Tour. It accounts for distance and measures performance relative to the field, so it fits this project much better.

To get the data, I used an analytical article from edensteak.com that compiled the top 20 and bottom 20 players in SG:Putting for the 2025 season. This gave me 40 records with SG:Putting averages, putter type, brand, and model. I included source citations for each row.

For the second dataset, I added the 2026 Masters Tournament, which was not part of the original plan. The tournament finished on April 12th, two days before the status report was due, and it is directly relevant to the topic. Rory McIlroy won using a mallet putter, and nine of the top ten finishers also used mallets.

This dataset was built from multiple sources, including Golf Monthly, EssentiallySports, Sky Sports, MyGolfSpy, and Wikipedia. For top finishers, I was able to confirm equipment using dedicated articles. For players further down the leaderboard, I included confidence levels as I had to rely on pre-tournament coverage, which isn't as reliable.


### Storage and Organization

For my project, raw data is stored in `data/raw` and is not modified. Cleaned data is written to `data/cleaned`, and the merged dataset is stored in `data/integrated`.

All transformations are handled through scripts that read from raw and write new outputs. This keeps the workflow reproducible and makes it clear where each dataset comes from.


### Data Cleaning

Cleaning is handled in `clean_and_integrate.py`. The main steps include standardizing player names so they match across datasets, enforcing a controlled vocabulary for `putter_type` with the values blade, mallet, or unknown, checking for duplicates, validating SG:Putting values, and adding a derived column for putter era.

One issue that came up is that some players switched putters during the 2025 season. The clearest example is Ben Griffin, who used a blade for most of the year and then switched to a mallet later in the season. I classified him based on majority usage and added a note. There are a few similar cases, and I will discuss more about them as a limitation in the final report.


### Integration

The two datasets are merged on player name using a full outer join, which preserves all records. The result is a dataset with 75 unique players.

Only five players appear in both datasets: Cameron Young, Jake Knapp, Rory McIlroy, Sam Burns, and Tommy Fleetwood. All five have consistent putter type classifications across both datasets.

The main limitation is low overlap. The PGA dataset only includes the top and bottom 20 players. The Masters tournament includes players outside the PGA dataset.


### Data Quality Assessment

The `quality_assessment.py` script checks completeness, validity, uniqueness, consistency, and timeliness. It writes the results to a log file.

The PGA dataset is complete with no missing values, and all putter types match the expected categories. The Masters dataset has missing round data only for players who missed the cut, which is expected.

All five overlapping players have consistent classifications. The main concerns are limited coverage in the PGA dataset and varying reliability of sources for the Masters dataset. Both are documented.


## 4. Changes to the Project Plan

I dropped ESPN scraping because of the JavaScript issue and because the metric I planned to use was not ideal. Switching to SG:Putting solved both problems.

I also moved away from GolfWRX as a primary source because the data is not consistently structured. Instead, I used more structured journalism sources.

Adding the 2026 Masters was not part of the original plan, but it adds a useful case study that fits well with the rest of the project.

Switching to SG:Putting is the most important change. It is a better metric for this type of analysis.


## 5. Updated Timeline

The next step is to expand the PGA dataset to include all players by around April 25. Statistical analysis and visualizations should be completed by April 28.

Metadata and the data dictionary will be finalized by May 1, and the final README/report is due May 3.


## 6. Challenges Encountered

One challenge was dealing with JavaScript-rendered data sources, which made scraping more difficult than expected. I worked around this by using compiled sources instead.

Another issue is that there is no structured API for Masters equipment data, so I had to combine multiple sources and assign confidence levels.

Mid-season equipment changes create classification issues, since players do not always use the same putter throughout the year.

There is also limited overlap between the two datasets, which reduces the number of direct comparisons.


## 7. Preliminary Findings

These are descriptive observations, not formal statistical results.

For the 2025 PGA Tour data, 17 of the top 20 players in SG:Putting use mallets, while 3 use blades. In the bottom 20, 11 use mallets and 9 use blades. That is roughly 85% mallet usage in the top group compared to about 55% in the bottom group.

If Ben Griffin is counted as a mallet user, the top group would be closer to 90%.

At the 2026 Masters, 9 of the top 10 finishers used mallets. The only exception was Collin Morikawa.

Both datasets show a similar pattern. I am interested to see if this holds under more analysis moving forward.


## 8. Contribution Summary

This is my individual project.
