import tweepy
import collections
from twitter_api import get_tweets
from emotion_scores import tweets_scoring


def main() -> None:
    try:
        keyword = input("keyword: ")
        count = int(input("searches count: "))

        tweets = get_tweets(keyword, count)
        emotion_sum_scores, positive_words, negative_words = tweets_scoring(tweets)
        positive_words_counter = sorted(collections.Counter(positive_words).items(),
                                        key=lambda x: x[1], reverse=True)[:10]
        negative_words_counter = sorted(collections.Counter(negative_words).items(),
                                        key=lambda x: x[1], reverse=True)[:10]

        positive_ratio, negative_ratio, normal_ratio = 0,0,0
        for emotion_sum_score in emotion_sum_scores:
            if emotion_sum_score > 0:
                positive_ratio += 1
            elif emotion_sum_score < 0:
                negative_ratio += 1
            else:
                normal_ratio += 1

        print()
        print("positive words: \n{}".format(positive_words_counter))
        print("negative_words: \n{}".format(negative_words_counter))
        print("-------------------------------")
        print("positive: {}/{}".format(positive_ratio, count))
        print("negative: {}/{}".format(negative_ratio, count))
        print("normal  : {}/{}".format(normal_ratio, count))
        print("score   : {}".format(sum(emotion_sum_scores) / count))

    except ValueError as e:
        print('Enter an integer for count.')

    except tweepy.TweepError as e:
        print('The API token may be wrong.')


if __name__ == "__main__":
    main()
