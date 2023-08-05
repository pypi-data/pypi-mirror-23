from __future__ import print_function
from __future__ import division

import topiceval.utils as utils
import topiceval.plotter as plotter
import topiceval.stats as stats

import numpy as np
import pickle

import logging


def proc_line(line):
    return map(int, line.strip().split(" "))


class BaseModel(object):
    """
    Base Class
    """

    def __init__(self, datasetname, id2word_dict=None, id2word_dict_path=None, corpus=None, corpus_path=None,
                 vocab_filepath=None, docword_filepath=None, vocab_size=None, num_docs=None, evaluation_mode=False,
                 Amatrix_needed=False):
        """
        Attributes:
        id2word_dict
        vocab_size
        A_matrix
        A_matrix_normalized
        num_docs
        avg_doc_size
        doc_lenghts
        vocab_corpus_frequency_list
        """
        self.datasetname = datasetname
        self.num_docs = num_docs
        self.vocab_size = vocab_size
        self.corpus = corpus
        self.representative_topic_tuples = []
        if id2word_dict is not None:
            self.id2word_dict = id2word_dict
        elif id2word_dict_path is not None:
            with open(id2word_dict_path, "rb") as handle:
                self.id2word_dict = pickle.load(handle)
        elif vocab_filepath is not None:
            utils.verify_filename(vocab_filepath)
            self.id2word_dict = self.make_id2word_dict(vocab_filepath)
        else:
            raise ValueError("Necessary to provide id2word_dict for printing topics and other methods.")
        if vocab_size is not None:
            assert (vocab_size == len(self.id2word_dict)), "Num words in id2word_dict dont match vocab size"
        self.vocab_size = len(self.id2word_dict)
        if evaluation_mode or Amatrix_needed:
            if corpus is not None:
                self.corpus = corpus
                self.num_docs, self.doc_lengths, self.avg_doc_size, \
                    self.vocab_corpus_frequency_list, self.vocab_document_frequency_list = self.read_corpus()
            elif corpus_path is not None:
                self.corpus = np.load(corpus_path)
                self.num_docs, self.doc_lengths, self.avg_doc_size, self.vocab_corpus_frequency_list, \
                    self.vocab_document_frequency_list = self.read_corpus()
            elif docword_filepath is not None:
                utils.verify_filename(docword_filepath)
                self.corpus, self.num_docs, self.doc_lengths, self.avg_doc_size, self.vocab_corpus_frequency_list, \
                    self.vocab_document_frequency_list = \
                    self.read_corpus_from_docword(docword_filepath=docword_filepath)
            else:
                raise ValueError("Necessary to provide either corpus, its filepath or docword filepath")
            if num_docs is not None:
                assert (num_docs == self.num_docs), \
                    "User given value of num_docs doesn't match inferred value from corpus"
            if Amatrix_needed:
                self.A_matrix = self.make_matrix_from_corpus()
            else:
                self.A_matrix = None
            logging.debug("basemodel: Vocab_size: %d, Num_docs: %d, avg_doc_size: %d"
                          % (self.vocab_size, self.num_docs, self.avg_doc_size))
        else:
            self.corpus, self.num_docs, self.doc_lengths, self.avg_doc_size, self.vocab_corpus_frequency_list, \
                self.vocab_document_frequency_list, self.A_matrix = [None]*7
        self.representative_topics_scores = []

    def make_id2word_dict(self, filepath):
        utils.verify_filename(filepath)
        id2word_dict = {}
        with open(filepath, "r") as vocab_file:
            for line_number, line in enumerate(vocab_file):
                word = line.strip()
                assert (word != ""), "Empty word encountered in vocabulary."
                id2word_dict[line_number] = word
        if self.vocab_size is not None and len(id2word_dict) != self.vocab_size:
            raise ValueError("Vocabulary size input does not match size of vocabulary in vocab_filepath")
        return id2word_dict, len(id2word_dict)

    def read_corpus(self):
        vocab_corpus_frequency_list = [0] * self.vocab_size
        vocab_document_frequency_list = [0] * self.vocab_size
        # TODO: Check that maximum vocab_id in corpus is == vocab_size

        if self.num_docs is not None and len(self.corpus) != self.num_docs:
            raise ValueError("corpus' column dimension do not match num_docs")

        num_docs = len(self.corpus)
        doc_lengths = []
        for doc in self.corpus:
            doc_lengths.append(sum([tup[1] for tup in doc]))
        doc_lengths = np.array(doc_lengths)
        avg_doc_size = np.mean(doc_lengths)

        for doc in self.corpus:
            for tup in doc:
                vocab_corpus_frequency_list[tup[0]] += tup[1]
                vocab_document_frequency_list[tup[0]] += 1

        # A_normalized = A / self.doc_lengths.reshape((1, -1)) * self.avg_doc_size
        # for j in range(num_docs):
        #     assert(round(sum(A[:, j]) - self.avg_doc_size, 7) == 0)
        return num_docs, doc_lengths, avg_doc_size, vocab_corpus_frequency_list, vocab_document_frequency_list

    def read_corpus_from_docword(self, docword_filepath):
        utils.verify_filename(docword_filepath)

        vocab_corpus_frequency_list = [0] * self.vocab_size
        vocab_document_frequency_list = [0] * self.vocab_size

        with open(docword_filepath, 'r') as infile:
            line = None
            for line in infile:
                pass
            end_line = line
            d_end, _, __ = proc_line(end_line)

        if self.num_docs is not None and d_end != self.num_docs:
            raise ValueError("Given num_docs don't match number of documents in docward_filepath")

        with open(docword_filepath, 'r') as infile:
            corpus = [[]] * d_end
            for line in infile:
                d, w, c = proc_line(line)
                if c < 0:
                    raise ValueError("Word frequency can't be negative")
                corpus[d - 1] = corpus[d - 1] + [(w - 1, c)]
                vocab_corpus_frequency_list[w - 1] += c
                vocab_document_frequency_list[w - 1] += 1
            corpus = [sorted(doc) for doc in corpus]
        doc_lengths = []
        for doc in corpus:
            doc_lengths.append(sum([tup[1] for tup in doc]))
        doc_lengths = np.array(doc_lengths)
        avg_doc_size = np.mean(doc_lengths)
        return corpus, d_end, doc_lengths, avg_doc_size, vocab_corpus_frequency_list, vocab_document_frequency_list

    def get_most_frequent_words(self, topn=10):
        topn_word_ids = np.argsort(self.vocab_corpus_frequency_list)[::-1][:topn]
        topn_word_frequncy_pairs = [(self.id2word_dict[idx], self.vocab_corpus_frequency_list[idx]) for idx in
                                    topn_word_ids]
        return topn_word_frequncy_pairs

    def get_least_frequent_words(self, topn=10):
        topn_word_ids = np.argsort(self.vocab_corpus_frequency_list)[:topn]
        topn_word_frequncy_pairs = [(self.id2word_dict[idx], self.vocab_corpus_frequency_list[idx]) for idx in
                                    topn_word_ids]
        return topn_word_frequncy_pairs

    def get_colormap_clusters(self, num_topics, W_matrix, upper_threshold, lower_threshold):
        """
        Cluster the documents based on the topic number that is dominant. Rest all in residual cluster.

        Input:
        W <ndarray, (num_topics, num_docs)>: The document topic matrix
        Output:
        clusters <dict of lists>: Keys - Topic Numbers from 0 to num_topics-1. Values - doc_id (1-indexed) with
        the 'key' topic number as the dominant topic.
        bad_cluster <list of ints>: list containing doc_ids (1-indexed) with no dominant topic.
        """
        clusters = [[]]*num_topics
        residual_cluster = []
        for i in range(self.num_docs):
            doc_id = i + 1
            dom_topic = np.argmax(W_matrix[:, i])
            dom_topic_weight = W_matrix[dom_topic, i]
            if dom_topic_weight >= upper_threshold and np.sort(W_matrix[:, i])[1] < lower_threshold:
                # noinspection PyTypeChecker
                clusters[dom_topic] = clusters[dom_topic] + [doc_id]
            else:
                residual_cluster.append(doc_id)
        return clusters, residual_cluster

    def plot_dominant_topic_document_distribution_base(self, W_matrix, upper_threshold, lower_threshold, kind):
        """
        Plot number of documents in each topic's dominant cluster.

        Given the topic-word distribution matrix (W_matrix), this function plots the distribution of number of
        documents having each topic as "dominant". The definition of "dominant" is that the document's dominant topic
        has probability weight >= upper_threshold and any other topic of the document has weight < lower_threshold.

        :param W_matrix: num_topics x num_docs matrix
        :param upper_threshold: lower bound probability weight for dominant topic
        :param lower_threshold: upper bound probability weight for non-dominant topics
        :param kind: 'vbar', 'hbar' or 'colorplot'
        :return: A list of length num_topics+1 where the last element is num_docs in residual cluster, and ith element
                is num_docs having topic i as dominant topic.
        """
        if upper_threshold < lower_threshold:
            raise ValueError("Upper Threshold can't be lower than lower_threshold")
        if kind not in ['vbar', 'hbar', 'colormap']:
            raise ValueError("Plot kind %s not implemented, see help for more." % kind)
        num_topics = W_matrix.shape[0]
        clusters, residual_cluster = self.get_colormap_clusters(num_topics=num_topics, W_matrix=W_matrix,
                                                                upper_threshold=upper_threshold,
                                                                lower_threshold=lower_threshold)
        if kind == 'colormap':
            W_color_matrix = self.get_W_color_matrix(W_matrix=W_matrix, clusters=clusters,
                                                     residual_cluster=residual_cluster)
            plotter.plot_colormap(W_color_matrix, xlabel="Topics", ylabel="Documents (normed to 0 to 1)",
                                  title="Colormap for document clustered by dominant topics")
        if kind == 'vbar' or kind == 'hbar':
            doc_distribution = [len(cluster) for cluster in clusters+[residual_cluster]]
            ticks = tuple(list(range(1, len(doc_distribution))) + ['Residual'])
            plotter.plot_bar(values=doc_distribution, bar_type=kind,
                             title="Document Distribution across Dominant Topics", ticks=ticks)

    @staticmethod
    def get_W_color_matrix(W_matrix, clusters, residual_cluster):
        num_topics = W_matrix.shape[0]
        num_docs = W_matrix.shape[1]
        W_color = np.zeros((num_docs, num_topics))
        current_row = 0
        for topic_num in range(num_topics):
            for doc_id in clusters[topic_num]:
                W_color[current_row, :] = W_matrix[:, doc_id - 1]
                current_row += 1
        for doc_id in residual_cluster:
            W_color[current_row, :] = W_matrix[:, doc_id - 1]
            current_row += 1
        assert (current_row == num_docs), "Number of rows in W_color don't match num_rows in W"
        return W_color

    def plot_topic_wordcloud(self, topicid, num_words, frequencies, figsize):
        plotter.plot_wordcloud(word_frequency_dict=frequencies, num_words=num_words, figsize=figsize)
        return

    @staticmethod
    def plot_comparative_topic_wordclouds_base(num_words, frequencies1, frequencies2,
                                               figsize):
        plotter.plot_wordcloud_pair(frequencies1, frequencies2, num_words=num_words, figsize=figsize)
        return

    @staticmethod
    def plot_topic_topwords_base(topic_tuples, cmaps, title, save=False, show=True, filename=None, show_weight=False):
        if cmaps is None:
            logging.debug("plot_topic_topwords: using default cmaps")
            cmaps = ['Blues', 'Greens', 'Reds', 'Purples', 'Greys']*(int(len(topic_tuples)/5) + 1)
        elif cmaps == 'Uniform':
            cmaps = ['Blues']*len(topic_tuples)
        plotter.plot_text_intensity_plot(topic_tuples, cmaps, title=title, save=save, show=show, filename=filename,
                                         show_weight=show_weight)

    @staticmethod
    def plot_entropy_distribution_base(distributions, *args, **kwargs):
        entropies = stats.get_entropies(distributions)
        try:
            kwargs["xlabel"]
        except KeyError:
            kwargs["xlabel"] = "Topics"
        try:
            kwargs["ylabel"]
        except KeyError:
            kwargs["ylabel"] = "Entropy"
        max_possible_entropy = stats.get_entropy([1/len(distributions[0])]*len(distributions[0]))
        plotter.plot_bar(entropies, const_val_line=max_possible_entropy, *args, **kwargs)
        return

    @staticmethod
    def plot_topic_entropy_colormap(distributions):
        entropy_matrix = stats.build_entropy_matrix(distributions)
        plotter.plot_colormap(entropy_matrix, xlabel="Topics", ylabel="Topics", title="Topic KL-Divergence Matrix",
                              yaxisnormed=False)
        return

    @staticmethod
    def make_corpus_from_matrix(A):
        corpus = []
        D = A.shape[0]
        N = A.shape[1]
        for i in range(N):
            corpus.append([])
            vocab_distribution = A[:, i]
            assert (len(vocab_distribution) == D), "Vocab distribution of document not matching D"
            for j in range(D):
                if vocab_distribution[j] > 0:
                    corpus[i].append((j, vocab_distribution[j]))
        return corpus

    def make_matrix_from_corpus(self):
        A = np.zeros((self.vocab_size, self.num_docs))
        for doc_num in range(self.num_docs):
            for tup in self.corpus[doc_num]:
                A[tup[0], doc_num] = tup[1]
        return A

    def save_topic_top_words(self, word_weight_list, filename, separator, datasetname):
        all_words = []
        for word_weights in word_weight_list:
            words = [tup[0] for tup in word_weights]
            all_words.append(words)
        with open(filename, "w") as f:
            for idx, words in enumerate(all_words):
                f.write(str(idx) + separator + datasetname)
                for word in words:
                    f.write(separator + word)
                f.write('\n')
        return