# Day 2: Python Foundations: File Handling

On day 2, I am mostly focusing on how config files and data files are handled. Generally this is how programming in real-time happens where in we will have configuration files which stores all the important information related to the program our code runs. Focussing on the data files is also in the agenda wherein working with CSV, JSON, etc files will be carried.

## 1. Configuration Files

### What is a config file?

A configuration file (config file) is a simple text file used to store settings and parameters for software applications. This contains variables and their values that control the behaviour of the application. Config files are commonly used to separate configuration settings from the main  code.

### Why use config files?

1. **Separation of Concerns**: Config files allow you to separate configuration settings from the main code, making it easier to manage and modify settings without changing the code itself.
2. **Flexibility**: Config files provide flexibility to change settings without recompiling or redeploying the application.
3. **Reusability**: Config files can be reused across different environments (development, testing, production) by simply changing the config file without modifying the code.
4. **Ease of Maintenance**: Config files make it easier to maintain and update settings, especially in large applications with multiple configuration options.

We'll use `.ini`, which is a simple text file used for configuration purposes. It consists of sections, each containing **key-value pairs** that define settings for an application. INI files are commonly used to store configuration data in a structured format that is easy to read and modify.

---

## 2. Data Formats: CSV and JSON

### What is CSV?
CSV (Comma-Separated Values) is a plain-text format that stores tabular data. Each line is a record, and fields are separated by a delimiter (commonly a comma). CSV is simple, widely supported, and ideal for spreadsheets and lightweight data exchange.

Key points:
- Fields may be quoted (e.g., "value, with comma").
- Use a header row to name columns.
- Be careful with newlines, encodings (UTF-8 recommended), and delimiters.
- Python stdlib: csv.reader, csv.DictReader, csv.writer, csv.DictWriter.

### What is JSON?
JSON (JavaScript Object Notation) is a text format for structured data, using objects (dictionaries) and arrays (lists). It supports nested structures and is widely used in APIs and configuration.

Key points:
- Use json.load / json.loads to parse, json.dump / json.dumps to write.
- Use indentation for readability (json.dump(`fp`, `obj`, `indent=2`)).
- Control non-ASCII handling with `ensure_ascii=False`.
- Validate structure and handle missing keys gracefully.

---

## 3. Mini Exercises

- `mini_exercise_config_file.py`
  - **Goal**: Practice reading configuration files and carry on tasks using those configuration

- `mini_exercise_json_to_csv.py`
  - **Goal**: Practice parsing nested JSON and converting those parsed data into CSV.

----
