The sentiment analysis project is aimed at analyzing or extracting sentiments from text. With so many ways in which people can interact with products and services, obtaining reliable feedack on a product or service has always been important to the provider.

As such,using text as input, the project works to output corresponding sentimentin form of polarity and subjectivity. In addition,  the project also analyses the similarity of the text to aid with sentiment analysis.


To achieve this, the project has used the following libraries:spacy, pandas and textblob. The text input, in our case, has been provided from amazon dataset included in the repo.

We provide an example of output for the text: 'alexa well young sister love new skill great'.

output: (Sentiment(polarity=0.3840909090909091, subjectivity=0.5511363636363636), 'alexa well young sister love new skill great')

The interpretation is that the text, 'alexa well young sister love new skill great', has polarity of 0.3484 with subjectivity of 0.5511.
