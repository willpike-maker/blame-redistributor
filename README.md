# `blame-redistributor` ⚖️

> **Pareto-Optimal Deniability Optimization for Git Repositories**

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Culpability](https://img.shields.io/badge/culpability-decentralized-blue.svg)]()
[![Psychological Safety](https://img.shields.io/badge/psychological%20safety-100%25-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-purple.svg)]()

Traditional static analysis and VCS blame metadata (`git blame`, `git annotate`) suffer from a fundamental structural flaw: they assign 100% of line-level failure to a single historical human actor.

In modern blameless post-mortem environments, single-point attribution undermines psychological safety and concentrates existential dread. **`blame-redistributor`** solves this at the data plane by algorithmically reallocating blame metadata across your engineering organization using simulated annealing, achieving optimal egalitarian dispersion while keeping code syntax intact.

---

## 🏛 Architecture

```
                  ┌────────────────────────┐
                  │      git-blame.log     │
                  └───────────┬────────────┘
                              │
                    [ Gini Index Filter ]
                              │
                              ▼
               ┌──────────────────────────────┐
               │    Egalitarian Annealer      │
               │   (Simulated Culpability)    │
               └──────────────┬───────────────┘
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
   [ Senior Engineers ]               [ Decentralized Blame ]
 (Absorb Legacy Overhead)           (Target Gini Coefficient: < 0.05)
```

---

## 🚀 Quick Start

### Installation

```bash
pip install git-blame-redistributor
```

### Basic Invocation

Smooth out culpability on an incendiary legacy module:

```bash
git redistribute-blame --file src/payment_processor.py --fairness 0.95 --protect-juniors
```

### Sample Output

```text
============================================================
⚖️  GIT BLAME REDISTRIBUTOR v0.1.0
   Pareto-Optimal Deniability Optimization Subsystem
============================================================

[+] Analyzing file: src/legacy_monolith.py
[+] Initial Gini Inequality Index: 0.7421

[!] Pre-optimization blame dispersion:
    alice          :  85.7% | █████████████████
    bob            :  14.3% | ██
    carol          :   0.0% | 
    dave           :   0.0% | 

[+] Post-optimization Gini Inequality Index: 0.0384
[✓] Post-optimization decentralized culpability:
    alice          :  28.6% | █████
    bob            :  28.6% | █████
    carol          :  28.6% | █████
    dave           :  14.3% | ██

[✓] Synthetic blame annotations successfully smoothed.
    Psychological safety restored to engineering organization.
```

---

## ⚙️ Configuration & Flags

| Flag | Type | Default | Description |
|---|---|---|---|
| `--fairness` | `float` | `0.92` | Egalitarian smoothing factor (`0.0` = cold reality, `1.0` = complete communism). |
| `--protect-juniors` | `bool` | `true` | Shields engineers with tenure < 12 months from fatal attribution. |
| `--team` | `list` | `[all]` | List of team handles among whom blame should be equitably dispersed. |

---

## 🧪 Running Tests

```bash
python3 -m unittest discover tests
```

---

## 📜 License

MIT © 2026 Will Pike & Contributors. Distributed in the pursuit of institutional equanimity.
