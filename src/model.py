from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

checkpoint = "Salwaaaa/t5-base-finetuned-summarize-dailymail"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

def generate_summary(text):

    inputs = tokenizer(text, return_tensors = "pt")
    summary_ids = model.generate(inputs['input_ids'], max_length = 75 )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens = True)

    return summary
