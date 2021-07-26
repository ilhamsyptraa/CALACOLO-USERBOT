from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝙰𝚜𝚜𝚊𝚕𝚊𝚖𝚞'𝚊𝚕𝚊𝚒𝚔𝚞𝚖 𝙳𝚞𝚕𝚞 𝙱𝚒𝚊𝚛 𝚂𝚘𝚙𝚊𝚗...")


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇... 𝐈𝐒𝐓𝐈𝐆𝐇𝐅𝐀𝐑 𝐃𝐎𝐍𝐆𝐎!!!")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐖𝐚'𝐚𝐥𝐚𝐢𝐤𝐮𝐦𝐬𝐚𝐥𝐚𝐦...")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇... 𝐈𝐒𝐓𝐈𝐆𝐇𝐅𝐀𝐑 𝐓𝐎𝐋𝐎𝐋!!!")


@register(outgoing=True, pattern='^K(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐍𝐆𝐎𝐍𝐓𝐎𝐋𝐋𝐋𝐋𝐋𝐋**")


@register(outgoing=True, pattern='^N(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐍𝐆𝐄𝐍𝐓𝐎𝐎𝐎𝐎𝐎𝐎𝐎𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓𝐓**")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐁𝐀𝐂𝐎𝐓 𝐁𝐄𝐓𝐓, 𝐌𝐔𝐋𝐔𝐓 𝐋𝐎 𝐁𝐀𝐔 𝐊𝐀𝐁𝐄𝐋 𝐓𝐎𝐋𝐎𝐋!!!**")


@register(outgoing=True, pattern='^M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐁𝐇𝐀𝐀𝐀𝐊𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒**")


@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐘𝐀𝐔𝐃𝐀𝐇 𝐈𝐘𝐀 𝐃𝐈𝐄𝐌 𝐁𝐀𝐁𝐈!!!**")


@register(outgoing=True, pattern='^C(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐌𝐔𝐊𝐀 𝐋𝐔 𝐇𝐈𝐍𝐀... 𝐆𝐀𝐔𝐒𝐀𝐇 𝐒𝐎 𝐊𝐄𝐑𝐀𝐒 𝐘𝐀 𝐀𝐍𝐀𝐊 𝐇𝐀𝐑𝐀𝐌!!!**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐒𝐎𝐊𝐀𝐏 𝐁𝐄𝐓𝐓 𝐁𝐎𝐂𝐀𝐇 𝐇𝐈𝐍𝐀... 𝐃𝐈𝐄𝐌 𝐋𝐔!!!**")


@register(outgoing=True, pattern='^V(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐌𝐀𝐂𝐄𝐌 𝐁𝐀𝐆𝐔𝐒 𝐀𝐄 𝐋𝐔 𝐁𝐄𝐆𝐈𝐓𝐔 𝐌𝐎𝐍𝐘𝐄𝐓𝐓*")


@register(outgoing=True, pattern='^J(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐉𝐄𝐋𝐄𝐊 𝐁𝐄𝐆𝐎 𝐋𝐔 𝐁𝐄𝐆𝐈𝐓𝐔, 𝐍𝐀𝐉𝐈𝐒 𝐂𝐔𝐈𝐇𝐇𝐇𝐇!!!!!!**")


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PASANG PP DULU TOLOL, BIAR ORANG SATU GRUP TAU BETAPA HINANYA MUKA LU😆**")


@register(outgoing=True, pattern='^X(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC SAMPAH, CUIHHHHH!**")


@register(outgoing=True, pattern='^Z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**War War Tai anjing, Ketrigger minta sharelok, Udah di sharelok Ga nyamperin, Keras di sosmed Bhakss...**")


@register(outgoing=True, pattern='^H(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Badut Lawak Mulu ocehan lu dongo, Ga ngena ke mental CUIHHHH!!!**")


@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JANGAN MAEN BOT MULU, ALAY LU NGENTOTT,KESANNYA NORAK, CUIHHHH!!!**")


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ga keren lu begitu tolol, Kuburan bapak lu gua kencingin, Gw gali buat dijadiin jamban bego. Cuihhhhh!!!**")

CMD_HELP.update({
    "salam":
    "P\
\nUsage: Untuk Memberi salam.\
\n\nL\
\nUsage: Untuk Menjawab Salam.\
\n\nK\
\nUsage: Untuk mengontoli mereka.\
\n\nN\
\nUsage: Kalo kesel coba aja.\
\n\nB\
\nUsage: Buat Ngatain Yang Suka Bacot.\
\n\nM\
\nUsage: Tersedak meledek.\
\n\nY\
\nUsage: Buat yang males adu bacot.\
\n\nC\
\nUsage: Buat menghujat.\
\n\nS\
\nUsage: Haha sokap."
})

CMD_HELP.update({
    "salam2":
    "V\
\nUsage: Hujat Orang caper.\
\n\nJ\
\nUsage: Hujat Jamet.\
\n\nA\
\nUsage: Hujat yang gapunya muka.\
\n\nX\
\nUsage: Ngatain Grup wkwk.\
\n\nZ\
\nUsage: teruntuk petarung.\
\n\nH\
\nUsage: Coba dewek ah.\
\n\n.atg\
\nUsage: Istighfar 1.\
\n\n.ast\
\nUsage: Istighfar 2.\
\n\nO\
\nUsage: Ngatain org norak.\
\n\nG\
\nUsage: Liat Sendiri."
})
