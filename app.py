
import streamlit as st
import numpy as np

def evaluate_rng_sequence(seq):
    low_count = sum(1 for x in seq[-5:] if x <= 1.5)
    high_recent = any(x >= 10 for x in seq[-3:])
    mid_range_repeat = sum(1 for x in seq[-5:] if 5 <= x <= 10)

    if low_count >= 2 and not high_recent:
        recommendation = "🔥 ŞİMDİ OYNA – Sistem ısınıyor, düşüklerden sonra sıçrama olabilir!"
    elif high_recent:
        recommendation = "⏳ BEKLE – Yeni büyük sayı geldi, sistem soğuyor olabilir."
    elif mid_range_repeat >= 2:
        recommendation = "🚫 GİRME – Orta aralıkta sıkışmış, sistem dengesiz."
    else:
        recommendation = "🤔 NÖTR – Dengesiz veriler, istersen az birimle yokla."

    return low_count, high_recent, mid_range_repeat, recommendation

st.title("🎯 Sena'nın RNG Radar Paneli")

user_input = st.text_input("Son 10 sayıyı gir (virgülle):", "2.75, 4.25, 1.20, 2.51, 1.02, 3.13, 11.63, 1.36, 1.37, 1.34")

if st.button("Analiz Et"):
    try:
        numbers = [float(x.strip()) for x in user_input.split(",")]
        if len(numbers) != 10:
            st.warning("Tam 10 sayı girmelisin.")
        else:
            low, high, mid, rec = evaluate_rng_sequence(numbers)
            st.subheader("📊 Analiz")
            st.write(f"• Son 5 sayı içinde 0–1.5 arası kaç tane? → **{low}**")
            st.write(f"• Son 3 sayı içinde 10+ sayı var mı? → **{high}**")
            st.write(f"• Orta aralık (5–10) tekrar ediyor mu? → **{mid}**")
            st.markdown(f"### 🎯 Tavsiye: {rec}")
    except:
        st.error("Sayılarda bir hata var gibi, tekrar dene.")
