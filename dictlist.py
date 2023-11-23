if __name__=='__main__':
     nested_dict = { 'dictA': {'key': 'value_1'}, 'dictB': {'key': 'value_2'}, 'dictC': {'key': 'value_3'}}
     print(nested_dict)
     for k, v in dictionary.items():
        pattern_found = pattern.search(k)
        if not pattern_found:
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        search(item, search_pattern, output)
            if isinstance(v, dict):
                search(v, search_pattern, output)
        else:
            if pattern_found:
                output.append(v)
