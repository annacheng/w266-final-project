# **Classification of China (PRC) State-Generated Sockpuppet Tweets on Twitter**
Anna Cheng and Jacob Barkow's submission for the W266 term project, involving the use of neural networks against BERTweet embeddings to detect whether tweets originated from a PRC-sponsored account.

## File Directory
README.md - You are here

data_processing - CSVs and associated processing notebook used for creation of datasets. Source data from Twitter's InfoSec releases were combined with manually crawled tweets to create the datasets.

follow-network - Notebook and python script used to retrieve a network of popular leftist Twitter accounts, used to create the "pro-China" dataset.

bertweet_embeddings - Notebook used to generate BERTweet embeddings of the source tweets alongside stored PyTorch tensors. The tensors needed to be persisted to disk due to resource limitations.

model - Notebooks involved in the formulation of the baseline model as well as architectural refinements.
