import time
from RiotAPI import *
from MySQLManager import *
from Classes import *

Challek = PplChall()
def AddChallToDB():
    for i in Challek:
        ID = (i["summonerId"], )
        MyCursor.execute("SELECT id FROM players WHERE id=%s", ID)
        InDB = MyCursor.fetchall()
        try:
            a=InDB[0][0]
        except:
            InDB=[["abcd"],["abcd"]]
        #print("wartość jaka jest w InDB: "+ InDB[0][0])
        if InDB[0][0] == ID[0]:
            print("Siema, ten zawodnik jest juz w bazie danych")
        else:
            try: Player = Summoner(**SummonerInfoSummonerId(ID[0]))
            except TypeError as e:
                print(str(e))
                if str(e) == "__init__() got an unexpected keyword argument 'status'":
                    print('halo')
                    time.sleep(121)
                    Player = Summoner(**SummonerInfoSummonerId(ID[0]))
            try: Account = AccountInfoPuuId(Player.puuid)
            except:
                time.sleep(121)
                Account = AccountInfoPuuId(Player.puuid)
            try:
                Rank = RankInfo(ID[0])
            except TypeError as e:
                time.sleep(121)
                Rank = RankInfo(ID[0])
            MyCursor.execute(SQLAddUpdatePlayers, {'puuid': Player.puuid, 'name': Player.name, 'accountId': Player.accountId,
            'id': Player.id, 'tag': Account['tagLine'], 'level': Player.summonerLevel, 'profile_icon': Player.profileIconId,
            'rankSolo': Rank['rank'], 'tierSolo': Rank['tier'], 'lpSolo': Rank['leaguePoints'], 'winSolo': Rank['wins'],
            'loseSolo': Rank['losses']})
            mydb.commit()
            print("Ziomeczek dodany do bazy")
#AddChallToDB()