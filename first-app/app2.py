import streamlit as st 

st.title('Herarchical Data Viewer')
st.header('Data Connectors')
st.subheader('What are data connectors?')
st.caption('Data connectors are used to fetch data from a variety of sources.')

st.write('Data connectors are used to fetch data from a variety of sources.')
st.text('Data connectors are used to fetch data from a variety of sources.')
st.code('A = B + C', language='python')
st.markdown("**bold**")
st.divider()

st.latex(r'''2x + 3y = 4''')

st.error('This is an error')
st.info('This is a info')
st.warning('This is a warning')
st.success('This is a success')

st.balloons()
st.snow()