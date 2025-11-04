allPosts = [
    {'id': 1, 'text': 'I LOVE the new #GuiPhone! Battery life is amazing.'},
    {'id': 2, 'text': 'My #GuiPhone is a total disaster. The screen is already broken!'},
    {'id': 3, 'text': 'Worst customer service ever from @GuPhoneSupport. Avoid this.'},
    {'id': 4, 'text': 'The @GuPhoneSupport team was helpful and resolved my issue. Great service!'}
]

PUNCTUATION_CHARS = '!"#$%&\'()*+,-./::<=>?@[\\]^_`{|}~'
STOPWORDS_SET = {'i', 'me', 'my', 'a', 'an', 'the', 'is', 'am', 'was', 'and', 'but', 'if', 'on', 'to', 'of', 'at', 'by', 'for', 'with', 'this', 'that'}
POSITIVE_WORDS_SET = {'love', 'amazing', 'great', 'helpful', 'resolved'}
NEGATIVE_WORDS_SET = {'disaster', 'broken', 'worst', 'avoid', 'bad'}

def PreProcessText(text, punctuationList, stopWordsSet):
    clean_text = ""
    final_text = ""
    text = text.lower()
    for ch in text:
        if ch not in punctuationList:
            clean_text += ch
    words = clean_text.split()
    for w in words:
        if w not in stopWordsSet:
            final_text += w + " "
    return final_text

def AnalyzePosts(postsList, punctuation, stopwords, positive, negative):
    newList = []
    for post in postsList:
        text = PreProcessText(post['text'], punctuation, stopwords)
        score = 0
        for word in text.split():
            if word in positive:
                score += 1
            elif word in negative:
                score -= 1
        newList.append({
            'id': post['id'],
            'text': post['text'],
            'processedText': text.strip(),
            'score': score
        })
    return newList

def GetFlaggedPosts(posts, sentimentThreshold=-1):
    flagged = []
    for post in posts:
        if post['score'] <= sentimentThreshold:
            flagged.append(post)
    return flagged

def FindNegativePosts(flaggedPosts):
    result = {}
    for post in flaggedPosts:
        text = post['text']
        words = text.split()
        for word in words:
            if "@" in word or "#" in word:
                if word not in result:
                    result[word] = 0
                result[word] += 1
    return result

text = "PAI  is kesy !@ (prhen?"
res = PreProcessText(text, PUNCTUATION_CHARS, STOPWORDS_SET)
print(res)

posts = AnalyzePosts(allPosts, PUNCTUATION_CHARS, STOPWORDS_SET, POSITIVE_WORDS_SET, NEGATIVE_WORDS_SET)
for p in posts:
    print(p)

flagged = GetFlaggedPosts(posts)
for f in flagged:
    print(f)

negatives = FindNegativePosts(flagged)
print(negatives)
