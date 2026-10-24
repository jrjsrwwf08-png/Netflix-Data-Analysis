import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Netflix Business Insights Dashboard",
    page_icon="🎬",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }

    .stMetric {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
        transition: all 0.3s ease-in-out;
    }
    
    .stMetric:hover {
        transform: translateY(-5px);
        border-color: #E50914;
        box-shadow: 0 8px 25px rgba(229, 9, 20, 0.35);
    }
    
    div[data-testid="stVerticalBlock"] > div:has(.stPlotlyChart) {
        transition: all 0.3s ease-in-out;
    }
    </style>
""",
    unsafe_allow_html=True,
)

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "Cleaned_Dataset.csv")

df = pd.read_csv(file_path)

st.title("🎬 Netflix Business Insights & Analytics Dashboard")
st.markdown(
    "An advanced interactive dashboard for analyzing Netflix platform content and extracting business insights"
)
st.markdown("---")

st.sidebar.header("🔍 Filters")

selected_type = st.sidebar.selectbox(
    "Select content type : ", ["All"] + list(df["Type"].unique())
)

all_countries = sorted(df["Country"].dropna().unique())
selected_country = st.sidebar.selectbox(
    "Select country : ", ["All"] + list(all_countries)
)

filtered_df = df.copy()
if selected_type != "All":
    filtered_df = filtered_df[filtered_df["Type"] == selected_type]
if selected_country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == selected_country]

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        label="📊 Total Works : ",
        value=f"{len(filtered_df):,}",
        delta="Known items",
    )
with col2:
    movies_count = len(filtered_df[filtered_df["Type"] == "Movie"])
    st.metric(label="🎥 Total movies : ", value=f"{movies_count:,}")
with col3:
    tv_count = len(filtered_df[filtered_df["Type"] == "Tv Show"])
    st.metric(label="📺 Total tv show : ", value=f"{tv_count:,}")
with col4:
    avg_year = (
        int(filtered_df["Release_Year"].mean())
        if not filtered_df.empty
        else 0
    )
    st.metric(label="📅 Average release year : ", value=str(avg_year))

st.markdown("---")

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("📌 The ratio of films to tv show")
    type_counts = filtered_df["Type"].value_counts().reset_index()
    type_counts.columns = ["Type", "Count"]

    fig_pie = px.pie(
        type_counts,
        names="Type",
        values="Count",
        hole=0.5,
        color_discrete_sequence=px.colors.sequential.RdBu,
    )
    fig_pie.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="<b>Type:</b> %{label}<br><b>Count:</b> %{value:,}<br><b>Percentage:</b> %{percent}<extra></extra>",
    )
    fig_pie.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        hoverlabel=dict(
            bgcolor="#161b22", font_color="white", bordercolor="#30363d"
        ),
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with row1_col2:
    st.subheader("📈 Chronological development of content by year of release")
    year_counts = (
        filtered_df["Release_Year"].value_counts().sort_index().reset_index()
    )
    year_counts.columns = ["Release_Year", "Count"]

    fig_line = px.line(
        year_counts,
        x="Release_Year",
        y="Count",
        markers=True,
        color_discrete_sequence=["#E50914"],
    )
    fig_line.update_traces(
        hovertemplate="<b>Year:</b> %{x}<br><b>Releases:</b> %{y:,}<extra></extra>"
    )
    fig_line.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        hoverlabel=dict(
            bgcolor="#161b22", font_color="white", bordercolor="#30363d"
        ),
    )
    st.plotly_chart(fig_line, use_container_width=True)

st.markdown("---")

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("🌍 Top 10 countries in terms of content production")
    top_countries = filtered_df["Country"].value_counts().head(10).reset_index()
    top_countries.columns = ["Country", "Count"]

    fig_bar = px.bar(
        top_countries,
        x="Count",
        y="Country",
        orientation="h",
        color="Count",
        color_continuous_scale="Reds",
    )
    fig_bar.update_traces(
        hovertemplate="<b>Country:</b> %{y}<br><b>Count:</b> %{x:,}<extra></extra>"
    )
    fig_bar.update_layout(
        yaxis=dict(autorange="reversed"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        hoverlabel=dict(
            bgcolor="#161b22", font_color="white", bordercolor="#30363d"
        ),
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with row2_col2:
    st.subheader("🏷️ Top genree and most popular")
    if "Listed_In" in filtered_df.columns:
        genres = filtered_df["Listed_In"].str.split(",").explode().str.strip()
        top_genres = genres.value_counts().head(10).reset_index()
        top_genres.columns = ["Genre", "Count"]

        fig_genres = px.bar(
            top_genres,
            x="Count",
            y="Genre",
            orientation="h",
            color="Count",
            color_continuous_scale="Sunset",
        )
        fig_genres.update_traces(
            hovertemplate="<b>Genre:</b> %{y}<br><b>Count:</b> %{x:,}<extra></extra>"
        )
        fig_genres.update_layout(
            yaxis=dict(autorange="reversed"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            hoverlabel=dict(
                bgcolor="#161b22", font_color="white", bordercolor="#30363d"
            ),
        )
        st.plotly_chart(fig_genres, use_container_width=True)

st.markdown("---")
st.subheader("📋 A sample of current data : ")
st.dataframe(filtered_df.head(10), use_container_width=True)