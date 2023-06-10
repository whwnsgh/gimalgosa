import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import streamlit as st

# 폐루프 전달함수 계수
num_coeffs = [100]
denom_coeffs = [1, 5, 6]

# 폐루프 전달함수 생성
sys = signal.TransferFunction(num_coeffs, denom_coeffs)

# 시간 범위
t = np.linspace(0, 10, 1000)

# Unit step 입력 신호 생성
u = np.heaviside(t, 1)

# 시스템 응답 계산
t, y, _ = signal.lsim(sys, u, t)

# 주파수 응답 계산
w, mag, phase = signal.bode(sys)

# Streamlit 앱
st.title("폐루프 전달함수 시뮬레이션")

# 폐루프 전달함수 출력
st.title("폐루프 전달함수")
st.latex("G(s) = \\frac{100}{{s^2 + 5s + 6}}")

# Unit step 입력의 응답곡선 그리기
fig1, ax1 = plt.subplots()
ax1.plot(t, u, label="Unit Step Input")
ax1.plot(t, y, label="System Response")
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax1.set_title('Step Response')
ax1.legend()
st.pyplot(fig1)

# 주파수 응답 보드선도 그리기
fig2, (ax2_mag, ax2_phase) = plt.subplots(2, 1)
ax2_mag.semilogx(w, mag)
ax2_mag.set_xlabel('Frequency [rad/s]')
ax2_mag.set_ylabel('Magnitude [dB]')
ax2_mag.set_title('Bode Plot - Magnitude')

ax2_phase.semilogx(w, phase)
ax2_phase.set_xlabel('Frequency [rad/s]')
ax2_phase.set_ylabel('Phase [degrees]')
ax2_phase.set_title('Bode Plot - Phase')

fig2.tight_layout()
st.pyplot(fig2)