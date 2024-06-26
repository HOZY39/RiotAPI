import time
import math
import requests
import json
from RiotAPI import *
from MySQLManager import *
from GetChallPpl import *
from Classes import *

def PrintPlayersInGame(name, tag):
    CurrentGame = LiveMatch(**GetLiveGameInfo(SummonerInfoNameTag(name,tag)['id']))
    print(SummonerInfoNameTag(name,tag)['id'])
    try:
        CurrentGame = LiveMatch(**GetLiveGameInfo(SummonerInfoNameTag(name,tag)['id']))
    except:
        print("Something went wrong! Can't show players in " + name + "'s game.")
        return
    for i in range(5):
        print(CurrentGame.participants[i]['summonerName'], '    ',CurrentGame.participants[i+5]['summonerName'])

with open('dragontail-14.3.1/14.3.1/data/en_US/item.json') as plik:
    DaneItem = json.load(plik)

with open('dragontail-14.3.1/14.3.1/data/en_US/runesReforged.json') as plik:
    DaneRunes = json.load(plik)

def ItemsTimeLine(matchid):
    timeline = MatchTimeLine(matchid)
    #print(len(timeline['info']['frames']))
    buggedElixir = False
    ItemyKoniec = []
    ItemyKupione = []
    ItemyKupioneTimeStamp = []
    #print(len(timeline['info']['frames']))
    for i in range(len(timeline['info']['frames'])):
        #print(timeline['info']['frames'][i]['events'][0])
        for j in range(len(timeline['info']['frames'][i]['events'])):
            try:
                player = timeline['info']['frames'][i]['events'][j]['participantId']
                if str(player)=='4':
                    if timeline['info']['frames'][i]['events'][j]['type'] == 'ITEM_PURCHASED' and not buggedElixir:
                        itemBought = timeline['info']['frames'][i]['events'][j]['itemId']
                        timeStamp = math.ceil(int(timeline['info']['frames'][i]['events'][j]['timestamp'])/60000)
                        ItemyKoniec.append(itemBought)
                        ItemyKupione.append(itemBought)
                        ItemyKupioneTimeStamp.append(timeStamp)
                        buggedElixir = False
                    elif timeline['info']['frames'][i]['events'][j]['type'] == 'ITEM_UNDO':
                        ItemyKoniec.pop()
                        ItemyKupione.pop()
                        ItemyKupioneTimeStamp.pop()
                        buggedElixir = False
                    elif timeline['info']['frames'][i]['events'][j]['type'] == 'ITEM_DESTROYED':
                        try: ItemyKoniec.remove(timeline['info']['frames'][i]['events'][j]["itemId"])
                        except: pass #print(timeline['info']['frames'][i]['events'][j]["itemId"])

                    elif timeline['info']['frames'][i]['events'][j]['type'] == 'ITEM_SOLD':
                        ItemyKoniec.remove(timeline['info']['frames'][i]['events'][j]["itemId"])
                        #print(timeline['info']['frames'][i]['events'][j]['type'])
                        buggedElixir = False
                    else:
                        buggedElixir = False
                    #print(player, DaneItem['data'][str(itemBought)]['name'])
            except:
                pass
    return ItemyKupione, ItemyKupioneTimeStamp


