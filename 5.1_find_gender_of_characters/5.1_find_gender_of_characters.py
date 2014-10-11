
import glob      
        
gender_dict = {}

for i in glob.glob("C:\\Data\\Folger_Digital_Texts_Complete\\*.xml"):
    
    filename = i.split("\\")[-1]
    
    if filename not in gender_dict.keys():
        gender_dict[filename] = {}
    
    with open(i) as f:
        f_s = f.read().split('<person xml:id="')
        for j in f_s:
            char_name = j.split('"')[0].split("_")[0]
            
            if "<sex value=" in j:
                sex_value = j.split("<sex value=")[1].split(">")[1].split("<")[0]
                
                if char_name not in gender_dict[filename].keys():
                    gender_dict[filename][char_name] = sex_value


with open("gender_identified_speaking_distributions.txt","w") as out:                    
    with open("speaking_distribution_by_play.txt") as f:
        f = f.read().split("\n")
        for i in f:
        
            i_s = i.split("\t")
            
            if len(i_s) > 2:
                filename = i_s[0]
                character_name = i_s[1]
                
                try:
                    character_gender = gender_dict[filename][character_name]
                    
                    out.write(i + "\t" + character_gender + "\n")
                    
                except Exception as e:
                    print e
