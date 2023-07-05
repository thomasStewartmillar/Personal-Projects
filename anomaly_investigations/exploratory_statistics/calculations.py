import json
import numpy as np
from scipy import stats

FILE = "data.json"


def calculate_statistics(data, identifier_field, value_field):
    # Create a dictionary to store data for each identifier
    data_by_identifier = {}

    # Iterate over the data and populate the dictionary
    for entry in data:
        identifier = entry[identifier_field]
        value = entry[value_field]

        if identifier not in data_by_identifier:
            data_by_identifier[identifier] = []

        data_by_identifier[identifier].append(value)

    # Calculate statistics for each identifier
    statistics_by_identifier = {}
    for identifier, values in data_by_identifier.items():
        total_data_points = len(values)
        mean = np.mean(values)
        std_dev = np.std(values)
        median = np.median(values)
        iqr = stats.iqr(values)
        anomaly_lower_threshold = mean - 3 * std_dev
        anomaly_upper_threshold = mean + 3 * std_dev
        z_scores = np.abs(stats.zscore(values))

        statistics_by_identifier[identifier] = {
            "total_data_points": total_data_points,
            "mean": mean,
            "std_dev": std_dev,
            "median": median,
            "iqr": iqr,
            "anomaly_lower_threshold": anomaly_lower_threshold,
            "anomaly_upper_threshold": anomaly_upper_threshold,
            "z_scores": z_scores,
        }

    return statistics_by_identifier