class DictionaryUtils:
    @staticmethod
    def print_dict(dictionary):
        result = ""
        for key, value in dictionary.items():
            if type(value) == list:
                result += key + "\n"
                for item in value:
                    result += "|\t" + item + "\n"
            else:
                result += key + '\n|\t' + value + "\n"
        print(result)
