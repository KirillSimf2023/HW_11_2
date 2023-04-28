# Создайте файл
# str_func.py
# и в нем функцию, которая принимает на вход строку и возвращает ее со всеми заглавными буквами.


def revert_upper(word: str)->str:
    """
       делает все буквы заглавными
       :param word: string
       :return:string
    """
    return word.upper()

def revert_f_upper(word: str)->str:
    """
    делает заглавными первые буквы каждого слова в строке
    :param word: string
    :return:string
    """
    return word.title()



