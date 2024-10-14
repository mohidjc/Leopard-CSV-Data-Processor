# Leopard CSV Data Processor

## Author
Mohid Javed Chaudhry

## Description
The **Leopard** class is a Python-based CSV data processor that allows users to analyze and summarize data stored in CSV files. It provides functionalities to extract headers, retrieve data, compute statistics, generate HTML reports, and count specific instances based on given criteria.

## Features
- Read and parse CSV files.
- Retrieve headers and data as lists.
- Calculate statistics (count, mean, min, max) for numeric columns.
- Generate an HTML report summarizing the statistics.
- Count instances matching specific criteria across two columns.

## Requirements
- Python 3.x
- CSV files to analyze

## Installation
To run this project, ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage
1. **Initialization**:
   Create an instance of the `Leopard` class by providing the path to your CSV file.
   ```python
   leopard = Leopard("your_file.csv")
    ```
2. **Get Headers**: Retrieve the headers of the CSV file.
   ```python
   headers = leopard.get_header()
    print(headers)
    ```
3. **Get Data**: Retrieve the data from the CSV file.
   ```python
    data = leopard.get_data()
    print(data)
    ```
4. **Statistics Calculation**: Compute statistics for the numeric columns.
   ```python
    stats = leopard.stats()
    print(stats)
    ```
5. **Generate HTML Report**: Create an HTML report with the calculated statistic.
   ```python
    leopard.html_stats(stats, "report.html")
    ```
6. **Count Instances**: Count the number of instances matching specific criteria across two columns.
   ```python
    count = leopard.count_instances("Column1", "Value1", "Column2", "Value2")
    print(count)
    ```
## Example
   ```python
   if __name__ == "__main__":
    leopard = Leopard("example_data.csv")
    print(leopard.get_header())
    print(leopard.get_data())
    stats = leopard.stats()
    leopard.html_stats(stats, "example_report.html")
    count = leopard.count_instances("Gender", "Male", "Age", "30")
    print("Count of Male instances with Age 30:", count)
   ```
## Error Handling
- If the specified CSV file is not found, a message will be printed, and a value will be returned to indicate the error.
- If the headers or data are invalid, appropriate messages will be displayed.

   
