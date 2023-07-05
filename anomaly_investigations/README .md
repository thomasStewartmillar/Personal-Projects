# Statistical Analysis for preparing data for subsequent manipulation prior to machine-learning training

*Last updated: 5th July 2023*

This project aims to provide a generalised and versatile approach for statistical analysis and data manipulation. It is a work in progress and can be adapted for various use cases, I am attempted to generalise various scripts utilised on known data, data structures and with known manipulation in mind, having written specific scripts for this purpose. 

## Overview

The project follows a step-by-step process to achieve the desired goals:

1. Importing a dataset from a JSON file.
2. Extracting the JSON fields and displaying them to the user. The user can input the value fields they want to analyse.
3. Mapping said value field to every other field from the initial data i.e. if value field is 'success', map success to every other field.
4. Generating relevant statistical data from the generated dictionary.
5. Writing the pertinent statistical data to a JSON file.
6. Parsing the statistics file to manipulate the initial dataset using meaningful thresholds established in step 4.
7. Creating an altered duplicate of the initial dataset with "fudged" values randomly assigned but within statistical ranges.
8. The generated duplicate files simulate a day/month or other timeframe of report data.
9. The process can be iterated as many times as required, starting from the initial dataset.
10. The generated data can be fed into a machine learning process to train it to detect anomalous data.

## Usage Guide
1. To be very much fucking confirmed!

N.B. This project may require modifications based on your specific dataset and use case despite attempts at generalisation

Any ideas please feel free to provide as you're likely smarter than me. Or better looking. Or both. 

**Disclaimer:** If you break anything, my name is Elon Musk and feel free to reach out to me for renumeration for any damages incurred ^_^

