import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import streamlit as st
from scipy import signal

def main():
    st.title("폐루프 전달함수")

    # 전달함수 계수
    num_coeffs = [100]
    denom_coeffs = [1, 5, 106]

    # 폐루프 전달함수 생성
    sys = signal.TransferFunction(num_coeffs, denom_coeffs)

    # 폐루프 전달함수 출력
    st.title("폐루프 전달함수")
    st.latex("G(s) = \\frac{100}{{(s+2)(s+3)}}")

    # 폐루프 전달함수의 분자 계수와 분모 계수 출력
    st.text("전달함수의 분자 계수: " + ', '.join(map(str, sys.num)))
    st.text("전달함수의 분모 계수: " + ', '.join(map(str, sys.den)))

    
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