{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
import nltk\
from nltk.sentiment import SentimentIntensityAnalyzer\
import streamlit as st\
from PIL import Image, ImageDraw, ImageFont\
import io\
\
# Download necessary NLTK data\
nltk.download('vader_lexicon')\
\
def generate_campaign_content(prompt, brand_guidelines):\
    # This is a very simple content generator\
    templates = [\
        "Introducing \{product\}: The perfect solution for \{audience\}!",\
        "Experience the difference with \{product\}. Ideal for \{audience\}.",\
        "Upgrade your life with \{product\}. Designed for \{audience\}.",\
        "\{audience\}, meet your new favorite \{product\}!",\
        "Transform your \{pain_point\} with \{product\}. Made for \{audience\}."\
    ]\
    \
    template = random.choice(templates)\
    product = prompt.split()[-1]  # Assume the last word in the prompt is the product\
    audience = brand_guidelines.split()[:3]  # Use the first three words of brand guidelines as audience\
    pain_point = random.choice(["routine", "lifestyle", "challenges", "needs"])\
    \
    return template.format(product=product, audience=" ".join(audience), pain_point=pain_point)\
\
def generate_image(prompt):\
    # Create a simple colored rectangle with text as the "generated" image\
    img = Image.new('RGB', (512, 512), color = (73, 109, 137))\
    d = ImageDraw.Draw(img)\
    font = ImageFont.load_default()\
    d.text((10,10), prompt, fill=(255,255,0), font=font)\
    \
    img_byte_arr = io.BytesIO()\
    img.save(img_byte_arr, format='PNG')\
    img_byte_arr = img_byte_arr.getvalue()\
    \
    return img_byte_arr\
\
def analyze_sentiment(text):\
    sia = SentimentIntensityAnalyzer()\
    return sia.polarity_scores(text)['compound']\
\
def brand_differentiation(campaign_content, competitor_content):\
    campaign_sentiment = analyze_sentiment(campaign_content)\
    competitor_sentiment = analyze_sentiment(competitor_content)\
    \
    if campaign_sentiment > competitor_sentiment:\
        return "Your campaign has a more positive tone than your competitor's."\
    elif campaign_sentiment < competitor_sentiment:\
        return "Your competitor's campaign has a more positive tone. Consider adjusting your content."\
    else:\
        return "Your campaign and your competitor's have similar tones. Try to make your content more unique."\
\
def main():\
    st.title("AI-Powered Marketing Campaign Generator")\
\
    # User inputs\
    campaign_goal = st.text_input("Enter your campaign goal:")\
    target_audience = st.text_input("Describe your target audience:")\
    brand_guidelines = st.text_area("Enter your brand guidelines:")\
    competitor_content = st.text_area("Enter a sample of your competitor's content for comparison:")\
\
    if st.button("Generate Campaign"):\
        # Generate campaign content\
        prompt = f"Create a marketing campaign for \{target_audience\} with the goal of \{campaign_goal\}."\
        campaign_content = generate_campaign_content(prompt, brand_guidelines)\
        \
        # Generate image\
        image_prompt = f"Ad for \{campaign_content\}"\
        image = generate_image(image_prompt)\
\
        # Analyze brand differentiation\
        differentiation = brand_differentiation(campaign_content, competitor_content)\
\
        # Display results\
        st.subheader("Generated Campaign Content:")\
        st.write(campaign_content)\
        \
        st.subheader("Generated Image:")\
        st.image(image)\
        \
        st.subheader("Brand Differentiation Analysis:")\
        st.write(differentiation)\
\
if __name__ == "__main__":\
    main()}