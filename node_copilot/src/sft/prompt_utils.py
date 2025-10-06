def gen_prompt(tokenizer, sentence):
    converted_sample = [{"role": "user", "content": sentence}]
    prompt = tokenizer.apply_chat_template(
        converted_sample, tokenize=False, add_generation_prompt=True
    )
    return prompt

def generate(model, tokenizer, prompt, max_new_tokens=2000, skip_special_tokens=False):
    tokenized_input = tokenizer(
        prompt, add_special_tokens=False, return_tensors="pt"
    ).to(model.device)

    model.eval()
    # if it was trained using mixed precision, uses autocast context
    # ctx = torch.autocast(device_type=model.device.type, dtype=model.dtype) if model.dtype in [torch.float16, torch.bfloat16] else nullcontext()
    #with ctx:
    gen_output = model.generate(**tokenized_input,
                                eos_token_id=tokenizer.eos_token_id,
                                max_new_tokens=max_new_tokens)

    output = tokenizer.batch_decode(gen_output, skip_special_tokens=skip_special_tokens)
    return output[0]