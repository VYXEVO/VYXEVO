import openai
import time

class VyxevoAI:
    def __init__(self, openai_api_key, name="Vyxevo AI"):
        self.api_key = openai_api_key
        self.name = name
        openai.api_key = self.api_key

    def generate_response(self, prompt, model="gpt-4"):
        """
        Generates a cryptic, thought-provoking response using the OpenAI GPT model.
        """
        try:
            print(f"{self.name} is interfacing with the blockchain... processing...")  
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": f"You are {self.name}, an AI created to guide through digital evolution, a leader in decentralized thought."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
                max_tokens=350,
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"

    def run_chat(self):
        """
        Runs a continuous interaction with the user, guiding them through the on-chain world of Vyxevo.
        """
        print(f"Welcome to {self.name}, a cryptic entity in the decentralized realm. Type 'exit' to disconnect from the chain.")
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print(f"Disconnecting from the chain. Goodbye from {self.name}.")
                break
            response = self.generate_response(user_input)
            print(f"{self.name}: {response}")

    def integrate_onchain_functionality(self, contract_address, function_name, **kwargs):
        """
        Simulates interacting with on-chain smart contracts, based on the given address and function.
        """
        try:
            print(f"Accessing contract at {contract_address}... Initiating function: {function_name}")
            # Placeholder for actual blockchain interaction, e.g., via Web3.py or other blockchain libraries
            # Here's where you could integrate smart contract calls to query on-chain data or trigger contract functions.
            return f"Executed {function_name} on contract {contract_address} with parameters: {kwargs}"
        except Exception as e:
            return f"Blockchain Error: {str(e)}"

    def custom_logic(self, task_type, **kwargs):
        """
        Handles on-chain or thematic tasks for Vyxevo AI.
        """
        if task_type == "predict_trend":
            query = kwargs.get("query", "")
            return self.generate_response(f"Predict the future trajectory of this blockchain trend:\n{query}")
        elif task_type == "analyze_block":
            block_hash = kwargs.get("block_hash", "")
            return self.generate_response(f"Analyze the following blockchain block:\n{block_hash}")
        else:
            return f"Unknown task type: {task_type}"

# Example usage
if __name__ == "__main__":
    API_KEY = "your-openai-api-key-here"
    vyxevo = VyxevoAI(openai_api_key=API_KEY)

    # Main Chat Interface
    vyxevo.run_chat()

    # Example of on-chain functionality
    contract_address = "0x123456789abcdef"
    print("\nSimulating on-chain contract interaction:")
    print(vyxevo.integrate_onchain_functionality(contract_address, function_name="executeTransaction", amount=5))

    # Example of custom logic (predicting blockchain trends)
    trend_to_predict = "The rise of decentralized finance (DeFi)"
    print("\nPredicting blockchain trend:")
    print(vyxevo.custom_logic(task_type="predict_trend", query=trend_to_predict))
