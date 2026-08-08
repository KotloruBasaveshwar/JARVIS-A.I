import pandas as pd
import datetime
import os
from pathlib import Path
from voice import speak
import matplotlib.pyplot as plt

# ==============================
# DATASET LOCATION
# ==============================

DATASET_FOLDER = Path.home() / "OneDrive" / "Documents"

CURRENT_DATASET = DATASET_FOLDER / "students.csv"


# ==============================
# LOAD DATASET
# ==============================

def load_dataset():
    return pd.read_csv(CURRENT_DATASET)


# ==============================
# CURRENT DATASET
# ==============================

def current_dataset():
    name = Path(CURRENT_DATASET).name
    speak(f"The current dataset is {name}")


# ==============================
# LOAD NEW DATASET
# ==============================

def load_new_dataset(command):

    global CURRENT_DATASET

    try:

        words_to_remove = {
            "load",
            "dataset",
            "please",
            "the",
            "data"
        }

        words = []

        for word in command.lower().split():

            if word not in words_to_remove:
                words.append(word)

        dataset = "_".join(words)

        file = DATASET_FOLDER / f"{dataset}.csv"

        if file.exists():

            CURRENT_DATASET = file

            speak(f"{dataset} dataset loaded successfully.")

        else:

            speak(f"{dataset} dataset was not found.")

    except Exception as e:

        print("Dataset loading error:", e)

        speak("Sorry, I could not load the dataset.")


# ==============================
# SMART DATASET ANALYSIS
# ==============================

def analyze_dataset():

    try:

        df = load_dataset()

        rows, columns = df.shape

        missing = df.isnull().sum().sum()

        duplicates = df.duplicated().sum()

        column_names = list(df.columns)

        speak(
            f"The dataset has {rows} rows and {columns} columns."
        )

        speak(
            f"It has {missing} missing values "
            f"and {duplicates} duplicate rows."
        )

        print("\nDataset:")
        print(df)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(list(df.columns))

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:

        print("Analysis error:", e)

        speak("Sorry, I could not analyze the dataset.")


# ==============================
# STATISTICS
# ==============================

def statistics(command):

    try:

        df = load_dataset()

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        if len(numeric_columns) == 0:

            speak("There are no numeric columns in this dataset.")

            return

        if "average" in command or "mean" in command:

            for column in numeric_columns:

                result = df[column].mean()

                speak(
                    f"The average {column} is {result:.2f}."
                )

        elif (
            "maximum" in command
            or "highest" in command
            or "max" in command
        ):

            for column in numeric_columns:

                result = df[column].max()

                speak(
                    f"The highest {column} is {result}."
                )

        elif (
            "minimum" in command
            or "lowest" in command
            or "min" in command
        ):

            for column in numeric_columns:

                result = df[column].min()

                speak(
                    f"The lowest {column} is {result}."
                )

        else:

            speak("I don't understand the statistics request.")

    except Exception as e:

        print("Statistics error:", e)

        speak("Sorry, I could not calculate statistics.")


# ==============================
# STUDENTS ABOVE AGE
# ==============================

def students_above(age):

    try:

        df = load_dataset()

        if "Age" not in df.columns:

            speak("This dataset does not have an Age column.")

            return

        filtered = df[df["Age"] > age]

        if filtered.empty:

            speak(f"No students above {age} years.")

        else:

            speak(f"Students above {age} years are.")

            if "Name" in df.columns:

                for name in filtered["Name"]:

                    speak(str(name))

    except Exception as e:

        print("Filter error:", e)

        speak("Sorry, I could not filter the dataset.")


# ==============================
# STUDENTS BELOW AGE
# ==============================

def students_below(age):

    try:

        df = load_dataset()

        if "Age" not in df.columns:

            speak("This dataset does not have an Age column.")

            return

        filtered = df[df["Age"] < age]

        if filtered.empty:

            speak(f"No students below {age} years.")

        else:

            speak(f"Students below {age} years are.")

            if "Name" in df.columns:

                for name in filtered["Name"]:

                    speak(str(name))

    except Exception as e:

        print("Filter error:", e)

        speak("Sorry, I could not filter the dataset.")


# ==============================
# COURSE FILTER
# ==============================

