import json
import sys

def get_motion(filename):
    tagnames = []
    m_filenames = []
    with open(filename, "r", encoding="utf8") as f:
        motion_data = f.read()
    parse_motion_data = json.loads(motion_data)
    motion_lists = parse_motion_data["parameter_list"]
    m_name = parse_motion_data["m_Name"]
    for motion_list in motion_lists:
        tagname = motion_list["TagName"]
        m_filename = motion_list["FileName"]
        tagnames.append(tagname)
        m_filenames.append(m_filename)
    return m_name, tagnames, m_filenames
    

def main():
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    else:
        json_file = input("Input motion list json filename: ")
    m_name, tagnamex, filenamex = get_motion(json_file)
    for tagname in tagnamex:
        print(tagname)
    for filename in filenamex:
        print(filename)
    print (m_name)
    
    
if __name__ == "__main__":
    main()