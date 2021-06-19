import oseti
import itertools


def tweets_scoring(tweets: list) -> int:
    analyzer = oseti.Analyzer()
    emotion_scores = []
    positive_words = []
    negative_words = []

    for tweet in tweets:
        try:
            tweet_text = tweet.full_text
            emotion_dicts = analyzer.analyze_detail(tweet_text)
            emotion_scores.append(sum(
                [emotion_dict['score'] for emotion_dict in emotion_dicts]))
            for emotion_dict in emotion_dicts:
                positive_words.append(emotion_dict['positive'])
                negative_words.append(emotion_dict['negative'])
        except IndexError as e:
            continue

    positive_words = list(itertools.chain.from_iterable(positive_words))
    negative_words = list(itertools.chain.from_iterable(negative_words))
    return emotion_scores, positive_words, negative_words


def texts_scoring(texts: list) -> int:
    analyzer = oseti.Analyzer()
    emotion_scores_list = [analyzer.analyze_detail(text) for text in texts]
    emotion_sum_scores = []
    for emotion_scores in emotion_scores_list:
        emotion_sum_scores.append(sum(
            [emotion_score['score'] for emotion_score in emotion_scores]))

    return emotion_sum_scores


def main():
    text = input("text: ")
    print("\n{}".format(texts_scoring([text])))


if __name__ == "__main__":
    main()
