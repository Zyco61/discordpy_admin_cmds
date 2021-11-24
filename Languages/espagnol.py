class Language:
	# c ezexo jai commence lespagnol
    #main
    pingbot = "Mi prefijo es `{}`.\nPara obtener ayuda, escriba `{}help` !\nMi latencia es `{}` ms !"
    #help
    cmdnotfoundhelp = "El comando {} no se encuentra"
    helptitle = "**📔 • Ayuda**"
    generaltitle = "**__General__**"
    helphelp = "> Envía este comando"
    serverinfohelp = "> Envía información sobre el gremio"
    memberinfohelp = "> Envía información sobre tí o sobre otra persona. (mención o ID)"
    botinfohelp = "> Envía informaciónes sobre mi, and allows you to invite me to your server"
    suggesthelp = "> Te permite enviar una sugerencia al servidor del bot"
    titlelvl = "**__Niveles__**"
    leaderboardhelp = "> Tabla de clasificación de niveles"
    levelhelp = "> Acceso a su nivel o al de otra persona. (mención o ID)"
    titleeco = "**__Economía__**"
    
    #helpmodo
    modotitle = "**__Moderador__**"
    clearhelp = "> Permite borrar x mensajes (valor máximo: 100)"
    kickhelp = "> Expulsar un miembro de este gremio (mención o ID)"
    banhelp = "> Banea a un miembro temporal o permanentemente de este gremio (mención tu id) \n - Ejemplo: {}ban {} 1d2h3m4s insultos"
    unbanhelp = "> Unban someone. (pseudo#tag or ID)"
    mutehelp = "> Mute a member temporarily or permanently (mention or ID)\nExample: {}mute {} 1d2h3m4s spam"
    unmutehelp = "> Unmute a member. (mention or ID)"
    lockhelp = "> Prevents people who are not administrators from speaking in the channel"
    unlockhelp = "> Allows everyone to talk in a locked channel"
    nukehelp = "> Permite eliminar y duplicar un canal"

    #helpadmin
    admintitle = "**__Administrator__**"
    helpsettings = "> Access to all settings"
    helpsay = "> Makes an announcement with @everyone"
    resetlevelhelp = "> Reset the level system of this guild"

    #unload
    nocmd = "This command does not exist."


	#ban
    nouser = "Please give a valid user or ID."
    banme = "You can't ban yourself"
    noreason = "No reason"
    titleban = "**BANISHMENT**"
    userbanned = "Banned member"
    banduration = "Duration"
    reason = "Reason"
    moderator = "Moderator"
    bantoprole = "You can't ban someone who has a higher role than you."
    banequalrole = "You can't ban someone who has a role equals of you."



    #botinfo
    botinfotitle = "**📢 • Information**"
    botinfos = "**__My informations__**"
    creator = "My creator:"
    creatoranswer = "My father is Zyco#9458."
    nbserv = "My statistics:"
    nbservanswer = "Currently I am on {} guilds, which makes {} peoples using me !"
    addbot = "How to invit me ?"
    addbotanswer = "You can now add me to your guild [here](https://discord.com/api/oauth2/authorize?client_id=864281572399251488&permissions=8&scope=bot)"


    #clear
    clearmax = "The maximal value is 100 messages."
    clearinvalidformat = "Please enter a valid value. (the maximal value is 100 messages)"


    #erreurs
    errorcmddoesntexist = "This command does not exist."
    errormissingarguments = "At least one argument is missing."
    errornopermission = "You do not have permissions to do this command."
    errorcantuse = "You cannot use this command."
    errorbotdoesnthavepermissions = "I do not have permissions to do this command."
    errorbadargument = "The member could not be found."

    #kick
    kickme = "You can't kick yourself" 
    kicktitle = "**KICK**"
    kickdescription = "The hammer has spoken !"
    kickuser = "Kicked member"
    kicktoprole = "You can't kick someone who has a higher role than you."
    kickequalrole = "You can't kick someone who has a role equals of you."
    kickbot = "I can't kick a bot."


    #leaderboard
    lbnoonespeak = "No one has ever talk."
    lbtitle = "**LEADERBOARD**"
    lbrep = "{}) <@{}> : **{}** XP | Level **{}**\n"

    #level
    lvlnosysxp = "The level system is not activated on this guild."
    lvlnouserxp = "This member has never talked, he is not in our database."
    lvltitle = "**LEVEL**"
    lvlxp = "XP"
    lvllvl = "Level"

    #lock / unlock
    lockmsg = "This channel has been locked by {}."
    unlockmsg = "This channel has been unlocked by {}."

    #logs
    #logsban
    logstitle = "**LOGS**"
    logsbantitle = "**__Banishment__**"
    logsbanmember = "Banned member"
    logsbanduration = "Duration"
    logsbanmodo = "Moderator"
    logsbanreason = "Reason"

    #logskick
    logskicktitle = "**__Kick__**"
    logskickmember = "Kicked member"
    logskickmodo = "Moderator"
    logskickreason = "Reason"

    #unban
    logsunbantitle = "**__Unban__**"
    logsunbanmember = "Unbanned"
    logsunbanmodo = "Moderator"

    #mute
    logsmutetitle = "**__Mute__**"
    logsmutemember = "Muted member"
    logsmutereason = "Reason"
    logsmuteduration = "Duration"
    logsmutemodo = "Moderator"

    #unmute
    logsunmutetitle = "**__Unmute__**"
    logsunmutemember = "Unmuted member"
    logsunmutemodo = "Moderator"

    #lock
    logstitlelock = "**__Lock__**"
    logslockchannel = "Channel lock"
    logslockmodo = "Moderator"

    #unlock
    logsunlocktitle = "**__Unlock__**"
    logsunlockchannel = "Channel unlock"
    logsunlockmodo = "Moderator"

    #unlock
    logsunlocktitle = "**__Nuke__**"
    logsunlockchannel = "New channel"
    logsunlockmodo = "Moderator"



    #memberinfo
    memberinfomuteforever = "Forever."
    memberinfomute = "Until {}."
    memberinfotitle = "**{}'S INFORMATIONS**"
    memberinfoid = "ID"
    memberinfojoinedat = "Date of arrival on {}"
    memberinfocreatedat = "Account creation date"
    memberinfobestrole = "Top role"
    memberinfomuteornot = "Muted ?"




    #mute
    mutealreadymute = "The member is already muted."
    mutetitle = "**MUTE**"
    mutemember = "Muted member"
    muteduration = "Duration"
    mutereason = "Reason"
    mutemodo = "Moderator"


    #resetlvl
    resetlvlwant = "Do you want to reset everyone's levels ? This action is irreversible."
    resetlvlallreset = "Everyone has been reset."

    #say
    saymsg = "||@everyone||\n {}'s message:\n> {}"

    #serverinfo
    serverinfotitle = "**📢 • Guild informations**"
    serverinfonameserver = "Guild name"
    serverinfoowneroftheserver = "Guild owner"
    serverinfodesc = "Guild description"
    serverinfocreatedat = "Guild creation date"
    serverinfonbofmembers = "Members count"
    serverinfonbofmembersanswer = "{} members."
    serverinfonbchann = "Channels count"
    serverinfonbchannanswer = "{} textual channels and {} voice channels. ({} channels)"
    serverinfonbroles = "Roles count"
    serverinfonbrolesanswer = "{} roles"
    serverinfonbboost = "Boosts count"
    serverinfomemberstatus = "Estado de los miembros del servidor"





    #settings
    
    #settingsprefix
    settingsprefixtitle = "**PREFIX**"
    settingsprefixf1 = "**__Prefix__**"
    settingsprefixselectprefix = "What prefix do you want ?"
    settingsprefixcantuseprefix = "You cannot use this prefix."
    settingsprefixtoolong = "This prefix is too long, you cannot use a prefix longer than 5 characters."
    settingsprefixnewprefix = "The prefix is now `{}` !"
    settingsprefixnow = "The prefix is `{}`, do you want to change it ?"

    #settingslogs
    settingslogswantchangeparams =  "Do you want to change these settings ?"
    settingslogsnewparams = "\nEnable / disable logs. \nCurrently: {}. (<#{}>)"
    settingslogsnewparams1 = "\nEnable / disable logs. \nCurrently: {}."
    settingslogslogsoff = "The logs are now off !"
    settingslogsmentionchann = "Please mention the channel on which the logs will be."
    settingslogspingchann = "Please mention the channel on which the logs will be"
    settingslogsnewchann = "The logs are now on on the channel <#{}> !"
    settingslogsonoffsyslog = "Enable / Disable the log system."
    settingslogschangelogchann = "\nChange the log channel."

    #settingslanguage
    settingslanguagechangeornot = "El idioma actual es el español."
    settingslanguagechangeornot2 = "¿Quiere cambiar esta opción?"
    settingslanguagewhatlangage = "¿Qué idioma quiere utilizar?"

    settingstitle = "**SETTINGS**"
    settingsallsettings = "\n:one: Prefix settings\n\n:two: Logs settings\n\n:three: Bot language"


    #unban
    unbantitle = "**DESBAN**"
    unbandesc = "Bienvenido de nuevo."
    unbanmember = "Desbancar a un miembro"
    unbanmodo = "Moderador"
    unbannotbanned = "Este usuario no está baneado."

    #unmute
    unmutetitle = "**UNMUTE**"
    unmutemember = "Miembro no silenciado"
    unmutemodo = "Moderador"
    unmuteusernotmute = "Este miembro es no silenciado"
    mutetoproleinpossible = "El rol mudo es más alto que el del bot"


    #nuke
    nukemsg = "Este canal fue bombardeado por {}"
    nukeimpossible = "No se puede destruir este canal"

    #suggest
    suggesttolong = "This message is too long, the maximum size is 500 characters"
    suggestsuccessfull = "This suggestion has just been sent. Thanks for your feedback!"