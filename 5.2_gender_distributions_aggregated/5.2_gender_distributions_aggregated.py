from __future__ import division

d = {}

with open("gender_identified_speaking_distributions.txt") as f:
    f = f.read().split("\n")
    for i in f:
        i_s = i.split("\t")
        
        if len(i_s) > 2:
        
            play = i_s[0]
            
            if play not in d.keys():
                d[play] = {}
                
            gender = i_s[6]
            
            if gender not in d[play].keys():
                d[play][gender] = int(i_s[2])
                
            else:
                d[play][gender] += int(i_s[2])
                
with open("gender_aggregated_values_by_play.txt","w") as out:
    for i in d:
    
        rel_freq_f = int(d[i]['female']) / int(d[i]['male'] + d[i]['female'])
        rel_freq_m = int(d[i]['male']) / int(d[i]['male'] + d[i]['female'])
        
        out.write( i + "\t" + str(d[i]['male']) + "\t" + str(d[i]['female']) + "\t" + str( rel_freq_m ) + "\t" + str( rel_freq_f ) + "\n" )