import glob

with open("shakespeare_metadata.csv") as f:
    f = f.read().split("\n")
    metadata_dict = {}
    
    #skip headers
    for i in f[1:]:
        i_s = i.split("\t")
        if len(i_s) > 1:
            filename          = i_s[0]
            genre             = i_s[1]
            first_performance = i_s[2]
            company           = i_s[3]
            title             = i_s[4]
            
            if filename not in metadata_dict.keys():
                metadata_dict[filename] = {}
                metadata_dict[filename]["genre"]             = genre
                metadata_dict[filename]["first_performance"] = first_performance
                metadata_dict[filename]["company"]           = company
                metadata_dict[filename]["title"]             = title

speaker_dict = {}

for i in glob.glob("C:\\Data\\Folger_Digital_Texts_Complete\\*.xml"):
    with open(i) as f:
    
        filename = i.split("\\")[-1]
    
        if filename not in speaker_dict.keys():
            speaker_dict[filename] = {}
            
        f = f.read()
        
        #now split by speaker, and for each speaker find out how many lines they're speaking in the given speaking instance
        f_s = f.split("<sp xml:")[1:]
        for j in f_s:
        
            try:
                speakers = j.split('who=')[1].split(">")[0].split("#")
                
                #there may be multiple speakers here, so add words for each
                for speaker in speakers:
                
                    speaker = speaker.replace('"',"").replace("\n","")
                
                    if speaker != "":
                        speaker = speaker.split("_")[0]
                        
                        if "." in speaker:
                            speaker = speaker.split(".")[0]
                    
                        if speaker not in speaker_dict[filename].keys():
                            speaker_dict[filename][speaker] = 0
                        
                        #now count the number of words the character speaks in this given instance
                        words_spoken = j.split("<w xml")[1:]
                        
                        #print words_spoken
            
                        speaker_dict[filename][speaker] += len(words_spoken)
                
            except:
                #we miss only one speaking event
                pass
                
with open("speaking_distribution_by_play.txt","w") as out:
    for k in speaker_dict:
    
        genre = metadata_dict[k]["genre"]
        first_performance = metadata_dict[k]["first_performance"]
        title= metadata_dict[k]["title"]
        
        for l in speaker_dict[k]:
            out.write(k + "\t" + l + "\t" + str(speaker_dict[k][l]) + "\t" + genre + "\t" + first_performance + "\t" + title + "\n")