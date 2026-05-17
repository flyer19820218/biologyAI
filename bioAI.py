import streamlit as st
import pandas as pd
import numpy as np

# 1. 頁面基本設定 (使用寬螢幕佈局)
st.set_page_config(
    page_title="全球醫療 AI 核心技術與前沿趨勢",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 注入自訂 CSS 來打造「深色科技簡報感」
st.markdown("""
<style>
    /* 全局字體與背景微調 */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* 標題顏色優化 */
    h1, h2, h3 {
        color: #2dd4bf !important;
        font-weight: 700 !important;
    }
    /* 建立卡片浮雕效果 */
    div.stMarkdown {
        font-size: 1.1rem;
    }
    /* 美化 Metric 數據區塊 */
    div[data-testid="metric-container"] {
        background-color: #1e293b;
        border-left: 5px solid #0d9488;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    hr {
        border-color: #334155;
    }
</style>
""", unsafe_allow_html=True)

# 3. 標題與側邊欄
st.title("🧬 全球醫療 AI 前沿進展與深度分析")
st.caption("報告層級：戰術戰略級深度評估 | 視覺化 UI：簡報模式 v2.0")
st.markdown("---")

st.sidebar.header("⚙️ 算力變數與市場動態模擬")
compute_multiplier = st.sidebar.slider(
    "設定未來算力倍數 (相較2020基準)", 
    min_value=1, max_value=50, value=10, step=1
)
st.sidebar.markdown("---")
st.sidebar.info("南屯指揮部控制台：已加入 2020-2030 全球醫療 AI 資本規模實體數據與 Rubin 次世代架構推演。")

# 4. 主要內容切換頁籤
tab1, tab2, tab3 = st.tabs([
    "💡 核心突破點 & 次世代推演", 
    "📈 市場規模與精確資本數字", 
    "⏳ 診療週期時間相變模擬"
])

# Tab 1: 核心突破點與下一代架構
with tab1:
    st.subheader("一、 醫療 AI 核心突破與「後 Rubin 時代」的物理極限")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🎯 當前進展 (2025-2026)
        * **新藥研發物理加速**：AI 輔助將新藥研發從 10 年壓縮至 18 個月，一期臨床成功率從 50% 暴增至 80%。
        * **影像絕對視覺**：EchoNext 系統在心電圖微小病變檢測上超越人類專家；早期肺癌篩查準確率突破 95%。
        * **CRISPR-GPT 基因剪輯**：自動化突變預測，精準規避脫靶效應，讓針對個人 DNA 缺陷的量身定制療法成為可能。
        """)
        
    with col2:
        st.markdown("""
        ### 🚀 次世代架構：超越 Rubin (2028+)
        當算力逼近矽晶片的極限，接下來的科技將全面迎來底層物理機制的相變：
        1. **傳輸相變 (矽光子)**：用光子取代電子傳輸，徹底消滅 RC 延遲與銅線熱摩擦力。
        2. **結構相變 (埃米製程)**：進入 1nm 以下尺度，採用 CFET 垂直堆疊電晶體，對抗量子穿隧效應。
        3. **熱力學極限 (3D SoIC)**：邏輯晶片與記憶體直接立體堆疊，散熱強制升級為浸沒式液冷系統。
        """)

# Tab 2: 資本數字與市場規模 (新增精確數據)
with tab2:
    st.subheader("二、 全球醫療 AI 資本質量與成長軌跡 (2020-2030)")
    
    # 強調數字的 Metric 區塊
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("2020 基準規模", "$ 49 億美元", "")
    m2.metric("2024 爆發期", "$ 195 億美元", "↑ 390%")
    m3.metric("2030 預估規模", "$ 1,180 億美元", "CAGR 37.5%")
    m4.metric("核心驅動引擎", "新藥探索 / 醫學影像", "高資本回報率")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 建立含有精確數字的 DataFrame
    market_data = pd.DataFrame({
        "年份": ["2020", "2022", "2024", "2026 (Rubin)", "2028 (矽光子)", "2030"],
        "市場規模 (億美元)": [49, 90, 195, 350, 650, 1180],
        "年增率 YoY (%)": ["-", "35%", "47%", "34%", "36%", "34%"]
    })
    
    # 畫出帶有趨勢的圖表
    st.area_chart(market_data.set_index("年份")["市場規模 (億美元)"], color="#2dd4bf")
    
    # 顯示精確數字表格
    st.markdown("#### 📊 歷史數據與未來預估對照表")
    st.dataframe(market_data, use_container_width=True, hide_index=True)

# Tab 3: 診療週期模擬
with tab3:
    st.subheader("三、 10倍以上算力對「黃金診療週期」的時間壓縮")
    st.write(f"當前設定算力速度： :green[{compute_multiplier} 倍速]")
    
    # 動態時間計算邏輯
    seq_time = 12  # 基因定序硬體物理極限
    bio_sim = max(0.25, 48 / compute_multiplier)
    clinical_sim = max(0.1, 336 / (compute_multiplier * 4))
    crispr_sim = max(24.0, 1440 / (compute_multiplier * 3))
    
    total_hours = seq_time + bio_sim + clinical_sim + crispr_sim
    total_days = total_hours / 24
    
    # 數據表
    sim_data = pd.DataFrame({
        "處理階段": ["1. 全基因組定序", "2. 生物資訊分析", "3. AI 臨床解密配對", "4. 客製化基因方案生成"],
        "傳統耗時": ["數天", "48 小時", "2 週 (336 小時)", "2 個月 (1440 小時)"],
        "當前算力模擬耗時": [
            f"{seq_time} 小時",
            f"{bio_sim:.1f} 小時" if bio_sim >= 1 else f"{bio_sim*60:.0f} 分鐘",
            f"{clinical_sim:.1f} 小時" if clinical_sim >= 1 else f"{clinical_sim*60:.0f} 分鐘",
            f"{crispr_sim:.1f} 小時"
        ]
    })
    
    st.table(sim_data)
    
    st.error(f"🚨 **南屯觀測站結論**：在 {compute_multiplier} 倍算力下，原本耗時數月的流程，被物理壓縮至 **{total_days:.1f} 天**完成！這標誌著通用醫療的終結與個人化精準醫療的全面普及。")

# 頁尾
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>© 2026 醫療科技前沿戰術指揮部 · 系統已優化為 Slide-UI 模式</p>", unsafe_allow_html=True)
