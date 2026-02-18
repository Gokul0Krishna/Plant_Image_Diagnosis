from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch
import os
from dotenv import load_dotenv

class Llm():

    def __init__(self):
        'fine tuned tinyLLama model'
        load_dotenv()

        self.base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        self.adapter_path = os.getenv('llm_file_path')

        print("Adapter Path:", self.adapter_path)

        self.tokenizer = AutoTokenizer.from_pretrained(self.base_model)

        self._loadmodel()
    
    def _loadmodel(self):
        'loads all the dependency for the model'
        self.model = AutoModelForCausalLM.from_pretrained(
            self.base_model,
            torch_dtype=torch.float16,
            device_map="auto"
        )

        self.model = PeftModel.from_pretrained(self.model, self.adapter_path)

        self.model.eval()
    
    def _test(self):

        messages = [
            {"role": "user", "content": "What disease affects rice leaves?"}
        ]

        prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=100
        )

        print(self.tokenizer.decode(outputs[0], skip_special_tokens=True))


if __name__ == '__main__':
    obj = Llm()
    obj._test()
