# -*- coding: utf-8 -*-
from os import listdir
from unittest import TestCase, skip
from underthesea import chunk
from os.path import dirname, join
import sys
import io

samples_dir = join(dirname(__file__), "samples")


def load_input(input_file):
    if sys.version_info >= (3, 0):
        content = [text.split("\t")[0] for text in open(input_file, "r", encoding="utf-8").read().strip().split("\n")]
        content = " ".join(content)
        return content
    else:
        content = [text.split("\t")[0].decode("utf-8") for text in open(input_file, "r").read().strip().split("\n")]
    content = u" ".join(content)
    return content


def load_output(input_file):
    lines = [text.split("\t") for text in io.open(input_file, "r", encoding="utf-8").read().strip().split("\n")]
    output = []
    for item in lines:
        word, pos_tag, chunk_tag = item
        if sys.version_info >= (3, 0):
            output.append((word, pos_tag, chunk_tag))
        else:
            output.append((word.decode("utf-8"), pos_tag, chunk_tag))
    return output


def save_temp(id, output):
    temp_file = join(samples_dir, "%s.actual" % id)
    content = u"\n".join([u"\t".join(item) for item in output])
    if sys.version_info >= (3, 0):
        open(temp_file, "w", encoding="utf-8").write(content)
    else:
        open(temp_file, "w").write(content.encode("utf-8"))


class TestChunking(TestCase):
    def test_simple_cases(self):
        sentence = u""
        actual = chunk(sentence)
        expected = []
        self.assertEqual(actual, expected)

    def test_accuracy(self):
        test_dir = join(dirname(__file__), "samples")
        files = listdir(test_dir)
        ids = [f.split(".")[0] for f in files]
        for id in ids:
            file = join(test_dir, "%s.txt" % id)
            sentence = load_input(file)
            actual = chunk(sentence)
            expected = load_output(file)
            if actual != expected:
                print("Fail {}".format(id))
                save_temp(id, actual)
            self.assertEqual(actual, expected)
