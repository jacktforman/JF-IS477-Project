"""
analysis.py
-----------
Generates all summary statistics and visualizations for the Blade vs. Mallet project.

Reads from data/cleaned/ and data/integrated/.
Saves all figures to results/.

Usage:
  python scripts/analysis.py
"""

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CLEAN_DIR   = os.path.join(os.path.dirname(__file__), "..", "data", "cleaned")
INT_DIR     = os.path.join(os.path.dirname(__file__), "..", "data", "integrated")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results")
LOG_DIR     = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

BLADE_COLOR  = "#C0392B"
MALLET_COLOR = "#2471A3"
LIGHT_GREY   = "#F4F6F7"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.facecolor": LIGHT_GREY,
    "figure.facecolor": "white",
})

pga        = pd.read_csv(os.path.join(CLEAN_DIR, "pga_sgputt_2025_clean.csv"))
masters    = pd.read_csv(os.path.join(CLEAN_DIR, "masters_2026_clean.csv"))
integrated = pd.read_csv(os.path.join(INT_DIR,   "integrated_putter_analysis.csv"))

top20 = pga[pga["group"] == "top20"]
bot20 = pga[pga["group"] == "bottom20"]

lines = []

def log(msg=""):
    print(msg)
    lines.append(str(msg))


# ─────────────────────────────────────────────────────────────
# SUMMARY STATISTICS
# ─────────────────────────────────────────────────────────────
log("=" * 60)
log("ANALYSIS RESULTS -- Blade vs. Mallet Project")
log("=" * 60)

log("\n--- 2025 PGA Tour: Top 20 ---")
top_counts = top20["putter_type"].value_counts()
log(f"  Mallet: {top_counts.get('mallet', 0)} players ({top_counts.get('mallet', 0)/len(top20)*100:.0f}%)")
log(f"  Blade:  {top_counts.get('blade', 0)} players ({top_counts.get('blade', 0)/len(top20)*100:.0f}%)")
log(f"  Mean SG:Putting (mallet): {top20[top20['putter_type']=='mallet']['sg_putting_avg'].mean():.3f}")
log(f"  Mean SG:Putting (blade):  {top20[top20['putter_type']=='blade']['sg_putting_avg'].mean():.3f}")

log("\n--- 2025 PGA Tour: Bottom 20 ---")
bot_counts = bot20["putter_type"].value_counts()
log(f"  Mallet: {bot_counts.get('mallet', 0)} players ({bot_counts.get('mallet', 0)/len(bot20)*100:.0f}%)")
log(f"  Blade:  {bot_counts.get('blade', 0)} players ({bot_counts.get('blade', 0)/len(bot20)*100:.0f}%)")
log(f"  Mean SG:Putting (mallet): {bot20[bot20['putter_type']=='mallet']['sg_putting_avg'].mean():.3f}")
log(f"  Mean SG:Putting (blade):  {bot20[bot20['putter_type']=='blade']['sg_putting_avg'].mean():.3f}")

log("\n--- Overall PGA 2025 (all 40 players) ---")
log(pga.groupby("putter_type")["sg_putting_avg"].agg(["mean", "std", "count"]).round(3).to_string())

masters_cut = masters[masters["finish"] != "MC"].copy()
log("\n--- 2026 Masters: Made cut ---")
mc_counts = masters_cut["putter_type"].value_counts()
log(f"  Mallet: {mc_counts.get('mallet', 0)} players ({mc_counts.get('mallet', 0)/len(masters_cut)*100:.0f}%)")
log(f"  Blade:  {mc_counts.get('blade', 0)} players ({mc_counts.get('blade', 0)/len(masters_cut)*100:.0f}%)")
log(f"  Mean score to par (mallet): {masters_cut[masters_cut['putter_type']=='mallet']['score_to_par'].mean():.2f}")
log(f"  Mean score to par (blade):  {masters_cut[masters_cut['putter_type']=='blade']['score_to_par'].mean():.2f}")

top10 = masters[masters["finish_num"] <= 10]
log("\n--- 2026 Masters: Top 10 ---")
t10_counts = top10["putter_type"].value_counts()
log(f"  Mallet: {t10_counts.get('mallet', 0)} players ({t10_counts.get('mallet', 0)/len(top10)*100:.0f}%)")
log(f"  Blade:  {t10_counts.get('blade', 0)} players ({t10_counts.get('blade', 0)/len(top10)*100:.0f}%)")


# ─────────────────────────────────────────────────────────────
# FIGURE 1: Putter type distribution, top 20 vs bottom 20
# ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle(
    "Putter Type Distribution: Top 20 vs. Bottom 20 Putters\n2025 PGA Tour SG:Putting",
    fontsize=13, fontweight="bold"
)

for ax, df, title in [(axes[0], top20, "Top 20 Putters"), (axes[1], bot20, "Bottom 20 Putters")]:
    counts = df["putter_type"].value_counts()
    m = counts.get("mallet", 0)
    b = counts.get("blade", 0)
    total = m + b
    bars = ax.bar(["Mallet", "Blade"], [m, b],
                  color=[MALLET_COLOR, BLADE_COLOR], width=0.5, edgecolor="white")
    ax.set_title(title, fontsize=12, fontweight="bold", pad=10)
    ax.set_ylabel("Number of Players")
    ax.set_ylim(0, 22)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color="white", linewidth=1.2)
    for bar, val in zip(bars, [m, b]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                f"{val}\n({val/total*100:.0f}%)",
                ha="center", va="bottom", fontsize=11, fontweight="bold")

