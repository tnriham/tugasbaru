import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="EOQ Calculator", page_icon="📦")

st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.markdown("Simulasi sistem persediaan barang untuk menentukan jumlah pemesanan optimal (EOQ).")

tab1, tab2 = st.tabs(["🔢 Input Manual", "📘 Studi Kasus Budi Jaya"])

# ---------------------------- TAB 1: Input Manual ----------------------------
with tab1:
    st.header("Masukkan Data Persediaan Anda")

    D = st.number_input("Permintaan Tahunan (unit)", min_value=1, value=5000)
    S = st.number_input("Biaya Pemesanan per Pesanan (Rp)", min_value=1.0, value=75000.0)
    H = st.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1.0, value=1500.0)
    P = st.number_input("Harga Jual per Unit (Rp)", min_value=1.0, value=100000.0)

    if D > 0 and S > 0 and H > 0:
        EOQ = np.sqrt((2 * D * S) / H)
        num_orders = D / EOQ
        total_cost = (D / EOQ) * S + (EOQ / 2) * H
        unit_cost = total_cost / D
        profit_total = D * (P - unit_cost)

        st.subheader("📈 Hasil Perhitungan")
        col1, col2, col3 = st.columns(3)
        col1.metric("EOQ (unit)", f"{EOQ:.2f}")
        col2.metric("Jumlah Pesanan/Tahun", f"{num_orders:.2f}")
        col3.metric("Total Biaya Persediaan", f"Rp {total_cost:,.2f}")
        st.metric("Laba Total", f"Rp {profit_total:,.2f}", delta_color="normal" if profit_total >= 0 else "inverse")

        # Grafik Biaya
        st.subheader("📉 Grafik Komponen Biaya vs Jumlah Pemesanan")
        Q_range = np.linspace(1, EOQ * 2, 100)
        ordering_cost = (D / Q_range) * S
        holding_cost = (Q_range / 2) * H
        total_costs = ordering_cost + holding_cost

        fig1, ax1 = plt.subplots()
        ax1.plot(Q_range, ordering_cost, label='Biaya Pemesanan', color='orange', linestyle='--')
        ax1.plot(Q_range, holding_cost, label='Biaya Penyimpanan', color='green', linestyle='--')
        ax1.plot(Q_range, total_costs, label='Total Biaya', color='blue')
        ax1.axvline(EOQ, color='red', linestyle=':', label=f'EOQ = {EOQ:.2f}')
        ax1.set_xlabel('Jumlah Pemesanan (Q)')
        ax1.set_ylabel('Biaya (Rp)')
        ax1.set_title('Grafik Komponen Biaya vs Jumlah Pemesanan')
        ax1.legend()
        ax1.grid(True)
        st.pyplot(fig1)

        # Grafik Laba
        st.subheader("📈 Grafik Laba Total vs Jumlah Pemesanan")
        unit_costs = total_costs / D
        profit_range = D * (P - unit_costs)

        fig2, ax2 = plt.subplots()
        ax2.plot(Q_range, profit_range, label='Laba Total', color='purple')
        ax2.axhline(0, color='gray', linestyle='--')
        ax2.axvline(EOQ, color='red', linestyle=':', label=f'EOQ = {EOQ:.2f}')
        ax2.fill_between(Q_range, profit_range, 0, where=(profit_range > 0), color='lightgreen', alpha=0.3, label='Untung')
        ax2.fill_between(Q_range, profit_range, 0, where=(profit_range < 0), color='salmon', alpha=0.3, label='Rugi')
        ax2.set_xlabel('Jumlah Pemesanan (Q)')
        ax2.set_ylabel('Laba Total (Rp)')
        ax2.set_title('Grafik Laba vs Jumlah Pemesanan')
        ax2.legend()
        ax2.grid(True)
        st.pyplot(fig2)

    else:
        st.error("Semua input harus lebih besar dari nol!")

