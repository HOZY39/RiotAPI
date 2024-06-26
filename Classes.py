class GameStatistics:
    def __init__(self, endOfGameResult, gameCreation, gameDuration, gameEndTimestamp, gameId, gameMode, gameName, gameStartTimestamp,
                 gameType, gameVersion, mapId, participants, platformId, queueId, teams, tournamentCode):
        self.endOfGameResult = endOfGameResult
        self.gameCreation = gameCreation
        self.gameDuration = gameDuration
        self.gameEndTimestamp = gameEndTimestamp
        self.gameId = gameId
        self.gameMode = gameMode
        self.gameName = gameName
        self.gameStartTimestamp = gameStartTimestamp
        self.gameType = gameType
        self.gameVersion = gameVersion
        self.mapId = mapId
        self.participant1 = Participants(**participants[0])
        self.participant2 = Participants(**participants[1])
        self.participant3 = Participants(**participants[2])
        self.participant4 = Participants(**participants[3])
        self.participant5 = Participants(**participants[4])
        self.participant6 = Participants(**participants[5])
        self.participant7 = Participants(**participants[6])
        self.participant8 = Participants(**participants[7])
        self.participant9 = Participants(**participants[8])
        self.participant10 = Participants(**participants[9])
        self.platformId = platformId
        self.queueId = queueId
        self.teams1 = Teams(**teams[0])
        self.teams2 = Teams(**teams[1])
        self.tournamentCode = tournamentCode

