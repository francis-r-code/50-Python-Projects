# Project 5: Biostats Graph
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV as a DataFrame and define searches
df = pd.read_csv("biostats.csv")
male = df.loc[0, "Sex"]
female = df.loc[5, "Sex"]

# Filter DataFrame, drop missing values
maleSet = df["Height (in)"].where(df["Sex"] == male)
femaleSet = df["Height (in)"].where(df["Sex"] == female)
maleSet.dropna()
femaleSet.dropna()

# Calculate distribution centers based on graph shape and create graph
graphY = [maleSet.median(), femaleSet.mean()]
fig, axd = plt.subplot_mosaic([["topleft", "right"],
                               ["bottomleft", "right"]], layout="constrained")

# Define graph axes & titles, then show the graph
axd["topleft"].set_title("Male Heights")
axd["topleft"].hist(maleSet, bins=7)
axd["bottomleft"].set_title("Female Heights")
axd["bottomleft"].hist(femaleSet, bins=7)
axd["right"].set_title("Height Comparison by Gender")
axd["right"].bar(["Male", "Female"], graphY)
plt.show()  # Show graph