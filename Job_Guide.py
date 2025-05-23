import streamlit as st

# Profession data dictionary
profession_data = {
    "Tailor / Fashion Designer": {
        "English": {
            "How AI Helps": [
                "Predict Trends: AI analyzes social media, runway shows, and sales data to forecast upcoming fashion trends.",
                "Automate Design: AI can generate design patterns, suggest color combinations, and even create digital prototypes.",
                "Virtual Fitting Rooms: AI-powered augmented reality (AR) allows customers to 'try on' clothes virtually before purchase."
            ],
            "AI Tools": [
                "Google TensorFlow → Used to build custom AI models for unique design generation.",
                "Vue.ai → Helps with personalized styling recommendations and automated catalog tagging.",
                "Fit3D → Uses body scanning to create accurate virtual fittings."
            ]
        },
        "Hausa": {
            "Yadda AI zai iya taimakawa": [
                "Hasashen Trends: AI yana nazarin soshial media, nunin fasinjoji, da bayanan siyarwa don hasashen abubuwan da zasu shigo cikin fashion.",
                "Ƙirƙira ta atomatik: AI na iya samar da ƙirar ƙira, ba da shawarwarin haɗin launi, har ma ƙirƙirar samfuran dijital.",
                "Dakin gwatin Virtual: AR mai ƙarfin AI yana ba abokin ciniki damar 'gwada' tufafi a zahiri kafin siye."
            ],
            "Kayan aikin AI": [
                "Google TensorFlow → Ana amfani da shi don gina ƙirar AI na musamman don samarwa.",
                "Vue.ai → Yana taimakawa tare da shawarwarin salo na keɓantacce da alamar katalog na atomatik.",
                "Fit3D → Yana amfani da duban jiki don ƙirƙirar ingantaccen kayan gwatin virtual."
            ]
        }
    },
    "Akara Seller (Food Vendor)": {
        "English": {
            "How AI Helps": [
                "Chatbots for Orders: AI chatbots handle customer inquiries and take orders via WhatsApp or Facebook.",
                "Inventory & Sales Prediction: AI predicts peak demand times and optimizes ingredient purchases."
            ],
            "AI Tools": [
                "ManyChat / Tidio → Simple chatbot builders for order automation.",
                "Zoho Inventory → AI-driven stock management to prevent shortages.",
                "Google Sheets AI Add-ons → Analyzes sales trends for better decision-making."
            ]
        },
        "Hausa": {
            "Yadda AI zai iya taimakawa": [
                "Chatbots don oda: Chatbots na AI suna ɗaukar tambayoyin abokin ciniki da kuma karɓar odar ta WhatsApp ko Facebook.",
                "Hasashen siyarwa da kayan aiki: AI yana hasashen lokutan buƙatu da inganta sayan kayan abinci."
            ],
            "Kayan aikin AI": [
                "ManyChat / Tidio → Sauƙaƙan ginin chatbots don sarrafa oda.",
                "Zoho Inventory → Gudanar da kayayyaki na AI don hana ƙarancin kayayyaki.",
                "Google Sheets AI Add-ons → Yana nazarin yanayin siyarwa don ingantaccen yanke shawara."
            ]
        }
    },
    "Farmer": {
        "English": {
            "How AI Helps": [
                "Crop Monitoring: AI analyzes drone/satellite images to detect diseases or pests.",
                "Irrigation Automation: AI adjusts watering schedules based on soil moisture and weather forecasts.",
                "Weather Prediction: AI models provide hyper-local weather insights."
            ],
            "AI Tools": [
                "Microsoft AI for Earth → Tracks crop health via satellite imagery.",
                "IBM Watson Decision Platform → Provides AI-driven farming recommendations.",
                "DroneDeploy → Uses drones to map and analyze fields."
            ]
        },
        "Hausa": {
            "Yadda AI zai iya taimakawa": [
                "Sauraron amfanin gona: AI yana nazarin hotunan jirgi sama/taɓararru don gano cututtuka ko kwari.",
                "Sarrafa ban ruwa: AI yana daidaita jadawalin ban ruwa bisa laimin ƙasa da hasashen yanayi.",
                "Hasashen yanayi: Samfuran AI suna ba da cikakkun bayanai game da yanayin gida."
            ],
            "Kayan aikin AI": [
                "Microsoft AI for Earth → Yana bin lafiyar amfanin gona ta hotunan tauraron dan adam.",
                "IBM Watson Decision Platform → Yana ba da shawarwarin noma na AI.",
                "DroneDeploy → Yana amfani da jirage marasa matuka don taswira da nazarin filayen."
            ]
        }
    },
    # Add other professions in the same format...
    "Taxi Driver / Ride-Hailing Operator": {
        "English": {
            "How AI Helps": [
                "Route Optimization: AI suggests the fastest routes in real time.",
                "Dynamic Pricing: Adjusts fares based on demand (like Uber's surge pricing).",
                "Customer Feedback Analysis: AI detects sentiment in reviews to improve service."
            ],
            "AI Tools": [
                "Google Maps API → Real-time traffic and route adjustments.",
                "Uber Movement → Analyzes traffic patterns for better planning.",
                "MonkeyLearn → Scans reviews for customer sentiment."
            ]
        },
        "Hausa": {
            "Yadda AI zai iya taimakawa": [
                "Ingantacciyar hanya: AI yana ba da shawarar mafi saurin hanyoyin a lokacin da ake buƙata.",
                "Farashin canzawa: Yana daidaita farashin bisa buƙata (kamar farashin Uber na yawan buƙata).",
                "Nazarin ra'ayin abokin ciniki: AI yana gano ra'ayi a cikin bita don inganta sabis."
            ],
            "Kayan aikin AI": [
                "Google Maps API → Daidaitawar hanyoyin cikin gaggawa da zirga-zirga.",
                "Uber Movement → Yana nazarin yanayin zirga-zirga don ingantaccen tsarawa.",
                "MonkeyLearn → Yana duba bita don gano ra'ayin abokin ciniki."
            ]
        }
    }
}

