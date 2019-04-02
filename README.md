# Anorexia
**DETECTION OF ANOREXIA USING SOCIAL MEDIA POSTS**
The project is being developed for CLEF eRisk2019 
We were given huge chunks of unprocessed data in the form of xml files
Chunks of test and training data were given.Considerable amount of time was spent on pre processing the information.

The clumsy nature of the dataset paved way for a lot of noise. A simple sentiment analysis model using eisting inbuilt functions could not be used in that situation.
Eg. A statement of a user may indicate a negative score in inbuilt sentiment analysis functions, but may not indicate the presence of anorexia.

Yet another problem faced was, the number of positive samples were extremely low as opposed to negative samples.
NLP techniques were used to rebuilt sentences after generating synonyms.

Deep Learning was performed.Project uses Neural Machine Translation to make prediction predominantly.
Keywords were identified pertaining to anorexia using Tf-Idf and a dictionary was built and used for analyzing sentiments thus moving towards an Ensemble approach including deep learning

**FILES**
FEW OF THE FILES USED IN THE PROJECT HAVE BEEN UPLOADED
1)sentin.py : Sentiment analyzer built specific to anorexia
2)Synonym_generator.py : Used to boost positive samples by framing new sentences using synonyms of adjectives.
3)Initial_preprocess.py : One of the many pre processing codes written
