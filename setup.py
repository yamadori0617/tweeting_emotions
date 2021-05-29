setup(
    name='tweeting_emotions',
    version='0.0.1',
    description='Analyze the sentiment towards keywords from twitter.',
    long_description=readme,
    author='Yamadori0617',
    url='https://github.com/yamadori0617/tweeting_emotions',
    install_requires=[
        "oseti",
        "tweepy",
        "collections",
        "mecab-python3"
    ],
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)