import re
import MeCab


tagger = MeCab.Tagger("-Owakati")


def parse_tweets(tweets: list) -> list:
    parse_texts = []
    for tweet in tweets:
        tweet_text = tweet.full_text
        tweet_text = re.sub(r'^(RT @).*?:', '', tweet_text)
        tweet_text = re.sub(r'@(TO_)?.*? ', '', tweet_text)
        tweet_text = re.sub(r"http\S+", "", tweet_text)
        tweet_text = re.sub(r'(https?://[\w/:%#\$&\?\(\)~\.=\+\-]+)', '', tweet_text)
        tweet_text = re.sub(r'[!-/:-@＠️️★☆*＊#＃️[-`{-~¢-¿“-⟿⬀-⯐、、。　-〶\u3099-ゞ・-ヾ㈠-㏿︐-﹪！-／：-［-｀｛-･ﾞﾟ￥|｜「」《》≪≫【】《》]', '', tweet_text)
        # parse_texts.append(tagger.parse(tweet_text).strip().split())
        parse_texts.append(tagger.parse(tweet_text).strip())
    return parse_texts


def parse_text(text: str) -> list:
    return tagger.parse(text)


def main() -> None:
    text = input("text: ")
    print("\n{}".format(parse_text(text)))


if __name__ == "__main__":
    main()
