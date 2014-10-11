library(lattice)
library(ggplot2)

##########################################################################################
#################### Plot Shakes #######################################################
##########################################################################################

df <- read.table("mean_char_values_by_genre.txt",
                 header = F,
                 sep = "\t")

ggplot(df, aes(V2, V3, fill=V1)) + 
  geom_bar(stat = "identity") +
  facet_wrap(~V1, ncol = 1, scales = "fixed") + 
  opts(title = "Characters on Stage in Shakespearean Drama") + 
  xlab("Characters on Stage") + 
  ylab("Fraction of Play (Mean by Genre)") +
  labs(fill="")