class Participants:
    def __init__(self, allInPings, assistMePings, assists, baronKills, basicPings, bountyLevel, challenges,
                  champExperience, champLevel, championId, championName, championTransform, commandPings, consumablesPurchased, damageDealtToBuildings,
                 damageDealtToObjectives, damageDealtToTurrets, damageSelfMitigated, dangerPings, deaths,
                 detectorWardsPlaced, doubleKills, dragonKills, eligibleForProgression, enemyMissingPings,
                 enemyVisionPings, firstBloodAssist, firstBloodKill, firstTowerAssist, firstTowerKill,
                 gameEndedInEarlySurrender, gameEndedInSurrender, getBackPings, goldEarned, goldSpent,
                 holdPings, individualPosition, inhibitorKills, inhibitorTakedowns, inhibitorsLost,
                 item0, item1, item2, item3, item4, item5, item6, itemsPurchased, killingSprees, kills, lane,
                 largestCriticalStrike, largestKillingSpree, largestMultiKill, longestTimeSpentLiving,
                 magicDamageDealt, magicDamageDealtToChampions, magicDamageTaken, missions, needVisionPings,
                 neutralMinionsKilled, nexusKills, nexusLost, nexusTakedowns, objectivesStolen,
                 objectivesStolenAssists, onMyWayPings, participantId, pentaKills, perks, physicalDamageDealt,
                 physicalDamageDealtToChampions, physicalDamageTaken, placement, playerAugment1,
                 playerAugment2, playerAugment3, playerAugment4, playerScore0, playerScore1, playerScore10,
                 playerScore11, playerScore2, playerScore3, playerScore4, playerScore5, playerScore6,
                 playerScore7, playerScore8, playerScore9, playerSubteamId, profileIcon, pushPings, puuid,
                 quadraKills, riotIdGameName, riotIdTagline, role, sightWardsBoughtInGame, spell1Casts,
                 spell2Casts, spell3Casts, spell4Casts, subteamPlacement, summoner1Casts, summoner1Id,
                 summoner2Casts, summoner2Id, summonerId, summonerLevel, summonerName, teamEarlySurrendered,
                 teamId, teamPosition, timeCCingOthers, timePlayed, totalAllyJungleMinionsKilled,
                 totalDamageDealt, totalDamageDealtToChampions, totalDamageShieldedOnTeammates, totalDamageTaken,
                 totalEnemyJungleMinionsKilled, totalHeal, totalHealsOnTeammates, totalMinionsKilled,
                 totalTimeCCDealt, totalTimeSpentDead, totalUnitsHealed, tripleKills, trueDamageDealt,
                 trueDamageDealtToChampions, trueDamageTaken, turretKills, turretTakedowns, turretsLost,
                 unrealKills, visionClearedPings, visionScore, visionWardsBoughtInGame, wardsKilled,
                 wardsPlaced, win,):
        self.allInPings = allInPings
        self.assistMePings = assistMePings
        self.assists = assists
        self.baronKills = baronKills
        self.basicPings = basicPings
        self.bountyLevel = bountyLevel
        self.champExperience = champExperience
        self.champLevel = champLevel
        self.championId = championId
        self.championName = championName
        self.championTransform = championTransform
        self.commandPings = commandPings
        self.consumablesPurchased = consumablesPurchased
        self.damageDealtToBuildings = damageDealtToBuildings
        self.damageDealtToObjectives = damageDealtToObjectives
        self.damageDealtToTurrets = damageDealtToTurrets
        self.damageSelfMitigated = damageSelfMitigated
        self.dangerPings = dangerPings
        self.deaths = deaths
        self.detectorWardsPlaced = detectorWardsPlaced
        self.doubleKills = doubleKills
        self.dragonKills = dragonKills
        self.eligibleForProgression = eligibleForProgression
        self.enemyMissingPings = enemyMissingPings
        self.enemyVisionPings = enemyVisionPings
        self.firstBloodAssist = firstBloodAssist
        self.firstBloodKill = firstBloodKill
        self.firstTowerAssist = firstTowerAssist
        self.firstTowerKill = firstTowerKill
        self.gameEndedInEarlySurrender = gameEndedInEarlySurrender
        self.gameEndedInSurrender = gameEndedInSurrender
        self.getBackPings = getBackPings
        self.goldEarned = goldEarned
        self.goldSpent = goldSpent
        self.holdPings = holdPings
        self.individualPosition = individualPosition
        self.inhibitorKills = inhibitorKills
        self.inhibitorTakedowns = inhibitorTakedowns
        self.inhibitorsLost = inhibitorsLost
        self.item0 = item0
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.item5 = item5
        self.item6 = item6
        self.itemsPurchased = itemsPurchased
        self.killingSprees = killingSprees
        self.kills = kills
        self.lane = lane
        self.largestCriticalStrike = largestCriticalStrike
        self.largestKillingSpree = largestKillingSpree
        self.largestMultiKill = largestMultiKill
        self.longestTimeSpentLiving = longestTimeSpentLiving
        self.magicDamageDealt = magicDamageDealt
        self.magicDamageDealtToChampions = magicDamageDealtToChampions
        self.magicDamageTaken = magicDamageTaken
        self.needVisionPings = needVisionPings
        self.neutralMinionsKilled = neutralMinionsKilled
        self.nexusKills = nexusKills
        self.nexusLost = nexusLost
        self.nexusTakedowns = nexusTakedowns
        self.objectivesStolen = objectivesStolen
        self.objectivesStolenAssists = objectivesStolenAssists
        self.onMyWayPings = onMyWayPings
        self.participantId = participantId
        self.pentaKills = pentaKills
        self.physicalDamageDealt = physicalDamageDealt
        self.physicalDamageDealtToChampions = physicalDamageDealtToChampions
        self.physicalDamageTaken = physicalDamageTaken
        self.placement = placement
        self.playerAugment1 = playerAugment1
        self.playerAugment2 = playerAugment2
        self.playerAugment3 = playerAugment3
        self.playerAugment4 = playerAugment4
        self.playerScore0 = playerScore0
        self.playerScore1 = playerScore1
        self.playerScore10 = playerScore10
        self.playerScore11 = playerScore11
        self.playerScore2 = playerScore2
        self.playerScore3 = playerScore3
        self.playerScore4 = playerScore4
        self.playerScore5 = playerScore5
        self.playerScore6 = playerScore6
        self.playerScore7 = playerScore7
        self.playerScore8 = playerScore8
        self.playerScore9 = playerScore9
        self.playerSubteamId = playerSubteamId
        self.profileIcon = profileIcon
        self.pushPings = pushPings
        self.puuid = puuid
        self.quadraKills = quadraKills
        self.riotIdGameName = riotIdGameName
        self.riotIdTagline = riotIdTagline
        self.role = role
        self.sightWardsBoughtInGame = sightWardsBoughtInGame
        self.spell1Casts = spell1Casts
        self.spell2Casts = spell2Casts
        self.spell3Casts = spell3Casts
        self.spell4Casts = spell4Casts
        self.subteamPlacement = subteamPlacement
        self.summoner1Casts = summoner1Casts
        self.summoner1Id = summoner1Id
        self.summoner2Casts = summoner2Casts
        self.summoner2Id = summoner2Id
        self.summonerId = summonerId
        self.summonerLevel = summonerLevel
        self.summonerName = summonerName
        self.teamEarlySurrendered = teamEarlySurrendered
        self.teamId = teamId
        self.teamPosition = teamPosition
        self.timeCCingOthers = timeCCingOthers
        self.timePlayed = timePlayed
        self.totalAllyJungleMinionsKilled = totalAllyJungleMinionsKilled
        self.totalDamageDealt = totalDamageDealt
        self.totalDamageDealtToChampions = totalDamageDealtToChampions
        self.totalDamageShieldedOnTeammates = totalDamageShieldedOnTeammates
        self.totalDamageTaken = totalDamageTaken
        self.totalEnemyJungleMinionsKilled = totalEnemyJungleMinionsKilled
        self.totalHeal = totalHeal
        self.totalHealsOnTeammates = totalHealsOnTeammates
        self.totalMinionsKilled = totalMinionsKilled
        self.totalTimeCCDealt = totalTimeCCDealt
        self.totalTimeSpentDead = totalTimeSpentDead
        self.totalUnitsHealed = totalUnitsHealed
        self.tripleKills = tripleKills
        self.trueDamageDealt = trueDamageDealt
        self.trueDamageDealtToChampions = trueDamageDealtToChampions
        self.trueDamageTaken = trueDamageTaken
        self.turretKills = turretKills
        self.turretTakedowns = turretTakedowns
        self.turretsLost = turretsLost
        self.unrealKills = unrealKills
        self.visionClearedPings = visionClearedPings
        self.visionScore = visionScore
        self.visionWardsBoughtInGame = visionWardsBoughtInGame
        self.wardsKilled = wardsKilled
        self.wardsPlaced = wardsPlaced
        self.win = win
        self.challenges = Challenges(**challenges)
        self.missions = Missions(**missions)
        self.perks = Perks(**perks)

