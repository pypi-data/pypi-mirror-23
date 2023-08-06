
    In text clustering, sometimes the output of a k-means analysis may not be intuitive. This
    function is designed to identify the main criteria of a cluster by identifying the top bi-gram
    associated with each cluster.

    This function creates a DataFrame of each cluster and their top bigram. It does this by
    creating a subset of each cluster, and then creates bigrams for each individual row.
    Those bigrams are joined together into a list, and then run through a counter to
    identify the top bigram.

    Parameters
    --------------
    dataset : DataFrame
        the dataframe being used as an input. At a minimum, it should have two fields: the cluster output and the text fed for clustering
    cluster_loop : string
        the title of the field that records the different clusters output
    row_loop : string
        the title of the field that includes the text for identifying the bigram (can be raw or preprocessed)
    stopwords : bool (optional)
        if True, use stoplist to strip text

    Returns
    ---------
    top_gram :
        returns a DataFrame with 2 columns: the cluster title and a tuple including the topbigram and its count