# 🌍 Page title
st.markdown("<h1 style='text-align: center; color: green;'>🌍 New World AI Guide</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Helping every profession understand and use AI — in English and Hausa.</p>", unsafe_allow_html=True)
st.write("---")

# 🧑‍🎓 Profession dropdown with emojis
profession_emojis = {
    "Tailor / Fashion Designer": "🧵",
    "Akara Seller (Food Vendor)": "🍽️",
    "Farmer": "👨🏾‍🌾",
    "Taxi Driver / Ride-Hailing Operator": "🚕",
    "Shoemaker": "👞",
    "Hairdresser / Barber": "✂️",
    "Food Truck Operator": "🍔",
    "Mobile Phone Repair Technician": "📱",
    "Photographer": "📷",
    "Event Planner": "📅",
    "Online Retailer (E-commerce)": "🛒",
    "Tailoring Fabric Seller": "🧶",
    "Furniture Maker": "🪑",
    "Real Estate Agent": "🏠",
    "Bookshop Owner": "📚",
    "Courier/Delivery Service": "📦",
    "Car Wash Business": "🚗",
    "Hair Product Seller": "🧴",
    "Bakery": "🍞",
    "Mechanic / Auto Repair Shop": "🔧"
}

selected_profession = st.selectbox("Choose your profession:", list(profession_emojis.keys()))
emoji = profession_emojis.get(selected_profession, "")

# 🌐 Language selection buttons
col1, col2 = st.columns(2)
with col1:
    english = st.button("Get Advice in English")
with col2:
    hausa = st.button("Nemi Shawara da Hausa")

# 💬 Optional: Ask your own question
st.write("---")
question = st.text_input("Do you want to ask something specific? (Optional)")
if question:
    st.info(f"🔎 You asked: {question}")
    st.warning("💡 Free question answering will be added in a future upgrade.")

# Function to display AI advice
def display_ai_advice(profession, language):
    data = profession_data.get(profession, {}).get(language, {})
    
    if not data:
        st.warning(f"No data available for {profession} in {language} yet.")
        return
    
    st.subheader(f"{emoji} {'AI Advice for' if language == 'English' else 'Shawarar AI ga'} {profession}")
    
    st.markdown("### 📌 How AI Helps" if language == "English" else "### 📌 Yadda AI zai iya taimakawa")
    for item in data.get("How AI Helps" if language == "English" else "Yadda AI zai iya taimakawa", []):
        st.markdown(f"- {item}")
    
    st.markdown("### 🛠️ AI Tools" if language == "English" else "### 🛠️ Kayan aikin AI")
    for item in data.get("AI Tools" if language == "English" else "Kayan aikin AI", []):
        st.markdown(f"- {item}")

# 🚀 Displaying response
if english and selected_profession:
    display_ai_advice(selected_profession, "English")

if hausa and selected_profession:
    display_ai_advice(selected_profession, "Hausa")

# Add footer
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2023 New World AI Guide - Helping professions adapt to AI</p>", unsafe_allow_html=True)