class Challenges:
    def __init__(self, abilityUses, acesBefore15Minutes, alliedJungleMonsterKills, baronTakedowns, blastConeOppositeOpponentCount, bountyGold, buffsStolen,
                 completeSupportQuestInTime, controlWardsPlaced, damagePerMinute, damageTakenOnTeamPercentage, deathsByEnemyChamps,
                 dancedWithRiftHerald, dodgeSkillShotsSmallWindow, doubleAces, dragonTakedowns, earlyLaningPhaseGoldExpAdvantage,
                 effectiveHealAndShielding, elderDragonKillsWithOpposingSoul, elderDragonMultikills,enemyChampionImmobilizations, enemyJungleMonsterKills, epicMonsterKillsNearEnemyJungler,
                 epicMonsterKillsWithin30SecondsOfSpawn, epicMonsterSteals, epicMonsterStolenWithoutSmite, firstTurretKilled, flawlessAces, fullTeamTakedown, gameLength,
                 goldPerMinute, hadOpenNexus, immobilizeAndKillWithAlly, initialBuffCount, initialCrabCount, jungleCsBefore10Minutes, junglerTakedownsNearDamagedEpicMonster, kTurretsDestroyedBeforePlatesFall,
                 kda, killAfterHiddenWithAlly, killParticipation, killedChampTookFullTeamDamageSurvived, killingSprees,
                 killsNearEnemyTurret, killsOnRecentlyHealedByAramPack, killsUnderOwnTurret, killsWithHelpFromEpicMonster,
                 knockEnemyIntoTeamAndKill, landSkillShotsEarlyGame, laneMinionsFirst10Minutes,
                 laningPhaseGoldExpAdvantage, legendaryCount, legendaryItemUsed, lostAnInhibitor, maxCsAdvantageOnLaneOpponent,
                 maxKillDeficit, maxLevelLeadLaneOpponent, mejaisFullStackInTime, moreEnemyJungleThanOpponent,
                 multiKillOneSpell, multiTurretRiftHeraldCount, multikills, multikillsAfterAggressiveFlash,
                 outerTurretExecutesBefore10Minutes, outnumberedKills, outnumberedNexusKill,
                 perfectDragonSoulsTaken, perfectGame, pickKillWithAlly, poroExplosions,
                 quickCleanse, quickFirstTurret, quickSoloKills, riftHeraldTakedowns, saveAllyFromDeath,
                 scuttleCrabKills, skillshotsDodged, skillshotsHit, snowballsHit, soloBaronKills,
                 soloKills, stealthWardsPlaced, survivedSingleDigitHpCount, survivedThreeImmobilizesInFight,
                 takedownOnFirstTurret, takedowns, takedownsAfterGainingLevelAdvantage,
                 takedownsBeforeJungleMinionSpawn, takedownsFirstXMinutes, takedownsInAlcove,
                 takedownsInEnemyFountain, teamBaronKills, teamDamagePercentage, teamElderDragonKills, teamRiftHeraldKills, tookLargeDamageSurvived, turretPlatesTaken, turretTakedowns,
                 turretsTakenWithRiftHerald, twentyMinionsIn3SecondsCount, twoWardsOneSweeperCount, unseenRecalls, visionScoreAdvantageLaneOpponent, visionScorePerMinute, wardTakedowns,
                 wardTakedownsBefore20M, wardsGuarded, **kwargs):
        self.assistStreakCount = kwargs.get('12AssistStreakCount')
        self.abilityUses = abilityUses
        self.acesBefore15Minutes = acesBefore15Minutes
        self.alliedJungleMonsterKills = alliedJungleMonsterKills
        self.baronTakedowns = baronTakedowns
        self.blastConeOppositeOpponentCount = blastConeOppositeOpponentCount
        self.bountyGold = bountyGold
        self.buffsStolen = buffsStolen
        self.completeSupportQuestInTime = completeSupportQuestInTime
        try: self.controlWardTimeCoverageInRiverOrEnemyHalf = kwargs.get('controlWardTimeCoverageInRiverOrEnemyHalf')
        except: self.controlWardTimeCoverageInRiverOrEnemyHalf = 0
        self.controlWardsPlaced = controlWardsPlaced
        self.damagePerMinute = damagePerMinute
        self.damageTakenOnTeamPercentage = damageTakenOnTeamPercentage
        self.deathsByEnemyChamps = deathsByEnemyChamps
        self.dancedWithRiftHerald = dancedWithRiftHerald
        self.dodgeSkillShotsSmallWindow = dodgeSkillShotsSmallWindow
        self.doubleAces = doubleAces
        self.dragonTakedowns = dragonTakedowns
        try: self.earliestBaron = kwargs.get('earliestBaron')
        except: self.earliestBaron = 0
        self.earlyLaningPhaseGoldExpAdvantage = earlyLaningPhaseGoldExpAdvantage
        self.effectiveHealAndShielding = effectiveHealAndShielding
        self.elderDragonKillsWithOpposingSoul = elderDragonKillsWithOpposingSoul
        self.elderDragonMultikills = elderDragonMultikills
        self.enemyChampionImmobilizations = enemyChampionImmobilizations
        self.enemyJungleMonsterKills = enemyJungleMonsterKills
        self.epicMonsterKillsNearEnemyJungler = epicMonsterKillsNearEnemyJungler
        self.epicMonsterKillsWithin30SecondsOfSpawn = epicMonsterKillsWithin30SecondsOfSpawn
        self.epicMonsterSteals = epicMonsterSteals
        self.epicMonsterStolenWithoutSmite = epicMonsterStolenWithoutSmite
        self.firstTurretKilled = firstTurretKilled
        try: self.firstTurretKilledTime = kwargs.get('firstTurretKilledTime')
        except: self.firstTurretKilledTime = None
        self.flawlessAces = flawlessAces
        self.fullTeamTakedown = fullTeamTakedown
        self.gameLength = gameLength
        try: self.getTakedownsInAllLanesEarlyJungleAsLaner = kwargs.get('getTakedownsInAllLanesEarlyJungleAsLaner')
        except: self.getTakedownsInAllLanesEarlyJungleAsLaner = 0
        self.goldPerMinute = goldPerMinute
        self.hadOpenNexus = hadOpenNexus
        self.immobilizeAndKillWithAlly = immobilizeAndKillWithAlly
        self.initialBuffCount = initialBuffCount
        self.initialCrabCount = initialCrabCount
        self.jungleCsBefore10Minutes = jungleCsBefore10Minutes
        self.junglerTakedownsNearDamagedEpicMonster = junglerTakedownsNearDamagedEpicMonster
        self.kTurretsDestroyedBeforePlatesFall = kTurretsDestroyedBeforePlatesFall
        self.kda = kda
        self.killAfterHiddenWithAlly = killAfterHiddenWithAlly
        self.killParticipation = killParticipation
        self.killedChampTookFullTeamDamageSurvived = killedChampTookFullTeamDamageSurvived
        self.killingSprees = killingSprees
        self.killsNearEnemyTurret = killsNearEnemyTurret
        try: self.killsOnOtherLanesEarlyJungleAsLaner = kwargs.get('killsOnOtherLanesEarlyJungleAsLaner')
        except: self.killsOnOtherLanesEarlyJungleAsLaner = 0
        self.killsOnRecentlyHealedByAramPack = killsOnRecentlyHealedByAramPack
        self.killsUnderOwnTurret = killsUnderOwnTurret
        self.killsWithHelpFromEpicMonster = killsWithHelpFromEpicMonster
        self.knockEnemyIntoTeamAndKill = knockEnemyIntoTeamAndKill
        self.landSkillShotsEarlyGame = landSkillShotsEarlyGame
        self.laneMinionsFirst10Minutes = laneMinionsFirst10Minutes
        self.laningPhaseGoldExpAdvantage = laningPhaseGoldExpAdvantage
        self.legendaryCount = legendaryCount
        self.legendaryItemUsed = legendaryItemUsed
        self.lostAnInhibitor = lostAnInhibitor
        self.maxCsAdvantageOnLaneOpponent = maxCsAdvantageOnLaneOpponent
        self.maxKillDeficit = maxKillDeficit
        self.maxLevelLeadLaneOpponent = maxLevelLeadLaneOpponent
        self.mejaisFullStackInTime = mejaisFullStackInTime
        self.moreEnemyJungleThanOpponent = moreEnemyJungleThanOpponent
        self.multiKillOneSpell = multiKillOneSpell
        self.multiTurretRiftHeraldCount = multiTurretRiftHeraldCount
        self.multikills = multikills
        self.multikillsAfterAggressiveFlash = multikillsAfterAggressiveFlash
        self.outerTurretExecutesBefore10Minutes = outerTurretExecutesBefore10Minutes
        self.outnumberedKills = outnumberedKills
        self.outnumberedNexusKill = outnumberedNexusKill
        self.perfectDragonSoulsTaken = perfectDragonSoulsTaken
        self.perfectGame = perfectGame
        self.pickKillWithAlly = pickKillWithAlly
        try: self.playedChampSelectPosition = kwargs.get('playedChampSelectPosition')
        except: self.playedChampSelectPosition = 0
        self.poroExplosions = poroExplosions
        self.quickCleanse = quickCleanse
        self.quickFirstTurret = quickFirstTurret
        self.quickSoloKills = quickSoloKills
        self.riftHeraldTakedowns = riftHeraldTakedowns
        self.saveAllyFromDeath = saveAllyFromDeath
        self.scuttleCrabKills = scuttleCrabKills
        self.skillshotsDodged = skillshotsDodged
        self.skillshotsHit = skillshotsHit
        self.snowballsHit = snowballsHit
        self.soloBaronKills = soloBaronKills
        self.soloKills = soloKills
        self.stealthWardsPlaced = stealthWardsPlaced
        self.survivedSingleDigitHpCount = survivedSingleDigitHpCount
        self.survivedThreeImmobilizesInFight = survivedThreeImmobilizesInFight
        self.takedownOnFirstTurret = takedownOnFirstTurret
        self.takedowns = takedowns
        self.takedownsAfterGainingLevelAdvantage = takedownsAfterGainingLevelAdvantage
        self.takedownsBeforeJungleMinionSpawn = takedownsBeforeJungleMinionSpawn
        self.takedownsFirstXMinutes = takedownsFirstXMinutes
        self.takedownsInAlcove = takedownsInAlcove
        self.takedownsInEnemyFountain = takedownsInEnemyFountain
        self.teamBaronKills = teamBaronKills
        self.teamDamagePercentage = teamDamagePercentage
        self.teamElderDragonKills = teamElderDragonKills
        self.teamRiftHeraldKills = teamRiftHeraldKills
        self.tookLargeDamageSurvived = tookLargeDamageSurvived
        self.turretPlatesTaken = turretPlatesTaken
        self.turretTakedowns = turretTakedowns
        self.turretsTakenWithRiftHerald = turretsTakenWithRiftHerald
        self.twentyMinionsIn3SecondsCount = twentyMinionsIn3SecondsCount
        self.twoWardsOneSweeperCount = twoWardsOneSweeperCount
        self.unseenRecalls = unseenRecalls
        self.visionScoreAdvantageLaneOpponent = visionScoreAdvantageLaneOpponent
        self.visionScorePerMinute = visionScorePerMinute
        self.wardTakedowns = wardTakedowns
        self.wardTakedownsBefore20M = wardTakedownsBefore20M
        self.wardsGuarded = wardsGuarded

