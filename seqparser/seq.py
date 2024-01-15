# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    result = ""
    for i in range(len(seq)):
        result += TRANSCRIPTION_MAPPING[seq[i]]
    if reverse:
        return result[::-1]
    return result
#     pass

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq, reverse = True)
    pass


# print(transcribe("ATCCGCA"))
# print(reverse_transcribe("ATCCGCA"))