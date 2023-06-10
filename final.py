import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control

def main():
    st.title("폐루프 전달함수 시뮬레이션")

    # 전달함수 G1과 G2 정의
    K = 1
    G1 = control.TransferFunction([100], [1])
    G2 = control.TransferFunction([1], [1, 5, 6])

    # 전체 전달함수
    G3 = control.feedback(G1 * G2)

    # 전체 전달함수의 분자와 분모
    num = G3.num
    den = G3.den

    # 극점과 영점 찾기
    zeros, poles, _ = signal.tf2zpk(num, den)

    # 폐루프 전달함수 출력
    st.title("폐루프 전달함수")
    st.latex(f"G(s) = \\frac{{{num}}}{{{den}}}")

    # 극점과 영점 그래프 그리기
    fig, ax = plt.subplots()
    ax.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')
    ax.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
    ax.set_xlabel('Real Axis')
    ax.set_ylabel('Imaginary Axis')
    ax.set_title('Poles and Zeros')
    ax.legend()
    ax.grid()

    # 그래프 출력
    st.pyplot(fig)

if __name__ == '__main__':
    main()
