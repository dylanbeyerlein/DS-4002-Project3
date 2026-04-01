import os
import pandas as pd
import matplotlib.pyplot as plt


CSV_PATH = "DATA/raw_data.csv"
OUTPUT_DIR = "OUTPUT/figures/"


def load_data():
    data = pd.read_csv(CSV_PATH)
    return data


def create_target_count_plot(data):
    target_counts = data["target"].value_counts().sort_index()

    labels = {
        0: "Benign",
        1: "Malignant"
    }

    x_labels = [labels[value] for value in target_counts.index]
    counts = target_counts.values
    total_count = len(data)
    percentages = [(count / total_count) * 100 for count in counts]

    bars = plt.bar(x_labels, counts)

    for bar, percentage in zip(bars, percentages):
        bar_height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar_height,
            f"{percentage:.2f}%",
            ha="center",
            va="bottom"
        )

    plt.title("Target Counts")
    plt.xlabel("Target")
    plt.ylabel("Count")
    plt.savefig(OUTPUT_DIR + "target_count.png")
    plt.close()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data = load_data()
    create_target_count_plot(data)


if __name__ == "__main__":
    main()
