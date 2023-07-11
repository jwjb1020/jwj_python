# Seaborn에 있는 Iris 데이터를 활용해 데이터 분석
## 패키지 불러오기
```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score #정확도 보는 패키지
from mlxtend.plotting import plot_decision_regions # 그래프로 일반화 
from sklearn.model_selection import train_test_split   # 테스트 데이터, 훈련데이터 구분 
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


plt.rcParams['font.family'] = 'Malgun Gothic' #폰트 설정
plt.rcParams['axes.unicode_minus'] = False

data = sns.load_dataset("iris")
data.info() # 데이터의 전반적인 컬럼명, 데이터 타입 읽기
data.head() # 데이터가 가지고 있는 데이터 보기

#결측치가 있는 지 확인
data.isna()
data.isna().sum() #결측치가 없었음


#변수명들이 길기 때문에 사용에 용이하도록 변수명 변경
data = data.rename(columns={data.columns[0] : "sl",
                            data.columns[1] : "sw",
                            data.columns[2] : "pl",
                            data.columns[3] : "pw",
                            data.columns[4] : "spec"})

#종에 따른 개수 확인
species_counts = data['spec'].value_counts() 
species_counts

