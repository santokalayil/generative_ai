import prep as _
from generative_ai.llms import gemini

genai = gemini.get()

model = genai.GenerativeModel("gemini-pro")
# response = model.generate_content("Please summarise this document: ...")
response = model.generate_content("Give one Film Actor Name in Hollywood")
print(response.text)


# # EMBEDDINGs
# # https://ai.google.dev/tutorials/python_quickstart
# result = genai.embed_content(
#     model="models/embedding-001",
#     content="What is the meaning of life?",
#     task_type="retrieval_document",
#     title="Embedding of single string",
# )

# # 1 input > 1 vector output
# print(str(result["embedding"])[:50], "... TRIMMED]")
