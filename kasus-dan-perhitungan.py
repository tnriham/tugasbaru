import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.optimize import linprog

st.set_page_config(page_title="Model Matematika Industri", layout="centered")
st.title("📊 Aplikasi Model Matematika Industri")

menu = st.sidebar.selectbox("Pilih Model:", [
    "Optimasi Produksi (LP)",
    "Model Persediaan (EOQ)",
    "Model Antrian (M/M/1)",
    "Optimasi Biaya (Parsial)"
])

if menu == "Optimasi Produksi (LP)":
    st.header("Optimasi Produksi - Linear Programming")
    c = [-500, -400]  # Maksimalkan = Minimalkan negatif
    A = [[3, 2], [4, 3]]
    b = [120, 160]
    bounds = [(0, None), (0, None)]

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    if res.success:
        x, y = res.x
        st.success(f"Produksi Optimal: {x:.0f} meja dan {y:.0f} kursi")
        st.info(f"Total Keuntungan Maksimum: Rp{(-res.fun):,.0f}")
    else:
        st.error("Solusi tidak ditemukan.")

elif menu == "Model Persediaan (EOQ)":
    st.header("Model Persediaan - EOQ")
    D = st.number_input("Permintaan Tahunan (unit)", value=2400)
    S = st.number_input("Biaya Pemesanan per Order (Rp)", value=100000)
    H = st.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", value=10000)

    if D > 0 and S > 0 and H > 0:
        EOQ = np.sqrt((2 * D * S) / H)
        st.success(f"EOQ Optimal: {EOQ:.2f} unit per pemesanan")

elif menu == "Model Antrian (M/M/1)":
    st.header("Model Antrian - M/M/1")
    lam = st.number_input("Rata-rata Kedatangan (λ)", value=10.0)
    mu = st.number_input("Rata-rata Pelayanan (μ)", value=15.0)

    if lam < mu:
        rho = lam / mu
        L = lam / (mu - lam)
        W = 1 / (mu - lam)
        st.write(f"Utilisasi Sistem (ρ): {rho:.2f}")
        st.write(f"Rata-rata pelanggan dalam sistem (L): {L:.2f}")
        st.write(f"Rata-rata waktu di sistem (W): {W*60:.2f} menit")
    else:
        st.error("λ harus lebih kecil dari μ agar sistem stabil.")

elif menu == "Optimasi Biaya (Parsial)":
    st.header("Optimasi Biaya Produksi - Turunan Parsial")
    x, y = sp.symbols('x y')
    C = 0.1*x**2 + 0.15*y**2 + 0.05*x*y + 200
    dC_dx = sp.diff(C, x)
    dC_dy = sp.diff(C, y)
    solusi = sp.solve([dC_dx, dC_dy], (x, y))

    st.latex(r"C(x, y) = 0.1x^2 + 0.15y^2 + 0.05xy + 200")
    st.latex(r"\frac{\partial C}{\partial x} = " + sp.latex(dC_dx))
    st.latex(r"\frac{\partial C}{\partial y} = " + sp.latex(dC_dy))
    st.write("Titik minimum lokal:", solusi)

    # Visualisasi kontur
    x_vals = np.linspace(0, 50, 100)
    y_vals = np.linspace(0, 50, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = 0.1*X**2 + 0.15*Y**2 + 0.05*X*Y + 200

    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z, levels=20)
    ax.clabel(CS, inline=True, fontsize=8)
    ax.set_xlabel('Gula (x)')
    ax.set_ylabel('Perisa (y)')
    st.pyplot(fig)
