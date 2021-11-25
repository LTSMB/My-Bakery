import streamlit as st
import numpy as np
import pandas as pd
import time

st.header("ShuShuMei Bakery")

option = st.sidebar.selectbox(
    'Our Menu',
     ['Bread','Cake','Pastery','Inbox','T n C'])

if option=='Bread':
    st.write('Our Bread are freshly made everyday to ensure your happines :)')
    st.image ('white bread.jpg', use_column_width=True)
    st.image ('croissant.jpg', use_column_width=True)


elif option=='Cake':
  st.write('Our Cake are freshly bake everyday to satisfy your craves :)')
  st.image ('cheesecake.jpg', use_column_width=True)
  st.image ('sponge cake.jpg', use_column_width=True)

elif option=='Pastery':
  st.write('Our Pastery are freshly bake everyday for our lovely customers :)')
  st.image ('karipap.jpg', use_column_width=True)
  st.image ('Pie.jpg', use_column_width=True)

elif option=='Inbox':
  st.write('We will uploads more menus  in this website... stay tuned and support our bakery with love!!! ')

elif option=='T n C':
    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    

else:
    'Starting a long computation...'
    
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'
