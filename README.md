# About the project
#### This project is a full-stack machine learning project that introduces a web application to predict whether a given song will make it onto the Hot 100 songs chart in its release year, primarily by checking its repeated chorus.

# Key Achievements
* Compiled a list of song names that made it onto the hot 100 chart in their release year, and a list of song names that did not make it for the same artists, ensuring a real-world distribution of both categories
* Downloaded each song's audio, extracted the chorus section, and converted it into various statistical features about the chorus audio descriptors, to finally obtain the dataset
* Visualized the dataset for exploratory data analysis to identify any necessary preprocessing steps, which were identified to be normal quantile transformation, standard scaling, and PCA transformation
* Applied the preprocessing steps to the dataset to observe how each handles the data
* Selected f1-score as the performance metric to maximize while testing multiple models, driven by the unbalanced dataset and the business goals, in order to gain insights into the best-performing model for the dataset, which appeared to be the Random Forest model, then fine-tuned it resulting in an F1 score of 60% and an accuracy of 85%
* Utilized raw data to construct a trained pipeline that incorporated preidentified preprocessing steps and the best model found, to provide predictions given raw song data samples
* Implemented a specific module (library) with the necessary functions to fetch songs from different given sources, extract their chorus statistical audio features, and provide predictions using the pipeline
* Implemented the back-end functionalities using the module, to introduce the following features:
  * Providing predictions for songs given their YouTube links
  * Providing predictions for songs given their Spotify links
  * Providing predictions for songs by uploading the audio file
  * Displaying predictions for recently released songs (updated periodically)
* Designed the front-end to be visually appealing, user-friendly, and intuitive


# Requirements
`python 3.9`
`pandas 1.5.3`
`numpy  1.23.1`
`Flask  2.2.5`
`librosa 0.10.0.post2`
`scipy  1.11.1`
`yt-dlp 2023.7.6`
`youtube-search 2.1.2`
`spotipy 2.23.0`
`datetime`
`scikit-learn 1.2.2`
`pychorus  0.1`
`pickle`

# Execution
* Locate `app.py` and run the following command:
```
python app.py
```
* Access the application through web browser by entering the address you will be provided

# Demonstration
#### [Google drive link](https://drive.google.com/file/d/181MsBU224xY8jPepnMWDMKwGZwOOnzo6/view?usp=sharing)


![image](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/c0c8a700-cdb5-4faf-ad01-09e806963960)

![image](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/37f370fe-e48f-4a54-9de8-e850df766e8b)

![image](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/111e811c-a6de-476d-97a4-af659f7adc0b)

![image](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/e1547fde-26d1-4d88-8e57-ce4380c01021)

![image](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/781f1026-d6bb-4480-9f03-da055be396a9)

![image](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/4ef80f30-85df-49bb-9488-f513a24aab9b)

![image](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/a146f64b-ebac-4742-9b3b-32ece1fd7688)

![image](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/93dabc5a-2059-4769-bf51-00102c645018)

![image](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/46ca09f4-a913-4a4d-9dfa-dbfedef6e2a3)

![aaaaa (1)](https://github.com/GalaluddinOwais/Hot-100-or-Not/assets/111979327/3a5f2cb5-ceaf-422d-b85e-6eb7905467dc)

