# 🇮🇳 Indian Financial Freedom Simulator

### A Monte Carlo-Based Retirement Planning and Financial Sustainability Simulator

> **Plan your future. Stress-test your assumptions. Understand how resilient your retirement plan could be.**

The Indian Financial Freedom Simulator is an interactive web application built with Python and Streamlit that helps users explore the long-term sustainability of their retirement plans.

The application allows users to enter their current age, planned retirement age, life expectancy, existing investments, annual savings, retirement expenses, equity allocation, and retirement-oriented investments such as EPF, PPF, and NPS.

Instead of relying on a single fixed investment-return assumption, the simulator uses Monte Carlo simulation to generate multiple possible combinations of investment returns and inflation. The results are presented through interactive visualizations and easy-to-understand financial indicators, helping users understand the range of outcomes their retirement plan could potentially experience.

The purpose of the project is not to predict the future with certainty. Instead, it is to demonstrate how statistical simulation and data-driven scenario analysis can be used to understand financial uncertainty and retirement sustainability.
---

## 🎯 Project Overview

Retirement planning is usually presented as a simple calculation: estimate how much money will be available at retirement, estimate future expenses, and check whether the money is enough.

However, real financial planning is much more uncertain than a single calculation suggests.

Investment returns can vary significantly from year to year, inflation can be higher or lower than expected, and retirement may last for several decades. Because of this uncertainty, a retirement plan that looks comfortable under one fixed return assumption may behave very differently under another set of market conditions.

The Indian Financial Freedom Simulator was developed to explore this uncertainty through simulation.

The application allows a user to describe their current financial position and retirement goals, including their age, planned retirement age, current investments, annual savings, expected retirement expenses, equity allocation, EPF, PPF, and NPS holdings.

The simulator then creates multiple possible financial scenarios by varying investment returns and inflation. Instead of presenting only one projected retirement corpus, it shows a range of potential outcomes and estimates how frequently the simulated portfolio remains funded until the selected life expectancy.

The project combines financial modeling, probability, Monte Carlo simulation, numerical computing, and interactive data visualization into a single web application.

---

## 💡 Why I Built This Project

I built this project to understand how data science can be applied to a practical financial decision-making problem.

One of the main ideas behind the project is that financial planning should not depend entirely on a single assumption such as "my investments will earn 10% every year." That assumption makes the calculation simple, but it does not represent the uncertainty present in real markets.

I wanted to build something where users could change their assumptions and immediately see how the overall retirement picture changes.

For example, a user can experiment with a different retirement age, annual savings amount, retirement spending level, equity allocation, inflation assumption, or stress scenario and observe how these changes affect the simulated outcomes.

This also gave me an opportunity to apply concepts from data science that are often studied separately in theory. The project brings together probability, random sampling, Monte Carlo simulation, numerical computation, statistical summaries, data visualization, and interactive application development.

The goal is therefore not to create a system that claims to predict exactly what will happen in the future. The goal is to create an understandable tool that helps users explore **financial uncertainty, risk, and the sustainability of a retirement plan**.
---

## ✨ Key Features

The simulator is designed to keep retirement planning simple for the user while still providing a meaningful simulation-based analysis in the background.

### 🧭 Guided Financial Planning Workflow

The application uses a step-by-step form instead of making the user search through different sections of the interface.

The financial information is organized into four main stages:

1. **Your Life** – current age, retirement age, and life expectancy.
2. **Your Money** – current investments, annual savings, retirement expenses, and equity allocation.
3. **Your EPF / PPF / NPS** – existing balances and future contributions to major Indian retirement-oriented schemes.
4. **Simulation Settings** – inflation assumptions, inflation uncertainty, number of scenarios, and stress-testing options.

This structure makes the application easier to use, especially for users who may not have a technical or financial background.

### 💰 Indian Retirement Investment Support

The simulator is designed with commonly used Indian retirement investments in mind. Users can include:

- Mutual funds and other liquid investments
- EPF
- PPF
- NPS

Each component can be entered separately so that the user can see how their different sources of retirement savings contribute to the overall financial picture.

### 🎲 Monte Carlo-Based Scenario Analysis

Instead of producing a retirement projection from only one fixed return assumption, the simulator generates multiple possible financial scenarios.

Investment returns and inflation are varied across the simulations, allowing the user to explore a range of possible outcomes.

The application summarizes these scenarios using percentile-based wealth projections and a modeled portfolio success rate.

### 📈 Interactive Financial Visualizations

The results are presented using interactive Plotly charts.

The wealth projection shows:

- A relatively favorable outcome
- The median or typical outcome
- A relatively difficult outcome

The application also displays how retirement expenses may increase over time as inflation affects purchasing power.

