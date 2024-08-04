from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# モデルのロード
model_name = "t5-base"  # 例: T5モデル
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

while True:
    # 入力文
    input_text = input(">>> ")
    if input_text == "quit":
        break

    # 入力文をトークナイズ
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # 応答生成
    output = model.generate(input_ids)
    output = tokenizer.decode(output[0], skip_special_tokens=True)

    print(output)