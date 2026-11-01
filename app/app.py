import streamlit as st
import pandas as pd
import joblib
import pickle
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Digital Marketing Conversion Predictor",
    page_icon="📈",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #777777;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_DIR / "models" / "conversion_model.pkl"


# ============================================================
# LOAD TRAINED PIPELINE
# ============================================================

model = None
load_method = None

try:

    # The saved model was successfully loaded with Joblib
    model = joblib.load(MODEL_PATH)

    load_method = "Joblib"

except Exception as joblib_error:

    try:

        with open(MODEL_PATH, "rb") as file:
            model = pickle.load(file)

        load_method = "Pickle"

    except Exception as pickle_error:

        st.error("The trained model could not be loaded.")

        st.write("### Model location")
        st.code(str(MODEL_PATH))

        st.write("### Joblib error")
        st.code(str(joblib_error))

        st.write("### Pickle error")
        st.code(str(pickle_error))

        st.stop()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📈 Digital Marketing Conversion Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict the likelihood of customer conversion using the trained XGBoost model.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("About the Model")

    st.write(
        """
        This application uses the trained XGBoost classification pipeline
        developed during the Digital Marketing Campaign Conversion
        Prediction project.
        """
    )

    st.write("### Model")

    st.write("XGBoost Classifier")

    st.write("### Preprocessing")

    st.write(
        """
        The saved pipeline automatically performs:

        • Numerical feature scaling

        • Categorical feature encoding
        """
    )

    st.write("### Prediction Target")

    st.write("Customer Conversion")

    st.write("### Application Purpose")

    st.write(
        """
        Estimate the likelihood that a customer will convert based on
        demographic, campaign, engagement and spending information.
        """
    )

    st.divider()

    st.caption(
        f"Model loaded successfully using {load_method}."
    )

    st.caption(
        "Predictions are model-based estimates and are not guaranteed outcomes."
    )


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.header("Customer Information")

col1, col2, col3 = st.columns(3)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35,
        step=1
    )

with col2:

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )

with col3:

    income = st.number_input(
        "Income",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )


# ============================================================
# CAMPAIGN INFORMATION
# ============================================================

st.header("Campaign Information")

col1, col2, col3 = st.columns(3)

with col1:

    campaign_channel = st.selectbox(
        "Campaign Channel",
        [
            "Referral",
            "PPC",
            "SEO",
            "Email",
            "Social Media"
        ]
    )

with col2:

    campaign_type = st.selectbox(
        "Campaign Type",
        [
            "Awareness",
            "Consideration",
            "Conversion",
            "Retention"
        ]
    )

with col3:

    ad_spend = st.number_input(
        "Ad Spend",
        min_value=0.0,
        value=5000.0,
        step=500.0
    )


# ============================================================
# CUSTOMER ENGAGEMENT
# ============================================================

st.header("Customer Engagement")

col1, col2, col3 = st.columns(3)

with col1:

    click_through_rate = st.number_input(
        "Click Through Rate",
        min_value=0.0,
        max_value=1.0,
        value=0.05,
        step=0.01,
        format="%.3f"
    )

with col2:

    conversion_rate = st.number_input(
        "Conversion Rate",
        min_value=0.0,
        max_value=1.0,
        value=0.10,
        step=0.01,
        format="%.3f"
    )

with col3:

    website_visits = st.number_input(
        "Website Visits",
        min_value=0,
        value=10,
        step=1
    )


col1, col2, col3 = st.columns(3)

with col1:

    pages_per_visit = st.number_input(
        "Pages Per Visit",
        min_value=0.0,
        value=3.0,
        step=0.5
    )

with col2:

    time_on_site = st.number_input(
        "Time On Site",
        min_value=0.0,
        value=5.0,
        step=0.5
    )

with col3:

    social_shares = st.number_input(
        "Social Shares",
        min_value=0,
        value=10,
        step=1
    )


# ============================================================
# EMAIL AND CUSTOMER HISTORY
# ============================================================

st.header("Email Engagement & Customer History")

col1, col2, col3 = st.columns(3)

with col1:

    email_opens = st.number_input(
        "Email Opens",
        min_value=0,
        value=5,
        step=1
    )

with col2:

    email_clicks = st.number_input(
        "Email Clicks",
        min_value=0,
        value=2,
        step=1
    )

with col3:

    previous_purchases = st.number_input(
        "Previous Purchases",
        min_value=0,
        value=2,
        step=1
    )


col1, col2 = st.columns(2)

