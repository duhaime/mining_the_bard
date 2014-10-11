from __future__ import division

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

with open("total_word_counts_by_play.txt") as f:

    total_count_dict = {}
    
    f = f.read().split("\n")
    for i in f:
        i_s = i.split()
        if len(i_s) > 1:
            total_count_dict[i_s[0]] = i_s[1]
            
with open("normalized_words_by_char_counts_by_play.txt","w") as out:
    with open("words_by_char_count_by_play.txt") as g:
        g = g.read().split("\n")
        for j in g:
            j_s = j.split()
            
            if len(j_s) > 2:
            
                filename = j_s[0]
            
                total_words_for_play = total_count_dict[ j_s[0] ]
                
                normalized_word_count = (int(j_s[2]) /  int(total_words_for_play) )
                
                out.write(j_s[0] + "\t" + j_s[1] + "\t" + str(normalized_word_count) + "\t" + metadata_dict[filename]["genre"] + "\t" + metadata_dict[filename]["first_performance"] + "\t" + metadata_dict[filename]["title"] + "\n")