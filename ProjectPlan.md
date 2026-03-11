# Blade vs Mallet: A Data Analysis of Putting Performance of Differing Designs on the PGA Tour

# Overview
Putting is one of the most important and highly debated parts of golf performance. In the current landscape of golf, two designs rank supreme: The blade, aptly named for its knifelike shape; and the mallet, which resembles more of a pancake shape. Players of the PGA tour argue about which design leads to better results. Blades are usually associated with better feel and homage to traditional designs. Mallet putters are associated more with forgiveness and alignment support, coming onto the scene more recently. This project investigates whether putter design is associated with any measureable differences in putting performance on the PGA Tour

To answer this question, this project will integrate two datasets from different origins. The first dataset will come from ESPN's PGA Tour player statistics pages, which provide structured player statistics by season, including putting-related statistics such as putts per hole. The second dataset will be built by scraping GolfWRX "What's in the Bag" pages, which name the putter model used by individual professional golfers. These equipment records will be transformed into a structured dataset and classified into putter types such as blade or mallet. A secondary validation source will be used, GOLF.com's article on the top 2025 PGA Tour Strokes gained.

This project will follow the data lifecycle discussed in class: acquisition, storage, cleaning, integration, quality assessment, analysis, visualization, and workflow automation. The final output will include reproducible scripts, project documentation, and a set of findings about the relationship between putter type and putting performance.

# Team
I will be working alone on this project, and will be handling all roles and responsibilities as per the data lifecycle.

# Research Questions
The main research question for this project is: "Does putter design between blade and mallet correlate with differences in PGA Tour putting performance?"

To answer this question, the project will investigate the following more specfic questions:
1. Do players using mallet putters have lower putts-per-hole values than players using blade putters?
2. Among the highest-performing putters on tour, what proportion use mallet putters versus blade putters?
3. Are there observable differences in average putting performance between players using blade putters and players using mallet putters?
4. Can putter model information from equipment pages be reliably transformed into a consistent categorical variable for equipment analysis?

# Datasets
### Dataset 1: ESPN PGA Tour Player Statistics
The first dataset will come from ESPN’s PGA Tour statistics pages. ESPN publishes season-based player rankings with structured tabular data, including player names and performance metrics. One relevant example is the 2025 PGA Tour player stats table sorted by putts per hole. The page includes player names, rankings, and a putts metric that can be scraped directly from the HTML. This is useful because it provides a public, structured, and repeatable source of player-level putting performance data.

#### Planned variables include:
- player_name
- season
- rank
- putts_per_hole
-rounds_played

This dataset is relevant because as a structured web table, it provides quantitative data to be used for analysis. It is different in format and origin from the equipment data source.

### Dataset 2: GolfWRX “What’s in the Bag” Equipment Data
The second dataset will be created from GolfWRX’s “What’s in the Bag” archive and selected player-specific WITB pages. The archive contains PGA player pages with repeated structure and visible player names. These pages include detailed lists of clubs in each player’s bag, including the putter model. This source is relevant because it provides the equipment side of the project.

#### Planned variables include:
- player_name
- article_date
- putter_model
- putter_brand
- putter_type (derived: blade or mallet)
- source_url

This dataset is not available as a prebuilt CSV, so it will require converting semi-structured equipment information into a structured tabular format.

### Dataset 3 - Secondary Validation Source - GOLF.com
To strengthen data quality and classification accuracy, this project will also use GOLF.com’s article listing the top 2025 PGA Tour Strokes Gained: Putting leaders and the putters they used. This source explicitly maps top players such as Sam Burns and Taylor Montgomery to named putter models and also notes when a player switched putters during the season. This will not serve as the main second dataset, but it will be used to validate a subset of putter classifications and to document uncertainty in equipment assignment.

# Timeline

### By The Interim Status Report (March 31st):

1. Acquisition 
   Scrape ESPN player stats pages and GolfWRX WITB pages using Python scripts.

2. Storage and Organization
   Store raw HTML or raw extracted files separately from cleaned CSV outputs.

3. Cleaning
   Standardize player names, remove duplicates, resolve formatting issues, and classify putters as blade or mallet.

4. Integration
   Merge the cleaned performance dataset with the cleaned equipment dataset using player names.

5. Data Quality Control
   Check for unmatched players, missing putter classifications, and duplicate records.

#### Gaps and Constraints
As player data will require manual scraping, there could potentially be some issues with regards to time constraints. As well, there may be gaps in player data regarding which putter styles are used as some players switch their putter several times during a season.

### By The Final Project Submission (May 3rd):

6. Analysis and Visualization  
   Compare putting performance across putter types using summary tables and charts.

7. Reproduceable Data
   Build an reproducible workflow so another person can rerun the project from raw data collection through final outputs.

#### Gaps and Constraints
As some data will be collected manually, it may not be feasable for a third party to reproduce the project from scratch.
