import streamlit as st
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

st.title("📊 Industrial Decision Support System")

# Membuat Tabs
tab1, tab2, tab3 = st.tabs([
    "Optimasi Produksi (LP)", 
    "Model Persediaan (EOQ)", 
    "Model Antrian (M/M/1)"
])

# Tab 1: Linear Programming
with tab1:
    st.header("🔧 Optimasi Produksi (Linear Programming)")
    st.write("**Studi Kasus:** Pabrik memproduksi dua produk (A dan B) dengan sumber daya terbatas.")
    
    st.markdown("""
    - Produk A: 1 jam kerja, 3 bahan baku per unit  
    - Produk B: 2 jam kerja, 1 bahan baku per unit  
    - Tersedia: 40 jam kerja dan 100 unit bahan baku  
    - Profit: Rp30.000/unit (A), Rp20.000/unit (B)
    """)
    
    st.latex(r"""
    \text{Maksimalkan: } Z = 30000A + 20000B
    """)
    st.latex(r"""
    \text{Kendala:} \\
    A + 2B \leq 40 \quad \text{(Jam kerja)} \\
    3A + B \leq 100 \quad \text{(Bahan baku)} \\
    A, B \geq 0
    """)

    if st.button("Hitung Produksi Optimal"):
        c = [-30000, -20000]
        A = [[1, 2], [3, 1]]
        b = [40, 100]
        res = linprog(c, A_ub=A, b_ub=b, method='highs')
        if res.success:
            st.success(f"Produksi Optimal:\nProduk A: {res.x[0]:.2f} unit\nProduk B: {res.x[1]:.2f} unit")
            st.write(f"Keuntungan Maksimal: Rp{(-res.fun):,.0f}")
        else:
            st.error("Solusi tidak ditemukan.")

# Tab 2: EOQ
with tab2:
    st.header("📦 Model Persediaan EOQ (Economic Order Quantity)")
    st.write("**Studi Kasus:** Toko elektronik menjual 1.000 kipas angin/tahun.")

    st.markdown("""
    - Permintaan tahunan (D) = 1.000 unit  
    - Biaya pemesanan (S) = Rp50.000  
    - Biaya penyimpanan per unit/tahun (H) = Rp2.000
    """)

    st.latex(r"""
    EOQ = \sqrt{\frac{2DS}{H}}
    """)

    D = st.number_input("Permintaan tahunan (D)", value=1000)
    S = st.number_input("Biaya pemesanan (S)", value=50000)
    H = st.number_input("Biaya penyimpanan/unit/tahun (H)", value=2000)

    if st.button("Hitung EOQ"):
        eoq = np.sqrt((2 * D * S) / H)
        st.success(f"EOQ = {eoq:.2f} unit per pesanan")

# Tab 3: Antrian M/M/1
with tab3:
    st.header("⏳ Model Antrian (M/M/1)")
    st.write("**Studi Kasus:** Kasir minimarket dengan kedatangan 2 pelanggan/menit dan pelayanan 5 pelanggan/menit.")

    st.markdown("""
    - λ (laju kedatangan) = 2 pelanggan/menit  
    - μ (laju pelayanan) = 5 pelanggan/menit  
    """)

    st.latex(r"""
    \rho = \frac{\lambda}{\mu}, \quad 
    L = \frac{\rho}{1 - \rho}, \quad 
    L_q = \frac{\rho^2}{1 - \rho}
    """)
    st.latex(r"""
    W = \frac{1}{\mu - \lambda}, \quad 
    W_q = \frac{\rho}{\mu - \lambda}
    """)

    lambd = st.number_input("Laju kedatangan (λ)", value=2.0)
    mu = st.number_input("Laju pelayanan (μ)", value=5.0)

    if st.button("Hitung Kinerja Antrian"):
        if lambd < mu:
            rho = lambd / mu
            L = rho / (1 - rho)
            Lq = rho**2 / (1 - rho)
            W = 1 / (mu - lambd)
            Wq = rho / (mu - lambd)

            st.success("Sistem Stabil (λ < μ)")
            st.write(f"Utilisasi Sistem (ρ): {rho:.2f}")
            st.write(f"Rata-rata pelanggan dalam sistem (L): {L:.2f}")
            st.write(f"Rata-rata dalam antrean (Lq): {Lq:.2f}")
            st.write(f"Rata-rata waktu dalam sistem (W): {W:.2f} menit")
            st.write(f"Rata-rata waktu antrean (Wq): {Wq:.2f} menit")
        else:
            st.error("Sistem tidak stabil (λ ≥ μ)")
