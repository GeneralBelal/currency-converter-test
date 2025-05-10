# Step 1: Importing libraries
import requests
import streamlit as st

# Step 2: Getting exchange rate
def get_exchange_rates(base_currency):
    api_key = '194bed32347c49090aed51aa'
    request = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    response = requests.get(request)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return 'Failed to fetch exchange rates'


# Step 3: Streamlit main app
st.title('💱Currency App Calculator💱')
st.subheader('Convert all currencies in real-time')

currencies = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP",
    "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS",
    "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF",
    "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD",
    "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT",
    "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD",
    "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN",
    "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK",
    "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR",
    "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL", "SOS", "SRD",
    "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY",
    "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES",
    "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"
]

col1, col2 = st.columns(2, border = True)

with col1:
    base_currency = st.selectbox('From currency', currencies, index=0)

with col2:
    target_currency = st.selectbox('To currency', currencies, index=1)

amount = st.number_input('Enter the amount:', value=1, step=1)

rates = get_exchange_rates(base_currency)['conversion_rates']

if st.button('Calculate Rate'):
    exchange_rate = rates[target_currency]
    total = exchange_rate * amount
    st.success(f'{amount} {base_currency} = {total:,} {target_currency}')





