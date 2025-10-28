# 💻 The TermiScript OS Simulation Project

## ✨ Overview

This repository contains a collection of interconnected Python scripts that form a **simulated, experimental command-line operating system (OS) or shell environment**.

The project features a custom shell language (`termiscript.py`), different "kernel" boot modes, core utility applications (like the `boba` bubble sort visualizer), and scripts to simulate system behaviors, including lawyer initialization and even system failure (bricking). It's a fun exploration of custom scripting and shell logic in Python.

---

## 📂 Core Components

The system is organized into several distinct Python modules, each serving a specific role:

| File Name | Description | Key Features |
| :--- | :--- | :--- |
| **`termiscript.py`** | The **custom shell interpreter** that handles basic commands for the "OS." | **`print <text>`**, **`echo >`** (for file writing), **`cat`** (for file reading), **`rm`**, custom loop logic, and mathematical operations. |
| **`atermiplusfold.py`** | The primary application environment, acting as the main interface or OS core. | Includes the **`lawyer`** class for object instantiation and information display, a **`boba`** sorting utility launcher, and commands for user reviews. |
| **`straight-line-kernel.py`** | A **"Straight Line" kernel** boot mode that runs an automated, non-interactive installation sequence on startup. | Includes a feature to randomly import either `malware.py` or `brick.py` if a generic `import` command is attempted. |
| **`losless-kernel.py`** | A more **restricted "Losless" kernel** mode that loads the custom shell while disabling potentially dangerous commands like `rm` and `do_this_now`. | Includes commands like `straightinstall` and `boot` to access different environments. |
| **`boba.py`** | An implementation of the **Bubble Sort** algorithm that visually tracks swaps and comparisons, displaying the sorting process step-by-step. | Detailed output including actual swap count and Big O notation (`O(n^2)`). |
| **`malware.py`** | A utility designed to simulate a disruptive process by generating a large, random string of mixed characters, including standard and non-standard symbols. |
| **`brick.py`** | The "system failure" script, which simply enters an infinite loop of printing empty strings to simulate a system hang or "bricking." |
| **`signature.py`** | A simple utility that prints author signatures/credits. |

---

## 🚀 Getting Started

Since this is a set of Python scripts, you can start by running one of the "kernel" files, which acts as the project's entry point.

### Prerequisites

You only need **Python 3** installed to run this project.

### Running a Kernel

1.  **Clone the repository** (or ensure all files are in the same directory).
2.  Choose the kernel mode you want to start with:

    * **Interactive (Losless Mode):** Use this for a standard, safer shell experience:
        ```bash
        python losless-kernel.py
        ```
    * **Automated (Straight Line Mode):** Use this to watch the automated install sequence:
        ```bash
        python straight-line-kernel.py
        ```

---

## 💡 Key Commands & Features

Once you are running the Losless Kernel, you can use the following commands:

| Command | Action | Notes |
| :--- | :--- | :--- |
| **`print <text>`** | Prints the specified text to the console. | |
| **`echo > <text>|<filename>`** | Writes `<text>` into the specified `<filename>`. | Note the use of the pipe `|` as a separator. |
| **`cat <filename>`** | Reads and prints the content of a file. | |
| **`for i in <text>|<count>`** | Prints the specified `<text>` a certain number of times. | |
| **`straightinstall`** | Initiates the automated Straight Line installation process (if available in the current kernel). | |
| **`boot`** | Launches the main TermiPlus application environment (`atermiplusfold.py`). |
| **`boba`** | Runs the Bubble Sort visualizer, asking for the array length and speed (fast/slow). | (Available once you `boot` into the main environment) |
| **`set lawyer`** | Creates and configures a new `lawyer` object with various rating and initialization metrics. | (Available once you `boot` into the main environment) |
| **`l.show_info`** | Displays the information for the currently set lawyer object. | (Available once you `boot` into the main environment) |
| **`sudo rm rf no-preserve-root`** | **WARNING:** This command is designed to import `brick.py` and cause a simulated system hang. | (Available once you `boot` into the main environment) |

---

## 🛠 Built With

* **Python 3** - Primary programming language.
* **`os`**, **`sys`**, **`time`**, **`random`** - Standard Python libraries for system, time, and randomization functionality.

---

### 🤔 What's Next?

Feel free to dive into the code! You can modify `termiscript.py` to add new shell commands or create a third custom kernel mode.
