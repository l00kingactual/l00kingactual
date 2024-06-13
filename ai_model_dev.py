# Import dependencies
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All

# Specify model weights path
PATH='./nous-hermes-13b.ggmlv3.q4_0.bin'

# Create LLM Class
llm = GPT4All(model=PATH, verbose=True)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=['instruction', 'input', 'response'],
    template="""
    ### Instruction:
    {instruction}
    ### Input:
    {input}
    ### Response:
    {response}
    """ )

chain = LLMChain(prompt=prompt, llm=llm)

# Run the prompt
# I used a childen story to test https://cuentosparadormir.com/infantiles/cuento/barba-flamenco-y-el-recortador-de-cuentos
# its about 783 words long!
chain.run(instruction="""Resume esta historia, hazlo en español""",
input="""[...story content...]""",
response='A: ')