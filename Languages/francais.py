class Language:

    #main
    pingbot = "Mon prefix est `{}`.\nPour avoir de l'aide, faites `{}help` !\n J'ai une latence de `{}` ms"
    #help
    cmdnotfoundhelp = "La commande {} est introuvable."
    helptitle = "**📔 • Aide**"
    generaltitle = "**__Général__**"
    helphelp = "> Envoie cette commande"
    serverinfohelp = "> Donne les informations du serveur"
    memberinfohelp = "> Donne les informations sur soi ou sur une autre personne"
    botinfohelp = "> Donne les informations sur le bot, et permet de l'inviter sur son serveur"
    suggesthelp = "> Permet d'envoyer une suggestion sur le serveur du bot"
    titlelvl = "**__Niveaux__**"
    leaderboardhelp = "> Classement de niveau"
    levelhelp = "> Acceder à son niveau ou celui d'un autre (mention ou ID)"
    titleeco = "**__Économie__**"

    #helpmodo
    modotitle = "**__Modérateur__**"
    clearhelp = "> permet de supprimer x messages (valeur maximal de 100)"
    kickhelp = "> Expulse la personne (mention ou ID) du serveur"
    banhelp = "> Banni la personne (mention ou id) temporairement ou définitivement du serveur\nExemple: {}ban {} 1d2h3m4s arnaques"
    unbanhelp = "> Unban une personne (pseudo#tag ou id)"
    mutehelp = "> Mute une personne temporairement ou définitivement (mention ou id)\nExemple: {}mute {} 1d2h3m4s insultes"
    unmutehelp = "> Unmute un membre (mention ou id)"
    lockhelp = "> Empêche les personnes qui ne sont pas administrateur de parler dans le channel"
    unlockhelp = "> Permet à tout le monde de parler dans un channel lock"
    nukehelp = "> Permet de supprimer et dupliquer un channel"

    #helpadmin
    admintitle = "**__Administrateur__**"
    helpsettings = "> Accès à tous les paramètres"
    helpsay = "> Faire une annonce en mentionnant @everyone"
    resetlevelhelp = "> Permet de réinitialiser le niveau de tout le serveur"

    #unload
    nocmd = "Cette commande n'existe pas."



    #ban
    nouser = "Veuiller donner une ID / mention valide."
    banme = "Vous ne pouvez pas vous bannir vous-même"
    noreason = "Aucune raison"
    titleban = "**BANISSEMENT**"
    userbanned = "Membre banni"
    banduration = "Durée"
    reason = "Raison"
    moderator = "Modérateur"
    bantoprole = "Vous ne pouvez pas bannir quelqu'un qui possède un rôle plus élevé."
    banequalrole = "Vous ne pouvez pas bannir quelqu'un qui possède un rôle qui vous est égale."



    #botinfo
    botinfotitle = "**📢 • Information**"
    botinfos = "**__Mes informations__**"
    creator = "Mon créateur"
    creatoranswer = "Mon papa est Zyco#9458."
    nbserv = "Mes statistiques"
    nbservanswer = "Actuellement je suis sur {} serveurs, ce qui fait {} personnes qui m'utilisent !"
    addbot = "Comment m'inviter ?"
    addbotanswer = "Vous pouvez désormais m'ajouter sur votre serveur [ici](https://discord.com/api/oauth2/authorize?client_id=864281572399251488&permissions=8&scope=bot)"



    #clear
    clearmax = "Valeur maximal de 100 messages"
    clearinvalidformat = "Veuillez entrer une valeur valide (un maximum de 100 messages)."


    #erreurs
    errorcmddoesntexist = "Cette commande est innexistante."
    errormissingarguments = "Il manque un/des argument/s."
    errornopermission = "Vous n'avez pas les permissions pour faire cette commande."
    errorcantuse = "Vous ne pouvez pas utiliser cette commande."
    errorbotdoesnthavepermissions = "Je n'ai pas les permissions nécéssaires pour faire cette commmande"
    errorbadargument = "Le membre est introuvable."

    #kick
    kickme = "Vous ne pouvez pas vous expulser vous-même"
    kicktitle = "**Expulsion**"
    kickdescription = "Le marteau a frappé !"
    kickuser = "Membre expulsé"
    kicktoprole = "Vous ne pouvez pas expulsé quelqu'un qui possède un plus grand rôle."
    kickequalrole = "Vous ne pouvez pas expulsé quelqu'un qui possède un rôle qui vous est égale."
    kickbot = "Je ne peut pas expulser un bot."


    #leaderboard
    lbnoonespeak = "Personne n'a jamais parler."
    lbtitle = "**LEADERBOARD**"
    lbrep = "{}) <@{}> : **{}** XP | Niveau **{}**\n"

    #level
    lvlnosysxp = "Le système d'xp est désactivé sur ce serveur."
    lvlnouserxp = "Cet utilisateur n'as jamais parler, il n'est pas dans notre base."
    lvltitle = "**NIVEAU**"
    lvlxp = "XP"
    lvllvl = "Niveau"

    #lock / unlock
    lockmsg = "Ce channel à été lock par {}."
    unlockmsg = "Ce channel à été unlock par {}."

    #logs
    #logsban
    logstitle = "**LOGS**"
    logsbantitle = "**__Banissement__**"
    logsbanmember = "Membre banni"
    logsbanduration = "Durée"
    logsbanmodo = "Modérateur"
    logsbanreason = "Raison"

    #logskick
    logskicktitle = "**__Expulsion__**"
    logskickmember = "Membre exclu"
    logskickmodo = "Modérateur"
    logskickreason = "Raison"

    #unban
    logsunbantitle = "**__Unban__**"
    logsunbanmember = "Membre unban"
    logsunbanmodo = "Modérateur"

    #mute
    logsmutetitle = "**__Mute__**"
    logsmutemember = "Membre mute"
    logsmutereason = "Raison"
    logsmuteduration = "Durée"
    logsmutemodo = "Modérateur"

    #unmute
    logsunmutetitle = "**__Unmute__**"
    logsunmutemember = "Membre unmute"
    logsunmutemodo = "Modérateur"

    #lock
    logstitlelock = "**__Lock__**"
    logslockchannel = "Channel lock"
    logslockmodo = "Modérateur"

    #unlock
    logsunlocktitle = "**__Unlock__**"
    logsunlockchannel = "Channel unlock"
    logsunlockmodo = "Modérateur"

    #nukelogs
    logsnuketitle = "**__Nuke__**"
    logsnukechannel = "Nouveau channel"
    logsnukemodo = "Modérateur"



    #memberinfo
    memberinfomuteforever = "Pour toujours."
    memberinfomute = "Jusqu'au {}."
    memberinfotitle = "**INFORMATIONS DE {}**"
    memberinfoid = "ID"
    memberinfojoinedat = "Date d'arrivé sur {}"
    memberinfocreatedat = "Date de création du compte"
    memberinfobestrole = "Meilleur rôle"
    memberinfomuteornot = "Mute ?"




    #mute
    mutealreadymute = "La personne est déjà muée"
    mutetitle = "**MUTE**"
    mutemember = "Membre mute"
    muteduration = "Durée"
    mutereason = "Raison"
    mutemodo = "Modérateur"
    mutetoproleinpossible = "Le role mute est plus haut que celui du bot"


    #resetlvl
    resetlvlwant = "Voulez-vous réinitialiser le niveau de tout le monde ? Cet action est irréversible."
    resetlvlallreset = "Tout le monde à été réinitialiser."

    #say
    saymsg = "||@everyone||\nMessage de {} :\n> {}"

    #serverinfo
    serverinfotitle = "**📢 • Informations du serveur**"
    serverinfonameserver = "Nom du serveur"
    serverinfoowneroftheserver = "Propriétaire du serveur"
    serverinfodesc = "Description du serveur"
    serverinfocreatedat = "Date de création du serveur"
    serverinfonbofmembers = "Nombre de membres"
    serverinfonbofmembersanswer = "{} membres"
    serverinfonbchann = "Nombres de channels"
    serverinfonbchannanswer = "{} channels textuels et {} channels vocaux (total de {} channels)"
    serverinfonbroles = "Nombres de rôles"
    serverinfonbrolesanswer = "{} roles"
    serverinfonbboost = "Nombre de boosts"
    serverinfomemberstatus = "Status des membres du serveur"




    #settings

    #settingsprefix
    settingsprefixtitle = "**PREFIX**"
    settingsprefixf1 = "Prefix"
    settingsprefixselectprefix = "Quel prefix voulez-vous ?"
    settingsprefixcantuseprefix = "Vous ne pouvez pas utiliser ce prefix."
    settingsprefixtoolong = "Ce prefix est trop long, vous ne pouvez pas utiliser un prefix de plus de 5 caractères."
    settingsprefixnewprefix = "Le prefix est désormais `{}` !"
    settingsprefixnow = "Le prefix est `{}`, voulez-vous le changer ?"

    #settingslogs
    settingslogswantchangeparams =  "Voulez-vous changer ces paramètres ?"
    settingslogsnewparams = "\nActiver / désactiver les logs. \nActuellement: {} (<#{}>)"
    settingslogsnewparams1 = "\nActiver / désactiver les logs. \nActuellement: {}"
    settingslogslogsoff = "Les logs sont maintenant Off !"
    settingslogspingchann = "Veuillez ping le channel sur lequel seront les logs"
    settingslogsnewchann = "Les logs sont maintenant On sur le channel <#{}> !"
    settingslogsonoffsyslog = "Activer / Désactiver le système de logs"
    settingslogschangelogchann = "\nChanger le channel de logs"

    #settingslanguage
    settingslanguagechangeornot = "La langue actuel est en français"
    settingslanguagechangeornot2 = "Voulez-vous changer ce paramètre ?"
    settingslanguagewhatlangage = "Quel langage voulez-vous utiliser ?"

    settingstitle = "**PARAMÈTRES**"
    settingsallsettings = "\n:one: Paramètres de prefix\n\n:two: Paramètres de logs\n\n:three: Langage du bot"


    #unban
    unbantitle = "**UNBAN**"
    unbandesc = "Bon retour parmis nous !"
    unbanmember = "Membre unban"
    unbanmodo = "Modérateur"
    unbannotbanned = "Cet utilisateur n'est pas banni."

    #unmute
    unmutetitle = "**UNMUTE**"
    unmutemember = "Membre unmute"
    unmutemodo = "Modérateur"
    unmuteusernotmute = "Cet utilisateur n'est pas mute"

    #nuke
    nukemsg = "Ce salon à été nuke par {}"
    nukeimpossible = "Impossible de nuke ce channel"

    #suggest
    suggesttolong = "Ce message est trop long, la taille maximal est de 500 caractères"
    suggestsuccessfull = "Cette suggestion viens d'être envoyer. Merci pour vos retours !"