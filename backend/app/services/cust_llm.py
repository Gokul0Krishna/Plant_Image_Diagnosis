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

    def run(self,pdata,fdata,plant_class):
        '''
        input: pdata = past data json
               fdata = future data json
               plant_class = diseases classification
        output: Llm result  
        '''
        messages = [
        {
            "role": "system",
            "content": (
                "You are an agricultural expert specializing in rice crop diseases. "
                "Provide practical treatment and prevention advice based on disease "
                "type, weather conditions, and elevation."
            )
        },
        {
            "role": "user",
            "content": f"""
            Disease detected: {plant_class[0]}

            Past Weather Data:
            - Min Temperature: {pdata['temperature_2m_min']}
            - Max Temperature: {pdata['temperature_2m_max']}

            Future Weather Forecast:
            - Min Temperature: {fdata['temperature_2m_min']}
            - Max Temperature: {fdata['temperature_2m_max']}

            Elevation: {pdata['elevation']} meters

            Please provide:
            1. Cause of this disease
            2. Immediate treatment steps
            3. Preventive measures
            4. Weather-based risk analysis
            5. Fertilizer or pesticide recommendation (if needed)
            """
                    }
        ]

        prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200
        )

        generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]

        assistant_response = self.tokenizer.decode(
            generated_tokens,
            skip_special_tokens=True
        )

        return assistant_response

if __name__ == '__main__':
    obj = Llm()
    a = obj.run(pdata={'temperature_2m_max': [30.0, 29.3, 29.3, 29.1, 30.2, 30.3, 30.3, 30.4, 30.7, 31.2, 30.8, 29.6, 30.1, 29.1], 'temperature_2m_min': [16.1, 15.4, 16.4, 15.6, 16.3, 17.3, 17.7, 17.8, 18.3, 17.9, 19.5, 19.5, 19.3, 19.7], 'elevation': 918.0},
            fdata={'temperature_2m_max': [30.4, 30.7, 31.2, 30.8, 29.6, 30.1, 29.1], 'temperature_2m_min': [17.8, 18.3, 17.9, 19.5, 19.5, 19.3, 19.7], 'elevation': 918.0},
            plant_class=['bercak_daun'])
    print(a)