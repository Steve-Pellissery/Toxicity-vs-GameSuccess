### Toxicity vs Game Success
An Empirical Analysis of Online Gaming Communities & Player Engagement

This project explores whether community toxicity impacts a game's success, or whether player engagement (playtime) is a more powerful driver of profitability. Using over 150,000 Steam reviews and game metadata, the analysis combines descriptive statistics, visualizations, and regression models to uncover what truly influences game performance.

--- 

### 🎯 Research Question

Does toxicity negatively influence a game's success, or do players continue to engage even in toxic environments?

---

### 📌 Key Findings

Toxicity does NOT reduce overall game success.

Engagement (playtime) is the strongest predictor of ownership and popularity (correlation ≈ 0.91).

Action & MMO genres show higher toxicity, yet remain commercially successful.

Logistic Regression shows:

✔ Playtime predicts “top game” status

✔ Toxicity has no significant predictive effect

---

### 🧠 Methods & Techniques Used
✔ Descriptive Analysis

Identified distributions, trends, and early patterns in engagement and sentiment.

✔ Data Visualizations

Correlation heatmaps

Genre-toxicity boxplots

Playtime vs ownership scatterplots

Logistic model prediction charts

✔ Statistical Modeling

OLS Regression

Regression with control variables

Logistic Regression (Top vs Non-top games)

✔ Advanced Techniques

Interaction effects

Model comparison

Predictive probability visualization

---

### 📂 Repository Structure
/Notebooks      → Colab notebooks for EDA, modeling & visuals

/data           → Raw & cleaned datasets

/outputs        → Final graphs, charts & summaries

/src            → Helper Python scripts

Academic Report.pdf → Professional Report of the Project

README.md       → Project overview

---

### 🛠️ Tech Stack

Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-Learn

Statsmodels

---

### 📈 Business Implications

Developers should prioritize engagement-oriented features, as playtime strongly predicts success.

High-toxicity genres (competitive/MMO) continue to perform well—indicating players often tolerate toxicity for gameplay value.

Engagement metrics can serve as early performance indicators for studios and publishers.

---

### ⚠️ Limitations

Steam data may not generalize across all gaming platforms.

Keyword-based toxicity scoring may miss context (sarcasm, slang, etc.).

Analysis reflects a snapshot in time, not long-term behavioral changes.

---

### 🚀 Future Work

Apply advanced NLP models (VADER, TextBlob, BERT) for richer sentiment analysis.

Build a machine learning model to predict future game success.

Analyze toxicity patterns over time to understand community evolution.

---

### 👤 Author

Steve Sebastian Pellissery

Graduate Student — Business Analytics

Clark University
