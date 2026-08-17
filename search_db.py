f = open("knowledge_base.txt")
chunk = f.read()

def clean(data):
    result = []

    for sentence in data:
        clean = sentence.strip()

        if clean:
            result.append(clean)

    return result

def find(data, ques):
    result = []
    for word in ques:
        for x in data:


question = "What is Paracetamol dosage for children"
question = question.lower().split()
sen = chunk.lower().split("\n")
print(clean(sen))
print(clean(question))