def filter_course(command):

    try:

        df = load_dataset()

        if "Course" not in df.columns:

            speak("This dataset does not have a Course column.")

            return

        words = command.lower().split()

        ignore = {
            "show",
            "student",
            "students",
            "the",
            "all",
            "list",
            "display",
            "find",
            "course"
        }

        course = " ".join(
            word for word in words
            if word not in ignore
        )

        filtered = df[
            df["Course"]
            .astype(str)
            .str.lower()
            .str.contains(course, na=False)
        ]

        if filtered.empty:

            speak(f"No {course} students found.")

        else:

            speak(f"{course} students are.")

            if "Name" in df.columns:

                for name in filtered["Name"]:

                    speak(str(name))

    except Exception as e:

        print("Course filter error:", e)

        speak("Sorry, I could not filter the course.")


# ==============================
# SORT DATASET
# ==============================

def sort_dataset(command):

    try:

        df = load_dataset()

        words = command.lower().split()

        column = None

        for available_column in df.columns:

            if available_column.lower() in words:

                column = available_column

                break

        if column is None:

            speak("I don't know which column to sort.")

            return

        sorted_df = df.sort_values(by=column)

        speak(f"Dataset sorted by {column}.")

        print(sorted_df)

    except Exception as e:

        print("Sort error:", e)

        speak("Sorry, I could not sort the dataset.")


# ==============================
# GENERATE REPORT
# ==============================

def generate_report():

    try:

        df = load_dataset()

        rows, columns = df.shape

        missing = df.isnull().sum().sum()

        duplicates = df.duplicated().sum()

        report = f"""
========== DATASET REPORT ==========

Dataset : {Path(CURRENT_DATASET).name}

Total Rows : {rows}

Total Columns : {columns}

Missing Values : {missing}

Duplicate Rows : {duplicates}

========== COLUMNS ==========

"""

        for column in df.columns:

            report += f"{column}\n"

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        if len(numeric_columns) > 0:

            report += "\n========== NUMERIC SUMMARY ==========\n\n"

            for column in numeric_columns:

                report += (
                    f"{column} Average : "
                    f"{df[column].mean():.2f}\n"
                )

                report += (
                    f"{column} Maximum : "
                    f"{df[column].max()}\n"
                )

                report += (
                    f"{column} Minimum : "
                    f"{df[column].min()}\n\n"
                )

        timestamp = datetime.datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        file = (
            Path.home()
            / "Documents"
            / f"Dataset_Report_{timestamp}.txt"
        )

        with open(file, "w") as f:

            f.write(report)

        os.startfile(file)

        speak("Dataset report generated successfully.")

    except Exception as e:

        print("Report error:", e)

        speak("Sorry, I could not generate the report.")


# ==============================
# AVAILABLE DATASETS
# ==============================

def available_datasets():

    try:

        csv_files = list(
            DATASET_FOLDER.glob("*.csv")
        )

        if not csv_files:

            speak("No datasets found.")

            return

        speak("Available datasets are.")

        for file in csv_files:

            speak(file.stem)

    except Exception as e:

        print("Dataset list error:", e)

        speak("Sorry, I could not read datasets.")
        # ==============================
# CLEAN DATASET
# ==============================

def clean_dataset():

    try:

        df = load_dataset()

        original_rows = len(df)

        # Remove duplicate rows
        df = df.drop_duplicates()

        duplicates_removed = original_rows - len(df)

        # Handle missing values
        missing_before = df.isnull().sum().sum()

        for column in df.columns:

            if df[column].isnull().sum() > 0:

                if pd.api.types.is_numeric_dtype(df[column]):

                    df[column] = df[column].fillna(
                        df[column].median()
                    )

                else:

                    mode = df[column].mode()

                    if not mode.empty:
                        df[column] = df[column].fillna(
                            mode[0]
                        )

        missing_after = df.isnull().sum().sum()

        # Save cleaned dataset
        output_file = (
            CURRENT_DATASET.parent
            / f"{CURRENT_DATASET.stem}_cleaned.csv"
        )

        df.to_csv(output_file, index=False)

        speak(
            f"Data cleaning completed. "
            f"{duplicates_removed} duplicate rows were removed."
        )

        speak(
            f"{missing_before - missing_after} missing values were handled."
        )

        speak(
            f"The cleaned dataset was saved as {output_file.name}."
        )

        print("\nCleaned Dataset:")
        print(df)

        print("\nSaved to:")
        print(output_file)

    except Exception as e:

        print("Cleaning error:", e)

        speak("Sorry, I could not clean the dataset.")
