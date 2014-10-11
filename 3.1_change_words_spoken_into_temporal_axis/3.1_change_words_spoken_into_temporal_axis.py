
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

with open("words_as_y_axis.txt","w") as out:
	with open("shakespeare_character_counts_by_scene.txt") as f:
		current_play = ''
		f = f.read().split("\n")
		for i in f:
			i_s = i.split("\t")

			if len(i_s) > 2:
				play = i_s[0]
				scene = i_s[1]
				words = int(i_s[3])

				#for the first line:
				if current_play == "":
					current_play = play
					current_play_words = 0
                                        current_word_num = 0

				elif play != current_play:
					current_play = play
					current_play_words = 0
                                        current_word_num = 0
			
				
				#we want to exclude the final exeunt of each scene:
				if int(i_s[2]) != 0:
                                        for j in xrange(words):
                                            current_word_num += 1
                                            
                                            out.write( play + "\t" + i_s[1] + "\t" + i_s[2] + "\t" + str(current_word_num) + "\t" + str(metadata_dict[play]["genre"]) + "\t" + str(metadata_dict[play]["first_performance"]) + "\t" + str(metadata_dict[play]["title"]) + "\n" )
                                
					current_play_words += words
					
			

			

		