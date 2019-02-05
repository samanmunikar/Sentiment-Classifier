
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for ch in word:
        if ch in punctuation_chars:
            clean_word = word.replace(ch,"")
            return strip_punctuation(clean_word)
    return word
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
#print(positive_words)
def get_pos(sentence):
    pos_cnt = 0
    words = sentence.strip().split()
    for word in words:
        clean_word = strip_punctuation(word)
        if clean_word in positive_words:
            pos_cnt = pos_cnt + 1
    return pos_cnt

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentence):
    neg_cnt = 0
    words = sentence.strip().split()
    for word in words:
        clean_word = strip_punctuation(word)
        if clean_word in negative_words:
            neg_cnt = neg_cnt + 1
    return neg_cnt

with open("project_twitter_data.csv", "r") as fileopener:
    with open("resulting_data.csv","w") as filewriter: 
        filewriter.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
        filewriter.write("\n")
        tweet_list = fileopener.readlines()[1:]
        for tweets_detail in tweet_list:
            tweet_info = tweets_detail.split(",")
            tweet_text = tweet_info[0]
            number_of_retweets = tweet_info[1]
            number_of_replies = tweet_info[2].rstrip()
            postive_tweet = get_pos(tweet_text)
            negative_tweet = get_neg(tweet_text)
            net_tweet = postive_tweet-negative_tweet
            row_string = '{},{},{},{},{}'.format(number_of_retweets, number_of_replies, postive_tweet, negative_tweet, net_tweet)
            filewriter.write(row_string)
            filewriter.write('\n')