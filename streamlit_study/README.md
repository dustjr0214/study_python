⚠️ 아직 작성중입니다.

배운 점 (추후 정리)

----

1. streamlit을 설치 후, 터미널 명령어로
   > streamlit hello 

실행 시, streamlit의 데모 페이지가 localhost:8501 로 열린다.

2. streamlit 페이지를 구현하는 간단한 페이지를 가진 main.py를 만들고, 이를 uv run main.py로 실행했더니 다음과 같은 오류가 발생함.
> Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
이는 streamlit 앱을 단순히 uv run 시켰기 때문으로, streamlit 앱은 streamlit run으로 실행시켜줘야 함.
이를 uv 환경에서 사용하려면 다음과 같이 사용함.
> uv run streamlit run main.py
이렇게 uv로 streamlit을 거쳐 실행시킬 수 있음.

3. streamlit run은 로컬 파일뿐만 아니라 streamlit으로 만들어진 앱의 링크도 실행시킬 수 있다.
   > streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
   (출처 : 공식 문서)

4. 데이터를 로드하는 함수에 @st.cache_data로 데이터를 프런트엔드 단에서 캐시 가능

5. streamlit 앱 우상단의 always rerun을 선택하면, 앱 코드가 변경될 때 앱이 활성화된 상태라도 변경을 반영함 (fastapi처럼)

6. st.map()은 data 자체에 lat, lon을 가지면 st.map(data)와 같이 간단한 작성으로도 지도 위 plot 출력 가능
7. 멀티페이지 구현 시, MPA 페이지 의 순서는 파일 이름 앞 숫자에 의해 정해지므로, 순서를 변경하려면 파일 이름을 변경해야 함, 각 앱의 이름은 파일 이름을 따라감.
   
## 참고 링크

https://docs.streamlit.io/get-started > 공식 문서

https://velog.io/@euisuk-chung/Streamlit-%EC%86%8C%EA%B0%9C-%EB%B0%8F-%ED%99%9C%EC%9A%A9-%EA%B0%80%EC%9D%B4%EB%93%9C

https://www.sktenterprise.com/bizInsight/blogDetail/dev/10237

https://www.datacamp.com/tutorial/streamlit