import streamlit as st
import control
import control as ct
# 전달함수 G1과 G2 정의
K=1
G1 = ct.TransferFunction([100],[1])
G2 = ct.TransferFunction([1],[1,1])

#전체 전달함수
G3 = ct.feedback(G1 * G2)
print(G3)

# 극점 출력
poles = ct.pole(G3)
print("극점: ", poles)