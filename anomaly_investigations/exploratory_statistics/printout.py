def print_stats(statistics, value_field):
    for identifier, stats in statistics.items():
        print("Identifier:", identifier)
        print("Value checked:", value_field)
        print("Total Data Points:", stats["total_data_points"])
        print("Mean:", stats["mean"])
        print("Standard Deviation:", stats["std_dev"])
        print("Median:", stats["median"])
        print("Interquartile Range (IQR):", stats["iqr"])
        print("Anomaly Lower Threshold:", stats["anomaly_lower_threshold"])
        print("Anomaly Upper Threshold:", stats["anomaly_upper_threshold"])
        print("Z-Scores:", stats["z_scores"])
        print()