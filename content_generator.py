import openai

# Start with reading API KEY to enable conversation 
def open_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
    
openai.api_key = open_file('api_key.txt')

# Process of sending PROMPT to the COMPLETIONS ENDPOINT
def blogIdeas(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=100, freq_pen=0.0, pres_pen=0.0):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    try: 
        response = openai.Completion.create(
            engine=engine,
            prompt=f"Generate blog topics on: {prompt}",
            temperature=temp,
            max_tokens=tokens,
            top_p=top_p,
            frequency_penalty=freq_pen,
            presence_penalty=pres_pen)
        text = response['choices'][0]['text'].strip()
        return text
    except Exception as e:
        return f'This is your error: ==> {e}'
    
def blogContent(prompt, engine='text-davinci-003', temp=0.5, top_p=1.0, tokens=200, freq_pen=0.0, pres_pen=0.0):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    try: 
        response = openai.Completion.create(
            engine=engine,
            prompt=f"Expand the blog title into high level blog sections: {prompt}",
            temperature=temp,
            max_tokens=tokens,
            top_p=top_p,
            frequency_penalty=freq_pen,
            presence_penalty=pres_pen)
        text = response['choices'][0]['text'].strip()
        return text
    except Exception as e:
        return f'This is your error: ==> {e}'    


def sectionExpander(prompt, engine='text-davinci-003', temp=0.5, top_p=1.0, tokens=200, freq_pen=0.0, pres_pen=0.0):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    try: 
        response = openai.Completion.create(
            engine=engine,
            prompt=f"Expand the blog section into a detailed professional, clever and goal oriented explanation: {prompt}",
            temperature=temp,
            max_tokens=tokens,
            top_p=top_p,
            frequency_penalty=freq_pen,
            presence_penalty=pres_pen)
        text = response['choices'][0]['text'].strip()
        return text
    except Exception as e:
        return f'This is your error: ==> {e}'    

    

if __name__ == '__main__':
    #prompt = 'The importance of AI in our everyday live. \n Key Words: "AI", "SASS", "Automation"'
    prompt = 'How AI can help us achieve our goals . \n 1) Introduction: How AI can help us identify our goals'
    #prompt = 'How AI can help us monitor our progress.'
    response = blogContent(prompt)
    #response = blogIdeas(prompt)
    #response = sectionExpander(prompt)
    print(response)