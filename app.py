import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏏 IPL AI Dashboard")

df = pd.read_csv("IPL_Matches_2008_2022.csv")

st.subheader("Dataset Overview")
st.write(df.head())

st.subheader("Data Cleaning")
df = df.drop_duplicates()
st.write("Shape:", df.shape)

st.subheader("KPIs")

col1, col2, col3 = st.columns(3)

col1.metric("Total Matches", len(df))
col2.metric("Total Teams", df['Team1'].nunique())
col3.metric("Cities", df['City'].nunique())

st.sidebar.header("Filters")

teams = st.sidebar.multiselect(
    "Select Team",
    df['Team1'].unique(),
    default=df['Team1'].unique()
)

filtered_df = df[df['Team1'].isin(teams)]

st.subheader("Visualization 1")
fig1 = px.histogram(filtered_df, x="Season")
st.plotly_chart(fig1)

st.subheader("Visualization 2")
fig2 = px.pie(filtered_df,
              names="WinningTeam")
st.plotly_chart(fig2)

st.subheader("Visualization 3")
fig3 = px.bar(
    filtered_df['WinningTeam'].value_counts().reset_index(),
    x='WinningTeam',
    y='count'
)
st.plotly_chart(fig3)

st.subheader("Visualization 4")
fig4 = px.scatter(filtered_df,
                  x="Margin",
                  y="MatchNumber")
st.plotly_chart(fig4)

st.subheader("Visualization 5")
fig5 = px.box(filtered_df,
              y="Margin")
st.plotly_chart(fig5)