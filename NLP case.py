import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.stem import PorterStemmer
import string
# nltk.download()
from nltk.corpus import wordnet as wn
text_file = open("NLP_case.txt")
text = text_file.read()
#nltk.download('punkt')
# print(type(text))
print(text)
# print(len(text))
sentences = sent_tokenize(text)
split_sen =[]
punctuation_string = string.punctuation
# print("All Punctuations：", punctuation_string)
# for i in punctuation_string:
#     stri = stri.replace(i, '')
# print(stri)
pos_pattern = ['DT NN NN', 'NP']
comparative_List = ['less than', 'more than', 'minimum', 'maximum', 'greater than', 'bigger than', 'larger than', 'smaller than']
Negation_list = ['not', 'no']
Quantity_unit = ['CD NN']
NN_list = ['JJ VBN JJ JJ VBG NN','NNP NN NN NN NN','NN NN NN NNS','JJ JJ JJ NN', 'RB VBN NN NN', 'RB VBN NNP NN', 'JJ JJ NN NN', 'JJ NN NN NN', 'NNP NNP NNP NNP',
           'RB VBN JJ NN', 'NNP NN NN NNS', 'NN VBG NN', 'RB JJ NNS','JJ VBG NN', 'VBN NN NN', 'VBN NN NNS', 'NNP NN NN', 'NNP VBD NNS', 'JJ JJ NN', 'NN NN NN', 'NN NN NNS', 'NNP NNP NNP', 'JJ JJ NNS', 'JJ NN NN','JJ NN NNS',
           'NNP NNS', 'VBG NN', 'NNP NNP', 'VBG NN', 'VBN NN','JJ NNS','JJS NN',  'NN NN',  'VBN NNS','JJ NN', 'NN NNS', 'NNS', 'NNP', 'NN','VBG']
print("POS NP_Patterns are ", NN_list)
print('\n')
sentences_no_punc = []
for sen in sentences:
    print(sen)
    for i in punctuation_string:
        sen = sen.replace(i, '')
    sentences_no_punc.append(sen)
# print(sentences)
    words = word_tokenize(sen)
# print(len(words))
    print(words)
    tag = nltk.pos_tag(words)
    print(tag)
    print("\n")
    split_sen.append(tag)

pos_sen = []
# print(split_sen[0])
for sen in split_sen:
    pos_w = []
    for ww in sen:
        pos_w.append(ww[1])
    pos_sen.append(pos_w)

for item in pos_sen:
    print(item)

print('\n')

for sen in sentences_no_punc:
    print('The original sentence:', sen)
    for com_list in comparative_List:
        if str(sen).find(str(com_list)) >=0:
            print('Extract Comparative Relation: ')
            sen = sen.replace(str(com_list), '')
            print(sen, 'Extract -> \"', com_list, '\" As comparative_List')
    print('\n')
    for nn in Negation_list:
        if str(sen).find(str(nn)) >=0:
            print('Extract Negation words: ')
            sen = sen.replace(str(nn), '')
            print(sen, 'Extract -> \"', nn, '\" As Negation_list')

    words = nltk.pos_tag(word_tokenize(sen))
    # print(words)
    print('\n')
    for word in words:
        if word[1] == 'CD':
            # print(words[words.index(word): words.index(word)+2])
            # print(words[words.index(word)+1])
            sen = sen.replace(word[0] + ' ' + words[words.index(word)+1][0], '')
            print('Extract Quantity data and measure unit:')
            print(sen, 'Extract -> \"', word[0]+ ' ' + words[words.index(word)+1][0], '\" As Quantity data and measure unit' )
    print('\n')
    words = nltk.pos_tag(word_tokenize(sen))
    for word in words:
        if word[1] == 'MD' and str(sen).find(str(word[0])) >=0:
            sen = sen.replace(word[0] + ' ' + words[words.index(word)+1][0], '')
            print('Extract Verb phrase')
            print(sen, 'Extract -> \"', word[0]+ ' ' + words[words.index(word)+1][0], '\" As Verb Phras' )
    print('\n')
    words = nltk.pos_tag(word_tokenize(sen))
    left_sen = ''
    left_sen_tag = ''
    for word in words:
        left_sen_tag= left_sen_tag + ' ' + str(word[1])
        left_sen = left_sen + ' ' + str(word[0])
    print(left_sen_tag)
    print(left_sen)
    for pos in NN_list:
        # print(pos)
        if left_sen_tag.find(str(pos)) >=0:
            print(pos) #left_sen_tag.index(str(pos)),
            # print(str(left_sen_tag[0:left_sen_tag.index(str(pos))]).count(' '))
            left_sen_tag = left_sen_tag.replace(str(pos), '', 1)
            # sen = sen.replace(word[0] + ' ' + words[words.index(word)+1][0], '')



    print('\n')



