# import streamlit as st
# import pandas as pd

# review_datas = pd.read_excel('reviews.xlsx')
# reviews = review_datas['Reviews']
# label_reviews = review_datas['Label']

# st.write('Data Reviews')
# st.dataframe(review_datas)
# st.table(review_datas)
# st.write(review_datas)
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)