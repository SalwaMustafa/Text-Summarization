from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

checkpoint = "Salwaaaa/t5-base-finetuned-summarize-dailymail"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

prompt = "You are the smartest model ever. Please summarize the following text in a concise manner:\n\n"

def generate_summary(text):

    inputs = tokenizer((prompt + text), max_length=512, truncation=True, return_tensors="pt")
    summary_ids = model.generate(inputs['input_ids'], max_length = 100 )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens = True)

    return summary