# ==============================
# VISUALIZATION
# ==============================

def create_chart(chart_type):

    try:

        df = load_dataset()

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        if len(numeric_columns) == 0:

            speak("This dataset has no numeric columns for visualization.")

            return

        column = numeric_columns[0]

        plt.figure(figsize=(8, 5))

        # ------------------------------
        # BAR CHART
        # ------------------------------

        if chart_type == "bar":

            plt.bar(
                range(len(df)),
                df[column]
            )

            plt.xlabel("Rows")
            plt.ylabel(column)
            plt.title(f"Bar Chart - {column}")

        # ------------------------------
        # PIE CHART
        # ------------------------------

        elif chart_type == "pie":

            if "Course" in df.columns:

                counts = df["Course"].value_counts()

                plt.pie(
                    counts.values,
                    labels=counts.index,
                    autopct="%1.1f%%"
                )

                plt.title("Course Distribution")

            else:

                counts = df[column].value_counts()

                plt.pie(
                    counts.values,
                    labels=counts.index,
                    autopct="%1.1f%%"
                )

                plt.title(f"Distribution of {column}")

        # ------------------------------
        # LINE CHART
        # ------------------------------

        elif chart_type == "line":

            plt.plot(
                range(len(df)),
                df[column],
                marker="o"
            )

            plt.xlabel("Rows")
            plt.ylabel(column)
            plt.title(f"Line Chart - {column}")

        # ------------------------------
        # HISTOGRAM
        # ------------------------------

        elif chart_type == "histogram":

            plt.hist(
                df[column].dropna(),
                bins=10
            )

            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.title(f"Histogram - {column}")

        else:

            speak("I don't know that chart type.")

            return

        plt.tight_layout()

        chart_file = (
            CURRENT_DATASET.parent
            / f"{CURRENT_DATASET.stem}_{chart_type}.png"
        )

        plt.savefig(chart_file)

        plt.show(block=False)
        plt.pause(0.1)
        plt.close()
        speak(
            f"{chart_type} chart created successfully."
        )

        print("Chart saved to:")
        print(chart_file)

    except Exception as e:

        print("Visualization error:", e)

        speak("Sorry, I could not create the chart.")     
# ==============================
# EXCEL AUTOMATION
# ==============================

def read_excel_file():

    try:

        excel_files = list(DATASET_FOLDER.glob("*.xlsx"))

        if not excel_files:

            speak("No Excel files were found in your Documents folder.")
            return

        file = excel_files[0]

        df = pd.read_excel(file)

        speak(
            f"Excel file {file.name} loaded successfully."
        )

        speak(
            f"It has {df.shape[0]} rows and {df.shape[1]} columns."
        )

        print("\nExcel Dataset:")
        print(df)

    except Exception as e:

        print("Excel reading error:", e)

        speak("Sorry, I could not read the Excel file.")


def write_excel_file():

    try:

        df = load_dataset()

        output_file = (
            CURRENT_DATASET.parent
            / f"{CURRENT_DATASET.stem}_excel.xlsx"
        )

        df.to_excel(
            output_file,
            index=False
        )

        speak(
            f"Excel file created successfully as {output_file.name}."
        )

        print("Excel file saved to:")
        print(output_file)

    except Exception as e:

        print("Excel writing error:", e)

        speak("Sorry, I could not create the Excel file.")


