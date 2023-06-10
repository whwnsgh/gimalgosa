import control
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st
# 전달함수 G1과 G2 정의
G1 = control.TransferFunction([100],[1])
G2 = control.TransferFunction([1],[1,5,6])

#전체 전달함수
G3 = control.feedback(G1 * G2)
st.write(G3)

#전체 전달함수의 분자와 분모
num = [100]
den = [1,5,6]

#극점과 영점 찾기
zeros, poles, _ = signal.tf2zpk(num, den)
#극점과 영점 그래프 그리기
fig = plt.figure()
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red',label='Poles')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue',label='Zeros')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.title('Poles and Zeros of H(s) = K/s+K+1')
plt.legend()
plt.grid()
#그래프 출력
st.pyplot(fig)
