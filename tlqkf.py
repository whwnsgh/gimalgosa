import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import streamlit as st
from scipy import signal

def main():
    st.title("폐루프 전달함수")

    # 전달함수 G(s) = 100/((s+2)(s+3))
    G = ctl.TransferFunction([100], [1, 5, 6])

    # 전달함수를 상태공간 모델로 변환
    ss = ctl.tf2ss(G)

    # 상태공간 모델을 다시 전달함수로 변환
    tf = ctl.ss2tf(ss)

    # 폐루프 전달함수 출력
    st.write("폐루프 전달함수: ", tf)

    
    # unit step 입력에 대한 응답곡선 그리기
    t, y = ctl.step_response(G3)
    plt.figure()
    plt.plot(t, y)
    plt.xlabel("Time")
    plt.ylabel("Response")
    plt.title("Step Response")
    st.pyplot(plt)

         # 전달함수 G(s) = 100/(s^2 + 5s + 106)
    G = ctl.TransferFunction([100], [1, 5, 106])

    # 전달함수를 scipy.signal.lti 객체로 변환
    G_lti = signal.lti(G.num[0][0], G.den[0][0])

    # 주파수 범위 설정
    frequencies = np.logspace(-2, 2, 500)

    # 주파수 응답 계산
    w, mag, phase = signal.bode(G_lti, frequencies)

    # 보드선도 그리기
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.semilogx(w, mag)
    ax1.set_ylabel('Magnitude [dB]')
    ax1.set_title('Bode Plot - Magnitude')
    ax2.semilogx(w, phase)
    ax2.set_xlabel('Frequency [Hz]')
    ax2.set_ylabel('Phase [degrees]')
    ax2.set_title('Bode Plot - Phase')

    # 그래프 출력
    st.pyplot(fig)

if __name__ == '__main__':
    main()