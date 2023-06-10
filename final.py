import control
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st

# 전달함수 G(s) 정의
G = control.TransferFunction([100], [1, 5, 6])

# 폐루프 전달함수 구하기
T = control.feedback(G)

# unit step 입력에 대한 응답곡선 그리기
t, y = control.step_response(T)
fig1 = plt.figure()
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid()

# 주파수 응답을 보드선도로 그리기
w, mag, phase = signal.bode(G)
fig2 = plt.figure()
plt.semilogx(w, mag)
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.title('Bode Plot')
plt.grid()

# 그래프 출력
st.pyplot(fig1)
st.pyplot(fig2)