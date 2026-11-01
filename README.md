<div align="center">

# 🛡️ Password Strength Analyzer

[![Thiranex Internship](https://img.shields.io/badge/Internship-Thiranex-blue.svg?style=for-the-badge&logo=shield)](https://thiranex.in)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Domain](https://img.shields.io/badge/Domain-Cybersecurity-red.svg?style=for-the-badge)](https://thiranex.in)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg?style=for-the-badge)]()

*A cybersecurity-focused tool designed to evaluate password strength using mathematical entropy calculation, rule-based scoring, and breach checks.*

---

</div>

## 📌 Project Overview & Internship Context

This project was developed as part of the **Thiranex Cybersecurity Internship Program**. The goal is to build an interactive, security-focused Python utility that evaluates user passwords in real time. It goes beyond simple length checks by measuring **mathematical entropy** ($H = L \cdot \log_2(N)$), detecting common/leaked credentials, and delivering actionable security feedback.

---

## 📊 Features & Evaluation Criteria

| Feature | Description | Impact on Score |
| :--- | :--- | :---: |
| **Common Password Check** | Cross-references inputs against known breached/common password dictionaries | **Instant Fail** (Score: 0) |
| **Length Verification** | Evaluates total character count ($\ge 12$ optimal, $\ge 8$ acceptable) | Up to +30 pts |
| **Character Diversity** | Detects lower, upper, digits, and special symbols | Up to +70 pts |
| **Entropy Calculation** | Computes brute-force resistance in bits ($\log_2$ space analysis) | Informational Metric |
| **Actionable Feedback** | Generates tailored recommendations to fix password weaknesses | Real-time Guidance |

---

## 🔄 Dataflow & System Architecture

```mermaid
flowchart TD
    A([User Input Password]) --> B{Is Password in Common/Leaked List?}
    B -- Yes --> C[Assign Score: 0 & Verdict: Weak]
    B -- No --> D[Calculate Mathematical Entropy]
    
    D --> E[Evaluate Character Sets]
    E --> E1[Lowercase Check +15 pts]
    E --> E2[Uppercase Check +15 pts]
    E --> E3[Numeric Check +20 pts]
    E --> E4[Special Symbol Check +20 pts]
    
    D --> F[Evaluate Length]
    F --> F1[12+ Chars: +30 pts]
    F --> F2[8-11 Chars: +15 pts]
    
    E1 & E2 & E3 & E4 & F1 & F2 --> G[Sum Total Score / Cap at 100]
    G --> H{Score Threshold Verdict}
    
    H -->|80 - 100| I[Very Strong 🟢]
    H -->|60 - 79|  J[Strong 🔵]
    H -->|40 - 59|  K[Moderate 🟡]
    H -->|< 40|     L[Weak 🔴]
    
    C & I & J & K & L --> M([Output Analysis & Recommendations Report])
```

---

## 📈 Scoring & Verdict Matrix

```
  Score Range     Verdict        Risk Level       Recommended Action
  -----------   -------------    ----------       -----------------------------------
   80 - 100     Very Strong       Minimal         Ready for production use.
   60 - 79      Strong            Low             Consider adding length or symbols.
   40 - 59      Moderate          Medium          Add uppercase, digits, or symbols.
    0 - 39      Weak              High            Do not use! Highly vulnerable.
```

---

## 🖥️ Terminal Interface Preview

```text
==========================================
      PYTHON PASSWORD STRENGTH CHECKER    
==========================================
Enter a password to analyze: P@ssw0rd2026!

--- Password Analysis ---
Length  : 13 characters
Entropy : 85.12 bits
Score   : 100/100
Verdict : Very Strong

Recommendations:
 - Good length.
```

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Core Modules Used:**
  * `math` — Logarithmic entropy calculations
  * `re` — Regular expressions pattern matching for character sets
* **Dependencies:** None (Uses standard library for maximum portability)

---

## 📂 Repository Structure

```text
password-strength-analyzer/
│
├── password_checker.py    # Core application logic & CLI
├── README.md              # Detailed project documentation
└── requirements.txt       # Environment dependencies tracker
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/password-strength-analyzer.git
cd password-strength-analyzer
```

### 2. Run the script
```bash
python password_checker.py
```

---

<div align="center">
  <sub>Developed for the <b>Thiranex Cybersecurity Virtual Internship</b></sub>
</div>