class Perks:
    def __init__(self, statPerks, styles, ):
        self.defense = statPerks.get('defense')
        self.flex = statPerks.get('flex')
        self.offense = statPerks.get('offense')
        self.mainStyle = styles[0].get('style')
        self.mainRune1 = styles[0].get('selections', {})[0].get('perk')
        self.mainRune2 = styles[0].get('selections', {})[1].get('perk')
        self.mainRune3 = styles[0].get('selections', {})[2].get('perk')
        self.mainRune4 = styles[0].get('selections', {})[3].get('perk')
        self.subStyle = styles[1].get('style')
        self.subRune1 = styles[1].get('selections', {})[0].get('perk')
        self.subRune2 = styles[1].get('selections', {})[1].get('perk')

class Missions:
    def __init__(self, playerScore0, playerScore1, playerScore10, playerScore11, playerScore2, playerScore3, playerScore4,
                 playerScore5, playerScore6, playerScore7, playerScore8, playerScore9, ):
        self.playerScore0 = playerScore0
        self.playerScore1 = playerScore1
        self.playerScore10 = playerScore10
        self.playerScore11 = playerScore11
        self.playerScore2 = playerScore2
        self.playerScore3 = playerScore3
        self.playerScore4 = playerScore4
        self.playerScore5 = playerScore5
        self.playerScore6 = playerScore6
        self.playerScore7 = playerScore7
        self.playerScore8 = playerScore8
        self.playerScore9 = playerScore9

