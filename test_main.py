from main import check_password, get_strength

def test_get_strength():
    assert get_strength(0) == "Weak"
    assert get_strength(1) == "Weak"
    assert get_strength(2) == "Weak"
    assert get_strength(3) == "Medium"
    assert get_strength(4) == "Medium"
    assert get_strength(5) == "Strong"

def test_check_password():
    score, suggestions = check_password("apple")
    assert score == 1
    assert len(suggestions) == 4
    assert "Increase password length" in suggestions
    assert "Consider adding uppercase letters" in suggestions
    assert "Consider adding numbers" in suggestions
    assert "Consider adding special characters" in suggestions

    score, suggestions = check_password("apple123")
    assert score == 2
    assert len(suggestions) == 3

    score, suggestions = check_password("Apple123")
    assert score == 3
    assert len(suggestions) == 2

    score, suggestions = check_password("Apple123!")
    assert score == 4
    assert len(suggestions) == 1

    score, suggestions = check_password("HelloWorld123!@#")
    assert score == 5
    assert len(suggestions) == 0

def test_edge_cases():

    # 1. Empty password
    score, suggestions = check_password("")
    assert score == 0
    assert len(suggestions) == 5

    # 2. Exactly 14 characters
    score, suggestions = check_password("Abcdefghijk12!")
    assert score == 4
    assert len(suggestions) == 1

    # 3. Exactly 15 characters
    score, suggestions = check_password("Abcdefghijkl12!")
    assert score == 5
    assert len(suggestions) == 0

    # 4. Exactly 16 characters
    score, suggestions = check_password("Abcdefghijklm12!")
    assert score == 5
    assert len(suggestions) == 0

    # 5. Only spaces
    score, suggestions = check_password("     ")
    assert score == 0
    assert len(suggestions) == 5

    # 6. Only numbers
    score, suggestions = check_password("123456")
    assert score == 1
    assert len(suggestions) == 4

    # 7. Very long password
    score, suggestions = check_password("a" * 1000)
    assert score == 2
    assert len(suggestions) == 3


test_get_strength()
print("All strength tests passed!")

test_check_password()
print("Password check test passed!")

test_edge_cases()
print("All edge case tests passed!")