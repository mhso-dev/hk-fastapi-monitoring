from locust import HttpUser, task
import pandas as pd
import random

feature_columns = {
    "fixed acidity": "fixed_acidity",
    "volatile acidity": "volatile_acidity",
    "citric acid": "citric_acid",
    "residual sugar": "residual_sugar",
    "chlorides": "chlorides",
    "free sulfur dioxide": "free_sulfur_dioxide",
    "total sulfur dioxide": "total_sulfur_dioxide",
    "density": "density",
    "pH": "ph",
    "sulphates": "sulphates",
    "alcohol": "alcohol_pct_vol",
}
dataset = (
    pd.read_csv(
        "winequality-red.csv",
        delimiter=",",
    )
    .rename(columns=feature_columns)
    .drop("quality", axis=1)
    .to_dict(orient="records")
)

# 스트레스 테스트 시나리오
#  - healthcheck
#  - predict
#    - 성공 케이스
#    - 실패 케이스
class WinePredictionUser(HttpUser):
    # @task 어노테이션을 이용하여 테스트 루틴 작성
    @task(1)
    def healthcheck(self):
        self.client.get("/healthcheck")
    
    @task(10)
    def prediction(self):
        # 랜덤하게 데이터 뽑기
        record = random.choice(dataset).copy()
        self.client.post("/predict", json=record)
    
    @task(2)
    def prediction_bad_value(self):
        record = random.choice(dataset).copy()
        corrupt_key = random.choice(list(record.keys()))
        record[corrupt_key] = 'bad data'
        self.client.post('/predict', json=record)