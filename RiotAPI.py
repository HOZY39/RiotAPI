import time

import requests
import json
import urllib.parse

key='RiotAPIkey'

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

####################             Info about Live Game             ###############################
def GetLiveGameInfo(id):
    LiveGameJSON = requests.get('https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/'+id+'?api_key='+key)
    return LiveGameJSON.json()

####################             Info about Summoner             ###############################
def SummonerInfoNameTag(name, tag):
    Nick = urllib.parse.quote(name)
    puuid = requests.get('https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'+Nick+'/'+tag+'?api_key='+key)
    return SummonerInfoPuuId(puuid.json()["puuid"])

def SummonerInfoSummonerId(id):
    try: PlayerInfo = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/'+id+'?api_key=' + key)
    except:
        time.sleep(121)
        PlayerInfo = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/' + id + '?api_key=' + key)
    return PlayerInfo.json()

def SummonerInfoPuuId(puuid):
    PlayerInfo = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/'+puuid+'?api_key=' + key)
    return PlayerInfo.json()
####################             Info about Account             ###############################
def AccountInfoPuuId(puuid):
    try:
        PlayerInfo = requests.get('https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/'+puuid+'?api_key=' + key)
        test = PlayerInfo.json()['tagLine']
    except:
        time.sleep(121)
        PlayerInfo = requests.get('https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/' + puuid + '?api_key=' + key)
    return PlayerInfo.json()

####################             Info about Rank             ###############################
def RankInfo(id):
    try: RankInfo = requests.get('https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+id+'?api_key='+key)
    except:
        time.sleep(121)
        RankInfo = requests.get('https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + id + '?api_key=' + key)
    try:
        a = RankInfo.json()[0]
        if a['queueType'] != 'RANKED_SOLO_5x5':
            a = RankInfo.json()[1]
        return a
    except IndexError as e:
        return "UNKNOWN"
    except KeyError as er:
        return RankInfo(id)

####################             Challenger             ###############################
def PplChall():
    try: PplInChall = requests.get('https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key='+key)
    except:
        time.sleep(121)
        PplInChall = requests.get('https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=' + key)
    return PplInChall.json()["entries"]

####################             Match_History             ###############################
def MatchHistory(puuid):
    try:
        MatchHistoryIds = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid+'/ids?queue=420&start=0&count=20&api_key='+key)
        test = MatchHistoryIds.json()[0][0]
    except:
        time.sleep(121)
        MatchHistoryIds = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?queue=420&start=0&count=20&api_key=' + key)
    return MatchHistoryIds.json()

####################             Match by match id            ###############################
def MatchData(matchid):
    try:
        MatchData = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/"+matchid+"?api_key="+key)
        test = MatchData.json()['info']
    except:
        time.sleep(121)
        MatchData = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/"+matchid+"?api_key="+key)
    return MatchData.json()

####################             Match timeline            ###############################
def MatchTimeLine(matchid):
    try: timeline = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/'+matchid+'/timeline?api_key='+key)
    except:
        time.sleep(121)
        timeline = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/' + matchid + '/timeline?api_key=' + key)
    return timeline.json()