'''calculate "word" totals for each play. These are slightly fuzzy, as stage directions, which may be the result
 of a compositorial hand, are given <w> status as well, but such words constitute *far* less than 1% of all words,
 and, one might assume, are distributed in a relatively normalized fashion, all of which means the analysis should
run fine even if one doesn't tweeze them out'''

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
			play_dict[play_title]["total_num_words"] = 0

		if int(chars_on_stage) != 0:
			play_dict[play_title]["total_num_words"] += int(num_words)

	with open("total_word_counts_by_play.txt","w") as out:
            for j in play_dict:
		out.write( str(j) + "\t" +  str( play_dict[j]["total_num_words"] ) + "\n" )

		