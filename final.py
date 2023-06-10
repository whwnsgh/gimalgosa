import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import streamlit as st

def main():
    st.title("폐루프 전달함수")

    # 전달함수 G1과 G2 정의
    G1 = ctl.TransferFunction([100], [1])
    G2 = ctl.TransferFunction([1], [1, 5, 6])

    # 폐루프 전달함수 구하기
    G3 = ctl.feedback(G1 * G2)

    # 폐루프 전달함수 출력
    num = G3.num[0][0]
    den = G3.den[0][0]
    G3_str = f"[ {num} ] / [ {den} ]"
    st.write("폐루프 전달함수:", G3_str)

    # unit step 입력에 대한 응답곡선 그리기
    t, y = ctl.step_response(G3)
    plt.figure()
    plt.plot(t, y)
    plt.xlabel("Time")
    plt.ylabel("Response")
    plt.title("Step Response")
    st.pyplot(plt)

    # 주파수 응답 보드선도 그리기
    mag, phase, omega = ctl.bode(G3)
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.semilogx(omega, mag)
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude (dB)")
    plt.title("Bode Plot - Magnitude")
    plt.subplot(2, 1, 2)
    plt.semilogx(omega, phase)
    plt.xlabel("Frequency")
    plt.ylabel("Phase (degrees)")
    plt.title("Bode Plot - Phase")
    st.pyplot(plt)

if __name__ == '__main__':
    main()