### 🧠 Plain-English Results

The application does not expect users to understand statistical terminology before using it.

After the simulation, important results are explained in simple language, including:

- Chance that the money lasts
- Typical retirement corpus
- Typical depletion point
- Years remaining until retirement
- Important assumptions
- Possible ways to improve the plan

### 🧪 Stress Testing

Users can also examine more difficult financial environments through optional stress scenarios, including:

- High inflation conditions
- Equity bear-market conditions

This helps users understand how sensitive their retirement plan may be to unfavorable conditions.

### 🔎 Input Review

After running the simulation, users can expand a dedicated section to review the exact values they entered.

This makes the analysis more transparent and helps users verify that the simulation is based on the intended assumptions.
---

## 🔄 How the Application Works

The application follows a simple flow from financial inputs to simulated retirement outcomes. The user does not need to understand the underlying calculations to use the simulator.

The overall process is:

User Financial Information
            ↓
      Input Validation
            ↓
     Financial Assumptions
            ↓
    Accumulation Simulation
            ↓
   Monte Carlo Scenario Generation
            ↓
     Retirement Simulation
            ↓
   Portfolio Depletion Analysis
            ↓
     Statistical Summaries
            ↓
 Interactive Charts & Results

 ---

## 📝 Inputs and Outputs

The simulator is designed to collect only the information required to build a retirement scenario. Each input is grouped according to its purpose so that users can understand why the information is needed.

---

### 👤 Personal and Retirement Inputs

The first section describes the user's retirement timeline.

| Input | Description |
|---|---|
| Current Age | The user's age at the beginning of the simulation |
| Planned Retirement Age | The age at which the user plans to stop working |
| Life Expectancy | The age until which the retirement plan is evaluated |

These values determine the length of the accumulation period and the number of years the retirement portfolio may need to support the user.

For example, if someone is currently 33 and plans to retire at 57, the model has 24 years to simulate the accumulation of wealth.

If the selected life expectancy is 86, the model then evaluates another 29 years of retirement.

---

### 💰 Investment and Savings Inputs

The simulator allows users to describe their current investment position and future savings.

| Input | Description |
|---|---|
| Current Investments | Current mutual funds or other liquid investments included in the plan |
| Annual Investment | Amount expected to be invested each year before retirement |
| Retirement Spending | Desired annual retirement spending expressed in today's money |
| Equity Allocation | Approximate percentage of the liquid portfolio invested in equity |

The annual investment amount is added to the portfolio during the accumulation phase.

The retirement spending amount is used as the starting annual withdrawal requirement during retirement and is increased over time using the simulated inflation rate.

---

### 🏛️ EPF, PPF and NPS Inputs

The application allows users to include three common Indian retirement-oriented savings components.

#### EPF

Users can enter:

- Current EPF balance
- Monthly EPF contribution
- EPF interest assumption

#### PPF

Users can enter:

- Current PPF balance
- Annual PPF contribution
- PPF interest assumption

#### NPS

Users can enter:

- Current NPS balance
- Monthly NPS contribution
- Expected NPS return

If a user does not have one of these schemes, the value can be entered as zero.

---

### 🌡️ Economic and Simulation Inputs

The user can also control the assumptions used by the simulation.

| Input | Purpose |
|---|---|
| Expected Inflation | Long-term inflation assumption |
| Inflation Uncertainty | Allows annual inflation to vary around the expected value |
| Number of Scenarios | Number of Monte Carlo paths generated |
| Stress Scenario | Optional adverse market or inflation environment |
| Simulation Seed | Allows the same simulation setup to be reproduced |

The simulation seed is particularly useful during testing because it allows the same random scenario set to be reproduced when the same inputs are used.

---

# 📊 What the Application Produces

After the user clicks the calculation button, the application generates several results.

### 🎯 Chance Your Money Lasts

This is the percentage of simulated scenarios in which the portfolio remains above zero at the end of the selected life-expectancy horizon.

It provides an indication of how often the current assumptions produce a financially sustainable outcome within the model.

---

### 🏖️ Typical Retirement Corpus

This represents the median simulated portfolio value at the user's selected retirement age.

It gives the user an idea of what the middle scenario looks like rather than relying on only an optimistic projection.

---

### ⚠️ Typical Depletion Point

The application examines scenarios where the portfolio becomes depleted during retirement.

It reports the median depletion age among those scenarios.

If the median simulated path does not become depleted within the modeled horizon, the application reports that depletion was not reached.

---

### ⏳ Years Until Retirement

The application calculates how many years remain between the user's current age and planned retirement age.

This provides a simple view of how much time remains for accumulation.

---

### 📈 Wealth Projection