# emp_list =[]
# print(pos_sen[0])
# print(str(pos_pattern[0]))
# for item_sen in pos_sen:
#     for item in item_sen:
#         if str(pos_pattern[0]).find(str(item))>= 0:
#             emp_list.append(item)
#             print(item)
    # else: print(emp_list)

# from nltk.probability import FreqDist
# fdist = FreqDist(words)
# print(fdist.most_common(10))



# words_no_punc = []
# for w in words:
#     if w.isalpha():
#         words_no_punc.append(w.lower())
#
# print(words_no_punc)
print("\n")
# print(len(words_no_punc))

# from nltk.probability import FreqDist
# fdist = FreqDist(words_no_punc)
# print(fdist.most_common(10))
#fdist.plot(10)

#nltk.download('stopwords')
# from nltk.corpus import stopwords
# stopwords = stopwords.words("english");
# print(stopwords);
#
# porter = nltk.PorterStemmer()
# word_list =["study","studying", "studies", "studied","became"]
#
# for w in word_list:
#     print(porter.stem(w))
# print('\n')
#
# from nltk.stem import SnowballStemmer
# snowball = SnowballStemmer("english")
# word_list =["study","studying", "studies", "studied"]
#
# for w in word_list:
#     print(snowball.stem(w))
#
# print(SnowballStemmer.languages)
#
# #nltk.download('wordnet')
# from nltk import WordNetLemmatizer
# lemma = WordNetLemmatizer()
# word_list =["study","studying", "studies", "studied"]
# for w in word_list:
#     print(lemma.lemmatize(w))
# print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
# word_list =["study","studying", "studies", "studied"]
# for w in word_list:
#     print(lemma.lemmatize(w, pos='v'))
# # v- verb n- Noun a- adjective r- adverb
#
# #pos tagging
# #nltk.download('averaged_perceptron_tagger')
# # tag = nltk.pos_tag(["studying", "study"])
# # print(tag)
# #
# # sentence = "building information modelling (BIM) models contain multiple dimensions of building information, including building design data, construction information, and maintenance-related contents,which are related with different engineering stakeholders."
# # tokenized_words = word_tokenize(sentence)
# # print(tokenized_words)
# # # for words in tokenized_words:
# # #chunking
# # grammer= "NP : {<DT>?<JJ>*<NN>}"
# # parser = nltk.RegexpParser(grammer)
# # output = parser.parse(tagged_words)
# # print(output)
# # output.draw()
#
# # from nltk.corpus import treebank
# # t = treebank.parsed_sents('wsj_0001.mrg')[0]
# # t.draw()

#semantic similarity
from nltk.corpus import wordnet
# for words in wordnet.synsets("joint"):
#     for lemma in words.lemmas():
#         print(lemma)
#     print("\n")

word1 = wordnet.synsets('room', 'n')
print(word1)
word2 = wordnet.synsets('bedroom', 'n')
print(word2)
scores =0
print(word1[0].wup_similarity(word2[0]))
w1 =[]
ww2= []
for w in word1:
    for ww in word2:
        if w.wup_similarity(ww)> scores:
            scores = w.wup_similarity(ww)
            w1 = w
            ww2 = ww
print(scores, w1, ww2)
print("\n")
# word1 = wordnet.synsets('opening', 'n')[0]
# # print(word1)
# word2 = wordnet.synsets('window', 'n')[0]
# inst:IfcElementQuantity_69， inst:IfcRelDefinesByProperties_184 210 212 214 216 218
# inst:IfcRelContainedInSpatialStructure_37715
# # print(word2)
# print(word1.wup_similarity(word2))

#
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# # nltk.download('punkt') # if necessary...
#
# stemmer = nltk.stem.porter.PorterStemmer()
# remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
#
# def stem_tokens(tokens):
#     return [stemmer.stem(item) for item in tokens]
#
# # '''remove punctuation, lowercase, stem'''
# def normalize(text):
#     return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))
#
# vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
#
# def cosine_sim(text1, text2):
#     tfidf = vectorizer.fit_transform([text1, text2])
#     return ((tfidf * tfidf.T).A)[0,1]
#
#
# print(cosine_sim('a little bird', 'a little bird'))
# print (cosine_sim('a little bird', 'a little bird chirps'))
# print (cosine_sim('low cost medical insurance', 'cheap health insurance'))
# # print (cosine_sim('habitable room', 'living room'))
# #
# # from gensim.test.utils import common_texts
# # from gensim.models import Word2Vec
# #
# # model = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)
# # model.save("word2vec.model")
# # print(model.wv.most_similar('cheap','inexpensive') )
#
# sentence="Hello Guru99, You had to build some very good sites and I love visiting your site."
# words = word_tokenize(sentence)
# ps = PorterStemmer()
# for w in words:
# 	rootWord=ps.stem(w)
# 	print(rootWord)
