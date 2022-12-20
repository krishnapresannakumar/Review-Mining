# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:16:24 2018

@author: krishna
"""

import re
import csv
import numpy as np
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize  
import pandas as pd
import nltk
from nltk.corpus import sentiwordnet as swn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from lxml import html  
import requests
import csv
import json
analyser = SentimentIntensityAnalyzer()
def ReadAsin():
    reviews_df=[]
    k=[]
    
    amazon_url = 'https://www.amazon.in/Apple-iPad-Tablet-inch-Wi-Fi/product-reviews/'+asin+'/ref=cm_cr_arp_d_paging_btm_'+str(i)+'?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    
    headers = {'User-Agent': user_agent}
    page = requests.get(amazon_url, headers = headers)
    parser = html.fromstring(page.content)
    xpath_reviews = '//div[@data-hook="review"]'
    reviews = parser.xpath(xpath_reviews)
    xpath_rating  = './/i[@data-hook="review-star-rating"]//text()' 
    xpath_title   = './/a[@data-hook="review-title"]//text()'
    xpath_author  = './/a[@data-hook="review-author"]//text()'
    xpath_date    = './/span[@data-hook="review-date"]//text()'
    xpath_body    = './/span[@data-hook="review-body"]//text()'
    xpath_helpful = './/span[@data-hook="helpful-vote-statement"]//text()'
    for review in reviews:
        rating  = review.xpath(xpath_rating)
        review_rating = ''.join(rating).replace('out of 5 stars','')
        title   = review.xpath(xpath_title)
        author  = review.xpath(xpath_author)
        date    = review.xpath(xpath_date)
        body    = review.xpath(xpath_body)
        helpful = review.xpath(xpath_helpful)
        k.append(body)
    return(k)

#from nltk.stem import WordNetLemmatizer
#from nltk.corpus import wordnet as wn
#from nltk import sent_tokenize, word_tokenize
stop = stopwords.words('english')
def print_sentiment_scores(sentence):
                    neg=[]
                    pos=[]
                    snt = analyser.polarity_scores(sentence)
                    print("{:-<40} {}".format(sentence, str(snt)))
                    for key,val in snt.items():
                        neg = snt.get('neg', val)
                        pos = snt.get('pos', val)
                    return neg ,pos                     
def process_text(text):
 
    #text = text.lower()
    text = text.replace(',', ' ')
    text = text.replace('/', ' ')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.replace('.', ' ')
    return text.split()
    # Convert text string to a list of words
    return 
def generate_ngrams(words_list, n):
    ngrams_list = []
 
    for num in range(0, len(words_list)):
        ngram = ' '.join(words_list[num:num + n])
        ngrams_list.append(ngram)
 
    return ngrams_list
if __name__ == '__main__':
        stop = stopwords.words('english')
        df=[]
        asin=input("enter the product id:")
        z=input("enter the number of pages:")
        fieldnames = ['Rating','Title','Date','Reviews']
        with open('Reviews.csv', 'w',newline='',encoding='utf-8') as f:
            dict_writer = csv.writer(f)
            dict_writer.writerow(fieldnames)
        for i in range(1,int(z)+1):
            print("________________________"+str(i))
            print("_______________________________")
            df=ReadAsin()
            #print(df)
# Read in the data
            df3 = pd.DataFrame({'col':df})
            #print (df3)
            #print("Reviews are flitered according to the Ratings")
        #df3=pd.read_csv('Reviews.csv',encoding='utf-8')
            df3.columns = ["Reviews"]
            df3.Reviews= df3.Reviews.astype(str)
            df3['Reviews'] = df3['Reviews'].str.lower().str.split()
            stop = stopwords.words('english')
            df3['Reviews']=df3['Reviews'].apply(lambda x: [item for item in x if item not in stop]) 
            print(df3['Reviews'])
        #df3.to_csv("WithoutstopwordsReviews.csv", index=False, encoding='utf8')
            #text ='A quick brown fox jumps over the lazy dog.'
        #df4=pd.read_csv('WithoutstopwordsReviews.csv') # readlines() returns a list of items, each item is a line in your file
    #for line in df4['Reviews']:
        #l=len(line)
        #line=re.sub(r'[^a-zA-Z0-9\s]', ' ', line)
        #print(line)
            pos=0
            neg=0
            df = pd.read_csv('emoticons.csv',encoding='utf-8')
            df3['Reviews'].to_string()
            np.savetxt('out.txt', df3['Reviews'],fmt='%s',delimiter="\t",encoding='utf-8')
            with open("out.txt", "r",encoding='utf-8') as f:
                k=f.readlines()
                k = [item.replace("'", "") for item in k]
                k = [item.replace(",", "") for item in k]
                k = [item.replace("[", "") for item in k]
                k = [item.replace("]", "") for item in k]
                #print(k)
                for line in k:
                    text=line
                    print(text)
                    with open("Final Output.txt", "a",encoding='utf-8') as f:
                        f.write(text)
                    #text=df4['Reviews'].iloc[1]
            #print(df4.Reviews.str.replace("',", ""))
            #df4['Reviews'] = df4['Reviews'].replace({','}, regex=True)
            #print(df4['Reviews'].iloc[1])
        #text = 'A quick brown fox jumps over the lazy dog.'
        ######################################################################
                    
#print(df['Unicode'])
                    #row = ['not good 😭  😭 😭  ']
                        k=re.findall(r'[^\w\s,]', text)
                        print(k)
                        listlen=len(k)
                        #print(listlen)
                        val=0
                        for i in range(0,int(listlen)):
                            
                            ut=(k[i].encode('utf-8')) ###Convert the emoji to unicode
                            #print(ut)
                            ln=len(df['Code'])
                        #print(ln)
                            
                            for i in range(int(ln)):
                                p=df['Code'].iloc[i]
                                #print(ut)
                                #print(p)
                                if(str(ut)==str(p)):
                                    #print("same charater")
                                    q=df['Sentiment score'].iloc[i]
                                    print(q)
                                    val=val+df['Sentiment score'].iloc[i]
                                #print(val)
                            
                                else:
                                    val=val+0
                        print("The score for emoticons="+str(val))
            ######################################################################
                        words_list = process_text(text)
                        unigrams = generate_ngrams(words_list, 1)
                        #file3 = open("Unigramfile.txt","a")
                        #file3.write(str(unigrams)+'\n')
                        #print("sucess")
                        bigrams = generate_ngrams(words_list, 2)
                        #file4 = open("Bigramfile.txt","a")
                        #file4.write(str(bigrams)+'\n')
                        #print("sucess")
                        trigrams = generate_ngrams(words_list, 3)
                        #file5 = open("Trigramfile.txt","a")
                        #file5.write(str(trigrams)+'\n')
                        #print("sucess")
                        #print (unigrams)
                        posscore=0
                        negscore=0
                        neg_score=[]
                        pos_score=[]
                        for i in unigrams :
                            #print(i)
                            g = nltk.tag.pos_tag([i])
                            print(g)
                                 
                            for word, tag in g:
                                if tag.startswith('JJ'):
                                    new = 'a'
                                elif  tag.startswith('V'):
                                    new = 'v'
                                elif  tag.startswith('R'):
                                    new = 'r'
                                elif  tag.startswith('NN'):
                                    new = 'n'
                                else:
                                    new =''
                                if new != '':
                                    synsets = print_sentiment_scores(word)
                                    
                                    neg_score.append(synsets[0])
                                    pos_score.append(synsets[1])
                                    synsets=[]
                                    synsets = list(swn.senti_synsets(word, new))
                                    if(synsets):
                                        b  = synsets[0]
                                   
                                    
                                        posscore=posscore+b.pos_score()
                                        negscore=negscore+b.neg_score()
                   # print(posscore)
                   # print(negscore)
                                sent_score=[]
                                if posscore>negscore:
                                     obj=posscore-negscore
                                     print(i,obj,'POSITIVE')
                                     #n1=obj
                                     sent_score.append(obj)
                        
                                elif posscore<negscore:
                        
                        
                                     obj=posscore-negscore
                                     sent_score.append(obj)
                                     print(obj,'NEGETIVE')
                                     n1=obj
                                else:
                        
                                     sent_score.append('0')
                        
                                     print('NEUTRAL')
                                     #n1=obj
                                #print(sent_score)
                                    
                                    #print(synsets[0])
                                   
                                        #b  = synsets[3]
                                        #print("testing;;;;;;;;;;;")
                                        #print(b)
                                    
                                        #print(neg)
                                        #negscore=negscore+b.neg_score()
                   # print(posscore)
                   # print(negscore)
                                
                        for p in bigrams :
                                            #print(i)
                                            g = nltk.tag.pos_tag([p])
                                            #print(g)
                                                
                                            for word, tag in g:
                                                if tag.startswith('JJ'):
                                                    new = 'a'
                                                elif  tag.startswith('V'):
                                                    new = 'v'
                                                elif  tag.startswith('R'):
                                                    new = 'r'
                                                elif  tag.startswith('NN'):
                                                    new = 'n'
                                                else:
                                                    new =''
                                                if new != '':
                                                    synsets=[]
                                                    synsets = print_sentiment_scores(word)
                                                    
                                                    neg_score.append(synsets[0])
                                                    pos_score.append(synsets[1])
                                   # print(posscore)if new != '':
                                                    synsets = list(swn.senti_synsets(word, new))
                                                    if(synsets):
                                                        b  = synsets[0]
                                                   
                                                    
                                                        posscore=posscore+b.pos_score()
                                                        negscore=negscore+b.neg_score()
                                   # print(posscore)
                                   # print(negscore)
                                                #sent_score=[]
                                                if posscore>negscore:
                                                     obj=posscore-negscore
                                                     print(p,obj,'POSITIVE')
                                                     sent_score.append(obj)
                                                     n2=obj
                                                elif posscore<negscore:
                                        
                                        
                                                     obj=posscore-negscore
                                                     sent_score.append(obj)
                                                     print(obj,'NEGETIVE')
                                                     n2=obj
                                                else:
                                        
                                                     sent_score.append('0')
                                        
                                                     print('NEUTRAL')
                                   # print(negscore)
                                                
                        for i in trigrams :
                                                #print(i)
                                                    g = nltk.tag.pos_tag([i])
                                                    #print(g)
                                                       
                                                    for word, tag in g:
                                                        if tag.startswith('JJ'):
                                                            new = 'a'
                                                        elif  tag.startswith('V'):
                                                            new = 'v'
                                                        elif  tag.startswith('R'):
                                                            new = 'r'
                                                        elif  tag.startswith('NN'):
                                                            new = 'n'
                                                        else:
                                                            new =''
                                                        if new != '':
                                                            synsets=[]
                                                            synsets = print_sentiment_scores(word)
                                                            
                                                            neg_score.append(synsets[0])
                                                            pos_score.append(synsets[1])
                                           # print(posscore)synsets = list(swn.senti_synsets(word, new))
                                                            #print(i)
                                                    g = nltk.tag.pos_tag([i])
                                                    #print(g)
                                                         
                                                    for word, tag in g:
                                                        if tag.startswith('JJ'):
                                                            new = 'a'
                                                        elif  tag.startswith('V'):
                                                            new = 'v'
                                                        elif  tag.startswith('R'):
                                                            new = 'r'
                                                        elif  tag.startswith('NN'):
                                                            new = 'n'
                                                        else:
                                                            new =''
                                                        if new != '':
                                                            synsets = list(swn.senti_synsets(word, new))
                                                            if(synsets):
                                                                b  = synsets[0]
                                                           
                                                            
                                                                posscore=posscore+b.pos_score()
                                                                negscore=negscore+b.neg_score()
                                           # print(posscore)
                                           # print(negscore)
                                                        #sent_score=[]
                                                        if posscore>negscore:
                                                             obj=posscore-negscore
                                                             print(i,obj,'POSITIVE')
                                                             sent_score.append(obj)
                                                             n3=obj
                                                
                                                        elif posscore<negscore:
                                                
                                                
                                                             obj=posscore-negscore
                                                             sent_score.append(obj)
                                                             print(obj,'NEGETIVE')
                                                             n3=obj
                                                        else:
                                                
                                                             sent_score.append('0')
                                                             n3=obj
                                                
                                                             print('NEUTRAL')  
                        print("VADER POLARITY CALCULATION")
                        print("---------------------------")
                        #print(neg_score)
                        #print(pos_score)
                        Total_Pos=sum(pos_score)
                        Total_Neg=sum(neg_score)
                        if(Total_Pos<Total_Neg):
                            Total=Total_Neg
                            print("Vader Negative Polarity=")
                            print(Total)
                            
                        else:
                            Total=Total_Pos
                            print("Vader Positive Polarity=")
                            print(Total)
                        #print("Total positive score of the Review=")
                        #print(Total_Pos)
                        #print("Total negtive score of the Review=")
                        #print(Total_Neg)
                        
                        print("WORDNET POLARITY CALCULATION")
                        print("---------------------------")
                        #print(sent_score)
                        sent_score = list(map(int, sent_score))
                        Total_Polarity=sum(sent_score)
                        Total_Polarity=(Total_Polarity)
                        print("Total Polarity=")
                        print(Total_Polarity)
                        
                        if(Total_Pos<Total_Neg):
                            val=0
                        
                        else:
                            val=1
                        if (Total_Polarity<=0):
                            value=0
                        
                        else:
                            value=1   
                        if(val==0 or value==0 ):
                            neg=neg+1
                            with open("Negative Class.txt", "a",encoding='utf-8') as f:
                                f.write(text)
                                f.write("\nVader Negative polarity="+str(Total))
                                f.write("\nWordnet Polarity="+str(Total_Polarity))
                                f.write("\n_____________________________________\n")
                            print("\n------------------------\nClass=Negative\n------------------------\n")
                        else:
                            pos=pos+1
                            with open("Positive Class.txt", "a",encoding='utf-8') as f:
                                f.write(text)
                                f.write("\nVader  Positive polarity="+str(Total))
                                f.write("\nWordnet Polarity="+str(Total_Polarity))
                                f.write("\n_____________________________________\n")
                            print("\n------------------------\nClass=Positive\n------------------------\n")
                        
                        
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        print("-------------REVIEW POLARITY--------------")                            
                        print("------------------------------------------")
                        print("------------------------------------------") 
                        #print(bigrams)
                        #print(trigrams)
                        print("Total Number of Positive Review="+str(pos))
                        print("Total Number of Negative Review="+str(neg))       
                #print(df['Review'])
