from prompt_utils import gen_prompt
from prompt_utils import generate


def inference(sentence, model, tokenizer):
    #sentence = 'Can you make the sky look black?'
    prompt = gen_prompt(tokenizer, sentence)
    print(prompt)
    return generate(model, tokenizer, prompt)