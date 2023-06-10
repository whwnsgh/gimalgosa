import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import streamlit as st

# 전달함수 G1과 G2 정의
G1 = ctl.TransferFunction([100], [1])
G2 = ctl.TransferFunction([1], [1,5,6])

# 전달함수 G = G1 * G2 전방향 경로 / 직렬 결합
G = G1 * G2

# G3 = feedback(G, sign=-1, name=None) 함수를 사용하여 피드백 블록 계산
G3 = ctl.feedback(G, sign = 1)

# 전달함수 출력
st.write("전달함수: ", G3)

# 극점 출력
poles = ctl.pole(G3)
st.write("극점: ", poles)