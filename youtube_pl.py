from requests import get
from bs4 import BeautifulSoup
from statistics import mean, stdev

def duration(timeDuration):
    '''Normally time durations of youtube videos is in the form 'xx:xx' (mins:seconds) or 'xx_x:xx:xx' (hours:mins:seconds)
This function transforms the mentioned form to the form xx_x.xx (mins.parts of min) 
'''
    timeDuration = timeDuration.split(':')
    if len(timeDuration) == 2 :
        timeDuration_minuits = int(timeDuration[0])
        timeDuration_seconds = int(timeDuration[1])
        return(timeDuration_minuits + timeDuration_seconds/60)
    if len(timeDuration) > 2 :
        timeDuration_hours = int(timeDuration[0])
        timeDuration_minuits = int(timeDuration[1])
        timeDuration_seconds = int(timeDuration[2])
        return(timeDuration_hours*60 + timeDuration_minuits + timeDuration_seconds/60)

class youtubePlaylist :
    def __init__(self, youtube_url):
        playlistReq = get(youtube_url)
        playlistSoup = BeautifulSoup(playlistReq.content, 'html.parser')
        #-------------------------------------------------------------------------------------------------------
        videolist = playlistSoup.find_all('div', attrs = {'class' : "timestamp"}) #Extracting time durations data.
        self.videosQty = len(videolist)    #Number of videos in the playlist
        videoLengthsText = [eachvideo.string for eachvideo in videolist]        
        playlistDuration = sum(map(lambda x: duration(x), videoLengthsText)) / 60  #In hours
        self.playlistDuration = round(playlistDuration, 2)    #Total hours of playlist
        self.timeAverage = round(mean(map(lambda x: duration(x), videoLengthsText)), 2)  #Average of video durations.
        self.timeDeviation = round(stdev(map(lambda x: duration(x), videoLengthsText)), 2)   #Standard deviation of video durations.
        #-------------------------------------------------------------------------------------------------------
        listLogo = playlistSoup.findAll('div', attrs = {'class' : "pl-header-thumb"})  #Extracting playlist logo.
        self.playlistLogo = listLogo[0].img['src']
        #-------------------------------------------------------------------------------------------------------
        listTitle = playlistSoup.findAll('h1', attrs = {'class' : "pl-header-title"})  #Extracting playlist title.        
        self.playlistTitle = listTitle[0].text.strip()
        


 
