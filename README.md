<p align="center">
  <img src="https://github.com/frankchang1000/EasyEco/blob/main/docs/EasyEco-1 (1).jpg", width="150"/>
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

According to the Environmental Protection Agency, almost 300 million tons of waste are produced by the United States per year. Trash can take decades to decompose, especially as more and more garbage is piled onto landfills. From a young age, we learn to recycle as much as we can to reduce the amount of trash. With recycling comes a huge problem: improper recycling due to laziness and/or lack of knowledge. Improper recycling not only ruins the efficiency of  recycling, but it also has the potential to negatively damage the environment by releasing toxic chemicals. EasyEco aims to promote proper recycling through the use of neural networks.

## What it does ❓

<p align="center">
  <img src="https://github.com/frankchang1000/PlasticPal/blob/main/docs/slides/07.png", width="500"/>
</p>

EasyEco uses computer vision to determine if an item is recyclable. Then, our end-user can use the information provided to properly dispose of the item, which helps the environment and builds proper recycling habits. 

EasyEco takes an image from a camera input, and feeds the image to our EfficientNetv2 model. The neural network classifies the image into one of 101 different categories, and is able to determine if the waste is fully recyclable, is only partly recyclable, or if it should not be recycled at all. Visual infographics are also displayed in order to easily inform the user of the reasoning behind the decision.

## Installation and Usage ⌨️🖱️

To use begin with cloning the repository from GitHub, install the requirements, and run the Streamlit application.

```cmd
git clone https://github.com/frankchang1000/EasyEco.git
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

Our backend is powered using Tensorflow 2.9 (the most recent version) as well as EfficientNetv2, which we modified to have a slightly larger width to increase feature and pattern recognition. We created a custom dataset containing over 10,000 images through the use of webscraping techniques with the Google Images api. To further improve inference, 8 different augmentation methods were applied to train on more realistic, real-world images. The results were a resounding 95% training accuracy on our private test set. EasyEco uses the most advanced technology available to solve the world’s leading problems.

The front-end was built with Streamlit and Python, and features a multi-page setup in order to have one page for initial camera scanning, and a final decision page. Once the classification is made, we pull the recycling status key from a dictionary and print out the final verdict. We also display an infographic depending on the recycling status. 

## Challenges we ran into 👷‍♂️

Taiwan boasts one of the highest recycling rates in the world, so we decided to webscrape our 101 different objects from their recycling website. However, we ran into many issues with this as most of the info was written in Chinese. We tried applying the GoogleTranslate API to pull the HTML data and translate it, but did not meet much success. In the end, we manually created a dictionary and used the info provided on the website to create our key. 

We also wanted our front end to switch pages when the user took a picture, but Streamlit was unable to support this feature. We resorted to a dropdown menu which was more widely documented by the Streamlit users.

The largest problem that we faced was training inference vs. testing inference accuracy. In the initial stages of testing, our model always worked well with any of the training images but webcam inference tests never worked correctly. After weeks of debugging, we realized that the webcam captured images with a 1920x1080, and our model made predictions with an image size of 128x128. 

## License

MIT License (MIT) Copyright (c) 2022 frankchang1000 and the contributors.
