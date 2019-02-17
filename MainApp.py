from flask import Flask, render_template, request, url_for, redirect
from statistics import mean, stdev, median, median_high, median_low, mode
from loadcell import  *
from youtube_pl import *

app = Flask(__name__)

@app.errorhandler(404)
def err404(error):
    return(render_template('err404.html'))

#HOME PAGE
#----------------
@app.route("/")
def homePage():
    return(render_template('home.html'))
  
#LOADCELLS PAGE
#----------------------
@app.route("/on;ine-loadcell-calculator",  methods = ['GET', 'POST'])
def LCinputPage():    
    if (request.method == 'POST'):        
        if "calcWeight" in request.form:
            formDict = {'formFlag' :  "calcWeight",
                                   'rateWeight': float(request.form.get('RateWeight')),
                                   'excitVolt' : float(request.form.get('ExcitVolt')),
                                   'sensParam' : float(request.form.get('SensParam')),
                                   'measVolt' : float(request.form.get('MeasVolt'))}
            formDict ['LCw']  =  LoadCell(formDict['sensParam'],  formDict['rateWeight'],  formDict['excitVolt']).getWeightFromVolt(formDict['measVolt'])                                   
            return(render_template('LCOutput.html', **formDict))                 
        elif "calcVolts" in request.form:
            formDict = {'formFlag' :  "calcVolts",
                                   'rateWeight': float(request.form.get('RateWeight')),
                                   'excitVolt' : float(request.form.get('ExcitVolt')),
                                   'sensParam' : float(request.form.get('SensParam')),
                                   'measWeight' : float(request.form.get('MeasWeight'))}
            formDict['LCv'] =  LoadCell(formDict['sensParam'],  formDict['rateWeight'],  formDict['excitVolt']).getVoltFromWeight(formDict['measWeight'])                                   
            return(render_template('LCOutput.html', **formDict))            
    else:
        return(render_template("LCInput.html"))

#DATA ANALYSIS PAGE
#----------------------------
@app.route("/online-data-analyzer",  methods = ['GET', 'POST'])
def DATAinputPage():    
    if (request.method == 'POST'):
        dataset = request.form.get('dataset')
        dataset = dataset.split(',')
        dataset = list(map(lambda k: float(k), dataset))
        def modifiedMode(xdata):
            try:
                return(mode(xdata))
            except:
                return("No multiple occurrence found")
        results = {
            'inputData' : dataset,
            'dataMean' : mean(dataset),
            'dataStandardDeviation' : stdev(dataset),
            'dataMedian' : median(dataset),
            'dataMedianHigh' : median_high(dataset),
            'dataMedianLow' : median_low(dataset),
            'dataMode' : modifiedMode(dataset)
            }
        return(render_template("DATAOutput.html",  **results, results = results))
    else:
        return(render_template("DATAInput.html"))


#YOUTUBE PLAYLISTS PAGE
#----------------------
@app.route("/youtube-data-miner",  methods = ['GET', 'POST'])
def YOUTUBEinputPage():
    if (request.method == 'POST'):
        playlist_url = request.form.get('playlist')
        playlist = youtubePlaylist(playlist_url)
        results = {
            'playlist_url' : playlist_url,
            'Playlist_title' : playlist.playlistTitle,
            'Number_of_videos' : playlist.videosQty,
            'Total_duration' : playlist.playlistDuration,
            'Average_duration' : playlist.timeAverage,
            'Durations_deviation' : playlist.timeDeviation,
            'Playlist_logo' : playlist.playlistLogo
            }
        return(render_template("PLAYLISTOutput.html", **results))
    else :
        return(render_template("PLAYLISTInput.html"))

    

if __name__ == '__main__' :
   app.run(debug = True)
