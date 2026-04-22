import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="MEV Sandwich Attack Monitor", layout="wide")

st.title("🥪 MEV Sandwich Attack Monitor")
st.markdown("Real-time analysis of Maximal Extractable Value (MEV) sandwich attacks on Ethereum")

@st.cache_data
def load_data():
    df = pd.read_csv('mev_sandwich_data.csv')
    df['block_time'] = pd.to_datetime(df['block_time'])
    return df

df = load_data()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Attacks", f"{len(df):,}")
    
with col2:
    st.metric("Total Profit", f"${df['profit_usd'].sum():,.0f}")
    
with col3:
    st.metric("Unique Bots", df['bot'].nunique())
    
with col4:
    st.metric("Avg Profit", f"${df['profit_usd'].mean():,.0f}")

st.markdown("---")

st.subheader("Filter Data")

col1, col2 = st.columns(2)

with col1:
    selected_tokens = st.multiselect(
        "Token Pairs",
        options=df['token_pair'].unique(),
        default=df['token_pair'].unique()
    )
    
with col2:
    min_profit = st.slider(
        "Minimum Profit (USD)",
        min_value=0,
        max_value=int(df['profit_usd'].max()),
        value=0,
        step=1000
    )

filtered_df = df[
    (df['token_pair'].isin(selected_tokens)) &
    (df['profit_usd'] >= min_profit)
]

st.markdown(f"**Showing {len(filtered_df)} attacks**")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Profit Over Time")
    
    hourly_profit = filtered_df.groupby('hour')['profit_usd'].sum().reset_index()
    
    fig1 = px.bar(
        hourly_profit,
        x='hour',
        y='profit_usd',
        labels={'hour': 'Hour (UTC)', 'profit_usd': 'Total Profit (USD)'},
        color='profit_usd',
        color_continuous_scale='Reds'
    )
    fig1.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Attacks by Token Pair")
    
    token_counts = filtered_df['token_pair'].value_counts().reset_index()
    token_counts.columns = ['token_pair', 'count']
    
    fig2 = px.pie(
        token_counts,
        values='count',
        names='token_pair',
        hole=0.4
    )
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("Top MEV Bots")

bot_stats = filtered_df.groupby('bot_short').agg({
    'profit_usd': ['sum', 'mean', 'count']
}).round(2)

bot_stats.columns = ['Total Profit', 'Avg Profit', 'Attacks']
bot_stats = bot_stats.sort_values('Total Profit', ascending=False).head(10)

st.dataframe(bot_stats, use_container_width=True)

st.markdown("---")

st.subheader("Recent Attacks")

recent = filtered_df.sort_values('block_time', ascending=False).head(20)

display_cols = ['block_time', 'bot_short', 'victim_short', 'token_pair', 'profit_usd', 'victim_amount']
st.dataframe(recent[display_cols], use_container_width=True)

st.markdown("---")
st.caption("Data source: Dune Analytics | Built with Streamlit")
