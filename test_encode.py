from encode import string_compressor

def test_empty_string():
    assert string_compressor("") == ""