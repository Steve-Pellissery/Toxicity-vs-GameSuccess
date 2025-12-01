Toxicity vs Game Success
An Empirical Analysis of Online Gaming Communities & Player Engagement

This project investigates whether community toxicity impacts a game's success, or whether player engagement (playtime) is a stronger predictor of profitability. Using 150k+ Steam reviews and game metadata, this study combines descriptive analytics, visualizations, and regression models to uncover what truly drives game performance.

🎯 Research Question

Does toxicity negatively influence a game's success, or do players continue to engage even in toxic environments?

📌 Key Findings

Toxicity does NOT reduce game success.

Engagement (playtime) is the strongest predictor of ownership and profitability (correlation ≈ 0.91).

Competitive genres (MMO, Action) consistently show higher toxicity but remain highly successful.

Logistic Regression confirms:
✔ Playtime significantly predicts “top game” status
✔ Toxicity has no statistically significant effect

🧠 Methods & Techniques

This project uses a full Python-based analytics workflow:

✔ Descriptive Analysis

Exploring distributions, engagement trends, and toxicity patterns.

✔ Data Visualizations

Correlation heatmaps

Genre-toxicity boxplots

Ownership vs playtime scatterplots

Logistic classification charts

✔ Statistical Modeling

OLS Regression

Regression with control variables

Binary Logistic Regression (Top Game vs Not)

✔ Advanced Techniques

Interaction effects

Model comparison

Predictive probability visualization

📂 Repository Structure
/data               → Raw & cleaned datasets  
/notebooks          → Colab notebooks for EDA, modeling & visuals  
/outputs            → Final graphs, charts & summaries  
/src                → Python scripts for helper functions  
README.md           → Project overview

🛠️ Tech Stack

Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-Learn

Statsmodels


📈 Business Implications

Game developers can focus on enhancing engagement rather than policing every instance of toxicity.

Competitive genres may naturally attract stronger emotions but still produce strong commercial results.

Engagement metrics (playtime, retention) can be used as early indicators of game success.

⚠️ Limitations

Steam data may not represent all gaming platforms

Toxicity is based on keyword detection, which may under/overestimate context

Cross-sectional snapshot; not long-term behavioral data

🚀 Future Work

Apply NLP models (VADER, TextBlob, BERT) for more accurate sentiment scoring

Build a predictive model for future game success

Explore community toxicity trends over time

👤 Author

Steve Sebastian Pellissery
Graduate Student — Business Analytics
Clark University
