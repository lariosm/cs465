from encode import string_compressor

def test_empty_string():
    assert string_compressor("") == ""

def test_single_character_string():
    assert string_compressor("a")

def test_non_repeating_character_string():
    assert string_compressor("abcdefg")