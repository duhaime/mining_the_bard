'''for each play, for each number of characters on stage during the play, find the number of words spoken while that
number of characters is on the stage. The prediction is that the relative frequency of words spoken while only a single
character is on stage will be greater in tragedies; rel. freqs. with large numbers of cast members on stage will
be more common in histories, and comedies will be somewhere in between.'''

with open("shakespeare_character_counts_by_scene.txt") as f:
	f = f.readlines()
	
	play_dict              = {}

	for i in f:
		i_s            = i.split("\t")
		play_title     = i_s[0]
		chars_on_stage = i_s[2]
		num_words      = i_s[3]

		if play_title not in play_dict.keys():
			play_dict[play_title] = {}

		if int(chars_on_stage) != 0:

			if chars_on_stage not in play_dict[play_title].keys():
				play_dict[play_title][chars_on_stage] = {}
				play_dict[play_title][chars_on_stage]["words_spoken"] = 0

			play_dict[play_title][chars_on_stage]["words_spoken"] += int(num_words)

	with open("words_by_char_count_by_play.txt","w") as out:	
		for j in play_dict:
			for k in play_dict[j]:
				#play_title, chars_on_stage, word_count 
				out.write( str(j) + "\t" + str(k) + "\t" + str( play_dict[j][k]["words_spoken"] ) + "\n" ) 		