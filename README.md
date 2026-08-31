# NumPy Analyzer

A robust, object-oriented interactive CLI application written in Python using **NumPy** for array manipulation, linear algebra, array combination/splitting, searching/sorting/filtering, and statistical analysis.

---

## Table of Contents
- [Features](#features)
- [Architecture & Class Overview](#architecture--class-overview)
- [Flowcharts](#flowcharts)
  - [Application Flowchart](#application-flowchart)
  - [Mathematical Operations Flowchart](#mathematical-operations-flowchart)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Method Summary](#method-summary)
- [License](#license)

---

## Features

- **Array Creation**: Supports creating 1D, 2D, and 3D arrays dynamically from user input.
- **Indexing & Slicing**: Navigate elements or extract sub-matrices (2D) with start:end range controls.
- **Mathematical Operations**: Perform matrix addition, subtraction, multiplication, division, dot product, and matrix multiplication (`matmul`).
- **Combine & Split**: Concatenate 2D arrays along vertical axes or split arrays into equal parts.
- **Search, Sort & Filter**: Flat array searching via `np.where`, ascending/descending sorting, and boolean condition filtering.
- **Statistical Analytics**: Calculate sum, mean, median, standard deviation, variance, min, max, percentiles, and Pearson correlation coefficients.
- **OOP Paradigm**: Built using encapsulation, class methods, and static methods.

---

## Architecture & Class Overview

```
DataAnalytics (Class)
│
├── Encapsulated Property
│   └── __array (Private NumPy NDArray)
│
├── Array Management
│   └── create_array()
│   └── indexing_slicing()
│
├── Mathematics & Transformations
│   └── mathematical_operations()
│   └── combine_split()
│
├── Searching & Statistics
│   └── search_sort_filter()
│   └── statistics()
│
└── Utility & Execution
    ├── run()
    ├── from_list(values) [@classmethod]
    └── show_project_info() [@staticmethod]
```

---

## Flowcharts

### Application Flowchart

```mermaid
flowchart TD
    Start([Start Program]) --> Init[Initialize DataAnalytics Object]
    Init --> Menu[Display Main Menu]
    
    Menu --> Choice{User Selection}
    
    Choice -->|1| Create[1. Create Array]
    Choice -->|2| IndexSlice[2. Indexing & Slicing]
    Choice -->|3| MathOps[3. Mathematical Operations]
    Choice -->|4| CombSplit[4. Combine or Split Arrays]
    Choice -->|5| SearchSort[5. Search, Sort, Filter]
    Choice -->|6| Stats[6. Aggregates & Statistics]
    Choice -->|7| Exit([7. Exit Program])
    
    Create --> CheckArray1[Store array in __array]
    IndexSlice --> CheckArray2{Is __array None?}
    MathOps --> CheckArray3{Is __array None?}
    CombSplit --> CheckArray4{Is __array None?}
    SearchSort --> CheckArray5{Is __array None?}
    Stats --> CheckArray6{Is __array None?}
    
    CheckArray2 -->|Yes| PromptCreate[Prompt: Create array first]
    CheckArray3 -->|Yes| PromptCreate
    CheckArray4 -->|Yes| PromptCreate
    CheckArray5 -->|Yes| PromptCreate
    CheckArray6 -->|Yes| PromptCreate
    
    CheckArray2 -->|No| Exec1[Perform Indexing/Slicing Submenu]
    CheckArray3 -->|No| Exec2[Execute Selected Math Operation]
    CheckArray4 -->|No| Exec3[Perform Combine/Split Submenu]
    CheckArray5 -->|No| Exec4[Execute Search/Sort/Filter Option]
    CheckArray6 -->|No| Exec5[Compute Selected Metric]
    
    PromptCreate --> Menu
    CheckArray1 --> Menu
    Exec1 --> Menu
    Exec2 --> Menu
    Exec3 --> Menu
    Exec4 --> Menu
    Exec5 --> Menu
```

---

### Mathematical Operations Flowchart

```mermaid
flowchart TD
    StartMath([Mathematical Operations Menu]) --> Check2D{Is array 2D?}
    
    Check2D -->|No| Err2D[Error: Requires 2D Array] --> Return([Return to Main Menu])
    Check2D -->|Yes| SelectOp{Select Operation}
    
    SelectOp -->|Addition / Subtraction / Multiplication / Division| ElementWise[Input 2nd array of matching shape]
    SelectOp -->|Dot Product / Matrix Multiplication| MatrixOps[Input dimensions & elements of 2nd array]
    
    ElementWise --> ValShape1{Does element count match?}
    ValShape1 -->|No| ShapeErr[Error: Incorrect element count] --> Return
    ValShape1 -->|Yes| Compute1[Execute element-wise NumPy operation] --> Display[Print Result] --> Return
    
    MatrixOps --> ValShape2{Do cols equal 2nd array rows?}
    ValShape2 -->|No| DimErr[Error: Incompatible matrix dimensions] --> Return
    ValShape2 -->|Yes| Compute2[Execute np.dot or np.matmul] --> Display --> Return
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Setup Steps
1. Clone or download the repository to your local machine:
   ```bash
   git clone https://github.com/amrawat0110-ctrl/numpy-analyzer.git
   cd numpy-analyzer
   ```

2. Install the required dependencies:
   ```bash
   pip install numpy
   ```

3. Run the application:
   ```bash
   python numpy_analyzer.py
   ```

---

## Usage Guide

1. **Creating an Array**: Run option `1` from the main menu and follow the prompts to specify dimensions (1D, 2D, 3D) and enter numeric values.
2. **Indexing & Slicing**: Choose option `2` to extract individual elements using zero-based indices or sub-matrices using range slicing (e.g., `0:2` for rows and `1:3` for columns).
3. **Performing Matrix Math**: Use option `3` to perform linear algebra operations. Ensure matching array sizes for element-wise operations or dimension alignment for dot/matmul operations.
4. **Statistical Analysis**: Option `6` provides instant summary statistics including mean, variance, standard deviation, and correlation calculations with a second array.

---

## Method Summary

| Method | Description |
| :--- | :--- |
| `__init__(array=None)` | Constructor to initialize private `__array` attribute. |
| `create_array()` | Dynamic menu for creating 1D, 2D, or 3D NumPy arrays. |
| `indexing_slicing()` | Zero-based element lookup and 2D sub-array slicing. |
| `mathematical_operations()` | Matrix arithmetic, `np.dot`, and `np.matmul`. |
| `combine_split()` | Vertical concatenation and split functionality. |
| `search_sort_filter()` | `np.where` search, sorting, and boolean filter masking. |
| `statistics()` | Summary stats (mean, median, std, var, percentile, corrcoef). |
| `from_list(values)` | Class method alternative constructor. |
| `show_project_info()` | Static method to print project banner details. |

---

## 👨‍💻 Author

**Armin Khareghat**  
B.Sc. Computer Science  
🤖 AI / ML & Data Science  

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

⭐ If you found this project useful, consider giving the repository a star!

