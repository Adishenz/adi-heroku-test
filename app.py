import streamlit as st


PAGE_CONFIG = {"page_title":"Text2Handwriting","page_icon":"images/page_logo.png"}
st.set_page_config(**PAGE_CONFIG)


def main():
    st.title('Hello')
    st.subheader('This is a test run')


if __name__ == '__main__':
    main()