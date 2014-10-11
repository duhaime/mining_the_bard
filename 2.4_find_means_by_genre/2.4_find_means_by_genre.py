from __future__ import division

with open("normalized_words_by_char_counts_by_play.txt") as f:
    f = f.read().split("\n")
    
    genre_freqs = {}
    
    for i in f:
        i_s = i.split("\t")
        
        if len(i_s) > 2:
        
            if i_s[0] != "TNK.xml":
                play  = i_s[0]
                chars = i_s[1]
                freq  = i_s[2]
                genre = i_s[3]
                
                if genre not in genre_freqs.keys():
                    genre_freqs[genre] = {}
                    genre_freqs[genre]["play_count"] = 0
                    
                #kludge
                if play not in genre_freqs[genre].keys():
                    genre_freqs[genre][play] = "cello"
                    genre_freqs[genre]["play_count"] += 1
                    
                if chars not in genre_freqs[genre].keys():
                    genre_freqs[genre][chars] = 0
                        
                genre_freqs[genre][chars] += float(freq)
                    
with open("mean_char_values_by_genre.txt","w") as out:
    for j in genre_freqs:
        for k in genre_freqs[j]:
        
            if k == "play_count":
                print j, genre_freqs[j][k]
                
            else:
            
                #because play titles are all str, try to coerce to float. Only our freqs will be coerced, and the strings will be skipped, as desired
                try:
                    out.write ( j + "\t" + k + "\t" + str( float(genre_freqs[j][k]) / int(genre_freqs[j]["play_count"]) ) + "\n" )
                except:
                    pass