# ---------------------------- TAB 2: Studi Kasus ----------------------------
with tab2:
    st.header("📘 Studi Kasus: Toko Elektronik Budi Jaya")
    st.write("""
    Toko Budi Jaya menjual lampu pintar. Berikut data tahunannya:
    - Permintaan tahunan (D): 2.400 unit
    - Biaya pemesanan per pesanan (S): Rp 100.000
    - Biaya penyimpanan per unit per tahun (H): Rp 2.000
    - Harga Jual per unit (P): Rp 150.000
    """)

    D2 = 2400
    S2 = 100000
    H2 = 2000
    P2 = 150000

    EOQ2 = np.sqrt((2 * D2 * S2) / H2)
    num_orders2 = D2 / EOQ2
    total_cost2 = (D2 / EOQ2) * S2 + (EOQ2 / 2) * H2
    unit_cost2 = total_cost2 / D2
    profit_total2 = D2 * (P2 - unit_cost2)

    st.subheader("📊 Hasil Perhitungan Studi Kasus")
    st.write(f"**EOQ:** {EOQ2:.2f} unit")
    st.write(f"**Jumlah Pemesanan/Tahun:** {num_orders2:.2f}")
    st.write(f"**Total Biaya Persediaan:** Rp {total_cost2:,.2f}")
    st.write(f"**Laba Total:** Rp {profit_total2:,.2f}")

    # Grafik Biaya
    st.subheader("📉 Grafik Komponen Biaya vs Jumlah Pemesanan")
    Q_range2 = np.linspace(1, EOQ2 * 2, 100)
    ordering_cost2 = (D2 / Q_range2) * S2
    holding_cost2 = (Q_range2 / 2) * H2
    total_costs2 = ordering_cost2 + holding_cost2

    fig3, ax3 = plt.subplots()
    ax3.plot(Q_range2, ordering_cost2, label='Biaya Pemesanan', color='orange', linestyle='--')
    ax3.plot(Q_range2, holding_cost2, label='Biaya Penyimpanan', color='green', linestyle='--')
    ax3.plot(Q_range2, total_costs2, label='Total Biaya', color='blue')
    ax3.axvline(EOQ2, color='red', linestyle=':', label=f'EOQ = {EOQ2:.2f}')
    ax3.set_xlabel('Jumlah Pemesanan (Q)')
    ax3.set_ylabel('Biaya (Rp)')
    ax3.set_title('Grafik Komponen Biaya vs Jumlah Pemesanan')
    ax3.legend()
    ax3.grid(True)
    st.pyplot(fig3)

    # Grafik Laba
    st.subheader("📈 Grafik Laba Total vs Jumlah Pemesanan")
    unit_costs2 = total_costs2 / D2
    profit_range2 = D2 * (P2 - unit_costs2)

    fig4, ax4 = plt.subplots()
    ax4.plot(Q_range2, profit_range2, label='Laba Total', color='purple')
    ax4.axhline(0, color='gray', linestyle='--')
    ax4.axvline(EOQ2, color='red', linestyle=':', label=f'EOQ = {EOQ2:.2f}')
    ax4.fill_between(Q_range2, profit_range2, 0, where=(profit_range2 > 0), color='lightgreen', alpha=0.3, label='Untung')
    ax4.fill_between(Q_range2, profit_range2, 0, where=(profit_range2 < 0), color='salmon', alpha=0.3, label='Rugi')
    ax4.set_xlabel('Jumlah Pemesanan (Q)')
    ax4.set_ylabel('Laba Total (Rp)')
    ax4.set_title('Grafik Laba vs Jumlah Pemesanan')
    ax4.legend()
    ax4.grid(True)
    st.pyplot(fig4)

# ---------------------------- Penjelasan Rumus ----------------------------
with st.expander("ℹ️ Penjelasan Rumus EOQ"):
    st.latex(r'''EOQ = \sqrt{\frac{2DS}{H}}''')
    st.markdown("""
    - **D** = Permintaan tahunan (unit)  
    - **S** = Biaya pemesanan per pesanan  
    - **H** = Biaya penyimpanan per unit per tahun  

    **Total Biaya Persediaan (TC):**
    """)
    st.latex(r'''TC = \left( \frac{D}{Q} \times S \right) + \left( \frac{Q}{2} \times H \right)''')

    st.markdown("""
    **Laba Total = D × (Harga Jual - Biaya per Unit)**  
    Zona untung dan rugi dapat dilihat pada grafik laba vs jumlah pemesanan.
    """)
