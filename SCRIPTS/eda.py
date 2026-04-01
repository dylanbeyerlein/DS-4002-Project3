"""
This script performs exploratory data analysis on the raw skin lesion dataset.
It reads data from DATA/raw_data.csv and creates several plots to help visualize
the distribution of important variables in the dataset.

The plots are saves to the OUTPUTS/figures/ directory.

Plots created:
    - target count plot
    - diagnosis count plot
    - age histogram
    - age by target boxplot
    - anatomical site count plot
    - anatomical site by target stacked bar chart
    - sex by target count plot
"""


# Import the libraries needed for file handling, data loading, and plotting
import os
import pandas as pd
import matplotlib.pyplot as plt


# Define the file path for the raw dataset and the folder for saved figures
CSV_PATH = "DATA/raw_data.csv"
OUTPUT_DIR = "OUTPUT/figures/"


# Load the raw dataset into a pandas DataFrame
def load_data():
    data = pd.read_csv(CSV_PATH)
    return data


# Create and save a bar chart showing the number of benign and malignant cases
def create_target_count_plot(data):
    # Count the number of cases in each target class
    target_counts = data["target"].value_counts().sort_index()

    # Rename the target values to more readable labels
    labels = {
        0: "Benign",
        1: "Malignant"
    }

    # Store the bar labels, counts, and percentages for the plot
    x_labels = [labels[value] for value in target_counts.index]
    counts = target_counts.values
    total_count = len(data)
    percentages = [(count / total_count) * 100 for count in counts]

    # Create the bar chart
    bars = plt.bar(x_labels, counts)

    # Add percentage labels over each bar
    for bar, percentage in zip(bars, percentages):
        bar_height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar_height,
            f"{percentage:.2f}%",
            ha="center",
            va="bottom"
        )

    # Add plot labels and save the figure
    plt.title("Target Counts")
    plt.xlabel("Target")
    plt.ylabel("Count")
    plt.savefig(OUTPUT_DIR + "target_count.png")
    plt.close()


# Create and save a bar chart showing the number of cases for each diagnosis
def create_diagnosis_count_plot(data):
    # Count the number of cases in each diagnosis category
    diagnosis_counts = data["diagnosis"].value_counts()

    # Store the bar labels, counts, and percentages for the plot
    x_labels = diagnosis_counts.index
    counts = diagnosis_counts.values
    total_count = len(data)
    percentages = [(count / total_count) * 100 for count in counts]

    # Create the bar chart
    bars = plt.bar(x_labels, counts)

    # Add percentage labels above each bar
    for bar, percentage in zip(bars, percentages):
        bar_height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar_height,
            f"{percentage:.2f}%",
            ha="center",
            va="bottom"
        )

    # Add plot labels, rotate the x-axis labels, and save the figure
    plt.title("Diagnosis Count")
    plt.xlabel("Diagnosis")
    plt.ylabel("Count")
    plt.xticks(rotation=90, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "diagnosis_count.png")
    plt.close()


# Create and save a histogram showing the distribution of approximate ages
def create_age_histogram(data):
    # remove missing values from the age column
    age_data = data["age_approx"].dropna()

    # Create the histogram with black outlines around each bin
    plt.hist(age_data, bins=20, edgecolor="black")

    # Add plot labels, set x-axis ticks, and save the figure
    plt.title("Age Histogram")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.xticks(range(0, 101, 5))
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "age_histogram.png")
    plt.close()


# Create and save a boxplot comparing age distributions for benign and malignant cases
def create_age_by_target_boxplot(data):
    # Keep only the age and target columns and remove rows with missing values
    boxplot_data = data[["age_approx", "target"]].dropna()

    # Separate ages into benign and malignant groups
    benign_ages = boxplot_data[boxplot_data["target"] == 0]["age_approx"]
    malignant_ages = boxplot_data[boxplot_data["target"] == 1]["age_approx"]

    # Create the boxplot for the two target groups
    plt.boxplot([benign_ages, malignant_ages], labels=["Benign", "Malignant"])

    # Add plot labels and save the figure
    plt.title("Age by Target")
    plt.xlabel("Target")
    plt.ylabel("Age")
    plt.savefig(OUTPUT_DIR + "age_by_target.png")
    plt.close()


# Create and save a bar chart showing the number of cases for each anatomical site
def create_anatomical_site_count_plot(data):
    # Count the number of cases in each anatomical site category
    site_counts = data["anatom_site_general_challenge"].value_counts()

    # Store the bar labels, counts, and percentages for the plot
    x_labels = site_counts.index
    counts = site_counts.values
    total_count = len(data)
    percentages = [(count / total_count) * 100 for count in counts]

    # Create the bar chart
    bars = plt.bar(x_labels, counts)

    # Add percentage labels above each bar
    for bar, percentage in zip(bars, percentages):
        bar_height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar_height,
            f"{percentage:.2f}%",
            ha="center",
            va="bottom"
        )

    # Add plot labels, rotate the x-axis labels, and save the figure
    plt.title("Anatomical Site Counts")
    plt.xlabel("Anatomical Site")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "anatomical_site_count.png")
    plt.close()


# Create and save a stacked bar chart showing benign and malignant counts for each anatomical site
def create_anatomical_site_by_target_stacked_bar_chart(data):
    # Build a table of counts for each anatomical site split by target
    site_target_counts = pd.crosstab(
        data["anatom_site_general_challenge"],
        data["target"]
    )

    # Rename the target values to more readable labels
    site_target_counts = site_target_counts.rename(
        columns={
            0: "Benign",
            1: "Malignant"
        }
    )

    # Create the stacked bar chart
    site_target_counts.plot(
        kind="bar",
        stacked=True
    )

    # Add plot labels, rotate the x-axis labels, and save the figure
    plt.title("Anatomical Site by Target")
    plt.xlabel("Anatomical Site")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Target")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "anatomical_site_by_target.png")
    plt.close()


# Create and save a bar chart comparing benign and malignant case counts by sex
def create_sex_by_target_count_plot(data):
    # Build a table of counts for each sex split by target
    sex_target_counts = pd.crosstab(
        data["sex"],
        data["target"]
    )

    # Rename the target values to more readable labels
    sex_target_counts = sex_target_counts.rename(
        columns={
            0: "Benign",
            1: "Malignant"
        }
    )

    # Create the grouped bar chart
    sex_target_counts.plot(
        kind="bar"
    )

    # Add plot labels, rotate the x-axis labels, and save the figure
    plt.title("Sex by Target")
    plt.xlabel("Sex")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Target")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "sex_by_target.png")
    plt.close()


# Create the output folder, load the data, and run all EDA plotting functions
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data = load_data()

    create_target_count_plot(data)
    create_diagnosis_count_plot(data)
    create_age_histogram(data)
    create_age_by_target_boxplot(data)
    create_anatomical_site_count_plot(data)
    create_anatomical_site_by_target_stacked_bar_chart(data)
    create_sex_by_target_count_plot(data)


# Run the EDA script
if __name__ == "__main__":
    main()
