# 🛡️ Professional Password Generator

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Type](https://img.shields.io/badge/category-Cybersecurity-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A CLI-based password generation tool designed for **Cybersecurity** and **Penetration Testing**. It features real-time password strength analysis, entropy calculation, and brute-force time estimation.

---

## ✨ Key Features

*   🚀 **Interactive Mode**: Run without arguments to be guided through an interactive setup menu.
*   🔍 **Password Checker**: Audit the strength, entropy, and crack time of any existing password.
*   📊 **Strength Analysis**: Evaluates password security based on industry-standard criteria.
*   🔐 **Entropy Calculation**: Measures the mathematical randomness of characters in bits.
*   ⏳ **Crack Time Estimation**: Estimates the time required to crack the password using modern hardware.
*   🎨 **Cyberpunk UI**: Sleek terminal interface with an ASCII banner and color-coded output.
*   📂 **Batch Output**: Save generated passwords directly to a `.txt` file for wordlist creation.

---

## 🛠️ Installation

Make sure you have Python installed on your system.

1. Clone this repository:
   ```bash
   git clone https://github.com/ForwardEcho/password-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-generator
   ```

---

## 🚀 Usage

There are three ways to run this script:

### 1. Interactive Mode (Easiest)
Simply run the script without any arguments:
```bash
python passgenerate.py
```

### 2. Generator Mode (CLI)
Use flags for fast and specific generation:
```bash
python passgenerate.py -l 16 -n 10 -o pass.txt -s 2 -d 2 -a 12
```

### 3. Checker Mode (Analysis)
Use the `-c` flag to audit a specific password:
```bash
python passgenerate.py -c your_password_here
```

---

### Command Line Arguments:
| Flag | Name | Description |
|---|---|---|
| `-l` | `--length` | Total length of the password. |
| `-n` | `--number` | Number of passwords to generate. |
| `-o` | `--output` | Output filename. |
| `-s` | `--special` | Minimum special characters. |
| `-d` | `--digits` | Minimum digits. |
| `-a` | `--letters` | Minimum letters. |
| `-c` | `--check` | Audit a specific password string. |
| `-i` | `--interactive`| Manually trigger interactive mode. |

---

## 📸 Preview
When executed, the tool provides a detailed security breakdown:
```text
[#] Sample: .[N6`878'*Z9NFM
[#] Entropy: 91.31 bits
[#] Strength: Strong
[#] Crack Time: 97,460,151.84 Centuries
[+] Successfully generated 10 passwords!
[+] Saved to: password-list.txt
```

---

## ⚠️ Disclaimer
Usage of this tool for illegal purposes is strictly prohibited. The author is not responsible for any misuse of this tool. Use it for education, security research, and authorized penetration testing only.

---

## 👨‍💻 Credits
Created with ❤️ by **ForwardEcho**