with col1:

    loyalty_points = st.number_input(
        "Loyalty Points",
        min_value=0,
        value=500,
        step=50
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🚀 Predict Conversion",
    type="primary",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    try:

        # ====================================================
        # STEP 1 — FEATURE ENGINEERING
        # ====================================================

        email_click_rate = (
            email_clicks / (email_opens + 1)
        )

        spend_per_visit = (
            ad_spend / (website_visits + 1)
        )


        # ====================================================
        # STEP 2 — CREATE RAW INPUT DATA
        # ====================================================

        # IMPORTANT:
        # Do NOT manually one-hot encode the categorical columns.
        #
        # The saved sklearn Pipeline already contains:
        #
        # StandardScaler
        # +
        # OneHotEncoder
        #
        # Therefore we pass the raw values directly to the pipeline.

        input_data = pd.DataFrame(
            {
                "Age": [age],
                "Gender": [gender],
                "Income": [income],
                "CampaignChannel": [campaign_channel],
                "CampaignType": [campaign_type],
                "AdSpend": [ad_spend],
                "ClickThroughRate": [click_through_rate],
                "ConversionRate": [conversion_rate],
                "WebsiteVisits": [website_visits],
                "PagesPerVisit": [pages_per_visit],
                "TimeOnSite": [time_on_site],
                "SocialShares": [social_shares],
                "EmailOpens": [email_opens],
                "EmailClicks": [email_clicks],
                "PreviousPurchases": [previous_purchases],
                "LoyaltyPoints": [loyalty_points],
                "EmailClickRate": [email_click_rate],
                "SpendPerVisit": [spend_per_visit]
            }
        )


        # ====================================================
        # STEP 3 — ENSURE COLUMN ORDER
        # ====================================================

        expected_columns = [
            "Age",
            "Gender",
            "Income",
            "CampaignChannel",
            "CampaignType",
            "AdSpend",
            "ClickThroughRate",
            "ConversionRate",
            "WebsiteVisits",
            "PagesPerVisit",
            "TimeOnSite",
            "SocialShares",
            "EmailOpens",
            "EmailClicks",
            "PreviousPurchases",
            "LoyaltyPoints",
            "EmailClickRate",
            "SpendPerVisit"
        ]

        input_data = input_data[
            expected_columns
        ]


        # ====================================================
        # STEP 4 — MODEL PREDICTION
        # ====================================================

        # The complete sklearn Pipeline handles:
        #
        # 1. StandardScaler
        # 2. OneHotEncoder
        # 3. XGBoost prediction

        prediction = model.predict(
            input_data
        )[0]

        probabilities = model.predict_proba(
            input_data
        )[0]

        conversion_probability = float(
            probabilities[1]
        )


        # ====================================================
        # STEP 5 — DISPLAY RESULT
        # ====================================================

        st.header("Prediction Result")

        result_col1, result_col2 = st.columns(2)

        with result_col1:

            if prediction == 1:

                st.success(
                    "✅ Customer is predicted to CONVERT"
                )

            else:

                st.warning(
                    "⚠️ Customer is predicted to NOT CONVERT"
                )


        with result_col2:

            st.metric(
                "Conversion Probability",
                f"{conversion_probability:.1%}"
            )


        # ====================================================
        # STEP 6 — BUSINESS INTERPRETATION
        # ====================================================

        st.subheader("Business Interpretation")

        if conversion_probability >= 0.70:

            st.success(
                """
                **High conversion likelihood**

                The model estimates a relatively high likelihood of
                conversion. The marketing team could consider prioritizing
                this customer for targeted marketing or follow-up activity.
                """
            )

        elif conversion_probability >= 0.40:

            st.info(
                """
                **Moderate conversion likelihood**

                The customer has a moderate predicted likelihood of
                conversion. Additional engagement or targeted marketing
                may be considered.
                """
            )

        else:

            st.warning(
                """
                **Lower conversion likelihood**

                The model estimates a lower likelihood of conversion.
                Marketing resources could be allocated more selectively,
                subject to other business considerations.
                """ 
            )


        # ====================================================
        # STEP 7 — CALCULATED FEATURES
        # ====================================================

        with st.expander(
            "View Calculated Features"
        ):

            calculated_features = pd.DataFrame(
                {
                    "Feature": [
                        "EmailClickRate",
                        "SpendPerVisit"
                    ],

                    "Value": [
                        email_click_rate,
                        spend_per_visit
                    ]
                }
            )

            st.dataframe(
                calculated_features,
                use_container_width=True,
                hide_index=True
            )


        # ====================================================
        # STEP 8 — CUSTOMER INPUT
        # ====================================================

        with st.expander(
            "View Customer Input"
        ):

            st.dataframe(
                input_data,
                use_container_width=True,
                hide_index=True
            )


        # ====================================================
        # FINAL NOTE
        # ====================================================

        st.caption(
            "The prediction is generated using the trained XGBoost "
            "pipeline. The probability represents the model's estimated "
            "likelihood of conversion and does not guarantee an actual "
            "customer outcome."
        )


    except Exception as e:

        st.error(
            "An error occurred while making the prediction."
        )

        st.code(
            str(e)
        )

        st.info(
            """
            The saved model loaded successfully, but the prediction
            could not be completed. The error shown above can be used
            to diagnose model compatibility.
            """
        )