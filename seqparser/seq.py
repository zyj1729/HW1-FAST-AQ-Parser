# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """

    if isinstance(seq, str) is False:
        raise ValueError("Seq must be of type string.")

    if seq == "":
        raise ValueError("Seq can't be an empty string.")

    seq = seq.upper()

    if reverse:
        seq = seq[::-1]

    # loop through once to see if any elements are not ATCG
    # this can be skipped, it's just to allow the end user to know
    # which position the bad character potentially is
    # you could remove this code because in the end we 
    # will return the result of the "".join(map()) statement
    for idx, nuc in enumerate(seq):
        if nuc not in ALLOWED_NUC:
            err = f"Nucleotide {nuc} at position {idx+1} for {seq} was not an allowed DNA nucleotide."
            if reverse:
                err = err[:-1]  # remove period
                err += "(reversed sequence)."

            raise ValueError(
                f"Nucleotide {nuc} at position {idx+1} for {seq} was not an allowed DNA nucleotide."
            )

    # map(TRANSCRIPTION_MAPPING.get) will plug in every element 
    # of seq into TRANSCRIPTION_MAPPING
    # you could also do this with a list comprehension, like
    # "".join([TRANSCRIPTION_MAPPING[character] for character in seq])
    # or "".join([TRANSCRIPTION_MAPPING.get(character) for character in seq])
    # which are equivalent. map is (in my understanding) 
    # very slightly faster than list comprehension for this example 

    # finally, you could do something like:
    #
    # output = ""
    # for character in seq: 
    #   output += TRANSCRIPTION_MAPPING[character]
    # return output

    return "".join(map(TRANSCRIPTION_MAPPING.get, seq))

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    return transcribe(seq, reverse=True)  # ''.join will return a reversed string
