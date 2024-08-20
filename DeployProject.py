import pandas as pd
import streamlit as st
import joblib

# model = joblib.load('model.joblib')

        
x_numericals = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'year': 0, 'month': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_lists = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Others', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }


dictionary = {}
for item in x_lists:
    for value in x_lists[item]:
        dictionary[f'{item}_{value}'] = 0


for item in x_numericals:
    if item == 'latitude' or item == 'longitude':
        value = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        value = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        value = st.number_input(f'{item}', step=1, value=0)
    x_numericals[item] = value

for item in x_tf:
    value = st.selectbox(f'{item}', ('Yes', 'No'))
    if value == "Yes":
        x_tf[item] = 1
    else:
        x_tf[item] = 0
    
    
for item in x_lists:
    value = st.selectbox(f'{item}', x_lists[item])
    dictionary[f'{item}_{value}'] = 1
    
button = st.button('Predict Property Value')

if button:
    dictionary.update(x_numericals)
    dictionary.update(x_tf)
    x_values = pd.DataFrame(dictionary, index=[0])
    data = pd.read_csv('data.csv')
    columns = list(data.columns)[1:-1]
    x_values = x_values[columns]
    model = joblib.load('model.joblib')
    price = model.predict(x_values)
    st.write(price[0])
    