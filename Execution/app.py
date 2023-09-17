from billpy import *


from flask import Flask, render_template, request

app = Flask(__name__)


try:
    recent_predictions_dataframe = pickle.load(open('dataframe_to_render.pkl','rb'))
except:
    recent_predictions_dataframe = pd.DataFrame({'Song':[],'Youtube_link':[],'Prediction':[]})
    

@app.route('/')
def index():
        return render_template('index.html',dataframe=recent_predictions_dataframe)

@app.route('/recent_songs')
def index_recent_songs_up_to_date():
    global recent_predictions_dataframe

    if (datetime.now() - pickle.load(open('last_update_time.pkl','rb'))).days > 10: 
        try:
            recent_predictions_dict = {'Song':[],'Youtube_link':[],'Prediction':[]}
            new_releases = get_latest_releases(10)
            for song_name in new_releases:
                try:
                    try:
                        youtube_link=get_video_youtube_link_by_name(song_name)
                        download_audio_from_youtube(youtube_link)
                        result = classify_song_file_in_same_dir()
                    except ValueError as ve:
                        if 'Audio duration exceeds 8 minutes' == str(ve) or 'No chorus detected' == str(ve):
                            recent_predictions_dict['Song'].append(song_name)
                            recent_predictions_dict['Youtube_link'].append(youtube_link)
                            recent_predictions_dict['Prediction'].append(str(ve))
                            continue
                        else:
                            recent_predictions_dict['Song'].append(song_name)
                            recent_predictions_dict['Youtube_link'].append(youtube_link)
                            recent_predictions_dict['Prediction'].append('something went wrong')
                            continue
                except:
                    recent_predictions_dict['Song'].append(song_name)
                    recent_predictions_dict['Youtube_link'].append(youtube_link)
                    recent_predictions_dict['Prediction'].append('something went wrong')
                    continue
                    
                recent_predictions_dict['Song'].append(song_name)
                recent_predictions_dict['Youtube_link'].append(youtube_link)
                recent_predictions_dict['Prediction'].append(result)
        except:
            return render_template('index_recent_songs_up_to_date.html',dataframe=recent_predictions_dataframe)
            
        recent_predictions_dataframe = pd.DataFrame(recent_predictions_dict)
        pickle.dump(recent_predictions_dataframe,open('dataframe_to_render.pkl','wb'))
        pickle.dump(datetime.now(),open('last_update_time.pkl','wb'))
        return render_template('index_recent_songs_up_to_date.html',dataframe=recent_predictions_dataframe)
    else:
        return render_template('index_recent_songs_up_to_date.html',dataframe=recent_predictions_dataframe)


@app.route('/predict_youtube', methods=['POST'])
def predict_youtube():
        link = request.form['youtube_link']
        try:
            try:
                download_audio_from_youtube(link)
                result = classify_song_file_in_same_dir()
            except ValueError as ve:
                if 'Audio duration exceeds 8 minutes' == str(ve) or 'No chorus detected' == str(ve) or 'Invalid YouTube link' == str(ve):
                    result = str(ve)
                else:
                    result = 'something went wrong'
        except:
            result = 'something went wrong'
        
        return render_template('result_youtube.html',result=result,link=link,dataframe=recent_predictions_dataframe)

@app.route('/predict_spotify', methods=['POST'])
def predict_spotify():
        spotify_link = request.form['spotify_link']
        try:
            try:
                name = get_song_name_by_spotify_link(spotify_link.split('?')[0])
                link = get_video_youtube_link_by_name(name)
                download_audio_from_youtube(link)
                result = classify_song_file_in_same_dir()

            except ValueError as ve:
                if 'Audio duration exceeds 8 minutes' == str(ve) or 'No chorus detected' == str(ve) or 'Invalid Spotify link' == str(ve):
                    result = str(ve)
                    link = spotify_link
                
                else:
                    result = 'something went wrong'
                    link = spotify_link
        except:
            result = 'something went wrong'
            link = spotify_link

        return render_template('result_spotify.html', result=result,link = link,dataframe=recent_predictions_dataframe)






@app.route('/upload_song', methods=['POST'])
def upload_song():
         file = request.files["audio_file"]
         try:
            try:
                if file.filename == '':
                    return render_template('result_upload.html', result='No File Selected',audio_file=file.filename,dataframe=recent_predictions_dataframe)

                if file.filename.split('.')[-1].lower() not in ['mp3', 'wav', 'ogg','opus','m4a']:
                    return render_template('result_upload.html', result='Invalid File Format',audio_file=file.filename,dataframe=recent_predictions_dataframe)
                
                file.save('song.opus')
                result = classify_song_file_in_same_dir()
                
                
            except ValueError as ve:
                if 'Audio duration exceeds 8 minutes' == str(ve) or 'No chorus detected' == str(ve):
                    result = str(ve)
                else:
                    result = 'something went wrong'    
         except:
             result = 'something went wrong'
        
         return render_template('result_upload.html', result=result,audio_file=file.filename,dataframe=recent_predictions_dataframe)

if __name__ == '__main__':
    app.run(debug=True)
