# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    
    # Test normal file
    good = FastaParser("/data/test.fa")
    sequences = list(good)
    for name, seq in sequences:
        assert isinstance(seq, str), "Sequences should be in String format"
        
    # Test empty file
    with pytest.raises(ValueError):
        blank = FastaParser("/tests/blank.fa")
        list(blank)
    
    # Test with a corrupted FASTA file
    with pytest.raises(ValueError):
        bad = FastaParser("/tests/bad.fa")
        list(bad)
    pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in. If a fastq file is
    read, the first item is None
    """
    fasta = FastaParser('/data/test.fa')
    sequences = list(fasta)
    assert len(sequences) > 0, "No sequences found"
    assert sequences[0][0] is not None, "Wrong FASTA format, FASTQ detected"
    pass

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # Test normal file
    good = FastqParser("/data/test.fq")
    sequences = list(good)
    for name, seq, qual in sequences:
        assert isinstance(seq, str), "Sequences should be in String format"
        assert len(seq) == len(qual), "Quality and sequence should be of the same length."
    pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq = FastqParser('/data/test.fq')
    sequences = list(fastq)
    assert len(sequences) > 0, "No sequences found"
    assert sequences[0][0] is not None, "Wrong FASTQ format, FASTA detected"
    pass