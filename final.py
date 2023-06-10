import numpy as np
import matplotlib.pyplot as plt
import control
import streamlit as st

def main():
    st.title("폐루프 전달함수 시뮬레이션")

    # 전달함수 G(s) 정의
    G = control.TransferFunction([100], [1, 5, 106])

    # 폐루프 전달함수 계산
    G_closed_loop = control.feedback(G, 1)

    # Unit step 입력 생성
    t = np.linspace(0, 10, 1000)
    u = np.heaviside(t, 1)

    # 폐루프 응답 계산
    t, y = control.step_response(G_closed_loop, T=t)

    # 폐루프 전달함수 출력
    st.title("폐루프 전달함수")
    st.latex("G(s) = \\frac{100}{{s^2 + 5s + 106}}")

    # Unit step 입력의 응답곡선 그리기
    fig, ax = plt.subplots()
    ax.plot(t, u, label="Unit Step Input")
    ax.plot(t, y, label="System Response")
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Step Response')
    ax.legend()
    st.pyplot(fig)

if __name__ == '__main__':
    main()
