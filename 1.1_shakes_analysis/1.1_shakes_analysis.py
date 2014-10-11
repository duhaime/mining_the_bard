
'''
div1 : Act breaks in metadata
div2 : Scene breaks in metadata (e.g. <div2 type="scene" n="2">)
foreign : tag for foreign words
stage : tag for stage directions; type indicates "entrance", "exit", "delivery", modifier"


******************************
<stage xml:id="stg-0000" n="SD 1.1.0" type="entrance" who="#Theseus_MND #Hippolyta_MND #Philostrate_MND #ATTENDANTS_MND">
<stage xml:id="stg-0016.1" n="SD 1.1.16.1" type="exit" who="#Philostrate_MND">
<stage xml:id="stg-0020.1" n="SD 1.1.20.1" type="entrance" who="#Egeus_MND #Hermia_MND #Lysander_MND #Demetrius_MND">
<stage xml:id="stg-0129.1" n="SD 1.1.129.1" type="exit" who="#Theseus_MND #Hippolyta_MND #Egeus_MND #Demetrius_MND #ATTENDANTS_MND">
<stage xml:id="stg-0182.1" n="SD 1.1.182.1" type="entrance" who="#Helena_MND">
<stage xml:id="stg-0229" n="SD 1.1.229" type="exit" who="#Hermia_MND">
<stage xml:id="stg-0231.1" n="SD 1.1.231.1" type="exit" who="#Lysander_MND">
<stage xml:id="stg-0257.1" n="SD 1.1.257.1" type="exit" who="#Helena_MND">
<stage xml:id="stg-0257.2" n="SD 1.2.0" type="entrance" who="#Quince_MND #Snug_MND #Bottom_MND #Flute_MND #Snout_MND #Starveling_MND">

workflow:

for play in dir:
for scene in play:
chars = 0
for entrance
for # in entrance:
chars += 1

for exit
for # in exit:
chars -= 1
'''

import glob

with open("shakespeare_character_counts_by_scene.txt","w") as out:
	for i in glob.glob("C:\\Data\\Folger_Digital_Texts_Complete\\*.xml"):
		with open(i) as f:
		
                        character_list = []
			act_count   = 0
			filename    = i.split("\\")[-1]
			f           = f.read().split("<body>")[1].split("<back>")[0]
                	acts        = f.split("<div1")[1:]

			for act in acts:

				scene_count = 0
				act_count  += 1
				scenes      = act.split("<div2")[1:]

				for j in scenes:

					scene_count += 1
                                        
					entrances_and_exits = j.split('" type="e')
			
					for k in entrances_and_exits:
		
						if k[0:6] == 'ntranc':
							entrance_queue = k.split("who=")[1].split(">")[0]
							split_on_pound = entrance_queue.split("#")
							for l in split_on_pound[1:]:
								l = l.replace('"',"").split("_")[0].strip()
                                                                
                                                                if ".0" in l:
                                                                
                                                                    #this is the tricky bit: if SERVANTS.LORD.0.2_Shr try to enter stage, check to see if SERVANTS.LORD are already on stage. If they are, don't let SERVANTS.LORD on. Otherwise, do.
                                                                    l = ".".join( x for x in l.split(".") if x[0].isalpha() )
                                                                        
                                                                    if l not in character_list:
                                                                        character_list.append(l)
                                                                
                                                                else:
                                                                    if l not in character_list:
                                                                
                                                                        character_list.append(l)

							words_spoken = k.split("<w xml")[1:]

							out.write(filename + "\t" + str(act_count) + "." + str(scene_count) + "\t" + str(len(character_list)) + "\t" + str(len(words_spoken)) + "\t" + " ".join(character_list) + "\n")

						if k[0:5] == 'xit" ':
							entrance_queue = k.split("who=")[1].split(">")[0]
							split_on_pound = entrance_queue.split("#")
							for l in split_on_pound[1:]:
								l = l.replace('"',"").split("_")[0].strip()
								
                                                                if ".0" in l:
                                                                    pass
                                                                    
                                                                else:
                                                                    try:
                                                                            character_list.remove(l)
                                                                    except:
                                                                            print l

							words_spoken = k.split("<w xml")

							out.write(filename + "\t" + str(act_count) + "." + str(scene_count) + "\t" + str(len(character_list)) + "\t" + str(len(words_spoken)) + "\t" + " ".join(character_list) + "\n")

		
		
