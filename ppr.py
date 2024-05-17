from music_name import get_music
from motion_name import get_motion
from random import randint
import os
import re
import sys
import shutil

allowFileChanges = True
convertdir = r""

def find_files(source_dir, regex):
  matching_files = []
  for dirpath, filenames in os.walk(source_dir):
    for filename in filenames:
      if re.search(regex, filename):
        matching_files.append(os.path.join(dirpath, filename))
  return matching_files

def main():
    if len(sys.argv) > 1:
        motion_file = sys.argv[1]
    else:
        motion_file = input("Input motion list json filename: ")
    
    m_name, m_tagname, m_filename = get_motion(motion_file)
    name_regex = re.search(r".*?motion_list(\d+)_*?(\d+)*?sheet1", m_name, flags=re.IGNORECASE)
    m_musictag, m_musicname = get_music(name_regex.group(1))
    if allowFileChanges:
        outdir = os.path.join(os.getcwd(), "out")
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        if m_musicname == "Music Name not found":
            workdir = os.path.join(outdir, f"NO_MUSIC_ID_{name_regex.group(1)}")
        else:     
            workdir = os.path.join(outdir, m_musicname)
        if not os.path.exists(workdir):
            os.makedirs(workdir)
        motiondir = os.path.join(workdir, "motion")
        if not os.path.exists(motiondir):
            os.makedirs(motiondir)
        if not os.path.exists(convertdir):
            print("Cannot find files. Ensure that you have the correct files.")
            return
        for motion_source in m_filename:
            if motion_source == "":
                print("Null. Skipping...")
            else:
                getfile = re.search(r"(.*)_(.*)", motion_source, flags=re.IGNORECASE)
                regex = r".*{0}_.*".format(getfile.group(1))
                print (regex)
                matched_files = find_files(convertdir, regex.lower())
                for matched in matched_files:
                    print(matched)
                    shutil.copy(matched, motiondir)     
    else:
        print(f"""===Music/Motion Name: {m_musicname}, Identifiers: {m_musictag}, {m_name}\n===Motions: (Sequence)""")
        for x in range(len(m_tagname)):
            print(f"""-{m_tagname[x]}: {m_filename[x]}""")
        
            
    

if __name__ == "__main__":
    main()