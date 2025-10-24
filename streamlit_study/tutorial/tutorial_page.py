"""
streamlit 튜토리얼

streamlit의 공식 문서의 tutorial을 따라서 공부합니다.
"""

import streamlit as st
import pandas as pd
import numpy as np


st.title("뉴욕 시의 우버 픽업 모니터링")

DATE_COLUMN = "date/time"
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
        'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

    return data


data_load_state = st.text("Loading data...")
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

# write로 data를 출력, data는 자동적으로 테이블 형식으로 출력됨
if st.checkbox("원시 데이터 보기"): #checkbox는 변수 할당 대신 컴포넌트 자체에 if 문 적용
    st.subheader("원시 데이터")
    st.write(data)

# bar_chart로 시간 별 픽업 수를 출력
st.subheader("시간 별 픽업 수")
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# map으로 모든 픽업 지도를 출력
hour_to_filter = st.slider("시간", 0, 23, 17) # 슬라이더 이름, min, max, default
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f"시간 {hour_to_filter} 시에 대한 픽업 지도")
st.map(filtered_data)