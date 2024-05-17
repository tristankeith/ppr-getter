import json

def get_music(musicid):
    parse_musicid = int(musicid)
    with open("music_list.txt", "r", encoding="utf8") as f:
        music_data = f.read()
    parse_music_data = json.loads(music_data)
    music_lists = parse_music_data["_Data"]
    for music_list in music_lists:
        music_id = music_list["MusicId"]
        music_name = music_list["MusicName"]
        if music_id == parse_musicid:
            return music_id, music_name
    return "Music ID not found", "Music Name not found"

def main():
    m_id, m_name = get_music("55")
    print (f"{m_id},{m_name}")
    
if __name__ == "__main__":
    main()