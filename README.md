<p align="center">
  <img src="https://github.com/frankchang1000/Poolesville/blob/main/docs/logo.png", width="150"/>
</p>

# EasyEco

Promoting **proper** plastic recycling with an AI classification app.

## Table of Contents 📑

* [Purpose and Inspiration](#purpose-and-inspiration)
* [What it does](#what-it-does)
* [Installation and Usage](#installation-and-usage)
* [How we built it](#how-we-built-it)
* [Challenges we ran into](#challenges-we-ran-into)
* [License](#license)

## Purpose and Inspiration 💡

<p align="center">
  <img src="https://github.com/frankchang1000/Poolesville/blob/main/docs/waste_statistics.png", width="500"/>
</p>

According to the Environmental Protection Agency, almost 300 million tons of waste are produced by the United States per year. Trash can take decades to decompose, especially as more and more garbage is piled onto landfills. Around 20% of the 300 million tons of trash are recycled, but most of the recycling is done incorrectly. Improper recycling can not only reduce the efficiency of recycling, but it can also harm the environment by releasing toxic chemicals. EasyEco aims to promote proper recycling through the use of neural networks.

## What it does ❓

<p align="center">
  <img src="https://github.com/frankchang1000/PlasticPal/blob/main/docs/slides/07.png", width="500"/>
</p>

EasyEco uses computer vision to determine if an item is recyclable. Then, our end-user can properly dispose of the item, helping to improve the environment and our recycling conditions.

EasyEco takes an image from a camera input, and feeds the image to our EfficientNet model. The neural network classifies the image into one of 101 different categories, and is able to determine if the waste is fully recyclable, is only partly recyclable, or if it should not be recycled at all. Visual infographics are also displayed in order to easily inform the user of the reasoning behind the decision.

## Installation and Usage ⌨️🖱️

To use begin with cloning the repository from GitHub, install the requirements, and run the Streamlit application.

```cmd
git clone https://github.com/frankchang1000/PlasticPal.git
python -m venv venv 
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run main.py
```

### Tensorflow GPU Support 💻

To utilize the GPU for AI processing download the proper drivers for your model of GPU. If your GPU has a compute capability of at least 7.0, you can use mixed precision inference; otherwise, you can use float32. Any RTX card should support this feature.

We utilized Tensorflow 2.9 which requires the latest version of the drivers for your Nvidia GPU.

## How we built it ⚙️🔧

<p align="center">
  <img src="https://github.com/frankchang1000/PlasticPal/blob/main/docs/slides/09.png", width="500"/>
</p>

Our backend is powered using the most recent version of Tensorflow, Tensorflow2.9. We incorporated optimizations to our backend server including mixed precision training and inference. Our neural network (EfficientNetv2) was slightly modified to be wider than normal to increase pattern recognition, and improve inference. The results were a resounding 95% accuracy on our private test set. Lastly, we utilized numerous web scraping techniques to advance, improve, and clean our large training dataset with over 10000 images. PlasticPal uses the most advanced technology available to solve the world’s leading problems.

The front-end was built with Streamlit and Python, and uses a multi-page setup in order to have one page for initial camera scanning, and a final decision page. Once the classification is made, we pull the recycling status key from a dictionary and print out the final verdict. We also display an infographic depending on the recycling status.

## Challenges we ran into 👷‍♂️

At first, we attempted to web scrape the different recycling categories for each type of waste from a website, but we faced many challenges as the website’s language was chinese. We tried applying the GoogleTranslate API to pull the html data and translate it, but did not meet much success. We also wanted our front end to switch pages when the user took a picture, but Streamlit was unable to support this feature. We resorted to a dropdown menu which was more widely documented by the Streamlit users.

## License

MIT License (MIT) Copyright (c) 2022 frankchang1000 and the contributors.
