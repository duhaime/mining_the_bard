library(lattice)
library(ggplot2)

##########################################################################################
#################### Plot Shakes  #######################################################
##########################################################################################

df <- read.table("normalized_words_by_char_counts_by_play.txt",
                 header = F,
                 sep = "\t",
                 quote="\'")

df$custom_order <- factor(df$V6, levels = c("2 Henry VI (1591)",
                                            "3 Henry VI (1591)",
                                            "Love's Labour Lost (1591)",
                                            "1 Henry VI (1592)",
                                            "The Comedy of Errors (1592)",
                                            "Richard III (1593)",
                                            "Two Gentlemen of Verona (1593)",
                                            "The Taming of the Shrew (1594)",
                                            "Titus Andronicus (1594)",
                                            "A Midsummer Night's Dream (1595)",
                                            "Richard II (1595)",
                                            "Romeo and Juliet (1595)",
                                            "King John (1596)",
                                            "The Merchant of Venice (1596)",
                                            "1 Henry IV (1597)",
                                            "2 Henry IV (1597)",
                                            "Much Ado about Nothing (1598)",
                                            "As You Like It (1599)",
                                            "Julius Caesar (1599)",
                                            "Henry V (1599)",
                                            "Twelfth Night (1600)",
                                            "The Merry Wives of Windsor (1600)",
                                            "Hamlet (1601)",
                                            "All's Well that Ends Well (1602)",
                                            "Troilus and Cressida (1602)",
                                            "Measure for Measure (1604)",
                                            "Othello (1604)",
                                            "King Lear (1605)",
                                            "Macbeth (1606)",
                                            "Antony and Cleopatra (1607)",
                                            "Timon of Athens (1607)",
                                            "Coriolanus (1608)",
                                            "Pericles (1608)",
                                            "Cymbeline (1609)",
                                            "The Winter's Tale (1610)",
                                            "The Tempest (1611)",
                                            "Henry VIII (1613)",
                                            "Two Noble Kinsmen (1613)"))


#use the which method to isolate df subset; e.g.: df[which(df$V4 == "History"),]
#pink = #F8766D ; green = #00BA38 ; blue = #619CFF
ggplot(df[which(df$V4 == "Tragedy"),], aes(V2, V3)) + 
  geom_bar(stat='identity', fill='#619CFF') +
  facet_wrap(~custom_order, ncol = 3, scales = "fixed") + 
  opts(title = "Characters on Stage in Shakespeare's Tragedies") + 
  xlab("Characters on Stage") + 
  ylab("Fraction of Play") +
  labs(fill="") +
  scale_fill_identity()