def AddChampBuildToDB(matchid):
    MyCursor.execute("SELECT * FROM champ_build WHERE gameID = %(gameID)s LIMIT 1", {"gameID": matchid[5:]})
    IfExist = MyCursor.fetchall()
    try:
        test = len(IfExist[0])
        return
    except: pass

    #Get match data from match id
    RawMatchData = MatchData(matchid)['info']
    try: GameData = GameStatistics(**RawMatchData)
    except TypeError as e:
        return
    #FixedPatch = ".".join(patch[:2])
    #print(".".join(gra["info"]["gameVersion"].split(".")[:2]))

    #Get participants info
    for i in range(1, 11):
        #print(i)
        participant = "participant" + str(i)
        participant_i = getattr(GameData, participant)

        # Build
        # Itemy
        items = []
        for j in range(7):
            #items.append(player["item"+str(i)])
            item = "item" + str(j)
            item_i = getattr(participant_i, item)
            items.append(item_i)

        Player = Summoner(**SummonerInfoSummonerId(participant_i.summonerId))
        try:
            Account = AccountInfoPuuId(Player.puuid)
            Rank = RankInfo(Player.id)
            #print(Rank['tier'])
            MyCursor.execute(SQLAddUpdatePlayers,
                             {'puuid': Player.puuid, 'name': Player.name, 'accountId': Player.accountId,
                              'id': Player.id, 'tag': Account['tagLine'], 'level': Player.summonerLevel,
                              'profile_icon': Player.profileIconId,
                              'rankSolo': Rank['rank'], 'tierSolo': Rank['tier'], 'lpSolo': Rank['leaguePoints'],
                              'winSolo': Rank['wins'],
                              'loseSolo': Rank['losses']})
            mydb.commit()
        except Exception as e:
            print(e+"HALOO")
            return

        try:
            ItemsHistory, ItemsTimeStamps = ItemsTimeLine(matchid)

            ItemsName = ['item' + str(k) for k in range(60)]
            for l in range(60-len(ItemsHistory)):
                ItemsHistory.append(0)

            TimeStampsName = ['item' + str(k) + 'TimeStamp' for k in range(60)]
            for l in range(60-len(ItemsTimeStamps)):
                ItemsTimeStamps.append(0)
            ItemsDict = dict(zip(ItemsName, ItemsHistory))
            TimeStampDict = dict(zip(TimeStampsName, ItemsTimeStamps))
            dataTimeStamp = {**ItemsDict, **TimeStampDict}
            #print(dataTimeStamp)
            MyCursor.execute(SQLAddItemTimeStamp, dataTimeStamp)
            mydb.commit()

            MyCursor.execute(SQLGetLastIdTimeStamp)
            TimeStampId = MyCursor.fetchall()[0][0]
            data = {
                "endOfGameResult": GameData.endOfGameResult,
                "gameDuration": GameData.gameDuration,
                "gameCreation": GameData.gameCreation,
                "gameEndTimestamp": GameData.gameEndTimestamp,
                "gameMode": GameData.gameMode,
                "gameId": GameData.gameId,
                "gameStartTimestamp": GameData.gameStartTimestamp,
                "gameType": GameData.gameType,
                "gameVersion": GameData.gameVersion,
                "mapId": GameData.mapId,
                "platformId": GameData.platformId,
                "queueId": GameData.queueId,
                "tournamentCode": GameData.tournamentCode,

                "allInPings": participant_i.allInPings,
                "assistMePings": participant_i.assistMePings,
                "assists": participant_i.assists,
                "baronKills": participant_i.baronKills,
                "basicPings": participant_i.basicPings,
                "bountyLevel": participant_i.bountyLevel,

                "12AssistStreakCount": participant_i.challenges.assistStreakCount,
                "abilityUses": participant_i.challenges.abilityUses,
                "acesBefore15Minutes": participant_i.challenges.acesBefore15Minutes,
                "alliedJungleMonsterKills": participant_i.challenges.alliedJungleMonsterKills,
                "baronTakedowns": participant_i.challenges.baronTakedowns,
                "blastConeOppositeOpponentCount": participant_i.challenges.blastConeOppositeOpponentCount,
                "bountyGold": participant_i.challenges.bountyGold,
                "buffsStolen": participant_i.challenges.buffsStolen,
                "completeSupportQuestInTime": participant_i.challenges.completeSupportQuestInTime,
                "controlWardTimeCoverageInRiverOrEnemyHalf": participant_i.challenges.controlWardTimeCoverageInRiverOrEnemyHalf,
                "controlWardsPlaced": participant_i.challenges.controlWardsPlaced,
                "damagePerMinute": participant_i.challenges.damagePerMinute,
                "damageTakenOnTeamPercentage": participant_i.challenges.damageTakenOnTeamPercentage,
                "dancedWithRiftHerald": participant_i.challenges.dancedWithRiftHerald,
                "deathsByEnemyChamps": participant_i.challenges.deathsByEnemyChamps,
                "dodgeSkillShotsSmallWindow": participant_i.challenges.dodgeSkillShotsSmallWindow,
                "doubleAces": participant_i.challenges.doubleAces,
                "dragonTakedowns": participant_i.challenges.dragonTakedowns,
                "earliestBaron": participant_i.challenges.earliestBaron,
                "earlyLaningPhaseGoldExpAdvantage": participant_i.challenges.earlyLaningPhaseGoldExpAdvantage,
                "effectiveHealAndShielding": participant_i.challenges.effectiveHealAndShielding,
                "elderDragonKillsWithOpposingSoul": participant_i.challenges.elderDragonKillsWithOpposingSoul,
                "elderDragonMultikills": participant_i.challenges.elderDragonMultikills,
                "enemyChampionImmobilizations": participant_i.challenges.enemyChampionImmobilizations,
                "enemyJungleMonsterKills": participant_i.challenges.enemyJungleMonsterKills,
                "epicMonsterKillsNearEnemyJungler": participant_i.challenges.epicMonsterKillsNearEnemyJungler,
                "epicMonsterKillsWithin30SecondsOfSpawn": participant_i.challenges.epicMonsterKillsWithin30SecondsOfSpawn,
                "epicMonsterSteals": participant_i.challenges.epicMonsterSteals,
                "epicMonsterStolenWithoutSmite": participant_i.challenges.epicMonsterStolenWithoutSmite,
                "firstTurretKilled": participant_i.challenges.firstTurretKilled,
                "firstTurretKilledTime": participant_i.challenges.firstTurretKilledTime,
                "flawlessAces": participant_i.challenges.flawlessAces,
                "fullTeamTakedown": participant_i.challenges.fullTeamTakedown,
                "gameLength": participant_i.challenges.gameLength,
                "getTakedownsInAllLanesEarlyJungleAsLaner": participant_i.challenges.getTakedownsInAllLanesEarlyJungleAsLaner,
                "goldPerMinute": participant_i.challenges.goldPerMinute,
                "hadOpenNexus": participant_i.challenges.hadOpenNexus,
                "immobilizeAndKillWithAlly": participant_i.challenges.immobilizeAndKillWithAlly,
                "initialBuffCount": participant_i.challenges.initialBuffCount,
                "initialCrabCount": participant_i.challenges.initialCrabCount,
                "jungleCsBefore10Minutes": participant_i.challenges.jungleCsBefore10Minutes,
                "junglerTakedownsNearDamagedEpicMonster": participant_i.challenges.junglerTakedownsNearDamagedEpicMonster,
                "kTurretsDestroyedBeforePlatesFall": participant_i.challenges.kTurretsDestroyedBeforePlatesFall,
                "kda": participant_i.challenges.kda,
                "killAfterHiddenWithAlly": participant_i.challenges.killAfterHiddenWithAlly,
                "killParticipation": participant_i.challenges.killParticipation,
                "killedChampTookFullTeamDamageSurvived": participant_i.challenges.killedChampTookFullTeamDamageSurvived,
                "killingSpreesChallenges": participant_i.challenges.killingSprees,
                "killsNearEnemyTurret": participant_i.challenges.killsNearEnemyTurret,
                "killsOnOtherLanesEarlyJungleAsLaner": participant_i.challenges.killsOnOtherLanesEarlyJungleAsLaner,
                "killsOnRecentlyHealedByAramPack": participant_i.challenges.killsOnRecentlyHealedByAramPack,
                "killsUnderOwnTurret": participant_i.challenges.killsUnderOwnTurret,
                "killsWithHelpFromEpicMonster": participant_i.challenges.killsWithHelpFromEpicMonster,
                "knockEnemyIntoTeamAndKill": participant_i.challenges.knockEnemyIntoTeamAndKill,
                "landSkillShotsEarlyGame": participant_i.challenges.landSkillShotsEarlyGame,
                "laneMinionsFirst10Minutes": participant_i.challenges.laneMinionsFirst10Minutes,
                "laningPhaseGoldExpAdvantage": participant_i.challenges.laningPhaseGoldExpAdvantage,
                "legendaryCount": participant_i.challenges.legendaryCount,
                "lostAnInhibitor": participant_i.challenges.lostAnInhibitor,
                "maxCsAdvantageOnLaneOpponent": participant_i.challenges.maxCsAdvantageOnLaneOpponent,
                "maxKillDeficit": participant_i.challenges.maxKillDeficit,
                "maxLevelLeadLaneOpponent": participant_i.challenges.maxLevelLeadLaneOpponent,
                "mejaisFullStackInTime": participant_i.challenges.mejaisFullStackInTime,
                "moreEnemyJungleThanOpponent": participant_i.challenges.moreEnemyJungleThanOpponent,
                "multiKillOneSpell": participant_i.challenges.multiKillOneSpell,
                "multiTurretRiftHeraldCount": participant_i.challenges.multiTurretRiftHeraldCount,
                "multikills": participant_i.challenges.multikills,
                "multikillsAfterAggressiveFlash": participant_i.challenges.multikillsAfterAggressiveFlash,
                "outerTurretExecutesBefore10Minutes": participant_i.challenges.outerTurretExecutesBefore10Minutes,
                "outnumberedKills": participant_i.challenges.outnumberedKills,
                "outnumberedNexusKill": participant_i.challenges.outnumberedNexusKill,
                "perfectDragonSoulsTaken": participant_i.challenges.perfectDragonSoulsTaken,
                "perfectGame": participant_i.challenges.perfectGame,
                "pickKillWithAlly": participant_i.challenges.pickKillWithAlly,
                "playedChampSelectPosition": participant_i.challenges.playedChampSelectPosition,
                "poroExplosions": participant_i.challenges.poroExplosions,
                "quickCleanse": participant_i.challenges.quickCleanse,
                "quickFirstTurret": participant_i.challenges.quickFirstTurret,
                "quickSoloKills": participant_i.challenges.quickSoloKills,
                "riftHeraldTakedowns": participant_i.challenges.riftHeraldTakedowns,
                "saveAllyFromDeath": participant_i.challenges.saveAllyFromDeath,
                "scuttleCrabKills": participant_i.challenges.scuttleCrabKills,
                "skillshotsDodged": participant_i.challenges.skillshotsDodged,
                "skillshotsHit": participant_i.challenges.skillshotsHit,
                "snowballsHit": participant_i.challenges.snowballsHit,
                "soloBaronKills": participant_i.challenges.soloBaronKills,
                "soloKills": participant_i.challenges.soloKills,
                "stealthWardsPlaced": participant_i.challenges.stealthWardsPlaced,
                "survivedSingleDigitHpCount": participant_i.challenges.survivedSingleDigitHpCount,
                "survivedThreeImmobilizesInFight": participant_i.challenges.survivedThreeImmobilizesInFight,
                "takedownOnFirstTurret": participant_i.challenges.takedownOnFirstTurret,
                "takedowns": participant_i.challenges.takedowns,
                "takedownsAfterGainingLevelAdvantage": participant_i.challenges.takedownsAfterGainingLevelAdvantage,
                "takedownsBeforeJungleMinionSpawn": participant_i.challenges.takedownsBeforeJungleMinionSpawn,
                "takedownsFirstXMinutes": participant_i.challenges.takedownsFirstXMinutes,
                "takedownsInAlcove": participant_i.challenges.takedownsInAlcove,
                "takedownsInEnemyFountain": participant_i.challenges.takedownsInEnemyFountain,
                "teamBaronKills": participant_i.challenges.teamBaronKills,
                "teamDamagePercentage": participant_i.challenges.teamDamagePercentage,
                "teamElderDragonKills": participant_i.challenges.teamElderDragonKills,
                "teamRiftHeraldKills": participant_i.challenges.teamRiftHeraldKills,
                "tookLargeDamageSurvived": participant_i.challenges.tookLargeDamageSurvived,
                "turretPlatesTaken": participant_i.challenges.turretPlatesTaken,
                "turretTakedownsChallenges": participant_i.challenges.turretTakedowns,
                "turretsTakenWithRiftHerald": participant_i.challenges.turretsTakenWithRiftHerald,
                "twentyMinionsIn3SecondsCount": participant_i.challenges.twentyMinionsIn3SecondsCount,
                "twoWardsOneSweeperCount": participant_i.challenges.twoWardsOneSweeperCount,
                "unseenRecalls": participant_i.challenges.unseenRecalls,
                "visionScoreAdvantageLaneOpponent": participant_i.challenges.visionScoreAdvantageLaneOpponent,
                "visionScorePerMinute": participant_i.challenges.visionScorePerMinute,
                "wardTakedowns": participant_i.challenges.wardTakedowns,
                "wardTakedownsBefore20M": participant_i.challenges.wardTakedownsBefore20M,
                "wardsGuarded": participant_i.challenges.wardsGuarded,

                "champExperience": participant_i.champExperience,
                "champLevel": participant_i.champLevel,
                "championId": participant_i.championId,
                "championName": participant_i.championName,
                "championTransform": participant_i.championTransform,
                "commandPings": participant_i.commandPings,
                "consumablesPurchased": participant_i.consumablesPurchased,
                "damageDealtToBuildings": participant_i.damageDealtToBuildings,
                "damageDealtToObjectives": participant_i.damageDealtToObjectives,
                "damageDealtToTurrets": participant_i.damageDealtToTurrets,
                "damageSelfMitigated": participant_i.damageSelfMitigated,
                "dangerPings": participant_i.dangerPings,
                "deaths": participant_i.deaths,
                "detectorWardsPlaced": participant_i.detectorWardsPlaced,
                "doubleKills": participant_i.doubleKills,
                "dragonKills": participant_i.dragonKills,
                "eligibleForProgression": participant_i.eligibleForProgression,
                "enemyMissingPings": participant_i.enemyMissingPings,
                "enemyVisionPings": participant_i.enemyVisionPings,
                "firstBloodAssist": participant_i.firstBloodAssist,
                "firstBloodKill": participant_i.firstBloodKill,
                "firstTowerAssist": participant_i.firstTowerAssist,
                "firstTowerKill": participant_i.firstTowerKill,
                "gameEndedInEarlySurrender": participant_i.gameEndedInEarlySurrender,
                "gameEndedInSurrender": participant_i.gameEndedInSurrender,
                "getBackPings": participant_i.getBackPings,
                "goldEarned": participant_i.goldEarned,
                "goldSpent": participant_i.goldSpent,
                "holdPings": participant_i.holdPings,
                "individualPosition": participant_i.individualPosition,
                "inhibitorKills": participant_i.inhibitorKills,
                "inhibitorTakedowns": participant_i.inhibitorTakedowns,
                "inhibitorsLost": participant_i.inhibitorsLost,
                "item0": participant_i.item0,
                "item1": participant_i.item1,
                "item2": participant_i.item2,
                "item3": participant_i.item3,
                "item4": participant_i.item4,
                "item5": participant_i.item5,
                "item6": participant_i.item6,
                "itemsPurchased": participant_i.itemsPurchased,
                "killingSprees": participant_i.killingSprees,
                "kills": participant_i.kills,
                "lane": participant_i.lane,
                "largestCriticalStrike": participant_i.largestCriticalStrike,
                "largestKillingSpree": participant_i.largestKillingSpree,
                "largestMultiKill": participant_i.largestMultiKill,
                "longestTimeSpentLiving": participant_i.longestTimeSpentLiving,
                "magicDamageDealt": participant_i.magicDamageDealt,
                "magicDamageDealtToChampions": participant_i.magicDamageDealtToChampions,
                "magicDamageTaken": participant_i.magicDamageTaken,
                "needVisionPings": participant_i.needVisionPings,
                "neutralMinionsKilled": participant_i.neutralMinionsKilled,
                "nexusKills": participant_i.nexusKills,
                "nexusLost": participant_i.nexusLost,
                "nexusTakedowns": participant_i.nexusTakedowns,
                "objectivesStolen": participant_i.objectivesStolen,
                "objectivesStolenAssists": participant_i.objectivesStolenAssists,
                "onMyWayPings": participant_i.onMyWayPings,
                "participantId": participant_i.participantId,
                "pentaKills": participant_i.pentaKills,
                "physicalDamageDealt": participant_i.physicalDamageDealt,
                "physicalDamageDealtToChampions": participant_i.physicalDamageDealtToChampions,
                "physicalDamageTaken": participant_i.physicalDamageTaken,
                "placement": participant_i.placement,
                "playerAugment1": participant_i.playerAugment1,
                "playerAugment2": participant_i.playerAugment2,
                "playerAugment3": participant_i.playerAugment3,
                "playerAugment4": participant_i.playerAugment4,
                "playerScore0": participant_i.playerScore0,
                "playerScore1": participant_i.playerScore1,
                "playerScore10": participant_i.playerScore10,
                "playerScore11": participant_i.playerScore11,
                "playerScore2": participant_i.playerScore2,
                "playerScore3": participant_i.playerScore3,
                "playerScore4": participant_i.playerScore4,
                "playerScore5": participant_i.playerScore5,
                "playerScore6": participant_i.playerScore6,
                "playerScore7": participant_i.playerScore7,
                "playerScore8": participant_i.playerScore8,
                "playerScore9": participant_i.playerScore9,
                "playerSubteamId": participant_i.playerSubteamId,
                "profileIcon": participant_i.profileIcon,
                "pushPings": participant_i.pushPings,
                "puuid": participant_i.puuid,
                "quadraKills": participant_i.quadraKills,
                "riotIdGameName": participant_i.riotIdGameName,
                "riotIdTagline": participant_i.riotIdTagline,
                "role": participant_i.role,
                "sightWardsBoughtInGame": participant_i.sightWardsBoughtInGame,
                "spell1Casts": participant_i.spell1Casts,
                "spell2Casts": participant_i.spell2Casts,
                "spell3Casts": participant_i.spell3Casts,
                "spell4Casts": participant_i.spell4Casts,
                "subteamPlacement": participant_i.subteamPlacement,
                "summoner1Casts": participant_i.summoner1Casts,
                "summoner1Id": participant_i.summoner1Id,
                "summoner2Casts": participant_i.summoner2Casts,
                "summoner2Id": participant_i.summoner2Id,
                "summonerId": participant_i.summonerId,
                "summonerLevel": participant_i.summonerLevel,
                "summonerName": participant_i.summonerName,
                "teamEarlySurrendered": participant_i.teamEarlySurrendered,
                "teamId": participant_i.teamId,
                "teamPosition": participant_i.teamPosition,
                "timeCCingOthers": participant_i.timeCCingOthers,
                "timePlayed": participant_i.timePlayed,
                "totalAllyJungleMinionsKilled": participant_i.totalAllyJungleMinionsKilled,
                "totalDamageDealt": participant_i.totalDamageDealt,
                "totalDamageDealtToChampions": participant_i.totalDamageDealtToChampions,
                "totalDamageShieldedOnTeammates": participant_i.totalDamageShieldedOnTeammates,
                "totalDamageTaken": participant_i.totalDamageTaken,
                "totalEnemyJungleMinionsKilled": participant_i.totalEnemyJungleMinionsKilled,
                "totalHeal": participant_i.totalHeal,
                "totalHealsOnTeammates": participant_i.totalHealsOnTeammates,
                "totalMinionsKilled": participant_i.totalMinionsKilled,
                "totalTimeCCDealt": participant_i.totalTimeCCDealt,
                "totalTimeSpentDead": participant_i.totalTimeSpentDead,
                "totalUnitsHealed": participant_i.totalUnitsHealed,
                "tripleKills": participant_i.tripleKills,
                "trueDamageDealt": participant_i.trueDamageDealt,
                "trueDamageDealtToChampions": participant_i.trueDamageDealtToChampions,
                "trueDamageTaken": participant_i.trueDamageTaken,
                "turretKills": participant_i.turretKills,
                "turretTakedowns": participant_i.turretTakedowns,
                "turretsLost": participant_i.turretsLost,
                "unrealKills": participant_i.unrealKills,
                "visionClearedPings": participant_i.visionClearedPings,
                "visionScore": participant_i.visionScore,
                "visionWardsBoughtInGame": participant_i.visionWardsBoughtInGame,
                "wardsKilled": participant_i.wardsKilled,
                "wardsPlaced": participant_i.wardsPlaced,
                "win": participant_i.win,

                
                "main_rune1_id": participant_i.perks.mainRune1,
                "main_rune2_id": participant_i.perks.mainRune2,
                "main_rune3_id": participant_i.perks.mainRune3,
                "main_rune4_id": participant_i.perks.mainRune4,
                "side_rune1_id": participant_i.perks.subRune1,
                "side_rune2_id": participant_i.perks.subRune2,
                "offenseRune": participant_i.perks.offense,
                "flexRune": participant_i.perks.flex,
                "defenseRune": participant_i.perks.defense,
                "mainStyle": participant_i.perks.mainStyle,
                "subStyle": participant_i.perks.subStyle,
                "TimeStampId": TimeStampId
            }
            MyCursor.execute(SQLAddChampionBuild, data)
            mydb.commit()
            #print("NOWY BUILD")
        except:
            #print("COS POSZLO NIE TAK")
            return
    print("END")

AddChallToDB()
MyCursor.execute("SELECT puuid FROM players")
ListaGraczyChall = MyCursor.fetchall()
try:
    Historia = MatchHistory(ListaGraczyChall[0][0])
except:
    AddChallToDB()
#print(len(ListaGraczyChall))
for i in range(len(ListaGraczyChall)):
    Historia = MatchHistory(ListaGraczyChall[i][0])
    #print(Historia)
    print("NOWY GRACZ", i)
    for j in range(20):
        #print(Historia[j])
        try:
            print("NOWY MECZ", j)
            AddChampBuildToDB(Historia[j])
        except TypeError as e:
            print(e+"HALO")
            AddChampBuildToDB(Historia[j])
