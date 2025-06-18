from langchain_core.prompts import PromptTemplate
template=PromptTemplate(
        
        template="""
        
        please summarize the research paper titled "{paper_input}" with the  following specificatin:
        
        Explanation style:"{select_type}" 
        Explanaion length:"{dsc}"
        
        1.mathmetical detail: 
        -include relavent mathmetical equaion if present in paper
        -Explain he mahmeical concepts using simple,intutive code snippets where applicable
        
        2.Analogies:
         -Use relattable analogy to explain complex ideas.
         If sufficient information is not available in the paper,respond with:Information is not available, instead of guessing.
         Ensure he summary aligned wih syle,length,accurate
        """,
        input_variables=['paper_input','select_type','dsc'],
        validate_template=True
    )

template.save('template.json')