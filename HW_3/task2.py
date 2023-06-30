# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

from typing import Dict, Any

text = "How do people represent knowledge about generalizations they make from experience" \
            "with concrete situations? Philosophers concerned with the theory of knowledge have debated" \
            "this question, but as we shall see, the issue is not without practical consequences for the " \
            "task of representing knowledge in object oriented systems. Because much of object oriented"\
            "programming involves constructing representations of objects in the real world, our mechanisms"\
            "for storing and using real world knowledge get reflected in mechanisms for dealing with objects"\
            "in computer languages. We'll examine how the traditional controversy between representing concepts"\
            "as sets versus representing concepts as prototypes gives rise to two mechanisms, inheritance"\
            "and delegation, for sharing behavior between related objects in object oriented languages."\
            "When a person has experience in a particular situation, say concerning a particular elephant"\
            "named Clyde, facts about Clyde can often prove useful when encountering another elephant, "\
            "say one Fred. If we have mental representations of a concept for (Clyde, and a concept for Fred,"\
            "the question then : How do the representations of Clyde and Fred share knowledge? How can we answer"\
            "questions, such as Fred's color, number of legs, size, etc. by reference to what we already know about"\
            "Clyde? In the absence of any mechanism for sharing knowledge between related concepts, we'd have to repeat"\
            "all the knowledge about Clyde in a representation of Fred."

# количество требуемых слов
word_count = 10


# Возврат count_words самых часто используемых слов из текста в виде строки, разделенных пробелами
def most_frequent_words(text: str, count_words: int) -> dict:
    # удалить знаки препинания, привести к единому регистру, тире ищем только как знак препинания,
    # дефис разделяющий части слова - является его частью
    words_list = text.upper() \
        .replace(".", " ") \
        .replace(",", " ") \
        .replace(";", " ") \
        .replace(":", " ") \
        .replace("!", " ") \
        .replace("?", " ") \
        .replace(" - ", " ") \
        .split()
    # подсчитываем кол-во слов, используем словарь для этого
    words_count = {}
    for w in words_list:
        words_count[w] = words_list.count(w)
    # сортируем словарь по значениям, отбираем только нужное количество
    return dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:count_words])


def main():
    for i, w in enumerate(most_frequent_words(text, word_count).items(), 1):
        print(f"{i:2}. {w[0]:<10} - {w[1]}")


if __name__ == "__main__":
    main()