class Summoner:
  def __init__(self, id, accountId, puuid, profileIconId, revisionDate, summonerLevel):
    self.id = id
    self.accountId = accountId
    self.puuid = puuid
    self.profileIconId = profileIconId
    self.revisionDate = revisionDate
    self.summonerLevel = summonerLevel

class LiveMatch:
    def __init__(self, gameId, mapId, gameMode, gameType, gameQueueConfigId, participants, gameStartTime, gameLength, observers, platformId, bannedChampions, ):
        self.gameId = gameId
        self.mapId = mapId
        self.gameMode = gameMode
        self.gameType = gameType
        self.gameQueueConfigId = gameQueueConfigId
        self.participants = participants
        self.gameStartTime = gameStartTime
        self.gameLength = gameLength
        self.observers = observers
        self.platformId = platformId
        self.bannedChampions = bannedChampions

class RankInfoSummoner:
    def __init__(self, leagueId, queueType, tier, rank, summonerId, summonerName, leaguePoints, wins, losses, veteran, inactive, freshBlood, hotStreak):
        self.leagueId = leagueId
        self.queueType = queueType
        self.tier = tier
        self.rank = rank
        self.summonerId = summonerId
        self.summonerName = summonerName
        self.leaguePoints = leaguePoints
        self.wins = wins
        self.losses = losses
        self.veteran = veteran
        self.inactive = inactive
        self.freshBlood = freshBlood
        self.hotStreak = hotStreak

class Teams:
    def __init__(self, bans, objectives, teamId, win):
        self.bans1 = Bans(**bans[0])
        self.bans2 = Bans(**bans[1])
        self.bans3 = Bans(**bans[2])
        self.bans4 = Bans(**bans[3])
        self.bans5 = Bans(**bans[4])
        self.baron = Objectives(**objectives["baron"])
        self.champion = Objectives(**objectives["champion"])
        self.dragon = Objectives(**objectives["dragon"])
        self.horde = Objectives(**objectives["horde"])
        self.inhibitor = Objectives(**objectives["inhibitor"])
        self.riftHerald = Objectives(**objectives["riftHerald"])
        self.tower = Objectives(**objectives["tower"])
        self.teamId = teamId
        self.win = win

class Bans:
    def __init__(self, championId, pickTurn, ):
        self.championId = championId
        self.pickTurn = pickTurn

class Objectives:
    def __init__(self, first, kills, ):
        self.first = first
        self.kills = kills
