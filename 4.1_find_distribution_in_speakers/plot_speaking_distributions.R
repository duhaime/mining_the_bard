library(ggplot2)
df <- read.table("speaking_distribution_by_play.txt",
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

# to analyze histories
df <- df[df$V1 %in% c("1H4.xml","2H4.xml","H5.xml","1H6.xml","2H6.xml","3H6.xml","R2.xml","R3.xml","Jn.xml","H8.xml"),]

# to analyze comedies
df <- df[df$V1 %in% c("Ado.xml","AWW.xml","AYL.xml","LLL.xml","MM.xml","MND.xml","MV.xml","Per.xml","Shr.xml","TGV.xml","Tmp.xml","TN.xml","TNK.xml","Wiv.xml","WT.xml"),]

# to analyze tragedies
df <- df[df$V1 %in% c("Ant.xml","Cor.xml","Cym.xml","Ham.xml","JC.xml","Lr.xml","Mac.xml","Oth.xml","Rom.xml","Tim.xml","Tit.xml","Tro.xml"),]

# used to create x-axis label restoring original name of role
roles <- function(x) sub("[^_]*_","",x )

#remove characters with fewer than n words from df for less crowded plots
threshold <- 100
df <- df[which(df$V3 > threshold),]

#pink = #F8766D ; green = #00BA38 ; blue = #619CFF
ggplot(cbind(df, V8=paste(df$V1,df$V2,sep="_")), aes(x=reorder(V8,V3), y=V3) ) + 
  geom_bar(stat = "identity",  fill='#619CFF') +
  facet_wrap(~ custom_order,  ncol=3, scales = "free_x") +
  labs(title = "Distribution of Speakers in Shakespeare's Comedies") + 
  xlab("Speaking Role") + 
  ylab("Words Spoken") +
  scale_x_discrete(labels=roles) +
  theme(axis.text.x=element_text(angle=90, hjust=1)) +
  labs(fill="")
