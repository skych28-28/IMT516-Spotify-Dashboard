import streamlit as st
import plotly.express as px
import pandas as pd

def render_popularity_by_key(df: pd.DataFrame):
    st.subheader("🎵 Popularity by Key")
    fig = px.bar(df, x="key", y="popularity", color="key", title="Popularity by Musical Key")
    st.plotly_chart(fig, use_container_width=True)

def render_avg_stream_by_label(df: pd.DataFrame):
    st.subheader("🏷 Average Stream Count by Label")
    grouped = df.groupby("label", as_index=False)["stream_count"].mean()
    fig = px.bar(grouped, x="label", y="stream_count", color="label", title="Average Stream Count by Label")
    st.plotly_chart(fig, use_container_width=True)

def render_popularity_distribution(df: pd.DataFrame):
    st.subheader("📈 Distribution of Track Popularity")
    fig = px.histogram(df, x="popularity", nbins=20, hover_data=["track_name"], title="Track Popularity Distribution")
    st.plotly_chart(fig, use_container_width=True)

def render_genres_over_time_by_country(df: pd.DataFrame):
    st.subheader("🌍 Genre Trends Over Time by Country")
    grouped = df.groupby(["release_year", "country", "genre"], as_index=False)["track_name"].count()
    fig = px.line(
        grouped,
        x="release_year",
        y="track_name",
        color="genre",
        line_group="country",
        title="Genre Trends Over Time by Country"
    )
    st.plotly_chart(fig, use_container_width=True)
