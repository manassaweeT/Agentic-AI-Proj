import pprint
f = open("knowledge_base.txt")
chunk = f.read()

def clean(data):
    result = []

    for sentence in data:
        clean = sentence.strip()

        if clean:
            result.append(clean)

    return result

def find(db, ques):
    result = {}
    stop = ['how', 'where', 'when', 'why', 'what', 'who', 'and', 'a', 'the', 'an', 'is', 'am', 'are', 'on', 'to', 'in', 'at', 'for']
    for word in ques:
        if word in stop:
            continue
        for i, sentence in enumerate(db):
            if word in sentence:
                result[word] = " ".join(db[max(0, i-3):i+3])
    return result


question = "What is Paracetamol dosage for children"
question = question.lower().split()
sen = chunk.lower().split("\n")
db = clean(sen)
ques = clean(question)
pprint.pprint(find(db, ques))
# print(clean(sen))
# print(clean(question))