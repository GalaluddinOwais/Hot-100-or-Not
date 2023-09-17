# About the project
#### This project is a full-stack machine learning project that introduces a web application to predict whether a given song will make it onto the Hot 100 songs chart in its release year, primarily by checking its repeated chorus.

# Key Achievements
* Collected names of songs that reached the Hot 100 chart and songs that did not for the same artists, ensuring a real-world distribution of both categories
* Downloaded each song's audio, extracted the chorus section, and converted it into various statistical features about the chorus audio descriptors, to finally obtain the dataset
* Visualized the dataset for exploratory data analysis to identify any necessary preprocessing steps
* Applied the preprocessing steps to the dataset to observe how each handles the data
* Tested multiple models to gain insights into the best-performing one for the dataset, which appeared to be the Random Forest model, then fine-tuned it maximize the F1 score, resulting in an F1 score of 60% and an accuracy of 85%
* Utilized raw data to construct a trained pipeline that incorporates predetermined preprocessing steps and the best found model. to provide prediction given a raw song data sample
* Implemented a specific module (library) with necessary functions to fetch songs from different given sources, extract their chorus statistical audio features, and provide predictions using the pipeline
* Implemented the back-end functionalities using the module, to introduce the following features:
  * Providing predictions for songs given their YouTube links
  * Providing predictions for songs given their Spotify links
  * Providing predictions for songs by uploading the audio file
  * Displaying predictions for recently released songs (updated periodically)
* Designed the front-end to be visually appealing, user-friendly, and intuitive


# Requirements
`python 3.9`
`pandas`
`numpy`
`Flask`
`librosa`
`scipy`
`yt-dlp`
`YoutubeSearch`
`spotipy`
`datetime`
`scikit-learn 1.2.2`
`pychorus`
`pickle`

# Execution
* Locate `app.py` and run the following command:
```
python app.py
```
* Access the application through web browser by entering the address you will be provided

# Demonstration

#### [Google drive link](https://drive.google.com/file/d/1TQSPZYRlYxPVGmBk8n_qeH7sMHErnzCm/view?usp=share_link)

