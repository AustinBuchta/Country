# CLI Country Code Dictionary Manager

A Python command-line utility for managing country codes and names. Uses key-value data structures (dictionaries) to provide full CRUD operations (Create, Read, Update, Delete) with normalized inputs.

## Technical Highlights

* **Dictionary Data Management:** Utilizes Python dictionary structures (`key: value` pairs) to store, fetch, and mutate country mappings in constant $O(1)$ time complexity.
* **Input Case Normalization:** Implements `.upper()` and `.title()` string sanitization methods on user inputs to ensure standardized key matching and consistent string formatting.
* **Keys Sorting & Extraction:** Converts dictionary keys to explicit list structures (`list(countries.keys())`) to execute alphabetic sorting before rendering key options to the terminal interface.
* **Dynamic Key Removal:** Leverages Python's native `.pop()` method to simultaneously purge targeted key-value pairs while returning deleted values for dynamic user feedback.

## Technical Requirements

* **Python Version:** Built using pure standard Python 3.x (requires zero external `pip` dependencies).

## Usage

```bash
python main.py
