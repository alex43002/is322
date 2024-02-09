from bot.utilities import count_characters, token_count
from faker import Faker

def test_character_count():
    faker = Faker()
    text = faker.texts(nb_texts=1000)
    assert count_characters(text) == 1000
    assert count_characters("hello") == 5

def test_token_count():
    assert token_count(16) == 4
    assert token_count(17) == 5