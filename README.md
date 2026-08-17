# 🇮🇳 Indian Financial Freedom Simulator

### A Monte Carlo-Based Retirement Planning and Financial Sustainability Simulator

> **What happens to your retirement plan when the future does not go exactly as expected?**

The **Indian Financial Freedom Simulator** is an interactive financial planning application built with Python and Streamlit. It helps users explore whether their current investments, savings, retirement contributions, and expected expenses could support their desired retirement period under different market-return and inflation scenarios.

The application is designed around a simple idea:
**Retirement planning should not depend on one perfect prediction of the future.**

Instead of calculating retirement wealth using only one fixed annual return, the simulator generates many possible financial scenarios using **Monte Carlo simulation**. Each scenario has different investment returns and inflation conditions, allowing the user to see a range of possible outcomes rather than a single number.

The application is particularly designed with the Indian financial context in mind by allowing users to include **Mutual Funds, EPF, PPF, and NPS** in their retirement planning assumptions.

---

## 🌐 Live Application

**Live Demo:**  
👉 Add your Streamlit Cloud URL here

---

# 📌 Why I Built This Project

Retirement calculators often look very simple.

A user enters:
- Current savings
- Expected return
- Retirement age
- Retirement expenses

and receives a final corpus amount.
The problem is that real life does not work with one fixed return.
A portfolio may perform very well for several years and then experience a major decline. Inflation may also be higher than expected for several years. Someone retiring early may need their savings to support them for decades.

This creates an important question:
> **How resilient is a retirement plan when investment returns and inflation are uncertain?**
I built this project to explore that question using data science and simulation.

Rather than saying:
> "You will have ₹X crore at retirement."
the application tries to provide a more useful perspective:

> "Across many simulated scenarios, how often does your money last until your selected life expectancy?"
This makes the project both a **financial planning simulator** and a practical demonstration of **Monte Carlo simulation, uncertainty modeling, data visualization, and Streamlit application development**.

---

# 🎯 Project Objective
The main objective of this project is to build an easy-to-use retirement simulation tool that can:

1. Collect a user's current financial situation.
2. Model their accumulation period before retirement.
3. Include common Indian retirement-oriented assets such as EPF, PPF, and NPS.
4. Model uncertainty in investment returns.
5. Model uncertainty in inflation.
6. Simulate multiple possible retirement scenarios.
7. Estimate how often the portfolio survives until the selected life expectancy.
8. Show the user how their projected wealth may change over time.
9. Identify potential depletion risk.
10. Present the results in a way that a non-technical user can understand.

---

# 👤 Who Is This Application For?
The simulator can be useful for people who want to experiment with questions such as:

- "Can I retire at 55?"
- "What happens if I retire at 60 instead?"
- "How much should I save every year?"
- "Will my current investments be enough?"
- "How important is inflation to my retirement plan?"
- "What happens if the stock market performs poorly?"
- "What happens if inflation remains high?"
- "How much could my EPF, PPF and NPS contribute to my retirement corpus?"
- "How sensitive is my retirement plan to my annual spending?"
It can also be useful as an educational demonstration of how **probabilistic modeling** can be applied to a real-world financial problem.

---

# ✨ Key Features
## 1. Simple Step-by-Step User Interface
The application is deliberately designed so that users do not need to search through a complicated dashboard.
The workflow is organized into four simple stages:

```text
Step 1 → Your Life
Step 2 → Your Money
Step 3 → Your EPF / PPF / NPS
Step 4 → Simulation Settings
              ↓
      Calculate Your Plan
              ↓
           Results
