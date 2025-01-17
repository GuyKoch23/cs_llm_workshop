from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor
import threading

global_counter = 0
counter_lock = threading.Lock()

def query_single_chatgpt(prompt, model="gpt-4o", temperature=0.7, max_tokens=1500, json=False):
    global global_counter
    with counter_lock:
        global_counter += 1
        print(f"Counter is {global_counter}")
    if(json):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                response_format={ "type": "json_object" }
                # temperature=temperature,
                # max_tokens=max_tokens,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"
    else:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                # temperature=temperature,
                # max_tokens=max_tokens,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"   
    

def query_list_chatgpt(prompts, model="gpt-4o", temperature=0.7, max_tokens=200):
    results = []
    for prompt in prompts:
        result = query_single_chatgpt(prompt)
        results.append(result)
    return results

def query_list_chatgpt_concurrently(prompts, model="gpt-4o", temperature=0.7, max_tokens=200):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(query_single_chatgpt, prompts))
    return results