plt.tight_layout()
out1 = os.path.join(RESULTS_DIR, "fig1_putter_distribution.png")
plt.savefig(out1, dpi=150, bbox_inches="tight")
plt.close()
log(f"\nFigure 1 saved: {out1}")


# ─────────────────────────────────────────────────────────────
# FIGURE 2: Mean SG:Putting by group and putter type
# ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))

means = [
    top20[top20["putter_type"] == "mallet"]["sg_putting_avg"].mean(),
    top20[top20["putter_type"] == "blade"]["sg_putting_avg"].mean(),
    bot20[bot20["putter_type"] == "mallet"]["sg_putting_avg"].mean(),
    bot20[bot20["putter_type"] == "blade"]["sg_putting_avg"].mean(),
]
colors = [MALLET_COLOR, BLADE_COLOR, MALLET_COLOR, BLADE_COLOR]
x      = [0, 0.5, 1.4, 1.9]

bars = ax.bar(x, means, color=colors, width=0.4, edgecolor="white")
ax.axhline(0, color="#555", linewidth=0.8, linestyle="--")
ax.set_xticks([0.25, 1.65])
ax.set_xticklabels(["Top 20 Putters", "Bottom 20 Putters"], fontsize=12)
ax.set_ylabel("Mean SG:Putting")
ax.set_title("Mean SG:Putting by Group and Putter Type\n2025 PGA Tour", fontsize=13, fontweight="bold")
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="white", linewidth=1.2)

for bar, val in zip(bars, means):
    offset = 0.015 if val >= 0 else -0.055
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + offset,
            f"{val:.3f}", ha="center", va="bottom", fontsize=10, fontweight="bold")

legend_patches = [
    mpatches.Patch(color=MALLET_COLOR, label="Mallet"),
    mpatches.Patch(color=BLADE_COLOR,  label="Blade"),
]
ax.legend(handles=legend_patches, loc="upper right")
plt.tight_layout()
out2 = os.path.join(RESULTS_DIR, "fig2_mean_sg_by_group.png")
plt.savefig(out2, dpi=150, bbox_inches="tight")
plt.close()
log(f"Figure 2 saved: {out2}")


# ─────────────────────────────────────────────────────────────
# FIGURE 3: Scatter -- individual player SG:Putting by rank
# ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))

for _, row in pga.iterrows():
    c = MALLET_COLOR if row["putter_type"] == "mallet" else BLADE_COLOR
    ax.scatter(row["rank"], row["sg_putting_avg"],
               color=c, s=70, zorder=3, edgecolors="white", linewidths=0.5)

ax.axhline(0, color="#888", linewidth=0.8, linestyle="--")
ax.set_xlabel("SG:Putting Season Rank (1 = best, 180 = worst)")
ax.set_ylabel("SG:Putting Average")
ax.set_title(
    "Individual Player SG:Putting by Rank -- 2025 PGA Tour\n(Top 20 and Bottom 20 shown)",
    fontsize=13, fontweight="bold"
)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="#ddd", linewidth=0.8)

legend_patches = [
    mpatches.Patch(color=MALLET_COLOR, label="Mallet"),
    mpatches.Patch(color=BLADE_COLOR,  label="Blade"),
]
ax.legend(handles=legend_patches)
plt.tight_layout()
out3 = os.path.join(RESULTS_DIR, "fig3_scatter_sg_rank.png")
plt.savefig(out3, dpi=150, bbox_inches="tight")
plt.close()
log(f"Figure 3 saved: {out3}")


# ─────────────────────────────────────────────────────────────
# FIGURE 4: Masters finish tier by putter type
# ─────────────────────────────────────────────────────────────
masters_cut["tier"] = pd.cut(
    masters_cut["finish_num"],
    bins=[0, 10, 25, 40],
    labels=["Top 10", "T11-T25", "T26+"]
)
tier_counts = masters_cut.groupby(["tier", "putter_type"], observed=True).size().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(tier_counts))
w = 0.35
ax.bar(x - w/2, tier_counts.get("mallet", [0]*len(x)), width=w,
       color=MALLET_COLOR, label="Mallet", edgecolor="white")
ax.bar(x + w/2, tier_counts.get("blade",  [0]*len(x)), width=w,
       color=BLADE_COLOR,  label="Blade",  edgecolor="white")
ax.set_xticks(x)
ax.set_xticklabels(tier_counts.index, fontsize=12)
ax.set_ylabel("Number of Players")
ax.set_title("Putter Type by Finish Tier -- 2026 Masters Tournament", fontsize=13, fontweight="bold")
ax.set_axisbelow(True)
ax.yaxis.grid(True, color="white", linewidth=1.2)
ax.legend()
plt.tight_layout()
out4 = os.path.join(RESULTS_DIR, "fig4_masters_tiers.png")
plt.savefig(out4, dpi=150, bbox_inches="tight")
plt.close()
log(f"Figure 4 saved: {out4}")


# ─────────────────────────────────────────────────────────────
# WRITE STATS LOG
# ─────────────────────────────────────────────────────────────
log_path = os.path.join(LOG_DIR, "analysis_results.txt")
with open(log_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"\nStats log written: {log_path}")
