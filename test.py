import lightgbm as lgb
import numpy as np

X = np.random.rand(100, 5)
y = np.random.rand(100)

train_data = lgb.Dataset(X, label=y)

params = {
    'objective': 'regression',
    'metric': 'l2',
    'boosting_type': 'gbdt',
}

model = lgb.train(params, train_data, num_boost_round=10)
preds = model.predict(X[:5])
print("Predictions:", preds)