def export_report_to_excel():

    try:

        df = load_dataset()

        rows, columns = df.shape

        missing = df.isnull().sum().sum()

        duplicates = df.duplicated().sum()

        report_data = {
            "Metric": [
                "Dataset",
                "Rows",
                "Columns",
                "Missing Values",
                "Duplicate Rows"
            ],
            "Value": [
                CURRENT_DATASET.name,
                rows,
                columns,
                missing,
                duplicates
            ]
        }

        report_df = pd.DataFrame(report_data)

        output_file = (
            CURRENT_DATASET.parent
            / f"{CURRENT_DATASET.stem}_report.xlsx"
        )

        with pd.ExcelWriter(
            output_file,
            engine="openpyxl"
        ) as writer:

            report_df.to_excel(
                writer,
                sheet_name="Summary",
                index=False
            )

            df.to_excel(
                writer,
                sheet_name="Dataset",
                index=False
            )

        speak(
            f"Excel report exported successfully as {output_file.name}."
        )

        print("Report saved to:")
        print(output_file)

    except Exception as e:

        print("Excel report error:", e)

        speak("Sorry, I could not export the Excel report.")           
# ==============================
# AI DATASET Q&A
# ==============================

def dataset_question(command):

    try:

        df = load_dataset()

        command = command.lower()

        # ------------------------------
        # ROW COUNT
        # ------------------------------

        if (
            "how many rows" in command
            or "number of rows" in command
            or "how many records" in command
            or "how many students" in command
            or "total students" in command
        ):

            speak(
                f"The dataset contains {len(df)} rows."
            )

        # ------------------------------
        # COLUMN COUNT
        # ------------------------------

        elif (
            "how many columns" in command
            or "number of columns" in command
        ):

            speak(
                f"The dataset contains {len(df.columns)} columns."
            )

        # ------------------------------
        # COLUMN NAMES
        # ------------------------------

        elif (
            "what columns" in command
            or "which columns" in command
            or "column names" in command
        ):

            columns = ", ".join(
                str(column) for column in df.columns
            )

            speak(
                f"The columns are {columns}."
            )

        # ------------------------------
        # AVERAGE
        # ------------------------------

        elif (
            "average" in command
            or "mean" in command
        ):

            numeric_columns = df.select_dtypes(
                include="number"
            ).columns

            if len(numeric_columns) == 0:

                speak(
                    "There are no numeric columns."
                )

            else:

                for column in numeric_columns:

                    result = df[column].mean()

                    speak(
                        f"The average {column} is "
                        f"{result:.2f}."
                    )

        # ------------------------------
        # HIGHEST
        # ------------------------------

        elif (
            "highest" in command
            or "maximum" in command
            or "maximum value" in command
        ):

            numeric_columns = df.select_dtypes(
                include="number"
            ).columns

            if len(numeric_columns) == 0:

                speak(
                    "There are no numeric columns."
                )

            else:

                for column in numeric_columns:

                    result = df[column].max()

                    speak(
                        f"The highest {column} is "
                        f"{result}."
                    )

        # ------------------------------
        # LOWEST
        # ------------------------------

        elif (
            "lowest" in command
            or "minimum" in command
            or "minimum value" in command
        ):

            numeric_columns = df.select_dtypes(
                include="number"
            ).columns

            if len(numeric_columns) == 0:

                speak(
                    "There are no numeric columns."
                )

            else:

                for column in numeric_columns:

                    result = df[column].min()

                    speak(
                        f"The lowest {column} is "
                        f"{result}."
                    )

        # ------------------------------
        # UNIQUE VALUES
        # ------------------------------

        elif (
            "unique values" in command
            or "different values" in command
        ):

            for column in df.columns:

                values = df[column].dropna().unique()

                if len(values) <= 10:

                    result = ", ".join(
                        str(value)
                        for value in values
                    )

                    speak(
                        f"{column} has {result}."
                    )

        # ------------------------------
        # COURSE COUNT
        # ------------------------------

        elif (
            "courses" in command
            or "course count" in command
        ):

            if "Course" in df.columns:

                counts = df["Course"].value_counts()

                for course, count in counts.items():

                    speak(
                        f"{course} has {count} students."
                    )

            else:

                speak(
                    "This dataset does not have a Course column."
                )

        # ------------------------------
        # GENERAL
        # ------------------------------

        else:

            speak(
                "I can answer questions about rows, "
                "columns, averages, highest values, "
                "lowest values and unique values."
            )

    except Exception as e:

        print("Dataset Q&A error:", e)

        speak(
            "Sorry, I could not answer that dataset question."
        )        