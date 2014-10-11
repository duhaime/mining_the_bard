library(ggplot2)

df <- read.table("gender_aggregated_values_by_play.txt",
                 header = T,
                 sep = "\t")

ggplot(df, aes(length, female_lines, color = genre, label=play, position='jitter')) + 
  geom_text(size=3) +
  opts(title = "Female Presence vs. Play Length in Shakespearean Drama") +
  xlab("Play Length (words)") + 
  ylab("Words Spoken by Females") +
  labs(fill="")