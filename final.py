import control
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def plot_step_response(system):
    t, y = control.step_response(system)
    plt.plot(t, y)
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.title('Step Response')
    plt.grid()

def plot_bode(system):
    mag, phase, omega = control.bode(system, Plot=False)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    ax1.semilogx(omega, mag)
    ax1.set_xlabel('Frequency [rad/s]')
    ax1.set_ylabel('Magnitude [dB]')
    ax1.set_title('Bode Plot - Magnitude')
    ax1.grid()
    ax2.semilogx(omega, phase)
    ax2.set_xlabel('Frequency [rad/s]')
    ax2.set_ylabel('Phase [degrees]')
    ax2.set_title('Bode Plot - Phase')
    ax2.grid()
    plt.subplots_adjust(hspace=0.4)

# 전달함수 G(s) 정의
num = [100]
den = [1, 5, 6]
G = control.TransferFunction(num, den)

# 폐루프 전달함수 구하기
T = control.feedback(G)

# Streamlit 앱 구성
st.title('Control System Analysis')

# 전달함수 출력
st.header('Transfer Function')
st.latex(r'G(s) = \frac{100}{{(s+2)(s+3)}}')

# 단위계단입력의 응답곡선 출력
st.header('Step Response')
fig_step = plt.figure()
plot_step_response(T)
st.pyplot(fig_step)

# 주파수응답 출력
st.header('Bode Plot')
fig_bode = plt.figure()
plot_bode(G)
st.pyplot(fig_bode)
