

x = "AWUBBWUBC"
y = "AWUBWUBWUBBWUBWUBWUBC"
z = "WUBAWUBBWUBCWUB"


def song_decoder(song):
    txt = (' '.join(song.split("WUB"))).strip()
    for i in txt:
       txt = txt.replace("  "," ") 
    return txt

print(song_decoder(y))
