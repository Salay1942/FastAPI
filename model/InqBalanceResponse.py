from typing import List
from pydantic import BaseModel

class Data(BaseModel):
    agreement_no: str
    customer_name: str
    mobile_no: str
    transfer_amount: float
    term: int
    start_date: str
    stop_date: str
    ccy: str
    company: str
    ref_no: str
    response_code: str
    response_desc: str
    company_account_number: str
    company_account_name: str
    company_detail_1: str
    company_detail_2: None
    company_detail_3: None