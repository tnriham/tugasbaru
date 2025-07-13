import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="EOQ Calculator", page_icon="📦")

st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.markdown("Simulasi sistem persediaan barang untuk menentukan jumlah pemesanan optimal (EOQ).")

tab1, tab2 = st.tabs(["🔢 Input Manual", "📘 Studi Kasus Budi Jaya"])

# Tab 1 – Input Manual
with tab1:
    st.header("Masukkan Data Persediaan Anda")

    D = st.number_input("Permintaan Tahunan (unit)", min_value=1, value=5000)
    S = st.number_input("Biaya Pemesanan per Pesanan (Rp)", min_value=1.0, value=75000.0)
    H = st.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1.0, value=1500.0)

    EOQ = np.sqrt((2 * D * S) / H)
    num_orders = D / EOQ
    total_cost = (D / EOQ) * S + (EOQ / 2) * H

    st.subheader("📈 Hasil Perhitungan")
    col1, col2, col3 = st.columns(3)
    col1.metric("EOQ (unit)", f"{EOQ:.2f}")
    col2.metric("Jumlah Pesanan per Tahun", f"{num_orders:.2f}")
    col3.metric("Total Biaya Persediaan", f"Rp {total_cost:,.2f}")

    # Grafik
    st.subheader("📉 Grafik Total Biaya vs Kuantitas Pemesanan")
    Q_range = np.linspace(1, EOQ * 2, 100)
    total_costs = (D / Q_range) * S + (Q_range / 2) * H

    fig, ax = plt.subplots()
    ax.plot(Q_range, total_costs, label='Total Cost', color='blue')
    ax.axvline(EOQ, color='red', linestyle='--', label=f'EOQ = {EOQ:.2f}')
    ax.set_xlabel('Jumlah Pemesanan (Q)')
    ax.set_ylabel('Total Biaya (Rp)')
    ax.set_title('Grafik Total Biaya vs Jumlah Pemesanan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Tab 2 – Studi Kasus
with tab2:
    st.header("📘 Studi Kasus: Toko Elektronik Budi Jaya")
    st.write("""
    Toko Budi Jaya menjual lampu pintar. Berikut data tahunannya:
    - Permintaan tahunan (D): 2.400 unit
    - Biaya pemesanan per pesanan (S): Rp 100.000
    - Biaya penyimpanan per unit per tahun (H): Rp 2.000
    """)

    D2 = 2400
    S2 = 100000
    H2 = 2000

    EOQ2 = np.sqrt((2 * D2 * S2) / H2)
    num_orders2 = D2 / EOQ2
    total_cost2 = (D2 / EOQ2) * S2 + (EOQ2 / 2) * H2

    st.subheader("📊 Hasil Perhitungan Studi Kasus")
    st.write(f"**EOQ:** {EOQ2:.2f} unit")
    st.write(f"**Jumlah Pemesanan per Tahun:** {num_orders2:.2f} kali")
    st.write(f"**Total Biaya Persediaan:** Rp {total_cost2:,.2f}")

    # Grafik
    st.subheader("📉 Grafik Total Biaya vs Kuantitas Pemesanan")
    Q_range2 = np.linspace(1, EOQ2 * 2, 100)
    total_costs2 = (D2 / Q_range2) * S2 + (Q_range2 / 2) * H2

    fig2, ax2 = plt.subplots()
    ax2.plot(Q_range2, total_costs2, label='Total Cost', color='green')
    ax2.axvline(EOQ2, color='red', linestyle='--', label=f'EOQ = {EOQ2:.2f}')
    ax2.set_xlabel('Jumlah Pemesanan (Q)')
    ax2.set_ylabel('Total Biaya (Rp)')
    ax2.set_title('Grafik Total Biaya vs Jumlah Pemesanan')
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)

# Penjelasan Rumus
with st.expander("ℹ️ Penjelasan Rumus EOQ"):
    st.latex(r'''EOQ = \sqrt{\frac{2DS}{H}}''')
    st.markdown("""
    - **D** = Permintaan tahunan (unit)
    - **S** = Biaya pemesanan per pesanan
    - **H** = Biaya penyimpanan per unit per tahun
    
    **Total Biaya Persediaan:**
    """)
    st.latex(r'''TC = \left( \frac{D}{EOQ} \times S \right) + \left( \frac{EOQ}{2} \times H \right)''')