An interactive Plotly chart shows three points of the simulated wealth distribution:

- **10th percentile** — relatively difficult outcome
- **50th percentile** — median or typical outcome
- **90th percentile** — relatively favorable outcome

The retirement age is also marked on the chart.

---

### 💸 Inflation-Adjusted Retirement Expenses

The application shows how the user's retirement spending may increase over time as inflation affects purchasing power.

This helps demonstrate why a retirement plan cannot simply assume that today's annual expenses will remain unchanged for several decades.

---

### 🧠 Financial Interpretation

The simulator also converts the numerical results into a simple interpretation.

Depending on the modeled outcome, the application may identify the plan as:

- 🟢 **Strong Result**
- 🟠 **Review Your Plan**
- 🔴 **High Modeled Risk**

The purpose of this interpretation is to make the simulation easier to understand without requiring the user to interpret statistical metrics independently.

---

## 🔎 Review Your Inputs

After running the simulation, users can expand the **"See exactly what you entered"** section.

This provides a summary of the assumptions used for the simulation and allows the user to verify that the calculation was based on the intended values.

This is particularly useful when experimenting with multiple retirement strategies because the user can compare the assumptions used in different runs.

---

## 🎲 Monte Carlo Simulation Methodology

The main analytical component of the Indian Financial Freedom Simulator is a **Monte Carlo simulation**.

A traditional retirement calculator may assume that an investment earns the same return every year. For example, it might assume a constant annual return of 10%.

While this makes the calculation simple, it does not represent the uncertainty that exists in real financial markets.

Investment returns can vary from year to year, and inflation can also change over time.

The simulator therefore generates many possible financial scenarios rather than relying on a single deterministic projection.

---

### Why Monte Carlo Simulation?

Consider two hypothetical retirement plans.

Both plans may use:
Expected investment return = 10%
---

## 🛠️ Technology Stack

The application was developed using Python-based data science and web application technologies.

### 🐍 Python

Python is the primary programming language used for the project.

It is used for:

- Financial calculations
- Monte Carlo simulation
- Input validation
- Data processing
- Application logic
- Result generation

Python was chosen because of its strong ecosystem for numerical computing, data science, statistics, and rapid application development.

---

### 🎈 Streamlit

**Streamlit** is used to convert the Python-based financial model into an interactive web application.

It handles:

- User input forms
- Application layout
- Interactive controls
- Session state
- Result presentation
- Deployment

One of the main advantages of Streamlit for this project is that the financial simulation can be connected directly to the user interface without requiring a separate frontend application.

---

### 🔢 NumPy

**NumPy** is used as the numerical computing engine for the Monte Carlo simulation.

It is used for:

- Random number generation
- Array operations
- Simulating investment returns
- Simulating inflation
- Portfolio calculations
- Percentile calculations
- Vectorized computation

Using NumPy arrays allows many simulation paths to be processed efficiently.

---

### 🐼 Pandas

**Pandas** is used primarily for organizing and displaying structured information.

For example, the application uses Pandas to create the table that allows users to review the financial assumptions they entered.

---

### 📊 Plotly

**Plotly** is used to create interactive financial visualizations.

The application currently uses Plotly for:

- Wealth projection
- Percentile-based financial scenarios
- Inflation-adjusted retirement expenses
- Retirement-age markers
- Interactive hover information

The interactive charts make it easier for users to understand how the simulated financial path changes over time.

---

### 🔧 Git

Git is used for local version control.

It allows the project to track changes to the application and makes it easier to experiment with improvements without losing previous versions.

---

### 🌐 GitHub

GitHub is used to store and manage the source code.

The repository contains:

- Application source code
- Dependency information
- Project documentation
- Version history

It also provides a public portfolio location where the project can be reviewed.

---

### ☁️ Streamlit Community Cloud

Streamlit Community Cloud is used to deploy the application.

This allows the completed Python application to be accessed through a web browser without requiring users to install Python or the project's dependencies locally.

---

# 📁 Project Structure

The repository is intentionally kept simple because the current application is a single-file Streamlit project.

```text
indian-financial-freedom-simulator/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
---

## 💻 Installation and Local Usage

The Indian Financial Freedom Simulator can be run locally on a computer with Python installed.

The following steps explain how to download the project, install its dependencies, and start the Streamlit application.

---

### 📋 Prerequisites

Before running the application, make sure the following are installed:

- Python 3
- Git
- pip
- A modern web browser

Python is required to run the financial simulation and Streamlit application.

Git is required if the project is being downloaded directly from GitHub.

---

## 1. Clone the Repository

Open Terminal or Command Prompt and run:

```bash
git clone https://github.com/rohithvs5434-max/Indian-financial-freedom-simulator








 
