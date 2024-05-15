import pandas as pd 
import streamlit as st
import plotly.graph_objects as go



def makeTreemap(labels, patents):
    data = go.Treemap(
        ids=labels,
        labels=labels,
        parents=patents,
        root_color='lightgrey'
    )
    fig = go.Figure(data)
    return fig

def makeIcicle(labels, patents):
    data = go.Icicle(
        ids=labels,
        labels=labels,
        parents=patents,
        root_color='lightgrey'
    )
    fig = go.Figure(data)
    return fig

def makeSunburst(labels, patents):
    data = go.Sunburst(
        ids=labels,
        labels=labels,
        parents=patents,
        insidetextorientation='horizontal',
        root_color='lightgreen'
    )
    fig = go.Figure(data)
    return fig

def makeSankey(labels, patents):
    data = go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=[list(labels).index(x) for x in labels],
            target=[-1 if pd.isna(x) else list(labels).index(x) for x in patents],
            label=labels,
            value=list(range(1, len(labels))))
    )
    fig = go.Figure(data)
    return fig

st.title('Herarchical Data Viewer')

df = pd.read_csv('data/employees.csv', header=0).convert_dtypes()
#st.dataframe(df)

labels = df[df.columns[0]]
patents = df[df.columns[1]]

tabs = st.tabs(["🎋 Treemap", "Icicle", "Sunburst", "Sankey"])

with tabs[0]:
    fig = makeTreemap(labels, patents)
    st.plotly_chart(fig, use_container_width=True)

with tabs[1]:
    fig = makeIcicle(labels, patents)
    st.plotly_chart(fig, use_container_width=True)

with tabs[2]:
    fig = makeSunburst(labels, patents)
    st.plotly_chart(fig, use_container_width=True)  

with tabs[3]:
    with st.expander("Sankey", expanded=True):
        fig = makeSankey(labels, patents)
        st.plotly_chart(fig, use_container_width=True)