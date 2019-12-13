from encode import encode

def test_empty_string():
    assert encode("") == ""

def test_single_character_string():
    assert encode("a") == "a"

def test_non_repeating_character_string():
    assert encode("abcdefg") == "abcdefg"
    assert encode("ab") == "ab"

def test_single_character_string_compression():
    assert encode("aaaa") == "a4"
    assert encode("aa") == "a2"

def test_multiple_characters_string_compression():
    assert encode("aabb") == "a2b2"
    assert encode("bbbaacccc") == "b3a2c4"

def test_upper_and_lower_case_combo_string_compression():
    assert encode("AbaaAAAAcdB") == "Aba2A4cdB"
    assert encode("AaAaaaAAa") == "AaAa3A2a"