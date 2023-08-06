# Filename: pubfetch.py
# Author: Thomas H. Smith 2017

import xml.dom.minidom
import urllib2
from urllib2 import HTTPError, URLError
#from operator import itemgetter
from multiprocessing.dummy import Pool as ThreadPool
from tqdm import tqdm_notebook
import pandas as pd
from requests.exceptions import ReadTimeout


def _get_pub_count(term1_list, term2_list, title_abs_only=False,
                  return_IDs_list=False, return_link=True):
    if title_abs_only:
        suffix = '[TIAB]'
    else:
        suffix = ''

    term1_string = '(%s%s)' % (term1_list[0], suffix)
    if len(term1_list) > 1:
        for term in term1_list[1:]:
            term1_string = '%s OR (%s%s)' % (term1_string, term, suffix)
    if term2_list[0] == '':
        search_string = term1_string
    else:
        term2_string = '(%s%s)' % (term2_list[0], suffix)
        if len(term2_list) > 1:
            for term in term2_list[1:]:
                term2_string = '%s OR (%s%s)' % (term2_string, term, suffix)
        search_string = '(%s) AND (%s)' % (term1_string, term2_string)
    search_string = search_string.replace(' ', '+')
    return _get_esearch_data(search_string, return_IDs_list=False, return_link=True)



def _build_args_tuples(df_in, search_terms):
    # Build list of gene-specific search terms for each row to pass to get_pub_count function

    unique_genes = list(df_in.Gene.unique())
    print 'Building list of search strings for %d unique genes...' % len(unique_genes)
    args_tuples = []
    for gene in unique_genes:
        row = df_in[df_in.Gene == gene].reset_index().loc[0]
        try:
            term1_list = [str(x) for x in row.Synonyms]
            if len(term1_list) > 0:
                term1_list.append(gene)
            else:
                term1_list = [gene]
            args_tuples.append( (gene, term1_list, search_terms))
        except AttributeError:
            print 'Error getting synonyms/building search string for gene: %s' % gene
            args_tuples.append( (gene, [''], search_terms))
    return args_tuples

def _get_esearch_data(search_string, return_IDs_list=False, return_link=True):
    URL_PREFIX = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='
    LINK_URL_PREFIX = 'https://www.ncbi.nlm.nih.gov/pubmed/?term='
    if return_IDs_list == False:
        URL_SUFFIX = '&rettype=Count&retmode=json'
    else:
        URL_SUFFIX = '&retmax=100000'
    search_string = search_string.replace(' ', '+')
    url = '%s%s%s' % (URL_PREFIX, search_string, URL_SUFFIX)

    if return_IDs_list == False:
        s = urllib2.urlopen(url).read()
        i = s.find('count')
        count = int(s[i:].split(':')[1].split('"')[1])
        if return_link:
            link_url = '=HYPERLINK("%s%s",%d)' % (LINK_URL_PREFIX, search_string, count)
            return (count, link_url)
        else:
            return count


# called by each thread
def _thread_helper_func(args_tuple):
    gene, term1_list, search_terms = args_tuple
    count, link = _get_pub_count(term1_list, search_terms, return_link=True)
    return {'Gene': gene, 'Count_link':link, 'Count':count}


def build_pubcount_df(df_in, search_terms, col_name):
    args_tuples = _build_args_tuples(df_in, search_terms)
    print 'Getting data from PubMed...'
    pool = ThreadPool(32)
    results = pool.map(_thread_helper_func, args_tuples)
    df_db = pd.DataFrame(results)
    df_db.set_index('Gene', inplace=True)
    df_db[col_name] = df_db['Count_link']
    df_db.drop(['Count_link'], inplace=True, axis=1)
    #df_db[col_name].apply(lambda x: _shorten_large_links(x))
    return df_db

