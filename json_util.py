# import json

# def parse_json_split(json_string: str) -> dict:
#     # # Remove the triple backticks if present
#     # json_string = json_string.strip().replace("\n", "").replace("```", "")
#     # start_index = json_string.find("json")
#     # end_index = json_string.find("", start_index + len("json"))

#     # if start_index != -1 and end_index != -1:
#     #     extracted_content = (
#     #         json_string[start_index + len("json") :].replace("'", "").strip()
#     #     )

#     #     # Parse the JSON string into a Python dictionary
#     #     parsed = json.loads(extracted_content)
#     # elif start_index != -1 and end_index == -1 and json_string.endswith("``"):
#     #     end_index = json_string.find("``", start_index + len("json"))
#     #     extracted_content = json_string[start_index + len("json") : end_index].strip()

#     #     # Parse the JSON string into a Python dictionary
#     #     parsed = json.loads(extracted_content)
#     # elif json_string.startswith("{"):
#     #     # Parse the JSON string into a Python dictionary
#     #     parsed = json.loads(json_string)
#     # else:
#     #     raise Exception("Could not find JSON block in the output.")
#     #a = json_string.replace("\n", "").replace("\t", "")
#     #parsed = json.loads(parse)


#     return 1


# # message = '''
# #             '\n{\n    "DataStructureChoice": {\n        "score": 2,\n        "notes": "The hypothesis uses a Red-Black Tree, which differs from the AVL Tree specified in the promise. While both are balanced binary search trees, the choice is inconsistent."\n    },\n    "ApproachExplanation": {\n        "score": 4,\n        "notes": "The hypothesis provides a comprehensive explanation of how Red-Black Trees maintain balance and ensure efficient operations, with detailed constraints and maintenance operations. However, it\'s not aligned with the AVL Tree explanation required by the promise."\n    },\n    "Correctness": {\n        "score": 3,\n        "notes": "The hypothesis is logically accurate in its own context (Red-Black Tree), but it does not align with the promise\'s context (AVL Tree). The accuracy within the scope of the chosen data structure is correct, yet misaligned with the promise."\n    },\n    "TimeComplexity": {\n        "score": 4,\n        "notes": "The hypothesis correctly indicates that operations in Red-Black Trees take O(log n) time, which matches the time complexity described in the promise for AVL Trees, despite using a different structure."\n    }\n}\n'
# #         '''

# # result = parse_json_split(message)
# # i = 2