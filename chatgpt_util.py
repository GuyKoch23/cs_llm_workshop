from openai import OpenAI



def query_single_chatgpt(prompt, model="gpt-4o", temperature=0.7, max_tokens=1500, json=False):
    
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