
# from google.cloud import translate_v2 as translate
# import PyPDF2
# import os

# pdf_filename = "inputGC.pdf"
# target_language = "zh-CN"


# translate_client = translate.Client.from_service_account_json('C:/Users/vysha/Downloads/cc-assignment-1-386417-1787837581ea.json')

# with open(pdf_filename, "rb") as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()


# result = translate_client.translate(text, target_language=target_language)

# print(result["input"])
# print(result["translatedText"])







# v2-nahh
# from google.cloud import translate_v2 as translate
# import PyPDF2
# import os

# pdf_filename = "inputGC.pdf"
# target_language = "zh-CN"
# output_filename = "output.txt"

# translate_client = translate.Client.from_service_account_json('C:/Users/vysha/Downloads/cc-assignment-1-386417-1787837581ea.json')

# with open(pdf_filename, "rb") as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()

# result = translate_client.translate(text, target_language=target_language)

# with open(output_filename, "w", encoding="utf-8") as output_file:
#     output_file.write(result["translatedText"])




from google.cloud import translate_v2 as translate
import PyPDF2
import os

pdf_filename = "inputGC.pdf"
target_language = "zh-CN"      #zh-CN kn de
output_filename = "output.txt"

translate_client = translate.Client.from_service_account_json('C:/Users/vysha/Downloads/cc-assignment-1-386417-1787837581ea.json')

with open(pdf_filename, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

result = translate_client.translate(text, target_language=target_language)

with open(output_filename, "w", encoding="utf-8") as output_file:
    output_file.write("Input text:\n")
    for line in text.split("\n"):
        output_file.write(line + "\n")
    output_file.write("\nTranslated text:\n")
    for line in result["translatedText"].split("\n"):
        output_file.write(line + "\n")
