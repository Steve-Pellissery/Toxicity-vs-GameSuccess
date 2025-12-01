import statsmodels.api as sm

def run_ols(X, y):
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    return model

def run_logistic(X, y):
    X = sm.add_constant(X)
    model = sm.Logit(y, X).fit()
    return model
