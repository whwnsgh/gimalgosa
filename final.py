import numpy as np
from scipy import signal
import streamlit as st

def main():
    st.title("Pole-Zero 전달함수 시뮬레이션")

    # 전달함수 계수
    num_coeffs = [100]
    denom_coeffs = [1, 5, 6]

    # 폐루프 전달함수 생성
    sys = signal.TransferFunction(num_coeffs, denom_coeffs)

    # 폐루프 전달함수 출력
    st.title("폐루프 전달함수")
    st.latex("G(s) = \\frac{100}{{(s+2)(s+3)}}")

    # 폐루프 전달함수의 분자 계수와 분모 계수 출력
    st.text("전달함수의 분자 계수: " + ', '.join(map(str, sys.num)))
    st.text("전달함수의 분모 계수: " + ', '.join(map(str, sys.den)))

if __name__ == '__main__':
    main()
