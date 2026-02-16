from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
import os
from dotenv import load_dotenv
from peft import LoraConfig, get_peft_model
from transformers import TrainingArguments,BitsAndBytesConfig
from trl import SFTTrainer


load_dotenv()

question_json_path = os.getenv('question_json_path')

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype="float16"
)


model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto"
)

dataset = load_dataset("json", data_files=question_json_path)

def format_example(example):
    prompt = f"""
        ### Instruction:
        {example['instruction']}

        ###context:
        {example['context']}

        ### Response:
        {example['response']}
        """
    return {"text": prompt}

dataset = dataset.map(format_example)

def tokenize(example):
    tokens = tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=512
    )
    tokens["labels"] = tokens["input_ids"].copy()
    return tokens


dataset = dataset.map(tokenize)

dataset = dataset.remove_columns(["instruction","context","response","text"])

config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj","v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, config)

training_args = TrainingArguments(
    output_dir="./tinyllama-agri",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    learning_rate=2e-4,
    fp16=True
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset["train"],
    args=training_args,
)

trainer.train()

trainer.save_model("agri_tinyllama")
