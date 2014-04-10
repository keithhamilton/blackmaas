#!/usr/bin/python

import words
import random


def generate(paragraph_count=4,sentence_variance=0,enochian=False,enochian_weight=1):
    sentence_length_min = 5 - sentence_variance
    sentence_length_max = 15 + sentence_variance
    paragraph_sentence_count_min = 2
    paragraph_sentence_count_max = 6
    paragraphs = []
    generated_text = []

    # create a word list to hold the words that will be used
    # to create the text
    word_list=[]
    word_list+=words.SATANIC
    # if enochian is True, include the enochian word list
    # the number of times declared by enochian_weight
    if enochian:
        while enochian_weight >= 1:
            word_list+=words.ENOCHIAN
            enochian_weight -= 1

    # shuffle the word order
    random.shuffle(word_list)

    while paragraph_count > 0:
        # decrement
        paragraph_count -= 1

        paragraph = []
        paragraph_sentence_count = random.randint(paragraph_sentence_count_min,paragraph_sentence_count_max)

        while paragraph_sentence_count > 0:
            # decrement
            paragraph_sentence_count -= 1

            sentence = []
            sentence_length = random.randint(sentence_length_min,sentence_length_max)

            previous_word_index = 0

            while sentence_length > 0:
                # decrement
                sentence_length -= 1
                index = random.randint(0,len(word_list)-1)
                # if the chosen index is the same as the previous index,
                # choose a new index
                while index == previous_word_index:
                    index = random.randint(0,len(word_list)-1)

                previous_word_index = index
                # add the word to the sentence array
                sentence.append(word_list[index])

            sentence[0] = '%s%s' % (sentence[0][0].upper(),sentence[0][1:])
            paragraph.append('%s.' % " ".join(sentence))

        paragraphs.append(' '.join(paragraph))
             
    generated_text.append('<br/><br/>'.join(paragraphs))

    generated_text[0] = 'Satan ipsum %s%s' % (generated_text[0][0].lower(),generated_text[0][1:])
    
    return ''.join(generated_text)

if __name__ == '__main__':
    print(generate())