import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import streamlit as st

st.title("202021089 조준호")

# 전달함수 G1과 G2 정의
G1 = ctl.TransferFunction([100], [1])
G2 = ctl.TransferFunction([1], [1, 5, 6])

# 전달함수 G = G1 * G2 전방향 경로 / 직렬 결합
G = G1 * G2

# G3 = feedback(G, sign=-1, name=None) 함수를 사용하여 피드백 블록 계산
G3 = ctl.feedback(G, sign=-1)

# 전달함수의 분자와 분모 계수 추출
num_coef = G3.num[0][0].tolist()
den_coef = G3.den[0][0].tolist()

# 전달함수 출력
num_str = " ".join(str(c) for c in num_coef)
den_str = " ".join(str(c) for c in den_coef)
G3_str = f"[ {num_str} ] / [ {den_str} ]"
st.write("전달함수:", G3_str)
