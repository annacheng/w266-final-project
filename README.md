# **Classification of China (PRC) State-Generated Sockpuppet Tweetsr**
Anna Cheng and Jacob Barkow's submission for the W266 term project, involving the use of neural networks against BERTweet embeddings to detect whether tweets originated from a PRC-sponsored account.

## File Directory
README.md - You are here

* `bertweet_embeddings` - Notebook used to generate BERTweet embeddings of the source tweets alongside stored PyTorch tensors. The tensors needed to be persisted to disk due to resource limitations.

* `data` - CSVs and associated processing notebook used for creation of datasets. Source data from Twitter's InfoSec releases were combined with manually crawled tweets to create the datasets. **Note that the raw data files from Twitter are not included in this repo as they are too large for Github's data limits.**

* `follow-network` - Notebook and python script used to retrieve a network of popular leftist Twitter accounts, used to create the "pro-China" dataset.

*  `model` - Notebooks involved in the formulation of the baseline model as well as architectural refinements.

* `sentiment-analysis` - Notebook and CSV for Appendix A (proving dataset comparability using Sentiment Analysis).
