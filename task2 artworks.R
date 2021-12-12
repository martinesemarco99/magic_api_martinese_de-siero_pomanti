df= read.csv('art1000.csv')

library(ggplot2)
library(dplyr)
##### HISTOGRAMS
# Marginal distribution of colorfulness
df %>%
  ggplot(aes(x= colorfulness, y= ..density.., color= I('white'), fill= I('skyblue2'))) +
  geom_histogram()+
  theme_bw()

# Distribution of colorfulness by artist_title
df%>%
  ggplot(aes(x= colorfulness, y= ..density.., color= I('white'), fill= artist_title)) +
  geom_histogram(position='identity')+
  theme_bw()

##### BOXPLOT
# boxplot of colorfulness by artist_title
df %>% 
  ggplot(aes(x = artist_title, y = colorfulness, fill = I("skyblue2"))) + geom_boxplot(position = "dodge") +
  labs(x = "") +
  theme_bw()

#### SCATTERPLOT
#scatterplot for correlation between colorfulness and id artists
df %>% 
  ggplot(aes(x = colorfulness, y = artist_id)) + geom_point()

#scatterplot for correlation between id artworks and id artists
df %>% 
  ggplot(aes(x = id, y = artist_id)) + geom_point()

### BUBBLEPLOT
df %>% 
  ggplot(aes(x = id, y = artist_id, color = place_of_origin)) + 
  geom_point() +
  scale_color_brewer(palette = "Set1") +
  theme_bw()

#Histogram for distribution of date_end artworks
df %>%
  ggplot(aes(x= date_end, y= ..density.., color= I('white'), fill= I('skyblue2'))) +
  geom_histogram()+
  theme_bw()

# Distribution of date_end by artist_title
df%>%
  ggplot(aes(x= date_end, y= ..density.., color= I('white'), fill= artist_title)) +
  geom_histogram(position='identity')+
  theme_bw()

# boxplot of date_end by artist_title
df %>% 
  ggplot(aes(x = date_end, y = artist_title, fill = I("skyblue2"))) + geom_boxplot(position = "dodge") +
  labs(x = "") +
  theme_bw()

#scatterplot for correlation between date_end and id artists
df %>% 
  ggplot(aes(x = date_end, y = artist_id)) + geom_point()

# Marginal distribution of colorfulness
df$is_zoomable = ifelse(df$is_zoomable== 'True',1,0)
df %>%
  ggplot(aes(x= is_zoomable, y= ..density.., color= I('white'), fill= I('skyblue2'))) +
  geom_histogram()+
  theme_bw()

# Distribution of artist_title by is_zoomable
df%>%
  ggplot(aes(x= artist_title, y= is_zoomable, color= I('white'))) +
  geom_col(position='identity')+
  theme_bw()

#scatterplot for correlation between is_zoomable and id artists
df %>% 
  ggplot(aes(x = is_zoomable, y = artist_id)) + geom_point()


