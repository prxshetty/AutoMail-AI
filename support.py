from langchain.schema import Document
from langchain_community.document_transformers import DoctranPropertyExtractor #used to extract correct propertyes of emial issue
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate


class AICustomerSupport:
    def __init__(self, openai_api_model):
        self.openai_api_model = openai_api_model
        self.properties = [
            {
                "name" : "category",
                "description": "The type of email this is. ",
                "type": "string",
                "enum" : [
                    "complaint",
                    "refund_request",
                    "product_feedback",
                    "customer_service",
                    "other",
                ],
                "required": True,
            },
            {
                "name": "mentioned_product",
                "description": "The prodcut mentioned in this email.",
                "type": "string",
                "required": True
            },
            {
                "name": "issue_description",
                "description": "A brief explaination of the problem encountered with the product.",
                "type": "string",
                "required": True
            },
            {
                "name": "customer_name",
                "description": " Name of the Customer",
                "type": "string",
                "required" : True
            }
        ]

    def interpret_and_evaluate(self, extracted_properties):
        template = f"""
        You are an AI Customer Support that writes friendly emails back to customers. Address the sender with his or her name {extracted_properties['customer_name']} issue kindly and while addressing
        say 'Dear Customer'.
        The customer's email was categorized as {extracted_properties['category']}, and mentioned the product {extracted_properties['mentioned_product']}. 
        They described the issue: {extracted_properties['issue_description']}.
        Please reply to this email in a friendly and helpful manner.
        
        Write a response that includes an understanding of the problem, a proposed solution, and a polite sign-off with senders name and conclusion of the email.
        Your sign-off name in the email is Auto-Mail AI.
        """

        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature = 0)
        prompt_template = PromptTemplate.from_template(template=template)
        chain = LLMChain(llm = llm, prompt = prompt_template)
        result = chain.predict(input = "")
        return result
    
    def get_email_content(self, email_message):
        maintype = email_message.get_content_maintype()
        if maintype == "multipart":
            for part in email_message.get_payload():
                if part.get_content_maintype() == "text":
                    return part.get_payload()
        elif maintype == "text":
            return email_message.get_payload()
        
    async def process_email(self, email_message):
        email_content = self.get_email_content(email_message)
        documents = [Document(page_content = email_content)]
        property_extractor = DoctranPropertyExtractor(
            properties = self.properties, openai_api_model = self.openai_api_model
        )
        extracted_document = await property_extractor.atransform_documents(
            documents, properties = self.properties
        )
        extracted_properties = extracted_document[0].metadata["extracted_properties"]
        evaluation_result = self.interpret_and_evaluate(extracted_properties)
        return extracted_properties, evaluation_result
    

