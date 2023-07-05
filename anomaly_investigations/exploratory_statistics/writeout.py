def write_stats_to_json(statistics, value_field, file_path):
    # Prepare data to be written to the JSON file
    data = {}
    for identifier, stats in statistics.items():
        data[identifier] = {
            "value_checked": value_field,
            "total_data_points": stats["total_data_points"],
            "mean": stats["mean"],
            "std_dev": stats["std_dev"],
            "median": stats["median"],
            "iqr": stats["iqr"],
            "anomaly_lower_threshold": stats["anomaly_lower_threshold"],
            "anomaly_upper_threshold": stats["anomaly_upper_threshold"],
            "z_scores": stats["z_scores"].tolist(),  # Convert numpy array to list
        }